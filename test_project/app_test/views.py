# Importamos las utilidades necesarias de Django:
# - `render`: Para renderizar plantillas HTML con datos.
# - `get_object_or_404`: Para obtener un objeto de la base de datos o lanzar un error 404 si no existe.
# - `JsonResponse`: Para devolver respuestas en formato JSON.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

# Importamos el modelo `Item` desde el archivo `models.py` del mismo directorio.
from .models import Item

# Definimos una vista llamada `item_list` que manejará las solicitudes para listar todos los ítems.
def item_list(request):
    try:
        # Obtenemos todos los objetos de la clase `Item` desde la base de datos.
        # `Item.objects.all()` realiza una consulta que devuelve un QuerySet con todos los ítems.
        items = Item.objects.all()

        # Renderizamos la plantilla 'item_list.html' pasando el contexto `{'items': items}`.
        # El contexto es un diccionario que contiene los datos que la plantilla puede utilizar.
        return render(request, 'item_list.html', {'items': items})
    except Exception as e:
        # Si ocurre algún error durante la ejecución, capturamos la excepción y devolvemos
        # una respuesta JSON con un mensaje de error y un código de estado HTTP 500 (Error del servidor).
        return JsonResponse({'error': 'An error occurred while fetching items.'}, status=500)

# Definimos una vista llamada `item_detail` que manejará las solicitudes para ver los detalles de un ítem específico.
def item_detail(request, item_id):
    # Utilizamos `get_object_or_404` para obtener un ítem por su `id`.
    # Si el ítem no existe, Django automáticamente devuelve una respuesta HTTP 404 (No encontrado).
    item = get_object_or_404(Item, id=item_id)

    # Renderizamos la plantilla 'item_details.html' pasando el contexto `{'item': item}`.
    # El contexto contiene el ítem específico que se mostrará en la plantilla.
    return render(request, 'item_details.html', {'item': item})
