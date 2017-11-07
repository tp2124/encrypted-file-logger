from PyQt4 import QtGui, QtCore
import os
import sys
import time
import subprocess

def run_command(command):
    p = subprocess.Popen(command, shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    return p.communicate()

class ThoughtsEntryWidget(QtGui.QDialog):
    def __init__(self, *args):
        super(ThoughtsEntryWidget, self).__init__()
        #General Window stuff
        self.move(300, 200)
        self.setWindowTitle('New Entry')
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
        self.subjectTitleLable = QtGui.QLabel('Subject')
        self.subjectText = QtGui.QLineEdit('Misc')
        self.entryText = QtGui.QTextEdit()
        self.entrySpace = QtGui.QLabel('')
        self.startEntryButton = QtGui.QPushButton('Create Entry')
        self.cancelButton = QtGui.QPushButton('Cancel')
        self.w_buttonSpace = QtGui.QLabel('')

        self.vTypeLayout.addWidget(self.subjectTitleLable)
        self.vTypeLayout.addWidget(self.subjectText)
        self.vTypeLayout.addWidget(self.entryText)
        self.vTypeLayout.addWidget(self.entrySpace)
        
        self.hButtonLayout.addWidget(self.startEntryButton)
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
                    
        '''
        self.connect(self.w_fileButton,
                    QtCore.SIGNAL('clicked()'),
                    self.getFileDialog)
        '''
        self.setMinimumWidth(300)
        #Show me
        self.show()
        
        
    def getFileDialog(self):
        #QFileDialog
        pass
        
    def exit(self):
        #Safe logout
        cmd = 'TrueCrypt.exe /q /dx /s'
        run_command(cmd)
        self.close()
    
    def attemptEntry(self):
        if (str(self.entryText.toPlainText())):
            #Create new organized entry, that isn't blank
            entryDir = 'X:\\' + time.strftime("%c", time.gmtime()).split()[0].replace('/', '-')

            if not os.path.exists(entryDir):
                os.mkdir(entryDir)
            entryFileName = '%s\\%s' % (entryDir, self.subjectText.text())
            entryFIO = open(entryFileName + '.tprimm', 'w')
            text = '%s' % self.entryText.toPlainText()
            entryFIO.write(text)
            entryFIO.close()

            self.exit()

