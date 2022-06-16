import json
from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response

from clientes import Cliente, generador_id_cliente
from carteras import Cartera, Totebag, CrossBody, Clutch, Mochila

app = Flask(__name__)


@app.route("/api/el_galpo_de_lujo/generar_usuario/, methods = ['POST']")
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
            cliente['Estado']
        )

    cliente.append(new_client)

    except KeyError as key_err:
    missing_param = (key_err.__str__())
    return jsonify(
        error_code=400,
        error_description="Bad request",
        error_body=missing_param
    ), 400

    return jsonify(nuevo_cliente.serialize())
