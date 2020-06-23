
from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

#Por defecto las rutas trabajan el metodo GET
# GET    = Obtener Datos
# POST   = Guardar Datos
# PUT    = Actualizar Datos
# DELETE = Borrar Datos
# len    = para longitud

@app.route('/ping')
def ping():
    return jsonify({"message": "'Pong'"})


# OBTENER PRODUCTOS / GET
@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products})

@app.route('/products/<string:product_name>')
def getProduct(product_name):

    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        return jsonify({"Product": productsFound[0]})
    return jsonify({"message": "Product Not Found"})


# AGREGAR PRODUCTOS / POST
@app.route('/products', methods=["POST"])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"Message": "Product Added Succesfully", "Products": products})


# ACTUALIZAR PRODUCTOS / PUT
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        productsFound[0]['name'] = request.json['name']
        productsFound[0]['price'] = request.json['price']
        productsFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "Product Updated",
            "product": productsFound[0]
        })
    return jsonify({"message": "Producto Not Found"})



# ELIMINAR PRODUCTOS
@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProducto(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound) > 0):
        products.remove(productsFound)
        return jsonify({
            "message": "Product Deleted",
            "Products": products
        })
    return jsonify({"message": "Product Not Found"})


if __name__ == '__main__':
    app.run(debug=True)