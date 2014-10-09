kosbot
======

A Jabber/XMPP bot to quickly check the CVA KOS list

License
-------

This repository is released under the MIT license, more details can be found in the ```LICENSE``` file.

Requirements
------------

All requirements are listed in ```requirements.txt```, Its designed to run on Python 2.7 but should run on Python 3.2+ but it hasn't been tested.

Installation
------------

For the quickest setup, the repository is setup to deploy to Heroku. It requires no add-ons or databases to operate just a few environmnet variables to be defined:

* ```KOSBOT_JID``` - JID of the bot
* ```KOSBOT_PASSWORD``` - Password to use for the JID 
* ```KOSBOT_NICKNAME``` - Nickname to use in MUC channels (defaults to KOSBot)
* ```KOSBOT_ROOMS``` - List of MUC channels, seperated by a comma, for the bot to join.

Usage
-----

The bot supports a single command of ```!kos <name>``` in a MUC where the bot is currently a member. 
