#comidas_controlador.py

from vista.comidas_vista import ComidasVista
from model.comida import Comida

class ComidasControlador:
    def __init__(self, comida_repositorio):
        self.comida_repositorio = comida_repositorio
        self.vista = ComidasVista()

    def listar(self):
        comidas = self.comida_repositorio.todos()
        self.vista.mostrar(comidas)

    def agregar(self):
        nombre = self.vista.pedir('nombre')
        precio = self.vista.pedir('precio')
        comida = Comida(nombre=nombre, precio=precio)
        self.comida_repositorio.agregar(comida)
