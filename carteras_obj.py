class Carteras:
    def __init__(self, id, fecha_ingreso, marca_cartera, color):
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.marca_cartera = marca_cartera
        self.color = color


class Mochila(carteras):
    def __init__(self, id, fecha_ingreso, modelo_cartera, marca_cartera, color):
        super().__init__(id, fecha_ingreso, modelo_cartera, marca_cartera, color)
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.modelo_cartera = modelo_cartera
        self.marca_cartera = marca_cartera
        self.color = color


class CrossBody(carteras):
    def __init__(self, id, fecha_ingreso, modelo_cartera, marca_cartera, color):
        super().__init__(id, fecha_ingreso, modelo_cartera, marca_cartera, color)
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.modelo_cartera = modelo_cartera
        self.marca_cartera = marca_cartera
        self.color = color


class Clutch(carteras):
    def __init__(self, id, fecha_ingreso, modelo_cartera, marca_cartera, color):
        super().__init__(id, fecha_ingreso, modelo_cartera, marca_cartera, color)
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.modelo_cartera = modelo_cartera
        self.marca_cartera = marca_cartera
        self.color = color


class Totebag(carteras):
    def __init__(self, id, fecha_ingreso, modelo_cartera, marca_cartera, color):
        super().__init__(id, fecha_ingreso, modelo_cartera, marca_cartera, color)
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.modelo_cartera = modelo_cartera
        self.marca_cartera = marca_cartera
        self.color = color
