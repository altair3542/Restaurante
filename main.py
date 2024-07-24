#main.py
from repository.cliente_repositorio import ClienteRepositorio
from repository.comida_repositorio import ComidaRepositorio
from controller.clientes_controlador import ClientesControlador
from controller.comidas_controlador import ComidasControlador
from router import Router

def main():
    cliente_repositorio = ClienteRepositorio('clientes.csv')
    comida_repositorio = ComidaRepositorio('comidas.csv')

    clientes_controlador = ClientesControlador(cliente_repositorio)
    comidas_controlador = ComidasControlador(comida_repositorio)

    router = Router(clientes_controlador, comidas_controlador)
    router.run()

if __name__ == '__main__':
    main()
