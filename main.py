from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    with open("listado.txt", "r") as datos:
        for linea in datos:
            uuu = linea
            if uuu[0] == "D":
                print(uuu)
            break
    return "Hello from Flask!"


##if __name__ == '__main__':
#app.run(host='0.0.0.0', port=5000)
# print("Listado DETALLES")
# count = 0
# with open("listado.txt", "r") as datos:
#     for linea in datos:
#         uuu = linea
#         if uuu[0] == "D":
#             nombreCompleto = uuu[224:374].strip()
#             dni = uuu[62:73]
#             montoPago = uuu[535:539]
#             fechaPago1 = uuu[542:546]
#             fechaPago2 = uuu[546:548]
#             print("Nombre:", nombreCompleto)
#             print("DNI:", dni)
#             print("Monto de Pago:", montoPago)
#             print(f"Fecha de Pago: {fechaPago2}/{fechaPago1}")
#             print()
#             count += 1
#             if count == 10:
#                 break


# @app.route('/api/listado', methods=['GET'])
# def obtener_listado():
#     datos = []
#     with open("listado.txt", "r") as archivo:
#         for linea in archivo:
#             uuu = linea
#             if uuu[0] == "D":
#                 nombreCompleto = uuu[224:374].strip()
#                 dni = uuu[62:73]
#                 montoPago = uuu[535:539]
#                 fechaPago1 = uuu[542:546]
#                 fechaPago2 = uuu[546:548]
#                 datos.append({
#                     'nombre': nombreCompleto,
#                     'dni': dni,
#                     'montoPago': montoPago,
#                     'fechaPago': f"{fechaPago2}/{fechaPago1}"
#                 })
#     datos = datos[:10]
#     return jsonify(datos)


@app.route('/api/recibir', methods=['POST'])
def recibir_archivo():
    archivo = next(request.files.values(), None)
    if archivo is None:
        return jsonify({'error': 'No se proporcionó ningún archivo'}), 400

    datos = []
    contenido = archivo.read().decode('utf-8').split('\n')

    for linea in contenido:
        uuu = linea
        if uuu[0] == "D":
            nombreCompleto = uuu[224:374].strip()
            dni = uuu[62:73]
            montoPago = uuu[535:539]
            fechaPago1 = uuu[542:546]
            fechaPago2 = uuu[546:548]
            datos.append({
                'nombre': nombreCompleto,
                'dni': dni,
                'montoPago': montoPago,
                'fechaPago': f"{fechaPago2}/{fechaPago1}"
            })
            if len(datos) == 10:
                break

    return jsonify(datos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
