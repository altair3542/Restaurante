#cliente_repositorio.py

import csv
import os
from model.cliente import Cliente


class ClienteRepositorio:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.clientes = []
        self.cargar_csv()

    def todos(self):
        return self.clientes

    def agregar(self, cliente):
        self.clientes.append(cliente)
        self.guardar_csv()

    def cargar_csv(self):
        if os.path.exists(self.archivo_csv):
            with open(self.archivo_csv, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.clientes.append(Cliente(id=int(row['id']), nombre=row['nombre'], direccion=row['direccion']))

    def guardar_csv(self):
        with open(self.archivo_csv, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nombre', 'direccion'])
            writer.writeheader()
            for cliente in self.clientes:
                writer.writerow({'id': cliente.id, 'nombre': cliente.nombre, 'direccion': cliente.direccion})
