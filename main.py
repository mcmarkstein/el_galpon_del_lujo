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
carteras: list = cargar_carteras()      #vamos a hacer algo igual para carteras


@app.route("/api/el_galpon_de_lujo/generar_usuario/", methods = ['POST'])
def crear_cliente():
    cliente = request.json

    try:
        nuevo_cliente = Cliente(
            generador_id_cliente(),
            cliente['nombre'],
            cliente['apellido'],
            cliente['dni'],
            cliente['telefono'],
            cliente['email'],
            cliente['estado'],
            cliente['carrito']
        )

        clientes.append(nuevo_cliente)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="400",
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(nuevo_cliente.serialize())

@app.route("/api/el_galpon_de_lujo/carrito/<id_cliente>", methods = ['GET'])        #ver carrito
def ver_carrito(id_cliente):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
                    return jsonify([producto.serialize() for producto in cliente.carrito])
        else:
            return jsonify({'Error': 'Cliente no encontrado'})

@app.route("/api/el_galpon_de_lujo/carteras", methods = ['GET'])    #ver catalogo
def ver_catalogo():
    return jsonify([cartera.serialize() for cartera in carteras])

@app.route("/api/el_galpon_de_lujo/carteras/<id>", methods=['GET'])     #ver una cartera por id
def ver_cartera_por_id(id):
    for cartera in carteras:
        if cartera.id == id:
            return jsonify(cartera.serialize())

"""
@app.route("/api/el_galpon_de_lujo/carteras/<marca>", methods=['GET'])      #ver carteras por marca  ARREGLAR
def ver_cartera_por_marca(marca):
    for cartera in carteras:
        if cartera.marca == marca:
            return jsonify(cartera.serialize())
"""


@app.route("/api/el_galpon_de_lujo/carrito/<id_cliente>/agregar/<id>", methods=['PUT'])       #Agregar a carrito por id
def agregar_a_carrito(id_cliente, id):
    for cartera in carteras:
        for cliente in clientes:
            if cartera.id == id and cliente.id_cliente == id_cliente:
                cliente.carrito.append(cartera)
                return jsonify([producto.serialize() for producto in cliente.carrito])


@app.route("/api/el_galpon_de_lujo/carrito/<id_cliente>/eliminar/<id>", methods=['DELETE'])      #Eliminar producto de carrito por id
def eliminar_de_carrito(id_cliente, id):
    for cliente in clientes:
        if cliente.id_cliente == id_cliente:
            for producto in cliente.carrito:
                if producto.id == id:
                    cliente.carrito.remove(producto)
                return jsonify({'Busqueda': id, 'Estado': 'Se ha eliminado el producto'})

#return jsonify({'Busqueda': id, 'Estado': 'Se ha eliminado el producto'})
#return jsonify({'Busqueda': id, 'Estado': 'no se ha encontrado el ID indicado en el carrito'})



#@app.route("/api/el_galpon_de_lujo/carteras/actualizar_precios", methods=['PUT'])      #Actualizar precios, ver como se hace para solo admin



#@app.route("/api/el_galpon_de_lujo/terminar_compra/<id>", methods=['GET'])         #terminar compra
