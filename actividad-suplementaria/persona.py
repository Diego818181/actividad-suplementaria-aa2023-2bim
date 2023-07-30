import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime

conn = sqlite3.connect('base_personas.db')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 514)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Campos de texto
        self.nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(140, 30, 113, 23))
        self.nombre.setObjectName("nombre")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 54, 15))
        self.label.setObjectName("label")

        self.edad = QtWidgets.QLineEdit(self.centralwidget)
        self.edad.setGeometry(QtCore.QRect(140, 70, 113, 23))
        self.edad.setText("")
        self.edad.setObjectName("edad")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 54, 15))
        self.label_2.setObjectName("label_2")

        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(140, 110, 113, 23))
        self.email.setText("")
        self.email.setObjectName("email")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 110, 54, 15))
        self.label_3.setObjectName("label_3")

        self.telefono = QtWidgets.QLineEdit(self.centralwidget)
        self.telefono.setGeometry(QtCore.QRect(140, 150, 113, 23))
        self.telefono.setText("")
        self.telefono.setObjectName("telefono")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 150, 54, 15))
        self.label_4.setObjectName("label_4")

        self.direccion = QtWidgets.QLineEdit(self.centralwidget)
        self.direccion.setGeometry(QtCore.QRect(140, 190, 113, 23))
        self.direccion.setText("")
        self.direccion.setObjectName("direccion")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 190, 54, 15))
        self.label_5.setObjectName("label_5")

        # Botones
        self.guardar = QtWidgets.QPushButton(self.centralwidget)
        self.guardar.setGeometry(QtCore.QRect(70, 230, 211, 21))
        self.guardar.setObjectName("guardar")
        self.actualizar = QtWidgets.QPushButton(self.centralwidget)
        self.actualizar.setGeometry(QtCore.QRect(70, 270, 211, 21))
        self.actualizar.setObjectName("actualizar")

        # Grilla con nombres de columnas
        self.listaPersonas = QtWidgets.QTableWidget(self.centralwidget)
        self.listaPersonas.setGeometry(QtCore.QRect(70, 310, 551, 171))
        self.listaPersonas.setObjectName("listaPersonas")
        self.listaPersonas.setColumnCount(5)
        self.listaPersonas.setRowCount(0)
        self.listaPersonas.setHorizontalHeaderLabels(["Nombre", "Edad", "Correo electronico", "Telefono", "Direccion"])

        # Organizacion de elementos
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.nombre)
        self.layout.addWidget(self.label_2)
        self.layout.addWidget(self.edad)
        self.layout.addWidget(self.label_3)
        self.layout.addWidget(self.email)
        self.layout.addWidget(self.label_4)
        self.layout.addWidget(self.telefono)
        self.layout.addWidget(self.label_5)
        self.layout.addWidget(self.direccion)
        self.layout.addWidget(self.guardar)
        self.layout.addWidget(self.actualizar)
        self.layout.addWidget(self.listaPersonas)
        self.centralwidget.setLayout(self.layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.crear_tabla()
        self.guardar.clicked.connect(self.guardar_informacion)
        self.actualizar.clicked.connect(self.obtener_informacion)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nombre"))
        self.label_2.setText(_translate("MainWindow", "Edad"))
        self.label_3.setText(_translate("MainWindow", "Correo"))
        self.label_4.setText(_translate("MainWindow", "Telefono"))
        self.label_5.setText(_translate("MainWindow", "Direccion"))
        self.guardar.setText(_translate("MainWindow", "Guardar"))
        self.actualizar.setText(_translate("MainWindow", "Actualizar"))

    def crear_tabla(self):
        cursor = conn.cursor()
        cadena_sql = 'CREATE TABLE IF NOT EXISTS Persona (nombre TEXT, edad INTEGER, email TEXT, telefono TEXT, direccion TEXT)'
        cursor.execute(cadena_sql)
        cursor.close()

    def guardar_informacion(self):
        cursor = conn.cursor()
        nombre = str(self.nombre.text())
        edad = int(self.edad.text())
        email = str(self.email.text())
        telefono = str(self.telefono.text())
        direccion = str(self.direccion.text())
        cadena_sql = """INSERT INTO Persona (nombre, edad, email, telefono, direccion) VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(cadena_sql, (nombre, edad, email, telefono, direccion))
        conn.commit()
        self.obtener_informacion()  # Llamamos a esta funcion despues de guardar para actualizar la tabla
        cursor.close()

    def obtener_informacion(self):
        cursor = conn.cursor()
        cadena_consulta_sql = "SELECT * from Persona"
        cursor.execute(cadena_consulta_sql)
        informacion = cursor.fetchall()
        self.listaPersonas.setRowCount(0)
        for row_num, row_data in enumerate(informacion):
            self.listaPersonas.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.listaPersonas.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))
        cursor.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
