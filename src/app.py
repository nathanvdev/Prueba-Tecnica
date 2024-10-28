import re
from flask import Flask, request, jsonify
from clientes import CClientes

app = Flask(__name__)

def verificarTexto(texto):
    try:
        if re.match(r'[A-Za-z\s]+', texto):
            return True
        else:
            return False
    except:
        return False
    
def verificarFechaNacimiento(fecha):
    try:
        if re.match(r"^\d{4}-\d{2}-\d{2}$", fecha):
            return True
        else:
            return False
    except:
        return False

def verificarNumeros(numero):
    try:
        int(numero)
        return True
    except:
        return False

@app.route('/')
def index():
    return jsonify({"mensaje": "Bienvenido a la API"})


@app.route('/agregarCliente', methods=['POST'])
def agregarCliente():
    nombre = request.json['nombre']
    apellidos = request.json['apellidos']
    nacimiento = request.json['nacimiento']
    celular = request.json['celular']
    dpi = request.json['dpi']

    if verificarTexto(nombre) == False:
        return jsonify({"mensaje": "El nombre solo debe contener letras"}), 400
    if verificarTexto(apellidos) == False:
        return jsonify({"mensaje": "Los apellidos solo deben contener letras"}), 400
    if verificarFechaNacimiento(nacimiento) == False:
        return jsonify({"mensaje": "La fecha de nacimiento debe tener el formato yyyy-mm-dd"}), 400
    if verificarNumeros(celular) == False:
        return jsonify({"mensaje": "El celular solo debe contener numeros"}), 400
    if verificarNumeros(dpi) == False:
        return jsonify({"mensaje": "El dpi solo debe contener numeros"}), 400

    response = CClientes.agregarCliente(nombre, apellidos, nacimiento, celular, dpi)

    if response == False:
        return jsonify({"mensaje": "Error al agregar el cliente"}), 500
    
    return jsonify({"mensaje": "Cliente agregado con exito"}), 201

@app.route('/obtenerClientes', methods=['GET'])
def obtenerClientes():
    clientes = CClientes.obtenerClientes()
    if clientes == False:
        return jsonify({"mensaje": "Error al obtener clientes"}), 500
    
    return jsonify(clientes), 200

@app.route('/obtenerCliente/<id>', methods=['GET'])
def obtenerCliente(id):
    cliente = CClientes.obtenerCliente(id)
    if cliente == False:
        return jsonify({"mensaje": "Error al obtener el cliente"}), 500
    
    return jsonify(cliente)

@app.route('/actualizarCliente/<id>', methods=['PUT'])
def actualizarCliente(id):
    nombre = request.json['nombre']
    apellidos = request.json['apellidos']
    nacimiento = request.json['nacimiento']
    celular = request.json['celular']
    dpi = request.json['dpi']

    if verificarTexto(nombre) == False:
        return jsonify({"mensaje": "El nombre solo debe contener letras"}), 400
    if verificarTexto(apellidos) == False:
        return jsonify({"mensaje": "Los apellidos solo deben contener letras"}), 400
    if verificarFechaNacimiento(nacimiento) == False:
        return jsonify({"mensaje": "La fecha de nacimiento debe tener el formato yyyy-mm-dd"}), 400
    if verificarNumeros(celular) == False:
        return jsonify({"mensaje": "El celular solo debe contener numeros"}), 400
    if verificarNumeros(dpi) == False:
        return jsonify({"mensaje": "El dpi solo debe contener numeros"}), 400

    response = CClientes.actualizarCliente(id, nombre, apellidos, nacimiento, celular, dpi)
    if response == False:
        return jsonify({"mensaje": "Error al actualizar cliente"}), 500

    return jsonify({"mensaje": "Cliente actualizado con exito"})

@app.route('/eliminarCliente/<id>', methods=['DELETE'])
def eliminarCliente(id):
    response = CClientes.eliminarCliente(id)
    if response == False:
        return jsonify({"mensaje": "Error al eliminar cliente"}), 500

    return jsonify({"mensaje": "Cliente eliminado con exito"})


if __name__ == "__main__":
    app.run(debug=True)