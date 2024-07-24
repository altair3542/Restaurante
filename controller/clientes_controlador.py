#clientes_controlador.py

from vista.clientes_vista import ClientesVista
from model.cliente import Cliente

class ClientesControlador:
    def __init__(self, cliente_repositorio):
        self.cliente_repositorio = cliente_repositorio
        self.vista = ClientesVista()

    def listar(self):
        clientes = self.cliente_repositorio.todos()
        self.vista.mostrar(clientes)

    def agregar(self):
        nombre = self.vista.pedir('nombre')
        direccion = self.vista.pedir('direccion')
        cliente = Cliente(nombre=nombre, direccion=direccion)
        self.cliente_repositorio.agregar(cliente)
