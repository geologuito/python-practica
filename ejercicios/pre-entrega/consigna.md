# Pre-Entrega - Sistema de Gestión Básica de Productos

## Requerimientos del sistema

### 1. Ingreso de productos
El sistema debe permitir ingresar:

- Nombre del producto
- Categoría
- Precio (sin centavos)

Los productos deben almacenarse en una lista.

Cada producto debe representarse como una sublista de 3 elementos.

Ejemplo:

```python
["banana", "fruta", 1500]
```

---

### 2. Mostrar productos
El sistema debe poder mostrar todos los productos registrados.

La información debe verse:
- ordenada
- legible
- numerada

Ejemplo:

```text
1. Banana - Fruta - $1500
2. Leche - Lacteo - $2300
```

---

### 3. Buscar productos
El sistema debe permitir buscar productos por nombre.

#### Si encuentra coincidencias:
Mostrar toda la información del producto.

#### Si NO encuentra:
Mostrar un mensaje indicando que no hubo resultados.

---

### 4. Eliminar productos
El sistema debe permitir eliminar productos usando su posición en la lista.

Ejemplo:

```text
Ingrese el numero del producto a eliminar:
```

---

# Requisitos técnicos

## ✔ Usar listas
Toda la información debe manejarse con listas.

---

## ✔ Usar bucles
Usar:
- `while`
- `for`

según corresponda.

---

## ✔ Validar datos
Validar:
- campos vacíos
- datos incorrectos
- opciones inválidas

---

## ✔ Usar condicionales
Utilizar:
- `if`
- `elif`
- `else`

para:
- menú
- validaciones
- búsqueda
- eliminación

---

## ✔ Crear un menú
El programa debe tener un menú con opciones similares a:

```text
1. Agregar producto
2. Mostrar productos
3. Buscar producto
4. Eliminar producto
5. Salir
```

---

## ✔ El programa debe seguir funcionando
El sistema debe ejecutarse continuamente hasta elegir la opción:

```text
Salir
```