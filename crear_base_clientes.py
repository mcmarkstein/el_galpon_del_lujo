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
clientes_tupl = []

for cliente in clientes:
    del(cliente['carrito'])
    tupl_cliente = tuple(cliente.values())
    clientes_tupl.append(tupl_cliente)



conexion = sqlite3.connect('./clientesBBDD.db')

cursor = conexion.cursor()
'''
cursor.execute('DROP TABLE clientes' )
conexion.commit()
conexion.close()


sentenciaSQL = 'CREATE TABLE clientes'
sentenciaSQL += '(id_cliente integer,'
sentenciaSQL += 'nombre VARCHAR(30),'
sentenciaSQL += 'apellido VARCHAR(30),'
sentenciaSQL += 'dni integer,'
sentenciaSQL += 'telefono integer,'
sentenciaSQL += 'email VARCHAR(40), '
sentenciaSQL += 'estado VARCHAR(30))'

cursor.execute(sentenciaSQL)
conexion.commit()

sentenciaSQL = "INSERT INTO clientes VALUES (?,?,?,?,?,?,?)"
cursor.executemany(sentenciaSQL, clientes_tupl)

conexion.commit()
conexion.close()
'''
sentenciaSQL = ('SELECT * FROM clientes')
cursor.execute(sentenciaSQL)
conexion.commit()
conexion.close()





