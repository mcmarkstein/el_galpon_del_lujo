from typing import List, Dict, Tuple
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


class Productos(Resource):
    def __init__(self, id: int, nombre: str, color: str, precio: float, marca: str):
        self.id_producto = id
        self.nombre = nombre
        self.color = color
        self.precio = precio
        self.marca = marca

    def get(self):
        data = pd.read_csv(  # archivo con la data)
            data=data.to_dict()  # convierte data frame a diccionario
        return {'data': data}, 200  # falta poner arriba el archivo (linea 21)

    def post(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('id_producto', required=True)
        parser.add_argument('nombre', required=True)  # add args
        parser.add_argument('color', required=True)
        parser.add_argument('precio', required=True)
        parser.add_argument('marca', required=True)

        args = parser.parse_args()  # parsea los argumentos a diccionario

        new_data = pd.DataFrame({
            'id_producto': args['id_producto'],
            'nombre': args['nombre'],
            'color': args['color'],
            'precio': args['precio'],
            'marca': args['marca'],
        })

        data = pd.read_csv(  # de donde vamos a leer??)

            data=data.append(new_data, ignore_index=True)

        data.to_csv(  # donde guardamos??, index=False)
        return {'data': data.to_dict()}, 200

    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('id_producto', required=True)
        parser.add_argument('nombre', required=True)  # add args
        parser.add_argument('color', required=True)
        parser.add_argument('precio', required=True)
        parser.add_argument('marca', required=True)
        args = parser.parse_args()  # parsea argumentos a diccionario

        data = pd.read_csv(  # archivo con la data)

        # falta terminar este método

    def delete(self):


# hay que agarrar el id del producto a eliminar
# luego eliminarlo de la base de datos
# guardar base de datos


api.add_resource(Productos, '/productos)