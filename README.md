# Booker
## Intro
__Booker__ is a set of python 3 scripts that automatically book group study rooms at the ANU library.

## Warning
It is in a very early development stage, core functions are still being implemented. No features are available as of yet.
All of the code is being written by two first-year engineering students, so its quality it pretty terrible (sorry).

## Planned features
+ Auto-book rooms for every timetable break
+ Multiple ANU accounts (more concurrent bookings)
+ Configurable timetable, room preferences, libraries
+ Email notifications or Google calendar integration

## Technical stuff
__Booker__ uses _requests_ python library to interact with the _anulib.anu.edu.au_ website. All the information is stored in plain-text .conf files.

Apart from the main __booker.py__ script, there are multiple utility modules:
+ __config.py__ works with (you guessed it), .conf files, storing and loading information from them.
+ __anulib.py__ is contains functions to interact with the _anulib_ website.
+ __notify.py__ generates and sends out email notifications and works with the calendar.

The configuration files are:
+ __timetable.conf__ contains information about breaks during which the rooms need to be booked.
+ __login.conf__, which is not actually present on the repo for obvious reasons, contains a list of logins and passwords to be used for booking. (There's an __.example__ file provided).
+ __cbook.conf__ stores all the current bookings.
+ __email.conf__ will be used for all notificaton-related stuff.
+ __rooms.conf__ is a room preference file (some study rooms are much better than the others).
