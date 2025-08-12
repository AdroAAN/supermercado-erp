[README.md](https://github.com/user-attachments/files/21724664/README.md)
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

 Figura 1: Inicio de Sesión (login.html): Formulario para username, contraseña, con bg-[#22272e], focus:ring-green-400.
 <img width="948" height="551" alt="image" src="https://github.com/user-attachments/assets/851775cb-e7d2-41c5-84f2-9db729c16afa" />

 Figura 2: Listado de Usuarios (lista_usuarios.html): Tabla filtrada por estado con DataTables.
 <img width="975" height="439" alt="image" src="https://github.com/user-attachments/assets/f464f473-5d81-4499-a444-be73f467ccba" />

Figura 3: Edición de Usuario (editar_usuario.html): Formulario para username, email, grupo, con widget_tweaks.
<img width="975" height="496" alt="image" src="https://github.com/user-attachments/assets/2d132f8c-41be-4b27-817b-9de4f1306020" />

 Figura 4: Creación de Usuario (crear_usuario.html): Formulario para registrar usuarios con CrearUsuarioForm, estilizado con bg-[#2f2f2f], focus:ring-lime-400.
<img width="975" height="529" alt="image" src="https://github.com/user-attachments/assets/4ac82055-2879-409b-88cf-dd756d569afb" />

 Figura 5: Listado de Productos (productos_list.html): Tabla interactiva con DataTables, modal AJAX, y Lucide Icons. 
 <img width="975" height="551" alt="image" src="https://github.com/user-attachments/assets/7cfbb647-6f62-4bfc-9a7f-1d5475bbcf5f" />

Figura 6: Vista de Catálogo (productos.html): Catálogo estático para usuarios con acceslimitado.
<img width="975" height="470" alt="image" src="https://github.com/user-attachments/assets/e8ec4a9c-aaea-45d9-9888-01885558d9b4" />

Figura 7: Creación/Edición de Producto (producto_form.html): Formulario para producto con widget_tweaks.
<img width="458" height="458" alt="image" src="https://github.com/user-attachments/assets/7039f7fc-9c93-429f-8d02-b50be3d491da" /><img width="472" height="459" alt="image" src="https://github.com/user-attachments/assets/348b9f1a-663d-4a35-9ad8-8abb7e66b824" />

 Figura 8: Formulario Genérico (formulario.html): Template reutilizable para formularios del módulo productos. 
 <img width="472" height="459" alt="image" src="https://github.com/user-attachments/assets/bbe349c1-0df4-4827-92fe-c35f1fe6c673" />

 Figura 9: Confirmación de Eliminación (confirmar_eliminar.html): Modal con botones editarProductoBtn, eliminarProductoBtn.
 <img width="975" height="559" alt="image" src="https://github.com/user-attachments/assets/c0e9e3df-a010-4037-ad41-8b0de94e769a" />

 Figura 10: Creación de Venta (crear_venta.html): Formulario para ventas con VentaForm, widget_tweaks.
 <img width="975" height="551" alt="image" src="https://github.com/user-attachments/assets/a2430da1-e957-419a-bf96-b1857628dda8" />

 Figura 11: Listado de Ventas (lista_ventas.html): Tabla con filtros y DataTables.
 <img width="975" height="551" alt="image" src="https://github.com/user-attachments/assets/8533adc0-dec4-4050-840e-2284232b251d" />

 Figura 12: Edición de Venta (editar_venta.html): Formulario para modificar ventas.
<img width="978" height="557" alt="image" src="https://github.com/user-attachments/assets/12700103-c882-4dc3-a50d-ac2be49c2d80" />

 Figura 13: Detalle de Venta (detalle_venta.html): Detalles de una venta específica.
 <img width="975" height="454" alt="image" src="https://github.com/user-attachments/assets/0d99bd9a-15a2-458a-b9ed-d3f167e58f3d" />

 Figura 14: Historial de Venta (historial_venta.html): Cambios registrados por simple_history.
 <img width="975" height="454" alt="image" src="https://github.com/user-attachments/assets/9e4e6e7e-38fc-461e-893c-faf65b1c7f5f" />

Figura 15: Comparación de Ventas (comparar_venta.html): Compara versiones históricas.
<img width="975" height="530" alt="image" src="https://github.com/user-attachments/assets/e11d8466-5026-41d7-81d6-4fd82170eb81" />

 Figura 16: Ticket de Venta (ticket_venta.html): Visualización/impresión de tickets con |safe. 
<img width="975" height="511" alt="image" src="https://github.com/user-attachments/assets/f4ef530e-89d6-4dd3-94a8-6d8c8b4b7c39" />

 Figura 17: Confirmación de Anulación (anular_venta_confirmacion.html): Modal para anulación.
 <img width="975" height="481" alt="image" src="https://github.com/user-attachments/assets/6ffb4109-754d-434a-9106-7ed47fc5f507" />

 Figura 18: Apertura de Caja (abrir_caja.html): Formulario para saldo inicial.
<img width="975" height="484" alt="image" src="https://github.com/user-attachments/assets/988770bb-4e6c-4619-ad8f-2c23b12c0633" />

 Figura 19: Estado de Caja (estado_caja.html): Saldo y movimientos con saldo_caja_actual.
<img width="975" height="568" alt="image" src="https://github.com/user-attachments/assets/45fd9ef8-f35a-4c91-ac1e-0db94d7a51fd" />

 Figura 20: Cierre de Caja (cerrar_caja.html): Formulario para cerrar caja.
<img width="975" height="450" alt="image" src="https://github.com/user-attachments/assets/2bd9762d-1170-4bbb-8878-c981a961a920" />

 Figura 21: Movimientos de Caja (movimientos.html): Historial de movimientos con DataTables.
<img width="981" height="559" alt="image" src="https://github.com/user-attachments/assets/90adf75b-78bb-4ecc-8ad5-d18920766424" />

 Figura 22: Dashboard (dashboard.html): Resumen de métricas según rol.
 <img width="943" height="529" alt="image" src="https://github.com/user-attachments/assets/f03843f1-2845-4881-a534-3c27708412d2" />

 Figura 23: Reporte de Ventas (reporte.html): Gráficos Plotly con bg-bg-main.
<img width="975" height="559" alt="image" src="https://github.com/user-attachments/assets/6b531a85-c3e4-4ae4-a293-ba51656c5712" />
 
Figura 24: Recuperación de Contraseña (password_reset_form.html): Formulario para correo.
<img width="951" height="454" alt="image" src="https://github.com/user-attachments/assets/de7f6ed2-64a1-42b0-ab2b-0bcfd533b161" />

 Figura 25: Correo Enviado (password_reset_done.html): Confirmación de envío.
 <img width="975" height="554" alt="image" src="https://github.com/user-attachments/assets/432cccb0-ef2f-41fe-8f97-5b0735334544" />

 Figura 26: Nueva Contraseña (password_reset_confirm.html): Formulario para nueva contraseña.
 <img width="975" height="552" alt="image" src="https://github.com/user-attachments/assets/80c0c165-23fe-403f-bd4b-53a71dca88de" />

 Figura 27: Contraseña Cambiada (password_reset_complete.html): Confirmación de cambio.
<img width="975" height="556" alt="image" src="https://github.com/user-attachments/assets/55bfc223-3e4e-4f58-9114-6f0cef27c35e" />




