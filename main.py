import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel
from PySide2.QtCore import QFile, QObject

# global vars
curNum = 0
firstNum = 0
secNum = 0
isOp = False
opDone = False
operation = ""


class MainWindow(QObject):
    def __init__(self, ui_file, parent=None):                           #class constructor
        super(MainWindow,self).__init__(parent)                         #call QObject constructor
        ui_file = QFile(ui_file)                                        #load the UI file into Python
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()                                                 #close file

        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        accumulator.setText("")

        #connect all buttons to window elements
        oneButton = self.window.findChild(QPushButton, 'oneButton')
        oneButton.clicked.connect(self.num_button_clicked)
        twoButton = self.window.findChild(QPushButton, 'twoButton')
        twoButton.clicked.connect(self.num_button_clicked)
        threeButton = self.window.findChild(QPushButton, 'threeButton')
        threeButton.clicked.connect(self.num_button_clicked)
        fourButton = self.window.findChild(QPushButton, 'fourButton')
        fourButton.clicked.connect(self.num_button_clicked)
        fiveButton = self.window.findChild(QPushButton, 'fiveButton')
        fiveButton.clicked.connect(self.num_button_clicked)
        sixButton = self.window.findChild(QPushButton, 'sixButton')
        sixButton.clicked.connect(self.num_button_clicked)
        sevenButton = self.window.findChild(QPushButton, 'sevenButton')
        sevenButton.clicked.connect(self.num_button_clicked)
        eightButton = self.window.findChild(QPushButton, 'eightButton')
        eightButton.clicked.connect(self.num_button_clicked)
        nineButton = self.window.findChild(QPushButton, 'nineButton')
        nineButton.clicked.connect(self.num_button_clicked)

        divideButton = self.window.findChild(QPushButton, 'divideButton')
        divideButton.clicked.connect(self.op_clicked)
        multiplyButton = self.window.findChild(QPushButton, 'multiplyButton')
        multiplyButton.clicked.connect(self.op_clicked)
        addButton = self.window.findChild(QPushButton, 'addButton')
        addButton.clicked.connect(self.op_clicked)
        subtractButton = self.window.findChild(QPushButton, 'subtractButton')
        subtractButton.clicked.connect(self.op_clicked)

        equalsButton = self.window.findChild(QPushButton, 'equalsButton')
        equalsButton.clicked.connect(self.equals_clicked)

        self.window.show()                                                  #show window. must always be last
    
    def num_button_clicked(self):
        global curNum
        global firstNum
        global secNum
        global isOp
        global opDone

        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')
        if opDone == True:
            accumulator.setText("")
            opDone = False
        sender = self.sender()

        curNum = int(sender.text())
        newNum = str(curNum)

        if isOp == False:
            accumulator.setText(accumulator.text() + newNum)
        else:
            accumulator.setText(newNum)
            isOp = False

    
    def op_clicked(self):
        global operation
        global firstNum
        global isOp

        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')

        firstNum = int(accumulator.text())

        sender = self.sender()
        operation = sender.text()
        isOp = True
        opDone = True

    def equals_clicked(self):
        global firstNum
        global secNum
        global operation
        global opDone
        accumulator = self.window.findChild(QLineEdit, 'accumulatorText')

        secNum = int(accumulator.text())

        if operation == "+":
            total = str(firstNum + secNum)
            accumulator.setText(total)
        elif operation == "-":
            total = str(firstNum - secNum)
            accumulator.setText(total)
        elif operation == "*":
            total = str(firstNum * secNum)
            accumulator.setText(total)
        elif operation == "/":
            total = str(firstNum / secNum)
            accumulator.setText(total)

        opDone = True
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('calculator.ui')
    sys.exit(app.exec_())