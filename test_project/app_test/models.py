# Importamos el módulo `models` de Django, que proporciona las herramientas necesarias
# para definir la estructura de la base de datos a través de clases de Python.
from django.db import models

# Definimos una clase llamada `Item` que hereda de `models.Model`.
# Esto indica que `Item` es un modelo de Django, lo que significa que Django
# creará una tabla en la base de datos para almacenar instancias de este modelo.
class Item(models.Model):
    # Campo `name` de tipo `CharField`, que almacenará una cadena de caracteres.
    # - `max_length=100`: Define la longitud máxima del campo (100 caracteres).
    # Este campo es ideal para almacenar nombres o títulos cortos.
    name = models.CharField(max_length=100)

    # Campo `description` de tipo `TextField`, que almacenará texto largo.
    # A diferencia de `CharField`, `TextField` no tiene un límite de longitud predefinido,
    # lo que lo hace adecuado para descripciones o contenido extenso.
    description = models.TextField()

    # Campo `price` de tipo `DecimalField`, que almacenará valores decimales.
    # - `max_digits=10`: Define el número máximo de dígitos que puede almacenar (incluyendo decimales).
    # - `decimal_places=2`: Especifica el número de decimales que se almacenarán.
    # Este campo es ideal para almacenar precios o cualquier valor monetario.
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Método `__str__` que define cómo se representa una instancia de `Item` como una cadena.
    # Este método es útil para mostrar un nombre legible en el panel de administración de Django
    # o en cualquier lugar donde se convierta el objeto a una cadena.
    def __str__(self):
        # Retorna el valor del campo `name` como representación del objeto.
        return self.name
    