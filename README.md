quickConnect
=============
quickConnect is a program written in Python and PyQt that provides a quick-access menu for connecting to servers listed in your ssh config file.

quickConnect is currently targeted at OSX systems but may become platform-independent in the future.

Using quickConnect
-------------------
To launch quickConnect, call the `quickConnect.py` file from the command line with your Python interpreter.

You should also be able to double click on the `quickConnect.py` file from within the Finder.

Once quickConnect is started, simply click the icon in the menu bar and select the server you would like to connect to. This will launch a new tab in the Terminal app and connect you to your selected server.

Files in this project
----------------------
`quickConnect.py`

- The main source file for quickConnect.

`connect_ssh.scpt`

- An AppleScript file that will open a new tab in the Terminal app and run a given command.

`icon.png`

- The icon displayed in the menu bar while running.

`README.md`

- This readme file.

Requirements
-------------
To use quickConnect, you will need to be running Mac OSX. It has currently been tested on 10.7.4 and 10.8, but it should work on older versions as well.

You will also need to have PyQt4 installed. You can install this easily using [brew](http://mxcl.github.com/homebrew/) (`brew install pyqt`).

Compiling a standalone app
---------------------------
If you would like to compile a self-contained app version of quickConnect, I will be providing a setup file for use with py2app in the future.