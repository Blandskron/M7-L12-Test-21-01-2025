# Importamos las clases y funciones necesarias para realizar pruebas en Django:
# - `TestCase`: Proporciona una base para escribir tests en Django.
# - `Client`: Simula un cliente HTTP para hacer solicitudes a las vistas.
# - `patch`: Del módulo `unittest.mock`, permite simular comportamientos en los tests.
from django.test import TestCase, Client
from unittest.mock import patch

# Importamos el modelo `Item` desde el archivo `models.py` del mismo directorio.
from .models import Item

# Definimos una clase de prueba para el modelo `Item`.
class ItemModelTest(TestCase):
    # Método `setUp` que se ejecuta antes de cada test.
    # Aquí se preparan los datos necesarios para las pruebas.
    def setUp(self):
        # Creamos dos instancias de `Item` en la base de datos de prueba.
        Item.objects.create(name="Item 1", description="Description 1", price=10.0)
        Item.objects.create(name="Item 2", description="Description 2", price=20.0)

    # Test para verificar la creación correcta de un ítem.
    def test_item_creation(self):
        # Obtenemos el ítem con nombre "Item 1" desde la base de datos.
        item = Item.objects.get(name="Item 1")

        # Verificamos que los campos del ítem coincidan con los valores esperados.
        self.assertEqual(item.description, "Description 1")
        self.assertEqual(item.price, 10.0)

# Definimos una clase de prueba para las vistas relacionadas con la lista de ítems.
class ItemViewTest(TestCase):
    # Método `setUp` que se ejecuta antes de cada test.
    def setUp(self):
        # Creamos una instancia de `Client` para simular solicitudes HTTP.
        self.client = Client()

        # Creamos un ítem en la base de datos de prueba.
        Item.objects.create(name="Item 1", description="Description 1", price=10.0)

    # Test para verificar que la vista `item_list` funciona correctamente.
    def test_item_list_view_success(self):
        # Simulamos una solicitud GET a la URL raíz ('/').
        response = self.client.get('/')

        # Verificamos que la respuesta tenga un código de estado HTTP 200 (Éxito).
        self.assertEqual(response.status_code, 200)

        # Verificamos que la respuesta contenga el nombre del ítem creado.
        self.assertContains(response, "Item 1")

    # Test para verificar el manejo de errores en la vista `item_list`.
    # Usamos `patch` para simular un error en la consulta a la base de datos.
    @patch('app_test.models.Item.objects.all')
    def test_item_list_view_error(self, mock_items):
        # Configuramos el mock para que lance una excepción cuando se llame a `Item.objects.all()`.
        mock_items.side_effect = Exception("Database error")

        # Simulamos una solicitud GET a la URL raíz ('/').
        response = self.client.get('/')

        # Verificamos que la respuesta tenga un código de estado HTTP 500 (Error del servidor).
        self.assertEqual(response.status_code, 500)

        # Verificamos que la respuesta sea un JSON con el mensaje de error esperado.
        self.assertJSONEqual(response.content, {'error': 'An error occurred while fetching items.'})

# Definimos una clase de prueba para la vista de detalles de un ítem.
class ItemDetailViewTest(TestCase):
    # Método `setUp` que se ejecuta antes de cada test.
    def setUp(self):
        # Creamos una instancia de `Client` para simular solicitudes HTTP.
        self.client = Client()

        # Creamos un ítem en la base de datos de prueba y lo guardamos en `self.item`.
        self.item = Item.objects.create(name="Item 1", description="Description 1", price=10.0)

    # Test para verificar que la vista `item_detail` funciona correctamente.
    def test_item_detail_view_success(self):
        # Simulamos una solicitud GET a la URL de detalles del ítem creado.
        response = self.client.get(f'/item/{self.item.id}/')

        # Verificamos que la respuesta tenga un código de estado HTTP 200 (Éxito).
        self.assertEqual(response.status_code, 200)

        # Verificamos que la respuesta contenga el nombre del ítem.
        self.assertContains(response, self.item.name)

    # Test para verificar el manejo de un ítem no encontrado en la vista `item_detail`.
    def test_item_detail_view_not_found(self):
        # Simulamos una solicitud GET a una URL con un `item_id` que no existe.
        response = self.client.get('/item/55/')

        # Verificamos que la respuesta tenga un código de estado HTTP 404 (No encontrado).
        self.assertEqual(response.status_code, 404)
        