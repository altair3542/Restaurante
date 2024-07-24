#comida_repositorio.py

import csv
import os
from model.comida import Comida


class ComidaRepositorio:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.comidas = []
        self.cargar_csv()

    def todos(self):
        return self.comidas

    def agregar(self, comida):
        self.comidas.append(comida)
        self.guardar_csv()

    def cargar_csv(self):
        if os.path.exists(self.archivo_csv):
            with open(self.archivo_csv, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.comidas.append(Comida(id=int(row['id']), nombre=row['nombre'], precio=float(row['precio'])))

    def guardar_csv(self):
        with open(self.archivo_csv, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nombre', 'precio'])
            writer.writeheader()
            for comida in self.comidas:
                writer.writerow({'id': comida.id, 'nombre': comida.nombre, 'precio': comida.precio})
