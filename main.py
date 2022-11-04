"""
Proyecto de ventana de busqueda.
Programacion de Sistemas.
Lic. Redes y Servicios de Computo.

Aldahir Abisai Leal Cardeña
Jesus Heron Galvez Vazquez
"""

# importacion de librerias
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QPlainTextEdit, QLabel
from PyQt5.QtGui import QImage, QPixmap


# clase principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proyecto Busqueda Peliculas")
        self.resize(775, 365)
        self.container = QWidget()
        self.container.setStyleSheet('background-color: grey')
        self.mainLyt = QGridLayout()

        # declaracion del header del contenedor
        search_label = QLabel("palabras clave: 'xx, yy'")
        search_label.setStyleSheet(
            'color: white; font-size: 15px; height: 40px;')
        self.line_text = QLineEdit()
        self.line_text.setStyleSheet('color: white;')
        self.search_button = QPushButton("buscar")
        self.search_button.setStyleSheet('color: white; font-size: 15px')
        self.search_button.clicked.connect(self.split_text)
        self.text = QPlainTextEdit()

        # definicion de columnas
        lColumn = QWidget()
        clColumn = QWidget()
        crColumn = QWidget()
        rColumn = QWidget()

        # se agregan los widgets al grid
        self.mainLyt.addWidget(search_label, 0, 0)
        self.mainLyt.addWidget(self.line_text, 0, 1, 1, 2)
        self.mainLyt.addWidget(self.search_button, 0, 3)
        self.mainLyt.addWidget(lColumn, 1, 0)
        self.mainLyt.addWidget(clColumn, 1, 1)
        self.mainLyt.addWidget(crColumn, 1, 2)
        self.mainLyt.addWidget(rColumn, 1, 3)

        # se define el layout
        self.container.setLayout(self.mainLyt)
        self.setCentralWidget(self.container)

    # identificacion de palabras clave
    def split_text(self):
        keywords = []
        list = self.line_text.text()
        print(list)
        for keywords in list:
            keywords = list.split(",")
        for i in keywords:
            self.get_movies(i)

    # recopilacion de peliculas
    def get_movies(self, keywords):
        url_service = "http://clandestina-hds.com:80/movies/title?search="
        r = requests.get(url_service + keywords)
        movie_data = r.json()
        index = 0
        limit = 4
        for movie in movie_data['results']:
            print("La pelicula de nombre: {} \n Tiene una URL de imagen: {} \n Resumen :{} \n Artistas: {}" .format(movie['title'],
                                                                                                                    movie['image'],
                                                                                                                    movie['plot'],
                                                                                                                    movie['starList']))
            self.show_movie(movie['image'])
            index = index + 1
            if index == limit:
                break

    # muestra de imagenes de peliculas
    def show_movie(self, url_image):
        image = QImage()
        image.loadFromData(requests.get(url_image).content)
        pixi = QPixmap.fromImage(image).scaled(185, 185)
        image_label = QLabel()
        image_label.setPixmap(QPixmap(pixi))
        image_label.show()
        self.mainLyt.addWidget(image_label)
        self.container.setLayout(self.mainLyt)
        self.setCentralWidget(self.container)


app = QApplication([])
window = MainWindow()
window.show()

app.exec_()
