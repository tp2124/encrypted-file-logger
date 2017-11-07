"""
UI Interface to a private note logger. This uses TrueCrypt file encryption in order to keep files secure. This program handles
the encrypted file having a second password to fall through on.
"""

from PyQt4 import QtGui, QtCore
from thoughtsMainWidget import ThoughtsPasswordWidget

app = None
win = None

def runStandalone():
    import sys
    global app
    global win
    app = QtGui.QApplication(sys.argv)
    win = ThoughtsPasswordWidget()
    win.show()
    app.exec_()

def runMaya():
    plugin = 'ThreadedQtPlugin.py'
    if not cmds.pluginInfo(plugin, Query = True, loaded = True):
        #if Qt isn't loaded, fix that
        cmds.loadPlugin(plugin)
    app = QtGui.qApp
    app.connect(app, QtCore.SIGNAL('lastWindowClosed()'),
                app, QtCore.SLOT('quit()'))
    win = ThoughtsPasswordWidget()
    win.show()
        
def run():
    #figure out if being run in standAlone or Maya
    isMaya = False
    try:
        import maya.cmds as cmds
        isMaya = True
    except ImportError:
        isMaya = False

    if isMaya:
        runMaya()
    else:
        runStandalone()

if __name__ == '__main__':
    run()
