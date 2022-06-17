import json
from clientes_obj import Cliente

def cargar_clientes():
    clientes = []

    with open('/bd_clientes.py', 'r') as file:
        bd_clientes = json.load(file)
        for cliente in bd_clientes:
            clientes.append(
                Cliente(
                    cliente['id_cliente'],
                    cliente['nombre'],
                    cliente['apellido'],
                    cliente['DNI'],
                    cliente['telefono'],
                    cliente['email'],
                    cliente['estado'],
                    cliente['carrito']
                )
            )
    return clientes