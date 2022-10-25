

#para dividir las palabras
def dividir_texto(self):
    palabras = []
    lista = self.lnedtTexto.text()
    for palabras in lista:
        palabras = lista.split(",")
    print(palabras)
    for i in palabras:
        self.get_peliculas(i)