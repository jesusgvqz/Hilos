import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QImage, QPixmap


url_image = 'https://m.media-amazon.com/images/M/MV5BNjk2ODQzNDYxNV5BMl5BanBnXkFtZTgwMTcyNDg4NjE@._V1_Ratio0.6837_AL_.jpg'

app = QApplication([])

image = QImage()
image.loadFromData(requests.get(url_image).content)

image_label = QLabel()
pixmap = QPixmap(image)
pixmap2 = pixmap.scaledToWidth(500)
image_label.setPixmap(pixmap2)
image_label.show()

app.exec_()
