# Final Test Yitzhak Matias

Final Test es un proyecto desarrollado con Django y Django Rest Framework que permite gestionar productos, clientes, pedidos y detalles de pedidos. Este proyecto incluye un conjunto de APIs para realizar operaciones CRUD sobre los datos.

## Requisitos Previos

Asegúrate de tener instalados los siguientes componentes:

- Python 3.9 o superior
- Git

## Instalación

Sigue estos pasos para clonar y ejecutar el proyecto en tu entorno local.

### 1. Clonar el Repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd test_yitzhak
```

### 2. Crear y Activar un Entorno Virtual
```bash
python -m venv env
env\\Scripts\\activate  # En Windows
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar la Base de Datos
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear un Superusuario
```bash
python manage.py createsuperuser
```

### 6. Iniciar el Servidor de Desarrollo
```bash
python manage.py runserver
```
### Uso de las APIs

El proyecto incluye las siguientes APIs disponibles en http://127.0.0.1:8000/api/:

* Productos: /productos/
* Clientes: /clientes/
* Pedidos: /pedidos/
* Detalles de Pedidos: /detalles/
* Además, hay una API personalizada disponible en /api/client/<int:client_id>/products/.


---

#### . **Añadir el Archivo al Repositorio**

1. Guarda el archivo `README.md`.

2. Añádelo al control de versiones y realiza un commit:

```bash
git add README.md
git commit -m "Add README.md with project instructions"
git push
```

---

### Licencia

```yaml
Copia este contenido en un archivo `README.md`. Si necesitas más ayuda, ¡házmelo saber! &#8203;:contentReference[oaicite:0]{index=0}&#8203;
```
