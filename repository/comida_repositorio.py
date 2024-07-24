#comida_repositorio.py

import csv
from model.comida import Comida
import os

class ComidaRepositorio:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.comidas = []
        if not os.path.exists(self.archivo_csv):
            self.crear_csv()
        self.cargar_csv()

    def todos(self):
        return self.comidas

    def agregar(self, comida):
        comida.id = len(self.comidas) + 1
        self.comidas.append(comida)
        self.guardar_csv()

    def cargar_csv(self):
        if os.path.exists(self.archivo_csv):
            with open(self.archivo_csv, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        id = int(row['id'])
                        precio = float(row['precio'])
                    except ValueError:
                        continue  # Ignorar filas con ID o precio inválidos
                    self.comidas.append(Comida(id=id, nombre=row['nombre'], precio=precio))

    def guardar_csv(self):
        with open(self.archivo_csv, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nombre', 'precio'])
            writer.writeheader()
            for comida in self.comidas:
                writer.writerow({'id': comida.id, 'nombre': comida.nombre, 'precio': comida.precio})

    def crear_csv(self):
        with open(self.archivo_csv, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nombre', 'precio'])
            writer.writeheader()
