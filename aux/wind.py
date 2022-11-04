from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Chafa")
        contenedor = QWidget()
        lytPrincipal = QHBoxLayout()
        search_bar = QHBoxLayout()
        self.btn_search = QPushButton("Buscar")
        search_bar.addWidget(self.btn_search)
        lytPrincipal.addLayout(search_bar)
        contenedor.setLayout(lytPrincipal)
        self.setCentralWidget(contenedor)

app = QApplication([])
window = VentanaPrincipal()
window.show()
app.exec_()
