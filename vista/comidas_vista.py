#comidas_vista.py

class ComidasVista:
    def mostrar(self, comidas):
        for comida in comidas:
            print(f"{comida.id}. {comida.nombre} - {comida.precio} $")

    def pedir(self, atributo):
        print(f"{atributo.capitalize()}?")
        return input('> ')
