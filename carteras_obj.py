class Carteras:
    def __init__(self, id, fecha_ingreso, marca, color):
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.marca = marca
        self.color = color


class Mochila(Carteras):
    def __init__(self, id, fecha_ingreso, marca, color):
        super().__init__(id, fecha_ingreso,  marca, color)
        self.modelo = "Mochila"


class CrossBody(Carteras):
    def __init__(self, id, fecha_ingreso, modelo, marca, color):
        super().__init__(id, fecha_ingreso, modelo, marca, color)
        self.modelo = "Cross body"


class Clutch(Carteras):
    def __init__(self, id, fecha_ingreso, modelo, marca, color):
        super().__init__(id, fecha_ingreso, modelo, marca, color)
        self.modelo = "Clutch"


class Totebag(Carteras):
    def __init__(self, id, fecha_ingreso, modelo, marca, color):
        super().__init__(id, fecha_ingreso, modelo, marca, color)
        self.modelo = "Totebag"
