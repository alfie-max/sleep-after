sleep-after
-----------

A simple python script to put your system to sleep/suspend after
specified amount of time

Uses
----
`pm-suspend` system tool

Usage
-----

`sleep-after hh:mm:ss`


Example :

`sleep-after 10`

This will put your system to sleep after 10 seconds.


`sleep-after 15:10`

This will put your system to sleep after 15 minutes and 10 seconds.


`sleep-after 2:15:10`

This will put your system to sleep 2 hours 15 minutes and 10 seconds.


Installation
------------
Please install it in your system and not in a virtual environment.
`pm-suspend` tool requires root previlages to execute, so installing
this in a virtualenv wont work.

`pip install sleep-after`

Developers
----------
Alfred Dominic

