import json
from carteras_obj import Carteras, Mochila, Totebag, Clutch, CrossBody      #Preguntar

def cargar_carteras():
    carteras = []

    with open('/bd_carteras.py', 'r') as file:
        bd_carteras = json.load(file)
        for cartera in bd_carteras:

            carteras.append(
                Carteras(
                    cartera['id'],
                    cartera['fecha_ingreso'],
                    cartera['modelo'],
                    cartera['marca'],
                    cartera['color']
                )
            )
    return carteras
