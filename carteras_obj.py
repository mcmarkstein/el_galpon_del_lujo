class Carteras:
    def __init__(self, id, fecha_ingreso, marca, color, tipo_de_cambio, precio):
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.marca = marca
        self.color = color
        self.tipo_de_cambio = tipo_de_cambio
        self.precio = precio


    def serialize(self):
        return {
            'id': self.id,
            'fecha_ingreso': self.fecha_ingreso,
            'marca': self.marca,
            'color': self.color,
            'tipo_de_cambio': self.tipo_de_cambio
            'precio': self.precio
        }


class Mochila(Carteras):
    def __init__(self, id, fecha_ingreso, marca, color, tipo_de_cambio, precio):
        super().__init__(id, fecha_ingreso,  marca, color, tipo_de_cambio, precio)
        self.modelo = "Mochila"

    def serialize(self):
        return {
            'id': self.id,
            'fecha_ingreso': self.fecha_ingreso,
            'marca': self.marca,
            'color': self.color,
            'tipo_de_cambio': self.tipo_de_cambio
            'precio': self.precio
        }


class CrossBody(Carteras):
    def __init__(self, id, fecha_ingreso, modelo, marca, color, tipo_de_cambio, precio):
        super().__init__(id, fecha_ingreso, modelo, marca, color, tipo_de_cambio, precio)
        self.modelo = "Cross body"

    def serialize(self):
        return {
            'id': self.id,
            'fecha_ingreso': self.fecha_ingreso,
            'marca': self.marca,
            'color': self.color,
            'tipo_de_cambio': self.tipo_de_cambio
            'precio': self.precio
        }


class Clutch(Carteras):
    def __init__(self, id, fecha_ingreso, modelo, marca, color, tipo_de_cambio, precio):
        super().__init__(id, fecha_ingreso, modelo, marca, color, tipo_de_cambio, precio)
        self.modelo = "Clutch"

    def serialize(self):
        return {
            'id': self.id,
            'fecha_ingreso': self.fecha_ingreso,
            'marca': self.marca,
            'color': self.color,
            'tipo_de_cambio': self.tipo_de_cambio
            'precio': self.precio
        }


class Totebag(Carteras):
    def __init__(self, id, fecha_ingreso, modelo, marca, color, tipo_de_cambio, precio):
        super().__init__(id, fecha_ingreso, modelo, marca, color, tipo_de_cambio, precio)
        self.modelo = "Totebag"

    def serialize(self):
        return {
            'id': self.id,
            'fecha_ingreso': self.fecha_ingreso,
            'marca': self.marca,
            'color': self.color,
            'tipo_de_cambio': self.tipo_de_cambio
            'precio': self.precio
        }
