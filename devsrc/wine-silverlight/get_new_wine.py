#!/usr/bin/python
# encoding: utf-8

import os
import sys
import hashlib
import datetime
import re
import subprocess

WINE_VERSION = '1.5.19'
WINE_VER_HASH = '713ad4e383abf4288c48c3cf9743a503'
WINE_COMP_VER = 'raring'

#
# DO NOT EDIT PAST THIS BLOCK
#

WUFILE = 'wine-{0}.tar.bz2'.format(WINE_VERSION)
WUFILEURL = ('http://downloads.sourceforge.net/project/wine/Source/{0}'
             '?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fwine%2Ffiles%'
             '2FSource%2F&ts=1353813614&use_mirror=iweb'.format(WUFILE))

WINE_COMP_HASH = ''  # Extracted from WCDFILE
WCDFILE = 'wine-compholio_{0}~{1}.dsc'.format(WINE_VERSION, WINE_COMP_VER)
WCDFILEURL = ('https://launchpad.net/~ehoover/+archive/compholio/+files/'
              '{0}'.format(WCDFILE))
WCFILE = 'wine-compholio_{0}~{1}.tar.gz'.format(WINE_VERSION, WINE_COMP_VER)
WCFILEURL = ('https://launchpad.net/~ehoover/+archive/compholio/'
             '+files/{0}'.format(WCFILE))

OUTPUT_PREFIX = '[>>>]'


def md5_hash(fpath):
    """Return the md5sum of a single file.

    :returns: None if the hash failed, otherwise a string of the hash.

    """
    if not os.path.exists(fpath):
        return None

    fobj = open(fpath, 'rb')
    mobj = hashlib.md5()

    while True:
        data = fobj.read(8192)
        if not data:
            break
        mobj.update(data)

    return mobj.hexdigest()


def get_time_string():
    """Returns a formatted time string.

    """
    now = datetime.datetime.now()
    return now.strftime('%a %b %d %H:%M:%S %Y')


def log(text, err=False, warn=False, begin=False, done=False, noprefix=False):
    """Pretty prints to stdout.

    >> THIS IS A HACK! Proper logging support and exception handling is coming
    >> in the future.

    log is responsible for making pretty output and is used throughout the
    entire program. Any whitepsace characters at the start or ends of the line
    are preserved. So lines containing '\r' will overlap. This is useful for
    progress bars and such.

    :text: The message to write to stdout.
    :err: Prepends ERROR in red and exits the script (naughty!).
    :warn: Prepends WARNING to the message.
    :done: Prepends COMPLETE to the message.
    :noprefix: Nothing will be prepended to the message.

    """
    # This function uses ansi escape sequences.
    # http://bluesock.org/~willg/dev/ansi.html#sequences
    # http://en.wikipedia.org/wiki/ANSI_escape_code
    # http://docs.python.org/reference/lexical_analysis.html

    # `\033[` is the escape sequence character. `\033` is octal.
    # `31m` sets the color
    fail = '\033[31m'
    okgreen = '\033[32m'
    warning = '\033[33m'
    okblue = '\033[34m'
    endc = '\033[0m'

    prefix = note = color = pre_pad = pos_pad = end = ''
    if not noprefix:
        prefix = ''.join((okgreen, OUTPUT_PREFIX, endc, ': '))
    brand = ''.join([prefix, get_time_string(), ': '])

    pad_re = re.match(r'(\s*).*(\s*)', text)
    if pad_re:
        pre_pad = pad_re.group(1)
        pos_pad = pad_re.group(2)
    end = '\r' if text[-1] == '\r' else '\n'
    stext = text.strip()

    if err:
        note = '[ERROR] '
        color = fail
    elif warn:
        note = '[WARNING] '
        color = warning
    elif begin:
        note = '[Begin] '
        color = okgreen
    elif done:
        note = '[FINISHED] '
        color = okblue

    # K = clear to the end of the line
    sys.stdout.write(''.join((pre_pad, brand, color, note, endc, stext,
                              pos_pad, '\033[K', end)))
    if err:
        sys.exit(1)


def download_file(url, filename, fhash=None):
    """Downloads a file and displays progress progress.

    """
    if os.path.exists(filename) and (not fhash or md5_hash(filename) == fhash):
        log(filename + ' already exists\n')
        return
    while True:
        log('Downloading "' + filename + '"...\n')
        args = ['curl', '--location', '-o', filename, url]
        ret = subprocess.call(args)
        if ret == 0 and os.path.exists(filename):
            if md5_hash(filename) == fhash or not fhash:
                log('\nDownload succesful!')
                break
            else:
                log('\nDownload of ' + filename + ' failed! Trying again...')
                os.remove(filename)


####################################
# IN THE BEGINNING, THERE WAS PYTHON
####################################

def main():
    """The main function.

    """
    log(sys.argv[0][2:] + ' has started\n')

    download_file(WUFILEURL, WUFILE, WINE_VER_HASH)

    download_file(WCDFILEURL, WCDFILE)

    fdsc = open(WCDFILE)
    fdsc_str = fdsc.read()
    fdsc.close()

    try:
        WINE_COMP_HASH = re.findall(r'Files:\s+([\w]+)', fdsc_str)[0]
    except IndexError:
        log('Could not determine hash for ' + WCFILE + '!', err=True)

    download_file(WCFILEURL, WCFILE, WINE_COMP_HASH)

    # extract the files
    uwd = 'upstream-wine-' + WINE_VERSION
    if os.path.exists(uwd):
        log(uwd + ' already exists! Implement support for creating new '
            'patches lazy ass!\n', warn=True)
        os.chdir(uwd)
        subprocess.call('git reset --hard HEAD^', shell=True)
        print()
        os.chdir('..')
    else:
        log('Extracting ' + WUFILE + '...')
        ret = subprocess.call(['tar', 'xjf', WUFILE])
        if ret != 0:
            log('\nAn error occurred extracting ' + WUFILE + '!', err=True)
        subprocess.call('mv wine-' + WINE_VERSION + ' ' + uwd, shell=True)
        os.chdir(uwd)
        subprocess.call('git init', shell=True)
        subprocess.call('git add .', shell=True)
        subprocess.call('git commit -m "Initial commit"', shell=True)
        os.chdir('..')

    log('Extracting ' + WCFILE + '...')
    ret = subprocess.call('tar xzf ' + WCFILE, shell=True)
    if ret != 0:
        log('\nAn error occurred extracting ' + WCFILE + '!', err=True)

    wch_name = (WCFILE[:-7] + '/*').replace('_', '-')
    subprocess.call('cp -R ' + wch_name + ' ' + uwd + '/', shell=True)

    # Create patch and commit changes
    os.chdir(uwd)
    subprocess.call('git clean -fd > /dev/null 2>&1', shell=True)
    subprocess.call('git status', shell=True)
    subprocess.call('git diff > ../silverlight.patch', shell=True)
    subprocess.call('git commit -a -m ' + WINE_COMP_VER, shell=True)

    # Cleanup
    os.chdir('..')
    subprocess.call('rm -rf ' + wch_name[:-2], shell=True)
    subprocess.call('rm -rf ' + WCFILE, shell=True)
    subprocess.call('rm -rf ' + WCDFILE, shell=True)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('\n\nToodles.')
