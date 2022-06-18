import csv
import sqlite3


clientes = [
    {
    "id_cliente": "12345",
    "nombre": "Mario",
    "apellido": "Arjona",
    "dni": "23700981",
    "telefono": "01148723458",
    "email": "marjona@gmail.com",
    "estado": "ACTIVO",
    "carrito": []
    },
    {
    "id_cliente": "98765",
    "nombre": "Alejandra",
    "apellido": "Sanchez",
    "dni": "38407221",
    "telefono": "01184926574",
    "email": "asanchez@gmail.com",
    "estado": "ACTIVO",
    "carrito": []
    },
    {
    "id_cliente": "12345",
    "nombre": "Manuel",
    "apellido": "Belgrano",
    "dni": "124589638",
    "telefono": "01132679472",
    "email": "mbelgrano@gmail.com",
    "estado": "INACTIVO",
    "carrito": []
    },
    {
    "id_cliente": "00751",
    "nombre": "Julieta",
    "apellido": "Mandalorian",
    "dni": "37889675",
    "telefono": "01154399633",
    "email": "mandalirian1@gmail.com",
    "estado": "ACTIVO",
    "carrito": []
    },
    {
    "id_cliente": "00843",
    "nombre": "Soledad",
    "apellido": "Gorgelin",
    "dni": "33425786",
    "telefono": "01166734324",
    "email": "gorge_sole@gmail.com",
    "estado": "INACTIVO",
    "carrito": []
    }
]

with open ("./consulta_2.csv", "w", newline="\n") as archivo:
        campos = ['id_cliente', 'email', 'estado']
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        for client in clientes:
             writer.writerow({ "id_cliente": client["id_cliente"],
                "email" : client["email"],
                "estado" : client["estado"]

            })
archivo.close()
del (archivo)



conexion = sqlite3.connect('./clientesBBDD.db')

cursor = conexion.cursor()

sentenciaSQL = 'CREATE TABLE clientes'
sentenciaSQL += '(id_cliente integer,'
sentenciaSQL += 'nombre VARCHAR(30), '
sentenciaSQL += 'apellido VARCHAR(30), '
sentenciaSQL += 'dni integer, '
sentenciaSQL += 'telefono integer, '
sentenciaSQL += 'email VARCHAR(40), '
sentenciaSQL += 'estado VARCHAR(30)) '

sentenciaSQL = "INSERT INTO clientes"
sentenciaSQL +=
sentenciaSQL +=
sentenciaSQL +=
sentenciaSQL +=
sentenciaSQL +=
sentenciaSQL +=
sentenciaSQL +=

cursor.execute(sentenciaSQL)
conexion.close()


