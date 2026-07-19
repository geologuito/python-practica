# Proyecto Final Integrador - Sistema de Gestión de Inventario

## Descripción

Desarrollar un programa en **Python** que permita gestionar un inventario de productos utilizando una base de datos SQLite.

---

# Requerimientos

## Base de datos

Crear una base de datos llamada:

```text
inventario.db
```

Crear una tabla llamada:

```text
productos
```

con la siguiente estructura:

| Campo | Tipo | Restricciones |
|--------|------|---------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT |
| nombre | TEXT | NOT NULL |
| descripcion | TEXT | |
| cantidad | INTEGER | NOT NULL |
| precio | REAL | NOT NULL |
| categoria | TEXT | |

---

# Funcionalidades

La aplicación debe permitir:

- Registrar nuevos productos.
- Visualizar todos los productos registrados.
- Actualizar un producto mediante su **ID**.
- Eliminar un producto mediante su **ID**.
- Buscar un producto mediante su **ID**.

### Opcional

- Permitir búsquedas por **nombre** o **categoría**.

---

# Reportes

Implementar un reporte que permita mostrar todos los productos cuya **cantidad sea menor o igual** a un límite especificado por el usuario.

---

# Interfaz de usuario

Crear una interfaz de usuario mediante la terminal que incluya un **menú principal** con las opciones necesarias para acceder a todas las funcionalidades.

### Opcional

Utilizar el módulo **Colorama** para mejorar la presentación visual de la aplicación.

---

# Requisitos técnicos

El proyecto debe:

- Utilizar **funciones** para modularizar la lógica.
- Contener comentarios que expliquen las partes importantes del código.
- Validar correctamente los datos ingresados por el usuario.

---

# Menú sugerido

```text
==============================
 Sistema de Gestión de Inventario
==============================

1. Registrar producto
2. Mostrar productos
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Reporte de stock bajo
7. Salir
```

---

# Orden recomendado de desarrollo

- [X] Crear la base de datos (`inventario.db`).
- [X] Crear la tabla `productos`.
- [X] Crear el menú principal.
- [X] Implementar **Registrar producto**.
- [X] Implementar **Mostrar productos**.
- [X] Implementar **Buscar producto**.
- [X] Implementar **Actualizar producto**.
- [X] Implementar **Eliminar producto**.
- [X] Implementar **Reporte de stock bajo**.
- [X] Mejorar la interfaz con **Colorama**.
- [X] Refactorizar y comentar el código.
- [X] Subir el proyecto a GitHub.