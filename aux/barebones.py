# Importar bibliotecas
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel, \
    QPlainTextEdit
from PyQt5.QtGui import QPixmap, QImage
import requests


#este es el esqueleto del programa

# Subclase QMainWindow
class VentanaPrincipal(QMainWindow):

    def _init_(self):
        super()._init_()
        self.setWindowTitle("Mi buscador de peliculas")
        self.resize(1000, 800)
        self.contenedor = QWidget()
        self.lytPrincipal = QGridLayout()

        lblBusca = QLabel("Palabras: ")
        self.lnedtTexto = QLineEdit()
        self.btnBusca = QPushButton("Buscar")
        self.btnBusca.clicked.connect(self.split_text)

        self.texto = QPlainTextEdit()
        leftcolumna = QWidget()
        centercolumna = QWidget()
        rightcolumna = QWidget()

        self.lytPrincipal = QGridLayout()
        self.lblBusca = QLabel("Palabras de peliculas a buscar: ")

        self.lnedtTexto = QLineEdit()
        self.btnBusca = QPushButton("Buscar")
        self.lytPrincipal.addWidget(lblBusca, 0, 0)
        self.btnBusca.clicked.connect(self.split_text)
        self.lytPrincipal.addWidget(self.lblBusca, 0, 0)
        self.lytPrincipal.addWidget(self.lnedtTexto, 0, 1)
        self.lytPrincipal.addWidget(self.btnBusca, 0, 2)
        self.lytPrincipal.addWidget(leftcolumna, 1, 0)
        self.lytPrincipal.addWidget(centercolumna, 1, 1)
        self.lytPrincipal.addWidget(rightcolumna, 1, 2)

        self.contenedor.setLayout(self.lytPrincipal)
        self.setCentralWidget(self.contenedor)

    def split_text(self):
        palabras = []
        lista = self.lnedtTexto.text()
        for palabras in lista:
            palabras = lista.split(",")
        print(palabras)
        for i in palabras:
            self.get_peliculas(i)

    def get_peliculas(self, palabra):
        url_servicio = "http://clandestina-hds.com:80/movies/title?search="
        r = requests.get(url_servicio + palabra)
        peliculas_data = r.json()
        index = 0
        limit = 3
        for pelicula in peliculas_data['results']:
            print("La pelicula de nombre: {} \n Tiene una URL de imagen: {}".format(pelicula['title'],
                                                                                    pelicula["image"]))
            self.mostrarimagenes(pelicula["image"])
            #Thread
            index = index + 1
            if index == limit:
                break

    def mostrarimagenes(self, url_image):
        image = QImage()
        image.loadFromData(requests.get(url_image).content)
        pixi = QPixmap.fromImage(image).scaled(350, 250)
        image_label = QLabel()
        image_label.setPixmap(QPixmap(pixi))
        image_label.show()

        self.lytPrincipal.addWidget(image_label)
        self.contenedor.setLayout(self.lytPrincipal)
        self.setCentralWidget(self.contenedor)


app = QApplication(sys.argv)
window = VentanaPrincipal()
window.show()

app.exec_()
