# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/phailiew/Desktop/calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.outputLabel.setFont(font)
        self.outputLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("%") )
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("C") )
        self.cButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove_it() )
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("/") )
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7") )
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9") )
        self.nineButton.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.timeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("x") )
        self.timeButton.setGeometry(QtCore.QRect(275, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.timeButton.setFont(font)
        self.timeButton.setObjectName("timeButton")
        self.eightbButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8") )
        self.eightbButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.eightbButton.setFont(font)
        self.eightbButton.setObjectName("eightbButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4") )
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6") )
        self.sixButton.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-") )
        self.minusButton.setGeometry(QtCore.QRect(275, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5") )
        self.fiveButton.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1") )
        self.oneButton.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3") )
        self.threeButton.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+") )
        self.plusButton.setGeometry(QtCore.QRect(275, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2") )
        self.twoButton.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.plusminusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plus_minus_it() )
        self.plusminusButton.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.dot_it() )
        self.decimalButton.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.math_it() )
        self.equalButton.setGeometry(QtCore.QRect(275, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0") )
        self.zeroButton.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.stored = ''
    #Remove character
    def remove_it(self):
        #grab what is on the screen already
        screen = self.outputLabel.text()
        #remove last item
        screen = screen[:-1]
        #output back to the screen
        self.outputLabel.setText(screen)
    #Math way
    def math_it(self):
        #grab what is on the screen already
        screen = self.outputLabel.text()
        try:
            self.stored = self.stored + self.outputLabel.text()
            print(self.stored)
            answer = eval(self.stored)
            #output the answer
            self.outputLabel.setText(str(answer))
            self.stored = ''
        except:
            #output error
            self.outputLabel.setText("ERROR")


    #change from positive or negative
    def plus_minus_it(self):
        #grab what is on the screen already
        screen = self.outputLabel.text()
        if "-" in screen:
           self.outputLabel.setText(screen.replace("-", ""))
        else:
           self.outputLabel.setText(f'-{screen}') 
    #add decimal
    def dot_it(self):
        screen = self.outputLabel.text()
        if "." in screen:
            pass
        else:
            self.outputLabel.setText(f'{screen}.')

    def press_it(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        elif pressed == "+":
            self.stored = self.stored + self.outputLabel.text() + '+'
            self.outputLabel.setText("0")
        elif pressed == "-":
            self.stored = self.stored + self.outputLabel.text() + '-'
            self.outputLabel.setText("0")
        elif pressed == "x":
            self.stored = self.stored + self.outputLabel.text() + '*'
            self.outputLabel.setText("0")
        elif pressed == "/":
            self.stored = self.stored + self.outputLabel.text() + '/'
            self.outputLabel.setText("0")
        else:
            #check to see if it starts with 0 and delete that 0
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            #concatenate the pressed button with what was there
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.timeButton.setText(_translate("MainWindow", "x"))
        self.eightbButton.setText(_translate("MainWindow", "8"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
