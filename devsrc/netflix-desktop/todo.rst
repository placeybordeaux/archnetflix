Things to Do
============
:Added: Tue Nov 20 12:00:45 PST 2012
:Modified: Tue Dec 04 12:55:36 PST 2012

1. [FIX]: Allow custom install path for netflix-desktop.

1. [FIX]: Use gtkdialog instead of zenity.

1. [FIX]: Test for Ext4 filesystem

   The firefox install failed on of ZFS root file system.

1. [FIX]: Get dependency reports from forum post and add to netflix-desktop
   PKGBUILD.

1. [FIX]: Figure out how to handle OpenGL dependencies.

1. [FIX]: Change netflix-desktop to arch specific.

1. [FIX]: Create chroot environment for testing

1. [TODO]: Figure out how to implement ccache and package signing in makechrootpkg.

1. [TODO]: Update the archnetflix webpage.

   - Write about the custom wine being installed to /opt

   - Write about ~/.netflix-desktop being a win32 prefix directory

   - Add information about package deltas

     - Enable UseDeltas in pacman.conf and install xdelta3.

1. [TODO]: Create netflix archwiki page
