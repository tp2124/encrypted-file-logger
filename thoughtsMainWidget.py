
from PyQt4 import QtGui, QtCore
import os
import sys
import time
import subprocess

DBLOC = "\\Entries\\6-8-2013.log"

def run_command(command):
    p = subprocess.Popen(command, shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    return p.communicate()

class ThoughtsPasswordWidget(QtGui.QDialog):
    def __init__(self, *args):
        super(ThoughtsPasswordWidget, self).__init__()
        #General Window stuff
        self.move(300, 200)
        self.setWindowTitle('Thoughts Entries')
        self.entryWidget = None
        self.existingAssets = []
        # self.getExistingAssets()
        self.existingTypes = []
        # self.getExistingTypes()
        
        #Create more widgets
        self.vMainLayout = QtGui.QVBoxLayout()
        self.vTypeLayout = QtGui.QVBoxLayout()
        self.vNameLayout = QtGui.QVBoxLayout()
        # self.vFileLayout = QtGui.QVBoxLayout()
        # self.hFileTextLayout = QtGui.QHBoxLayout()
        self.hButtonLayout = QtGui.QHBoxLayout()
        # self.typeLabel = QtGui.QLabel('Asset Types')
        # self.w_typeName = QtGui.QComboBox()
        self.w_typeNameText = QtGui.QLineEdit()
        self.w_typeNameText.setEchoMode(QtGui.QLineEdit.Password)
        self.w_typeSpace = QtGui.QLabel('')
        self.startEntryButton = QtGui.QPushButton('Begin Entry')
        self.readEntriesButton = QtGui.QPushButton('View Entries')
        self.cancelButton = QtGui.QPushButton('Quit')
        self.w_buttonSpace = QtGui.QLabel('')

        self.vTypeLayout.addWidget(self.w_typeNameText)
        self.vTypeLayout.addWidget(self.w_typeSpace)
        
        self.hButtonLayout.addWidget(self.startEntryButton)
        self.hButtonLayout.addWidget(self.readEntriesButton)
        self.hButtonLayout.addWidget(self.cancelButton)
        
        
        self.vMainLayout.addLayout(self.vTypeLayout)
        self.vMainLayout.addLayout(self.vNameLayout)
        self.vMainLayout.addLayout(self.hButtonLayout)
        self.setLayout(self.vMainLayout)
        
        #Pair signals with slots
        self.connect(self.startEntryButton,
                    QtCore.SIGNAL('clicked()'),
                    self.attemptEntry)
                    
        self.connect(self.cancelButton,
                    QtCore.SIGNAL('clicked()'),
                    self.exit)

        self.connect(self.readEntriesButton,
                    QtCore.SIGNAL('clicked()'),
                    self.readEntries)
                    
        '''
        self.connect(self.w_fileButton,
                    QtCore.SIGNAL('clicked()'),
                    self.getFileDialog)
        '''
        self.setMinimumWidth(300)
        #Show me
        self.show()
        
        
    def exit(self):
        self.clearMountedDrive()
        try:
            self.entryWidget.close()
        except:
            pass
        self.close()
        

    def getDataPath(self):
        return os.getcwd() + DBLOC

    def clearMountedDrive(self):
        run_command('TrueCrypt.exe /q /dx /s')

    def readEntries(self):
        self.clearMountedDrive()
        filePath = self.getDataPath()
        cmd = 'TrueCrypt.exe /s /q /v %s /p %s /lx' % (filePath, self.w_typeNameText.text())
        rez = run_command(cmd)
        if os.path.exists("X:"):
            cmd = 'explorer X:'
            rez = run_command(cmd)

    def attemptEntry(self):
        #mount
        self.clearMountedDrive()
        filePath = self.getDataPath()
        cmd = "TrueCrypt.exe /q /s /v %s /p %s /lx" % (filePath, self.w_typeNameText.text())
        rez = run_command(cmd)

        if os.path.exists("X:"):
            #Correct Password
            from thoughtsEntryWidget import ThoughtsEntryWidget

            self.entryWidget = ThoughtsEntryWidget()
            self.entryWidget.exec_()


