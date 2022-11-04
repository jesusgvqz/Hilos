# Importar bibliotecas

import json
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QPlainTextEdit, QLabel
from PyQt5.QtGui import QImage, QPixmap


# Subclase QMainWindow
class VentanaPrincipal(QMainWindow):

    def _init_(self):
        super()._init_()
        self.setWindowTitle("Mi buscador de peliculas")
        self.resize(1000, 800)
        contenedor = QWidget()
        self.lytPrincipal = QGridLayout()

        lblBusca = QLabel("Palabras: ")
        self.lnedtTexto = QLineEdit()
        self.btnBusca = QPushButton("Buscar")
        self.btnBusca.clicked.connect(self.split_text)

        self.texto = QPlainTextEdit()

        leftcolumna = QWidget()
        centercolumna = QWidget()
        rightcolumna = QWidget()

        self.lytPrincipal.addWidget(lblBusca, 0, 0)
        self.lytPrincipal.addWidget(self.lnedtTexto, 0, 1)
        self.lytPrincipal.addWidget(self.btnBusca, 0, 2)
        self.lytPrincipal.addWidget(leftcolumna, 1, 0)
        self.lytPrincipal.addWidget(centercolumna, 1, 1)
        self.lytPrincipal.addWidget(rightcolumna, 1, 2)

        contenedor.setLayout(self.lytPrincipal)
        self.setCentralWidget(contenedor)
    def split_text(self):
        palabras = []
        lista = self.lnedtTexto.text()
        print(lista)
        for palabras in lista:
            palabras = lista.split(",")
        for i in palabras:
            self.get_movies(i)


    def get_movies(self, palabra):
        url_servicio = "http://clandestina-hds.com:80/movies/title?search="
        r = requests.get(url_servicio + palabra)
        peliculas_data = r.json()
        index = 0
        limit = 4
        for pelicula in peliculas_data['results']:
            print("La pelicula de nombre: {} \n Tiene una URL de imagen: {} \n Resumen :{} \ Aritstas: {}" .format(pelicula['title'],
                                                                                    pelicula["image"],
                                                                                    pelicula['plot'],
                                                                                    pelicula['starList']))
            self.show_movie(pelicula["image"])
            index = index + 1
            if index == limit:
                break


    def show_movie(self, url_image):
        image = QImage()
        image.loadFromData(requests.get(url_image).content)
        pixi = QPixmap.fromImage(image).scaled(185, 185)
        image_label = QLabel()
        image_label.setPixmap(QPixmap(pixi))

        image_label.show()
        self.lytPrincipal.addWidget(image_label)
        self.contenedor.setLayout(self.lytPrincipal)
        self.setCentralWidget(self.contenedor)


    def serch_text(self):
        cursor = self.texto.textCursor()
        cursor.setPosition(0)
        self.texto.setTextCursor(cursor)
        cadena = self.lnedtTexto.text()
        escrito = self.texto.find(cadena)
        print("Película: ", escrito)


app = QApplication([])
window = VentanaPrincipal()
window.show()

app.exec_()
