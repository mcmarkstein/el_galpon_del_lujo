import random

def generador_id_cliente():
    return str(random.randint(00000, 99999))


class Cliente:

    def __init__(self, id_cliente, nombre, apellido, DNI, telefono, email, estado):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.DNI = DNI
        self.telefono = telefono
        self.email = email
        self.estado = estado

    def serialize(self):
        return {
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'apellido': self.last_name,
            'DNI': self.DNI
            'telefono': self.telefono
            self.email
            self.estado

            'address': self.address.serialize()
        }


class ClientAddress:

    def __init__(self, street, street_number, city, state, post_code, country) -> None:
        self.street = street

    self.street_number = street_number
    self.city = city
    self.state = state
    self.post_code = post_code
    self.country = country

    def serialize(self):
        return {
            'street': self.state,
            'street_number': self.street_number,
            'city': self.city,
            'state': self.state,
            'post_code': self.post_code,
            'country': self.country
        }

