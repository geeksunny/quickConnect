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

`build.py`

- Build script to assist in building with py2app.

`setup.py`

- py2app setup file for building a self contained .app version of quickConnect.

`connect_ssh.scpt`

- An AppleScript file that will open a new tab in the Terminal app and run a given command.

`icon.png`

- The icon displayed in the menu bar while running.

`README.md`

- This readme file.

Requirements
-------------
To use quickConnect, you will need to be running Mac OSX. It has currently been tested on 10.7.4 and 10.8, but it should work on older versions as well.

You will also need to have PyQt4 installed. You can install this easily using [brew](http://mxcl.github.com/homebrew/) with the command `brew install pyqt`.

To build a self-contained distributable version of quickConnect, you will need [setuptools](http://pypi.python.org/pypi/setuptools/) and [py2app](http://pypi.python.org/pypi/py2app/).

Building a standalone app
--------------------------
I have included a build script to make building with py2app easier.  To build your app, just run `python build.py` in your terminal. Your app will be in the 'dist' directory.

To see more options for the build script, run `python build.py -h`.

This is just a preliminary py2app build and will be improved upon in the future.