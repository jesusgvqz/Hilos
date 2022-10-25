import sys
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    app = QApplication([])

    w = QWidget()

# grid de botones
    grid = QGridLayout(w)

    for i in range(3):
        for j in range(3):
            grid.addWidget(QPushButton("Button"),i,j)
#botón combinado
    grid.addWidget(QPushButton("Button comb"), 0, 0, 1, 0)

    w.show()
    sys.exit(app.exec_())

#para dividir las palabras
def dividir_texto(self):
    palabras = []
    lista = self.lnedtTexto.text()
    for palabras in lista:
        palabras = lista.split(",")
    print(palabras)
    for i in palabras:
        print(i)