"""
URL configuration for test_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importamos el módulo `admin` de Django, que proporciona la interfaz de administración
# para gestionar los modelos de la base de datos.
from django.contrib import admin

# Importamos la función `path` de Django, que se utiliza para definir rutas (URLs) en la aplicación.
from django.urls import path

# Importamos las vistas definidas en el archivo `views.py` de la aplicación `app_test`.
# Estas vistas manejarán las solicitudes HTTP y devolverán las respuestas correspondientes.
from app_test import views

# Definimos la lista `urlpatterns`, que contiene las rutas (URLs) de la aplicación.
# Cada ruta está asociada a una vista específica que se ejecutará cuando se acceda a esa URL.
urlpatterns = [
    # Ruta para acceder a la interfaz de administración de Django.
    # - 'admin/': Define la URL relativa para acceder al panel de administración.
    # - admin.site.urls: Incluye las URLs predeterminadas del panel de administración.
    path('admin/', admin.site.urls),

    # Ruta para la página principal de la aplicación.
    # - '': Define la URL raíz (por ejemplo, http://tusitio.com/).
    # - views.item_list: Asocia esta URL a la vista `item_list` que lista todos los ítems.
    # - name='item_list': Asigna un nombre único a esta URL para referenciarla en el código.
    path('', views.item_list, name='item_list'),

    # Ruta para ver los detalles de un ítem específico.
    # - 'item/<int:item_id>/': Define una URL dinámica que incluye un parámetro `item_id`.
    #   - `<int:item_id>`: Captura un valor entero de la URL y lo pasa como argumento `item_id` a la vista.
    # - views.item_detail: Asocia esta URL a la vista `item_detail` que muestra los detalles de un ítem.
    # - name='item_detail': Asigna un nombre único a esta URL para referenciarla en el código.
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
]
