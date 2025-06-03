ControlEee701
=============

Questo è un fork del progetto originariamente scritto da Andrea Grandi, vedi di seguito la descrizione originale.

Lo scopo di questo fork è la completa implementazione su un eeepc 701 4G.



ControlEee
==========

ControlEee is an application written in Python/Qt4 that allows users to turn on/off bluetooth, webcam and wlan devices on a EeePC. Often these devices are not used and if they remain active, they increase the power consumption. So if you want your battery to last longer, it's a good idea to turn them off.

At the moment turning off wlan device is not allowed because it causes a kernel panic (at least on the distribution/hardware I've tested this: Ubuntu-eee/AsusEeePC 901).

To run this application you need Python and Qt4 bindings. On a Debian/Ubuntu based distribution you can install them in this way: sudo apt-get install python-qt4

This application is partially based on poweeersave written by Georg Holzmann.
