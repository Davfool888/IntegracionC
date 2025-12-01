from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db
from models import Producto

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventario.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Crear las tablas al iniciar la app
with app.app_context():
    db.create_all()

# ---------- RUTAS CRUD ----------

@app.route("/")
def index():
    return jsonify({"status": "API funcionando"})

# Crear producto
@app.route("/productos", methods=["POST"])
def crear_producto():
    data = request.json
    nuevo = Producto(
        nombre=data["nombre"],
        tipo=data["tipo"],
        referencia=data["referencia"]
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({"mensaje": "Producto creado", "id": nuevo.id})

# Listar productos
@app.route("/productos", methods=["GET"])
def listar_productos():
    productos = Producto.query.all()
    resultado = [
        {
            "id": p.id,
            "nombre": p.nombre,
            "tipo": p.tipo,
            "referencia": p.referencia
        }
        for p in productos
    ]
    return jsonify(resultado)

# Obtener por ID
@app.route("/productos/<int:id>", methods=["GET"])
def obtener_producto(id):
    p = Producto.query.get_or_404(id)
    return jsonify({
        "id": p.id,
        "nombre": p.nombre,
        "tipo": p.tipo,
        "referencia": p.referencia
    })

# Actualizar
@app.route("/productos/<int:id>", methods=["PUT"])
def actualizar_producto(id):
    data = request.json
    p = Producto.query.get_or_404(id)

    p.nombre = data["nombre"]
    p.tipo = data["tipo"]
    p.referencia = data["referencia"]

    db.session.commit()
    return jsonify({"mensaje": "Producto actualizado"})

# Eliminar
@app.route("/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    p = Producto.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return jsonify({"mensaje": "Producto eliminado"})

# Al final de app.py
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

