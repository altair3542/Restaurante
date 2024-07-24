from controller.clientes_controlador import ClientesControlador
from controller.comidas_controlador import ComidasControlador

class Router:
    def __init__(self, clientes_controlador, comidas_controlador):
        self.clientes_controlador = clientes_controlador
        self.comidas_controlador = comidas_controlador

    def run(self):
        while True:
            print("\n--- MENU ---")
            print("1. Listar clientes")
            print("2. Agregar cliente")
            print("3. Listar comidas")
            print("4. Agregar comida")
            print("5. Salir")

            choice = input("Elige una opción: ")
            if choice == "1":
                self.clientes_controlador.listar()
            elif choice == "2":
                self.clientes_controlador.agregar()
            elif choice == "3":
                self.comidas_controlador.listar()
            elif choice == "4":
                self.comidas_controlador.agregar()
            elif choice == "5":
                break
            else:
                print("Opción no válida, por favor intenta de nuevo.")
