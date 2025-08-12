# 🛒 Supermercado ERP

**Supermercado ERP** es un sistema web desarrollado en **Django + PostgreSQL** para la gestión integral de un supermercado o tienda.  
Incluye módulos para productos, ventas, usuarios, reportes y caja, con interfaz web adaptable a diferentes dispositivos.

---

## 🚀 Características principales
- **Productos:** creación, edición, control de stock y categorías.
- **Ventas:** registro de ventas, formas de pago, control de caja.
- **Usuarios:** autenticación, permisos y roles por grupos.
- **Reportes:** estadísticas y exportaciones a PDF/Excel.
- **Auditoría:** historial de acciones con `django-simple-history`.
- **Caja:** módulo para control de efectivo *(en desarrollo)*.

---

## 📦 Requisitos
- **Python** 3.10 o superior  
- **PostgreSQL**  
- **Entorno virtual** (`venv`)  
- Navegador actualizado (Chrome, Firefox, Edge)

Dependencias principales (`requirements.txt`):
```txt
asgiref==3.8.1
chardet==5.2.0
Django==5.2.3
django-simple-history==3.8.0
django-widget-tweaks==1.5.0
et_xmlfile==2.0.0
narwhals==1.42.0
openpyxl==3.1.5
packaging==25.0
pillow==11.2.1
plotly==6.1.2
psycopg2-binary==2.9.10
reportlab==4.4.1
sqlparse==0.5.3
tzdata==2025.2
```

---

## ⚙️ Instalación y ejecución

1. **Clonar repositorio**
   ```bash
   git clone https://github.com/AdroAAN/supermercado-erp.git
   cd supermercado_erp
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   # En Windows
   venv\Scripts\activate
   # En Mac/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**
   - Crear base de datos en PostgreSQL:
     ```sql
     CREATE DATABASE supermercado_db;
     ```
   - Configuración por defecto en `settings.py`:
     ```python
     ENGINE = 'django.db.backends.postgresql'
     NAME = 'supermercado_db'
     USER = 'postgres'
     PASSWORD = '1782'
     HOST = 'localhost'
     PORT = '5432'
     ```

5. **Aplicar migraciones y crear superusuario**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Ejecutar servidor**
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```
   Accede en tu navegador: **http://localhost:8000**

---

## 📊 Módulos
- **Productos:** gestión de inventario y categorías.
- **Ventas:** registro y control de transacciones.
- **Usuarios:** permisos y roles.
- **Reportes:** análisis y exportaciones.
- **Auditoría:** seguimiento de cambios.
- **Caja:** *(próximamente)*.

---

## 📄 Licencia
Uso académico y personal permitido.  
Para uso comercial, contactar al autor.

---

## 🤝 Soporte
Este proyecto está configurado para entorno local.  
Para producción se recomienda:
- Servidor Linux
- Gunicorn + Nginx
- PostgreSQL
- HTTPS
