class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ["rojo", "verde", "negro", "amarillo", "blanco"]:
            self.color = color


class Auto:
    cantidadCreados = 0
    
    def __init__(self, precio, modelo, asientos, marca, motor, registro):
        self.precio = precio
        self.modelo = modelo 
        self.asientos = asientos
        self.marca = marca
        self.motor = motor   
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        return sum(1 for asiento in self.asientos if asiento is not None)
    
    def verificarIntegridad(self):
        if self.motor.registro != self.registro:
            return "Las piezas no son originales"
        
        for asiento in self.asientos:
            if asiento is not None and asiento.registro != self.registro:
                return "Las piezas no son originales"

        return "Auto original"
        

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo





    







            
        
