import os

from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QStatusBar, QFileDialog, QWidget, QSizePolicy, QColorDialog, QStackedWidget, QTreeWidget, QTreeWidgetItem, QHeaderView, QDialog
from PySide2.QtGui import QKeySequence, QPixmap, QIcon, QColor
from PySide2.QtCore import QFile, Qt, Signal

from athena import mainwindow, ATHENA_DIR

class LogWindow(QDialog):
    default_ui_path = os.path.join( ATHENA_DIR, 'ui', 'LogWindow.ui' )
    def __init__( self, ui_filepath=default_ui_path ):
        super().__init__(None)
        mainwindow.UiLoader.populateUI( self, ui_filepath )

    def appendText( self, text ):
        self.textView.appendPlainText( text )
        self.textView.verticalScrollBar().setValue( self.textView.verticalScrollBar().maximum() )

