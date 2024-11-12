class Asiento:
    def __init__(self, color, precio, registro):
        self.color
        self.precio
        self.registro

    def camniarColor(self, color):
        while True:
            if color == "rojo" or color == "verde" or color = "negro" or color = "amarillo" or color = "blanco":
                self.color = color
                break
            else: 
                continue

class Auto:
    def __init__(self, precio, modelo, asientos, marca, motor, registro, cantidadCreados):
        self.precio
        self.modelo
        self.asientos
        self.marca
        self.motor
        self.registro
        self.cantidadCreados

    def cantidadAsientos(self, asientos):
        numAsientos = 0
        for i in len(asientos):
            numAsientos = numAsientos + 1
        return numAsientos
    
    def verificarIntegridad(self, motor , registro):
        if self.motor == self.registro:
            for i in len(self.asientos):
                if self.asientos[i] != "":
                    if self.asientos.registro != self.registro:
                        return "las piezas no son originales"
        
        return "auto original"
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros
        self.tipo
        self.registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        while True:
            if tipo == "electrico" or tipo == "gasolina":
                self.tipo = tipo
                break
            else:
                continue








    







            
        