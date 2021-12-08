

class Atleta():

    tipo = 'Atletico'

    def __init__ (self, nombre, apellido, altura, peso, telefono):

        self.nombre = nombre
        self.apellido = apellido
        self.altura = altura
        self.peso = peso
        self.telefono = telefono
        self.imc = peso/((altura/100)**2)
    
    def correr(self):
        print('El atleta esta corriendo')
    
    def saltar(self):
        print('El atleta esta saltando')

atleta1 = Atleta('Juan', 'Pedretti', 175, 85, 1155254444)

atleta1.nombre()