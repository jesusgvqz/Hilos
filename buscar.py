# Importar bibliotecas
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QPlainTextEdit, \
    QLabel

# Subclase QMainWindow
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi buscador")
        contenedor = QWidget()
        lytPrincipal = QGridLayout()

        lblBusca = QLabel("Palabra: ")
        self.lnedtTexto = QLineEdit()
        btnBusca = QPushButton("Buscar")
        btnBusca.clicked.connect(self.buscarTexto)

        self.texto = QPlainTextEdit()

        lytPrincipal.addWidget(lblBusca, 0, 0)
        lytPrincipal.addWidget(self.lnedtTexto, 0, 1)
        lytPrincipal.addWidget(btnBusca, 0, 2)
        lytPrincipal.addWidget(self.texto, 1, 0, 1, 3)

        contenedor.setLayout(lytPrincipal)
        self.setCentralWidget(contenedor)


    def buscarTexto(self):
        cursor = self.texto.textCursor()
        cursor.setPosition(0)
        self.texto.setTextCursor(cursor)
        cadena = self.lnedtTexto.text()
        escrito = self.texto.find(cadena)
        print("Escrito: ", escrito)


app = QApplication([])
window = VentanaPrincipal()
window.show()

app.exec_()