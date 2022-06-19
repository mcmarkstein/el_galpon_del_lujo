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
cursor.execute('DROP TABLE clientes_2' )
conexion.commit()
conexion.close()

'''
'''
sentenciaSQL = 'CREATE TABLE clientes_2'
sentenciaSQL += '(id_cliente VARCHAR(30),'
sentenciaSQL += 'nombre VARCHAR(30),'
sentenciaSQL += 'apellido VARCHAR(30),'
sentenciaSQL += 'dni VARCHAR(30),'
sentenciaSQL += 'telefono VARCHAR(30),'
sentenciaSQL += 'email VARCHAR(40), '
sentenciaSQL += 'estado VARCHAR(30))'

cursor.execute(sentenciaSQL)
conexion.commit()
'''

sentenciaSQL2 = "INSERT INTO clientes_2 VALUES ("12345", "Mario", "Arjona", "23700981", "01148723458", "marjona@gmail.com", "ACTIVO")"
#sentenciaSQL2 += 'INSERT INTO clientes_2 VALUES ("98765","Alejandra","Sanchez","38407221","01184926574","asanchez@gmail.com","ACTIVO")'
#sentenciaSQL2 += 'INSERT INTO clientes_2 VALUES ("12345", "Manuel", "Belgrano", "124589638", "01132679472", "mbelgrano@gmail.com","INACTIVO")'
#sentenciaSQL2 += 'INSERT INTO clientes_2 VALUES ("00751", "Julieta", "Mandalorian", "37889675", "01154399633","mandalirian1@gmail.com","ACTIVO")'
#sentenciaSQL2 += 'INSERT INTO clientes_2 VALUES ("00843", "Soledad", "Gorgelin", "33425786", "01166734324", "gorge_sole@gmail.com","INACTIVO")'
cursor.execute(sentenciaSQL2)

conexion.commit()

'''

sentenciaSQL3 = "SELECT email FROM clientes_2 WHERE estado = 'ACTIVO'"
cursor.execute(sentenciaSQL3)
mails_activos = cursor.fetchall()

for mail in mails_activos:
    print(mail)
conexion.close()
'''






