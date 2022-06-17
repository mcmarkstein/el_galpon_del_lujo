import json
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response

from clientes_obj import Cliente, generador_id_cliente
from load_cliente import cargar_clientes
from carteras_obj import Carteras, Totebag, CrossBody, Clutch, Mochila
from load_cartera import cargar_carteras

app = Flask(__name__)
clientes: list = cargar_clientes()      #formas de aclarar que tipo de datos es
#vamos a hacer algo igual para carteras

@app.route("/api/el_galpon_de_lujo/generar_usuario/, methods = ['POST']")
def crear_cliente():
    cliente = request.json

    try:
        nuevo_cliente = Cliente(
            generador_id_cliente(),
            cliente['Nombre'],
            cliente['Apellido'],
            cliente['DNI'],
            cliente['Telefono'],
            cliente['email'],
            cliente['Estado'],
            cliente['carrito']
        )

        cliente.append(nuevo_cliente)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code=400,
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(nuevo_cliente.serialize())

@app.route("/api/el_galpon_de_lujo/ver_carrito/<id_cliente>, methods = ['GET']")
def ver_carrito(id_cliente):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            for producto in cliente.carrito:
                    return jsonify(producto.serialize())



