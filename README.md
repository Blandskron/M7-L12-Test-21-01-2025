# Aplicación Django: Gestión de Ítems

Este proyecto es una aplicación Django que permite gestionar ítems, incluyendo su nombre, descripción y precio. Proporciona una interfaz para listar todos los ítems y ver los detalles de un ítem específico.

## Características principales

- **Modelo `Item`**: Define la estructura de los ítems con campos para nombre, descripción y precio.
- **Vistas**:
  - `item_list`: Muestra una lista de todos los ítems.
  - `item_detail`: Muestra los detalles de un ítem específico.
- **Pruebas unitarias**: Incluye pruebas para el modelo y las vistas.
- **Panel de administración**: Acceso al panel de administración de Django para gestionar los ítems.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.8 o superior.
- Pip (gestor de paquetes de Python).
- Virtualenv (recomendado para crear un entorno virtual).

## Configuración del proyecto

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/tu-repositorio.git
cd tu-repositorio
```

### 2. Crea y activa un entorno virtual (opcional pero recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura la base de datos

Realiza las migraciones para crear las tablas en la base de datos:

```bash
python manage.py migrate
```

### 5. Crea un superusuario (opcional)

Si deseas acceder al panel de administración, crea un superusuario:

```bash
python manage.py createsuperuser
```

### 6. Ejecuta el servidor de desarrollo

```bash
python manage.py runserver
```

Visita `http://127.0.0.1:8000/` en tu navegador para ver la aplicación en funcionamiento.

## Estructura del proyecto

```
tu-repositorio/
├── app_test/
│   ├── migrations/          # Migraciones de la base de datos
│   ├── __init__.py
│   ├── admin.py             # Registro de modelos en el panel de administración
│   ├── apps.py              # Configuración de la aplicación
│   ├── models.py            # Definición del modelo `Item`
│   ├── tests.py             # Pruebas unitarias
│   ├── views.py             # Vistas de la aplicación
│   └── ...
├── tu-repositorio/
│   ├── __init__.py
│   ├── settings.py          # Configuración del proyecto
│   ├── urls.py              # Rutas (URLs) del proyecto
│   ├── wsgi.py
│   └── ...
├── manage.py                # Script de gestión de Django
└── README.md                # Este archivo
```

## Ejecución de pruebas

El proyecto incluye pruebas unitarias para el modelo y las vistas. Para ejecutar las pruebas, usa el siguiente comando:

```bash
python manage.py test
```

Esto ejecutará todas las pruebas definidas en `app_test/tests.py` y mostrará un resumen de los resultados.

## Panel de administración

Si creaste un superusuario, puedes acceder al panel de administración de Django en:

```
http://127.0.0.1:8000/admin/
```

Desde aquí, puedes gestionar los ítems (crear, editar, eliminar) y realizar otras tareas administrativas.

## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu contribución (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añade nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request en GitHub.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Gracias por usar esta aplicación! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue en el repositorio.
