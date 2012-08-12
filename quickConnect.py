from os import path
from subprocess import Popen
from sys import argv, exit
from functools import partial
from PyQt4 import QtGui, QtCore

class SystemTrayIcon(QtGui.QSystemTrayIcon):
	def __init__(self, menuList, parent=None):
		QtGui.QSystemTrayIcon.__init__(self, parent)

		self.setIcon(QtGui.QIcon("icon.png"))

		self.iconMenu = QtGui.QMenu(parent)

		# Submenu object storage
		self.subMenus = []
		# Create menu from menuList variable
		self.add_items_to_menu(menuList, self.iconMenu)
		# Add built-in static entries
		self.iconMenu.addSeparator()
		appabout = self.iconMenu.addAction("About")
		self.connect(appabout,QtCore.SIGNAL('triggered()'),self.showAbout)
		appexit = self.iconMenu.addAction("Exit")
		self.connect(appexit,QtCore.SIGNAL('triggered()'),self.appExit)

		self.setContextMenu(self.iconMenu)

		self.show()

	def add_items_to_menu(self, menuList, Parent):
		for item in menuList:
			if callable(item[1]):
				newItems = Parent.addAction(str(item[0]))
				self.connect(newItems,QtCore.SIGNAL('triggered()'),partial(item[1],self))
			elif non_string_iterable(item[1]):
				self.subMenus.append(QtGui.QMenu(str(item[0])))
				lastIndex = self.subMenus.index(self.subMenus[-1])
				self.add_items_to_menu(item[1], self.subMenus[-1])	# Recursive call for sub-menus
				Parent.addMenu(self.subMenus[lastIndex])
			else:
				newItems = Parent.addAction(str(item[0]))
				self.connect(newItems,QtCore.SIGNAL('triggered()'),partial(self.runCmdStr,str(item[1])))

	def runCmdStr(self, str):
		print str #debug
		args = str.split('|')
		cmd = []
		for arg in args:
			cmd.append(arg)
		Popen(cmd)

	def showAbout(self):
		self.iconMenu.setEnabled(False)
		msgBox = QtGui.QMessageBox()
		msgBox.setTextFormat(QtCore.Qt.RichText)
		msgBox.setWindowTitle("About quickConnect")
		msgBox.setText("<h1>quickConnect</h1>")
		msgBox.setInformativeText("<center>Written by <a href=\"http://www.faecbawks.com/\">Justin Swanson</a><br /><br />Source code available on <a href=\"http://www.github.com/geeksunny/quickConnect\">GitHub</a>.</center>")
		msgBox.exec_()
		self.iconMenu.setEnabled(True)

	def appExit(self):
		app.quit()

# Checks the given variable object to see if it is an iterable list or not.
def non_string_iterable(obj):
	try:
		iter(obj)
	except TypeError:
		return False
	else:
		return not isinstance(obj, basestring)

if __name__ == "__main__":
	app = QtGui.QApplication(argv)
	app.setQuitOnLastWindowClosed(False)

	# Read the ssh config file.
	filename = path.expanduser("~/.ssh/config")

	servers = {}
	host, hostname, user = '','',''
	menu_options = []

	if path.isfile(filename):
		fh = open(filename)
		for line in fh.readlines():
			line = line.strip()		# Strip surrounding whitespace
			if line.find("Host ") > -1:
				host = line.replace("Host ","")
				servers[host] = {}
			elif line.find("HostName ") > -1:
				hostname = line.replace("HostName ","")
				servers[host]['hostname'] = hostname
			elif line.find("User ") > -1:
				user = line.replace("User ","")
				servers[host]["user"] = user
		server_list = servers.keys()
		server_list.sort()
		for server in server_list:
			menu_options.append([server+" ("+servers[server]["user"]+")", "osascript|./connect_ssh.scpt|ssh "+server])
	else:
		print "File not found!"
		menu_options = (('Could not load!', 0, 0),)
	# Configuration menu.
	#menu_options.append(['Configuration', [['Edit Config', 'notepad|shortcuts'],['Reload Config', restartProgram]]])

	trayIcon = SystemTrayIcon(menu_options)
	trayIcon.show()

	exit(app.exec_())