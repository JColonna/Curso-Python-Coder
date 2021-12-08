
class Vehiculo():
    tipo = 'Deportivo'

    def __init__(self, marca, modelo, año,velocidad):

        self.marca = marca
        self.modelo = modelo
        self.año = año 
        self.velocidad = velocidad

    def mostrar(self):
        print(f' Marca {self.marca} \n Modelo {self.modelo}\n Año: {self.año} \n Velocidad Maxima: {self.velocidad}')

