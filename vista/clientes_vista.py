#clientes_vista.py

class ClientesVista:
    def mostrar(self, clientes):
        for cliente in clientes:
            print(f"{cliente.id}, {cliente.nombre} - {cliente.direccion} ")

    def pedir(self, atributo):
        print(f"atributo.capitalize()?")
        return input("> ")
