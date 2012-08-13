#!/usr/local/bin/python2
import os                       # For running system commands.
import argparse                 # For argument parsing.

# Configuration
_setup_file_ = 'setup.py'	# Your Py2App setup file.
_app_file_ = 'quickConnect.py'		# Should mirror the APP variable in your Py2App setup file.
_delete_ = ['Frameworks/QtDeclarative.framework', 'Frameworks/QtMultimedia.framework', 'Frameworks/QtScript.framework', 'Frameworks/QtSvg.framework','Frameworks/QtXml.framework', 'Frameworks/QtDesigner.framework', 'Frameworks/QtNetwork.framework',	 'Frameworks/QtScriptTools.framework','Frameworks/QtTest.framework', 'Frameworks/QtXmlPatterns.framework', 'Frameworks/QtHelp.framework', 'Frameworks/QtOpenGL.framework','Frameworks/QtSql.framework', 'Frameworks/QtWebKit.framework', 'Frameworks/libQtCLucene.4.dylib', 'Frameworks/phonon.framework', 'Frameworks/*.framework/*.prl']	# Files within [name].app/Contents/ to be deleted during the trimming process.

# DU function... uses the system's du command because Python's os.walk was giving
def checkDirSize(dir = '.'):
	f = os.popen("du -sh "+dir+" | awk '{print $1}'")
	return f.read().strip()

### Parsing command arguments
parser = argparse.ArgumentParser(description='Build and trim a PyQt .app')
#parser.add_argument('setupfile', metavar='SETUP FILE', type=str,
#					help='Target setup file for the Py2App build.')
parser.add_argument('p2a_flags', metavar='FLAGS', type=str,
					nargs='*', default='',
					help='Optional flags for Py2App.')
parser.add_argument('-d', '--donotbuild', action='store_const', const=True, required=False, default=False,
					help='Don\'t build the app.')
parser.add_argument('-n', '--notrim', action='store_const', const=True, required=False, default=False,
					help='Don\'t trim the un-wanted libraries from the app.')
parser.add_argument('-c', '--clean', action='store_const', const=True, required=False, default=False,
					help='Clear out the build directories.')
#parser.add_argument('-s', '--silent', action='store_const', const=True, required=False, default=False,
#					help='Suppress system command output.')

# Parsing argument values into the 'args' namespace object.
args = parser.parse_args()

# Get the .app name
app_name = _app_file_[:-3] + ".app/"

# Set the system command processor based on -s flag
#cmd_process = os.system if args.silent is False else os.popen
cmd_process = os.system

# Clean the build directores
if args.clean is True:
	f = cmd_process('rm -rf ./build ./dist')
	print '\n - Build directories have been cleaned.'

# Build the Py2App project
if args.donotbuild is False:
	f = cmd_process('python '+_setup_file_+' py2app '+' '+' '.join(args.p2a_flags))
	print '\n - App is now built. Current file size: '+checkDirSize('./dist/'+app_name)

# Trim the fat from the app
if args.notrim is False:
	for filename in _delete_:
		f = cmd_process('rm -rf ./dist/'+app_name+'/Contents/'+filename)
	print '\n - App has now been trimmed. Current file size: '+checkDirSize('./dist/'+app_name)

print '\n'
