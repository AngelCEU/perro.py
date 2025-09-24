class perro: 
    def __init__ (self, nombre, color, color_ojos, altura, longitud, peso):
        self.nombre = nombre
        self.color = color
        self.color_ojos = color_ojos
        self.altura = altura
        self.longitud = longitud
        self.peso = peso

    def __str__(self):
        return f"Perro: {self.nombre}, Color: {self.color}, Ojos: {self.color_ojos}, Altura: {self.altura}cm, Longitud: {self.longitud}cm, Peso: {self.peso}kg"

    def sentarse(self):
        return "El perro se ha sentado"
    def tumbarse(self):
        return "El perro se ha tumbado"
    def pata(self):
        return "El perro ha dado la pata"
    def venir(self):
        return "El perro ha venido"
    


        

  




    
        