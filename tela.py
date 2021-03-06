# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scnner.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1115, 614)
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0.446, y1:0.625, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.label_2 = QtWidgets.QLabel(self.page1)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 91, 81))
        self.label_2.setStyleSheet("background-color: rgb(123, 123, 123, 0.5);\n"
"")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("iconescanner/capa_2.png"))
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(self.page1)
        self.progressBar.setGeometry(QtCore.QRect(100, 0, 821, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(200, 200, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(123, 123, 123, 1))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.progressBar.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("\n"
"QProgressBar {\n"
"    \n"
"    background-color: rgb(123, 123, 123, 0.5);\n"
"    color: rgb(200, 200, 200);\n"
"    border-style: none;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 5px;\n"
"    \n"
"    background-color: qconicalgradient(cx:1, cy:1, angle:69.3, stop:0 rgba(25, 38, 35, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 25)
        self.progressBar.setTextVisible(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget = QtWidgets.QTabWidget(self.page1)
        self.tabWidget.setGeometry(QtCore.QRect(110, 40, 961, 511))
        self.tabWidget.setStyleSheet("background-color: rgb(123, 123, 123, 0.5);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(-200, 10, 1181, 511))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("iconescanner/capafundo.png"))
        self.label_6.setObjectName("label_6")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 951, 481))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("color:green;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(123, 123, 123, 0.5);\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(9)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setAutoScrollMargin(31)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setBackground(QtGui.QColor(116, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        item.setFont(font)
        item.setBackground(QtGui.QColor(116, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        item.setFont(font)
        item.setBackground(QtGui.QColor(116, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        item.setFont(font)
        item.setBackground(QtGui.QColor(116, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        item.setFont(font)
        item.setBackground(QtGui.QColor(116, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        item.setFont(font)
        item.setBackground(QtGui.QColor(116, 0, 0))
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(48)
        self.tableWidget.verticalHeader().setDefaultSectionSize(33)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 961, 481))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color:negrito\n"
";background-color: rgb(123, 123, 123, 0.5);\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 941, 481))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("iconescanner/capafundo.png"))
        self.label_7.setObjectName("label_7")
        self.label_7.raise_()
        self.textEdit.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.frame_3 = QtWidgets.QFrame(self.page1)
        self.frame_3.setGeometry(QtCore.QRect(0, 80, 101, 471))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.BT_Scanner = QtWidgets.QPushButton(self.frame_3)
        self.BT_Scanner.setGeometry(QtCore.QRect(0, 0, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.BT_Scanner.setFont(font)
        self.BT_Scanner.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconescanner/cil-zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_Scanner.setIcon(icon)
        self.BT_Scanner.setObjectName("BT_Scanner")
        self.BT_deleta = QtWidgets.QPushButton(self.frame_3)
        self.BT_deleta.setGeometry(QtCore.QRect(0, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.BT_deleta.setFont(font)
        self.BT_deleta.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("iconescanner/delet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_deleta.setIcon(icon1)
        self.BT_deleta.setObjectName("BT_deleta")
        self.BT_VER = QtWidgets.QPushButton(self.frame_3)
        self.BT_VER.setGeometry(QtCore.QRect(0, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.BT_VER.setFont(font)
        self.BT_VER.setStyleSheet("background-color: rgb(112, 0, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("iconescanner/binoculars.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BT_VER.setIcon(icon2)
        self.BT_VER.setObjectName("BT_VER")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.lineEdit = QtWidgets.QLineEdit(self.page2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 410, 201, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(59, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setMaxLength(15)
        self.lineEdit.setObjectName("lineEdit")
        self.listWidget_2 = QtWidgets.QListWidget(self.page2)
        self.listWidget_2.setGeometry(QtCore.QRect(-10, 0, 601, 361))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("background-color: rgb(123, 123, 123, 0.5);\n"
"\n"
"color: rgb(0, 0, 0);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 450, 201, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(59, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setMaxLength(15)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.ip = QtWidgets.QPushButton(self.page2)
        self.ip.setGeometry(QtCore.QRect(930, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.ip.setFont(font)
        self.ip.setStyleSheet("\n"
"background-color: rgb(112, 0, 0);\n"
"color: rgb(255, 255, 255);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("iconescanner/375.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ip.setIcon(icon3)
        self.ip.setObjectName("ip")
        self.ip_inicial = QtWidgets.QComboBox(self.page2)
        self.ip_inicial.setGeometry(QtCore.QRect(600, 90, 291, 20))
        self.ip_inicial.setStyleSheet("background-color: rgb(59, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.ip_inicial.setObjectName("ip_inicial")
        self.ip_inicial.addItem("")
        self.ip_inicial.setItemText(0, "")
        self.ip_final = QtWidgets.QComboBox(self.page2)
        self.ip_final.setGeometry(QtCore.QRect(600, 160, 291, 20))
        self.ip_final.setStyleSheet("background-color: rgb(59, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.ip_final.setObjectName("ip_final")
        self.ip_final.addItem("")
        self.ip_final.setItemText(0, "")
        self.tipo_ip_box1 = QtWidgets.QLabel(self.page2)
        self.tipo_ip_box1.setGeometry(QtCore.QRect(600, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.tipo_ip_box1.setFont(font)
        self.tipo_ip_box1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(112, 0, 0);")
        self.tipo_ip_box1.setObjectName("tipo_ip_box1")
        self.tipo_ip_box2 = QtWidgets.QLabel(self.page2)
        self.tipo_ip_box2.setGeometry(QtCore.QRect(600, 140, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.tipo_ip_box2.setFont(font)
        self.tipo_ip_box2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(112, 0, 0);")
        self.tipo_ip_box2.setObjectName("tipo_ip_box2")
        self.label = QtWidgets.QLabel(self.page2)
        self.label.setGeometry(QtCore.QRect(690, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(123, 123, 123, 0.5);\n"
"\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label.setObjectName("label")
        self.ip_3 = QtWidgets.QPushButton(self.page2)
        self.ip_3.setGeometry(QtCore.QRect(20, 490, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setBold(True)
        font.setWeight(75)
        self.ip_3.setFont(font)
        self.ip_3.setStyleSheet("\n"
"background-color: rgb(112, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.ip_3.setIcon(icon3)
        self.ip_3.setObjectName("ip_3")
        self.label_5 = QtWidgets.QLabel(self.page2)
        self.label_5.setGeometry(QtCore.QRect(10, 370, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(123, 123, 123, 0.5);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_5.setObjectName("label_5")
        self.progressBar_2 = QtWidgets.QProgressBar(self.page2)
        self.progressBar_2.setGeometry(QtCore.QRect(250, 430, 381, 23))
        self.progressBar_2.setProperty("value", 3)
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_3 = QtWidgets.QLabel(self.page2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1061, 531))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("iconescanner/capafundo.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page2)
        self.label_4.setGeometry(QtCore.QRect(350, 390, 131, 31))
        self.label_4.setStyleSheet("background-color: rgb(123, 123, 123, 0.5);\n"
"color: rgb(0, 0, 0);\n"
"font: 87 14pt \"Arial Black\";")
        self.label_4.setObjectName("label_4")
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.listWidget_2.raise_()
        self.lineEdit_2.raise_()
        self.ip.raise_()
        self.ip_inicial.raise_()
        self.ip_final.raise_()
        self.tipo_ip_box1.raise_()
        self.tipo_ip_box2.raise_()
        self.label.raise_()
        self.ip_3.raise_()
        self.label_5.raise_()
        self.progressBar_2.raise_()
        self.label_4.raise_()
        self.stackedWidget.addWidget(self.page2)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1115, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.tela1 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("iconescanner/home33.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tela1.setIcon(icon4)
        self.tela1.setObjectName("tela1")
        self.tela2 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("iconescanner/pagina1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tela2.setIcon(icon5)
        self.tela2.setObjectName("tela2")
        self.toolBar.addAction(self.tela1)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.tela2)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NOME-PC"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IP LOCAL"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IP WEB"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ENDERE??O MAC"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "FABRICANTE"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "STATUS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "IP"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "PRINT"))
        self.BT_Scanner.setText(_translate("MainWindow", "SCANNER"))
        self.BT_deleta.setText(_translate("MainWindow", "DELETE"))
        self.BT_VER.setText(_translate("MainWindow", "VISUALIZAR"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "DIGITE IP INICIAL"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "DIGITE IP FINAL"))
        self.ip.setText(_translate("MainWindow", "SCANNERIP"))
        self.tipo_ip_box1.setText(_translate("MainWindow", "IP_INICIAL"))
        self.tipo_ip_box2.setText(_translate("MainWindow", "IP_FINAL"))
        self.label.setText(_translate("MainWindow", "SELECIONA IP"))
        self.ip_3.setText(_translate("MainWindow", "SCANNERIPSL"))
        self.label_5.setText(_translate("MainWindow", "DIGITE O IP DESEJA"))
        self.label_4.setText(_translate("MainWindow", "loading...."))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.tela1.setText(_translate("MainWindow", "TELA"))
        self.tela2.setText(_translate("MainWindow", "TELA2"))
