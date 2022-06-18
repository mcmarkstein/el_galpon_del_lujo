import json
from clientes_obj import Cliente

def cargar_clientes():
    clientes = []

    with open('https://github.com/mcmarkstein/el_galpon_del_lujo/blob/79c1f06b569178a3578a310b00a010b995b9cec6/bd_clientes.py', 'r') as file:
        bd_clientes = json.load(file)
        for cliente in bd_clientes:
            clientes.append(
                Cliente(
                    cliente['id_cliente'],
                    cliente['nombre'],
                    cliente['apellido'],
                    cliente['dni'],
                    cliente['telefono'],
                    cliente['email'],
                    cliente['estado'],
                    cliente['carrito']
                )
            )
    return clientes