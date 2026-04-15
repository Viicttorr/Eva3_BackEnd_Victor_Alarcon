# 📚 Evaluación 3 - Programación Back End (Django)

Aplicación web desarrollada en **Django** como parte de la Evaluación Sumativa 3 de Programación Back End.  
El proyecto consiste en un sistema de **gestión y reserva de salas de estudio** para la biblioteca del Instituto Tecnológico de Innovación Digital (ITID).

---

## 🚀 Funcionalidades principales

### Gestión de salas
- El administrador puede **crear, editar, eliminar y habilitar salas**.
- Cada sala almacena:
  - Nombre
  - Capacidad máxima
  - Estado de disponibilidad (reservada o disponible)
- En la página principal los usuarios pueden ver todas las salas y su disponibilidad.

### Reserva de salas
- Los usuarios pueden reservar una sala disponible.
- Datos de la reserva:
  - Rut del usuario
  - Fecha y hora de inicio (automática)
  - Fecha y hora de término (máximo 2 horas)
  - Sala reservada
- Una vez cumplidas las 2 horas, la sala queda automáticamente disponible.

### Interfaz de administración
- Acceso al **Django Admin** para gestionar salas y reservas.
- Visualización de registros en la **Base de Datos externa**.

---

## 🎯 Objetivos de aprendizaje

1. Crear una aplicación web con **Django**.  
2. Implementar **CRUD** de salas y reservas.  
3. Conectar el proyecto a una **Base de Datos externa**.  
4. Usar **formularios de Django (ModelForm)** para reservas.  
5. Proteger credenciales con **variables de entorno (django-environ)**.  
6. Aplicar buenas prácticas de seguridad (no subir `venv`, `.env`, `pycache`, `db.sqlite3`, etc.).

---

## 🛠️ Tecnologías utilizadas

- **Python 3.x**
- **Django**
- **Oracle DB** (o base externa)
- **django-environ**
- **Visual Studio Code**

---

## 📂 Estructura del proyecto

- `/project/` → Configuración principal de Django.  
- `/app/` → Aplicación con modelos, vistas y formularios.  
- `/templates/` → Archivos HTML. 

---

## ⚙️ Instalación y ejecución

1. Clonar el repositorio.
2. Crear y activar entorno virtual:
   - python -m venv venv
   - venv\Scripts\activate.bat
3. Instalar dependencias:
   - pip install django django-environ
4. Configurar archivo .env con credenciales de la base de datos:
   - DB_NAME=nombre_bd
   - DB_USER=usuario
   - DB_PASSWORD=clave
   - DB_HOST=host
   - DB_PORT=puerto
5. Migrar la base de datos:
   - python manage.py migrate
6. Crear superusuario:
   - python manage.py createsuperuser
7. Ejecutar servidor:
   - python manage.py runserver
8. Ingresar al admin y crear las Salas.

---

## 👨‍💻 Actividades demostradas
1. Creación, edición y eliminación de salas en el admin y visualización en BD.
2. Visualización de salas en la página principal y comparación con registros en BD.
3. Creación de reservas y visualización en BD.
4. Modificación de hora de término para corroborar disponibilidad automática.

---

## 📜 Licencia
Este proyecto se distribuye bajo la licencia MIT.
Puedes usarlo, modificarlo y compartirlo libremente, siempre mencionando la autoría original.
