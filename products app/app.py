import stripe
from pymongo import MongoClient # El cliente de MongoDB
from bson.objectid import ObjectId # Para crear ObjectId, porque _id como cadena no funcion

stripe.api_key = 'sk_test_51I7K4uLcW4XlqZuyZBsn9klxVdmvpiO4wr3ia0VyrPT63ijWEALwCmYsFWFfHn6YghzBfXwgNTpfOU2u4LgZSyKj003HatAEq0'


def obtener_bd():
    host = "localhost"
    puerto = "27017"
    base_de_datos = "tienda"
    cliente = MongoClient("mongodb://127.0.0.1:27017/")
    return cliente[base_de_datos]

def insertar(name, precio):
    base_de_datos = obtener_bd()
    productos = base_de_datos.productos
    return productos.insert_one({
        "name": name,
        "precio": precio,
        }).inserted_id

def obtener():
    base_de_datos = obtener_bd()
    return base_de_datos.productos.find()
  

def actualizar(id, producto):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.productos.update_one(
        {
        '_id': ObjectId(id)
        }, 
        {
            '$set': {
                "name": producto.name,
                "precio": producto.precio,
            }
        })
    return resultado.modified_count

def eliminar(id):
    base_de_datos = obtener_bd()
    resultado = base_de_datos.productos.delete_one(
        {
        '_id': ObjectId(id)
        })
    return resultado.deleted_count

menu = """Bienvenido a la tienda.
1 - Insertar producto
2 - Ver todos
3 - Actualizar
4 - Eliminar
5 - Salir
"""
eleccion = None
while eleccion != 5:
    print(menu)
    eleccion = int(input("Elige: "))
    
    if eleccion == 1:
        print("Insertar")
        name = str(input("Nombre del producto: "))
        precio = float(input("Precio del producto: "))
        producto = insertar(name, precio)
        print("producto insertado exitosamente")

    elif eleccion == 2:
        print("Obteniendo productos...")
        for i, producto in enumerate(obtener(), 1):
            print("=================")
            print(i, producto["name"], producto["precio"])
            

    elif eleccion == 3:
        print("Insertar datos de pago")
            
    elif eleccion == 3:
        print("Actualizar")
        id = input("Dime el id: ")
        nombre = input("Nuevo nombre del producto: ")
        precio = float(input("Nuevo precio del producto: "))
        cantidad = float(input("Nueva cantidad del producto: "))
        producto = insertar(nombre, precio, cantidad)
        productos_actualizados = actualizar(id, producto)
        print("Número de productos actualizados: ", productos_actualizados)

    elif eleccion == 4:
        print("Eliminar")
        id = input("Dime el id: ")
        productos_eliminados = eliminar(id)
        print("Número de productos eliminados: ", productos_eliminados)