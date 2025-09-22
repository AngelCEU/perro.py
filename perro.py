class perro: 
    def __init__ (self, nombre, color, color_ojos, altura, longitud, peso):
        self.nombre = nombre
        self.color = color
        self.color_ojos = color_ojos
        self.altura = altura
        self.longitud = longitud
        self.peso = peso

    def sentarse(self):
        return "El perro se ha sentado"
    def tumbarse(self):
        return "El perro se ha tumbado"
    def pata(self):
        return "El perro ha dado la pata"
    def venir(self):
        return "El perro ha venido"
    
if __name__ == "__main__":
    perro1 = perro("Bobby", "marrón", "avellana", 50, 80, 20)
    perro2 = perro("Luna", "blanco", "azul", 45, 75, 25)
    

        

  




    
        