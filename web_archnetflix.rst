==================================================
Arch Netflix - Netflix on the desktop through WINE
==================================================
:status: hidden
:slug: archnetflix

This is the un-official repository for Netflix support in Arch Linux, created
by `Jesus Alvarez (demizer)`_. In this repository you will find two packages,
wine-silverlight and netflix-desktop. The i686 and x86_64 architectures are
supported.

The wine-silverlight package is wine-git_ with patches applied to allow
Silverlight to function correctly. These patches were authored by `Erich
Hoover`_ and can be found on his website. These patches were first reported on
iheartubuntu_.

The netflix-desktop package provides the netflix-desktop command that sets
up the environment from which one could watch Netflix. On the first activation
of the script, it creates a win32 `WINEPREFIX` in `~/.netflix-desktop` and
downloads and installs Firefox and Silverlight. Once the environment is setup,
activating the script simply loads Firefox with the browser pointed towards
netflix.com.

The source code for both of the packages can be found at archnetflix-github_.

For reporting problems, please see the AUR page at netflix-desktop-aur_ or
the announcement_.

wine-silverlight and netflix-desktop are LGPL licensed. Firefox is licensed
under the `Mozilla Public License`_.

------------------------
NON-FREE SOFTWARE NOTICE
------------------------

netflix-desktop downloads and installs Microsoft's Silverlight into a wine
prefix directory. By activating netflix-desktop you also agree to the terms of
the `Silverlight Install License`_. Silverlight is non-free software and if
RMS_ discovered what you were doing he would likely be very disappointed.

---------------------------------
My contributions to the community
---------------------------------

* `AUR - Packages`_

* `ArchWiki - Edits`_

* `bbs.archlinux.org - Posts`_ (Search for demizer)

* github_

-------------------------------------
My Unofficial Arch Netflix Repository
-------------------------------------

If you are adding my repository to pacman, you will first need to un-install
all previously install versions of netflix-desktop.

Next, add the following to `/etc/pacman.conf`:

.. code-block:: bash

    [archnetflix]
    SigLevel = Required DatabaseOptional TrustedOnly
    Server = http://demizerone.com/$repo/$arch

Both the database and the packages are signed, so you will have to add my key
to pacman's trusted key list.

.. code-block:: console

    # pacman-key -r 0EE7A126

verify it using the info below and then sign it with the local master key:

.. code-block:: console

    # pacman-key --lsign-key 0EE7A126

next, update your pacman database

.. code-block:: console

    # pacman -Syy

and install the netflix script,

.. code-block:: console

    # pacman -S netflix-desktop

Notes
=====

* My key is not signed by any of the master keys, so you will have to self sign
  it with your local master key. This page is hopefully an attempt to persuade
  you that it is legit and I mean no harm. Look below on how to verify my key.

* To read about key management in Arch, see
  `pacman-key <https://wiki.archlinux.org/index.php/Pacman-key>`_ and
  `pacman.conf <https://www.archlinux.org/pacman/pacman.conf.5.html#_package_and_database_signature_checking>`_.

----------
My PGP Key
----------

All of my packages and package databases are signed with the following key,

0EE7A126_
=========

The short version::

    pub   2048R/0EE7A126 2012-10-24
	Key fingerprint = B18A 9C9F 1E4E EAFF 072D  AB9E 5E1A BF24 0EE7 A126
    uid                  Jesus Alvarez <jeezusjr@gmail.com>
    sub   2048R/DAB97A2B 2012-10-24

and the long version::

    -----BEGIN PGP PUBLIC KEY BLOCK-----
    Version: SKS 1.1.0

    mQENBFCHi6oBCADbqiZasgwE//HtfGvyOynXapEP67tNFsKUgFR/XIVi8Io5ehCD88wOpN0O
    02u73OjDssTNh+yEN8ItixhxbZQClE7X4AG2/I49PBsPnY2G3zGPa2TB6vt5GStyVOFJjxsX
    F3sWcxfaBXSGonc9Qc8MSKmwwyvG5ASjCYYjK60UKoEqRF09DI/fMaOWcGoosNzNUntzuyAw
    9anRPZc/Chtmpd0DyQ4MhkGV18BWSsoGJsTeASo+jq98FcTKhUOfzpPccwmrQ+ViX+RIXIc/
    6WtnFs1rE0peWio3sgy+JvywT+8z2yrKZ+ovE1BQYgm2hZ4z6t55gdjfpw4uWtV4BsGzABEB
    AAG0Ikplc3VzIEFsdmFyZXogPGplZXp1c2pyQGdtYWlsLmNvbT6JATgEEwECACIFAlCHi6oC
    GwMGCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEF4avyQO56EmiKoH/iPqzt2+OycQ+tXX
    Gv2f/21dSEihGzvyXaC+yOwVrtvMamgxTeChnGi8H3gSabmTGyTJT60WsMmVtgUKZ7rqKh6b
    KbV1mIU8m/ZrzGJVrDc8JI+MrDmeaCaqTqZby+NeM5QNZ+FQiHX0dogpO3nvr3EvuipeSGu/
    KKsCfR9UxK0SwowBbfn6/3t7obO1il+eq6fHOB0+SuM6a9CssTOtPXim43VaDusaDJ13d5+3
    Ey/Mxbif5N+RzMgVavkAL5w0Cf4PElqNWA4aGfDxfhUvZ+WUOC+AFGZ/uGHwxdJLaCSx4aEI
    8CDj3trZnPit2umi64JHBb3KYLKey0duz/ztgtS5AQ0EUIeLqgEIALZx/agW3opcodJvUF7K
    4L1H9xnqw+bVBXIFyDvSCfWxLgS2MDTl/q38o62u4Htngwix8RsLEWqrtFfAi90VAxJ57pQZ
    xYZBAyEOoEOOBYJWbNxneHUSCp6+yGQiiyB0kMoCG9JMlcEmv8fwGqqardBR4+ZM2Acf+aLg
    xxi+7B3Ey7Vo/2MnzIu5GeUolDSmyDkUA91WdQByEoUWRVcRvQ+gQz/HGInHxPmqRIKFWSbg
    k1oBpCD7yJV+MfJAFaXvrEXn6jLKdIzWixIzhbVpt5RA+2wLzuTA/V5OGglNKOCWshkkjQBw
    SCOKPnYez/081Quw+1TIY8FuJY/fEv1Z1ZEAEQEAAYkBHwQYAQIACQUCUIeLqgIbDAAKCRBe
    Gr8kDuehJh47B/4myliSn3064a+a77wmvxNphuxKkUPU1gYu0aKF5bmT6nD3iOt3WA8pEcXL
    aVkA++nquTu2K8vGqZT4qBvcxP5W8s7mjVhP0h9N7VpikiAouRjEFYCVTjdwJbn0junCTjm4
    Ixr4fX5L7EgqCrToKbuQhlocwNPy1aJglm2MwDFzOFxK8R8Dx5O7xD/2b0pBdX/KHPqn2ENC
    yiKh/uUuykKpwEXVPPijL6nuA7BBacseXTn8ldAHStrhPEKnZ7mPV9j3VjlRHbYblvLGBBQi
    R6y3yNGqe7NjgJQW4e0ibvsbkG6PyUP4BLVUY6CGQFPt1p7dX4xioErHqdqPkjLzMvpi
    =TUqo
    -----END PGP PUBLIC KEY BLOCK-----

--------------------------------
How this repository is assembled
--------------------------------

This repository is based on Erich Hoover's excellent work on patching WINE to
allow Netflix playback within Silverlight. wine-silverlight contains these
patches and netflix-desktop is based off of his early script by the same name.
netflix-desktop has been modified to fit the Arch ethos.

It is possible to browse archnetflix-github_ for all source code involved in
the creation of this repository.

Here are the steps I use to update this repository and packages:

Check for updates on `Erich Hoover's Ubuntu PPA`_
=================================================

This is where he stores his package sources. In our case, we currently use
`wine-compholio - 1.5.19~raring`. This package is the wine development release
1.5.19 with his Silverlight patches applied on top.

Edit and use the automated script
=================================

We will use the extracted sources as the control to see what patches have been
applied to Erich Hoover's own wine-1.5.19 sources below. We use git to track
the initial state and to create the patch.

Adjust the global variable at the start of the script::

    WINE_VERSION = '1.5.19'
    WINE_VER_HASH = '713ad4e383abf4288c48c3cf9743a503'
    WINE_COMP_VER = 'raring'

The WINE_VER_HASH can be acquired on the `winehq.org download page`_ at
sourceforge.net. Click the "View details" icon next to the file
wine-1.5.19.tar.bz2. The MD5 field is the string we want.

Now use get_new_wine.py to automate the process of creating a new patch.

.. code-block:: console

    $ ./get_new_wine.py

Updating the packages
=====================

In the wine-silverlight directory edit PKGBUILD and change the following
values:

.. code-block:: bash

    pkgver=1.5.19
    pkgrel=1

We change `pkgrel` to 1 since it is a new version of wine.

Next we must regenerate the md5 hashes:

.. code-block:: console

    $ makepkg -g

Copy the output and replace the old md5sums at the bottom of the file.

Building the code
=================

Bulding the packages requires that the devtools_ package be installed. This
section assumes the host system is of x86_64 architecture.

Building x86_64
---------------

.. code-block:: console

    $ cd wine-silverlight
    $ makepkg -f --sign

Rebuilding x86_64
~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ cd wine-silverlight
    $ makepkg -Rf --sign
    $ makepkg -S

Setting up an i686 build environment
------------------------------------

See `Buldinig 32-bit packages on a 64-bit system`_ for more information.

.. code-block:: console

    $ cd wine-silverlight
    # cp /etc/{pacman.conf,makepkg.conf} /opt/arch32

Edit pacman.conf and makepkg.conf and change x86_64 to i686

.. code-block:: console

    # vim pacman.conf makepkg.conf
    # mkarchroot -C /opt/arch32/pacman.conf -M /opt/arch32/makepkg.conf /opt/arch32/root base base-devel sudo gnupg

In case a package is required that wasn't install in the command above, chroot
into the environment and install the missing packages with pacman:

.. code-block:: console

    # linux32 arch-chroot /opt/arch32/root /bin/bash
    # pacman -S <package>
    # exit

Building the i686 package
~~~~~~~~~~~~~~~~~~~~~~~~~

We use the `devtools`_ makechrootpkg script to build a package in the
previously setup chroot environment.

.. code-block:: console

    # makechrootpkg -c -r /opt/arch32 -n

NOTE: Do not use `-c` if you want to repackage!

now sign the package:

.. code-block:: console

    $ gpg --detach-sign --use-agent -u 0EE7A126 wine-silverlight-1.5.19-1-i686.pkg.tar.xz

Rebuilding the i686 package
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    # makechrootpkg -r /opt/arch32 -- -R

now sign the package:

.. code-block:: console

    $ gpg --detach-sign --use-agent -u 0EE7A126 wine-silverlight-1.5.19-1-i686.pkg.tar.xz

Add the packages to the repo
============================

.. code-block:: console

    $ cd x86_64/
    $ repo-add -s -d archnetflix.db.tar.xz netflix-desktop-0.1.2-2-any.pkg.tar.xz wine-silverlight-1.5.19-1-x86_64.pkg.tar.xz
    $ cd i686/
    $ repo-add -s -d archnetflix.db.tar.xz netflix-desktop-0.1.2-2-any.pkg.tar.xz wine-silverlight-1.5.19-1-i686.pkg.tar.xz

Push the changes
----------------

.. code-block:: console

    $ cd archnetflix
    $ rsync -vrtlhP --delete-before --exclude=index.html * jalvarez@jalvarez.webfactional.com:webapps/default/archnetflix/ -n

Inform the community
--------------------

bbs.archlinux.org
~~~~~~~~~~~~~~~~~

Here is the template for the anouncement post on the Arch Linux forums.

::

    wine-silverlight has been updated to wine-1.5.19 in AUR and the archnetflix repository. See anouncement at winehq.org. You can see the changes to the repository at https://github.com/demizer/archnetflix.
    -demizer

.. _Jesus Alvarez (demizer): http://demizerone.com
.. _wine-git: https://aur.archlinux.org/packages/wine-git/
.. _Erich Hoover: http://www.compholio.com
.. _iheartubuntu: http://www.iheartubuntu.com/2012/11/netflix-on-ubuntu-is-here.html
.. _archnetflix-github: https://github.com/demizer/archnetflix
.. _netflix-desktop-aur: https://aur.archlinux.org/packages/netflix-desktop
.. _announcement: https://bbs.archlinux.org/viewtopic.php?pid=1195746#p1195746
.. _Mozilla Public License: http://www.mozilla.org/MPL/
.. _Silverlight Install License: http://www.microsoft.com/getsilverlight/get-started/install/license-win.aspx
.. _RMS: http://stallman.org/
.. _AUR - Packages: https://aur.archlinux.org/packages/?O=0&C=0&SeB=m&K=demizer&outdated=&SB=n&SO=a&PP=50&do_Search=Go
.. _ArchWiki - Edits: https://wiki.archlinux.org/index.php/Special:Contributions/Demizer
.. _bbs.archlinux.org - Posts: https://bbs.archlinux.org/search.php
.. _github: http://www.github.com/demizer
.. _0EE7A126: http://pgp.mit.edu:11371/pks/lookup?op=vindex&search=0x5E1ABF240EE7A126
.. _Erich Hoover's Ubuntu PPA: https://launchpad.net/~ehoover/+archive/compholio/+packages
.. _winehq.org download page: http://sourceforge.net/projects/wine/files/Source/
.. _devtools: https://www.archlinux.org/packages/extra/any/devtools/
.. _Buldinig 32-bit packages on a 64-bit system: https://wiki.archlinux.org/index.php/Building_32-bit_packages_on_a_64-bit_system
