class perro: 
    def __init__ (self, nombre, color, color_ojos, altura, longitud, peso):
        self.nombre = nombre
        self.color = color
        self.color_ojos = color_ojos
        self.altura = altura
        self.longitud = longitud
        self.peso = peso

    def __str__(self):
        return f"Perro: se llama {self.nombre}, es de color {self.color}, sus Ojos son de color {self.color_ojos}, mide {self.altura}cm de altira, {self.longitud}cm de largo, y pesa {self.peso} kg"

    def sentarse(self):
        return "El perro se ha sentado"
    def tumbarse(self):
        return "El perro se ha tumbado"
    def pata(self):
        return "El perro ha dado la pata"
    def venir(self):
        return "El perro ha venido"
    


        

  




    
        