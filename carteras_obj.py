class Carteras:
    def __init__(self, id, fecha_ingreso, marca, color):
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.marca = marca
        self.color = color

    def serialize(self):
        return {
            'id': self.id,
            'fecha_ingreso': self.fecha_ingreso,
            'marca': self.marca,
            'color': self.color
        }


class Mochila(Carteras):
    def __init__(self, id, fecha_ingreso, marca, color):
        super().__init__(id, fecha_ingreso,  marca, color)
        self.modelo = "Mochila"

    def serialize(self):
        return {
            'id': self.id,
            'fecha_ingreso': self.fecha_ingreso,
            'marca': self.marca,
            'color': self.color,
            'modelo': self.modelo
        }


class CrossBody(Carteras):
    def __init__(self, id, fecha_ingreso, modelo, marca, color):
        super().__init__(id, fecha_ingreso, modelo, marca, color)
        self.modelo = "Cross body"

    def serialize(self):
        return {
            'id': self.id,
            'fecha_ingreso': self.fecha_ingreso,
            'marca': self.marca,
            'color': self.color,
            'modelo': self.modelo
        }


class Clutch(Carteras):
    def __init__(self, id, fecha_ingreso, modelo, marca, color):
        super().__init__(id, fecha_ingreso, modelo, marca, color)
        self.modelo = "Clutch"

    def serialize(self):
        return {
            'id': self.id,
            'fecha_ingreso': self.fecha_ingreso,
            'marca': self.marca,
            'color': self.color,
            'modelo': self.modelo
        }


class Totebag(Carteras):
    def __init__(self, id, fecha_ingreso, modelo, marca, color):
        super().__init__(id, fecha_ingreso, modelo, marca, color)
        self.modelo = "Totebag"

    def serialize(self):
        return {
            'id': self.id,
            'fecha_ingreso': self.fecha_ingreso,
            'marca': self.marca,
            'color': self.color,
            'modelo': self.modelo
        }
