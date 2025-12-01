import unittest
from app import app, db
from models import Producto
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config["TESTING"] = True
        # Usar una base de datos en memoria para pruebas
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        with app.app_context():
            db.create_all()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'API funcionando', response.data)

    def test_crud_producto(self):
        # Crear producto
        response = self.app.post('/productos', json={
            "nombre": "Lapiz",
            "tipo": "Escritura",
            "referencia": "A123"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data["mensaje"], "Producto creado")

        # Listar productos
        response = self.app.get('/productos')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(json.loads(response.data)) == 1)

        # Obtener producto
        prod_id = json.loads(response.data)[0]["id"]
        response = self.app.get(f'/productos/{prod_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Lapiz", response.data.decode())

        # Actualizar producto
        response = self.app.put(f'/productos/{prod_id}', json={
            "nombre": "Lapiz Azul",
            "tipo": "Escritura",
            "referencia": "A123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("Producto actualizado", response.data.decode())

        # Eliminar producto
        response = self.app.delete(f'/productos/{prod_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Producto eliminado", response.data.decode())

if __name__ == "__main__":
    unittest.main()
