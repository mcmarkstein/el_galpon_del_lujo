class Carteras:
    def __init__(self, id, date_created, marca_cartera, color):
        self.id = id
        self.date_created = date_created
        self.marca_cartera = marca_cartera
        self.color = color


class Mochila(carteras):
    def __init__(self, id, date_created, modelo_cartera, marca_cartera, color):
        super().__init__(id, date_created, modelo_cartera, marca_cartera, color)
        self.id = id
        self.date_created = date_created
        self.modelo_cartera = modelo_cartera
        self.marca_cartera = marca_cartera
        self.color = color


class CrossBody(carteras):
    def __init__(self, id, date_created, modelo_cartera, marca_cartera, color):
        super().__init__(id, date_created, modelo_cartera, marca_cartera, color)
        self.id = id
        self.date_created = date_created
        self.modelo_cartera = modelo_cartera
        self.marca_cartera = marca_cartera
        self.color = color


class Clutch(carteras):
    def __init__(self, id, date_created, modelo_cartera, marca_cartera, color):
        super().__init__(id, date_created, modelo_cartera, marca_cartera, color)
        self.id = id
        self.date_created = date_created
        self.modelo_cartera = modelo_cartera
        self.marca_cartera = marca_cartera
        self.color = color


class Totebag(carteras):
    def __init__(self, id, date_created, modelo_cartera, marca_cartera, color):
        super().__init__(id, date_created, modelo_cartera, marca_cartera, color)
        self.id = id
        self.date_created = date_created
        self.modelo_cartera = modelo_cartera
        self.marca_cartera = marca_cartera
        self.color = color
