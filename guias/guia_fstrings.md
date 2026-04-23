# 🧪 Guía de práctica — f-strings en Python

Esta guía propone una serie de ejercicios progresivos para practicar el uso de **f-strings** en Python.

📌 Los ejercicios están organizados por niveles de dificultad.

📁 La resolución de los ejercicios se encuentra en:

```
sandbox/fstrings_practica.py
```

---

## 🧠 ¿Qué es un f-string?

Un **f-string** permite insertar variables y expresiones dentro de un string de forma clara y sencilla, y además **formatear texto** de manera muy flexible.

### Sintaxis básica:

```python
f"texto {variable}"
```

También permite aplicar formato:

```python
f"{valor:formato}"
```


---

### 🧩 Componentes

* **valor** → variable o expresión (`nombre`, `edad`, etc.)
* `:` → separa el valor del formato
* **formato** → define alineación, ancho, relleno, etc.

---

### 🎯 Alineación

Permite ubicar el texto dentro de un ancho determinado:

```python
f"{texto:<10}"   # izquierda
f"{texto:^10}"   # centrado
f"{texto:>10}"   # derecha
```

---

### ✨ Relleno

Podés completar espacios vacíos con caracteres:

```python
f"{texto:*^10}"  # centrado con *
f"{texto:-<10}"  # izquierda con -
```

---

### 💡 Ejemplo aplicado

```python
nombre = "Gonzalo"
print(f"{nombre:^20}")
```

---

### 🔗 Recursos

* https://www.w3schools.com/python/python_strings_format.asp
* https://www.w3schools.com/python/python_string_formatting.asp

---

### 🧠 Nota

Este tipo de formateo se usa, por ejemplo, para:

* construir tarjetas de presentación
* alinear datos en consola
* mejorar la legibilidad de la salida

Podés ver un ejemplo práctico en:

```
sandbox/tarjeta_v3_dinamica.py
```

---

## 🎮 Nivel 1 — Básico

👉 Mostrá el siguiente mensaje:

```
Hola Gonzalo
```

📌 Condiciones:

* Usar una variable `nombre`
* Usar f-string (no concatenación)

---

## 🎮 Nivel 2 — Expresión

👉 Mostrá:

```
El próximo año tendrás 35 años
```

📌 Condiciones:

* Tenés `edad = 34`
* Hacer el cálculo dentro del f-string

---

## 🎮 Nivel 3 — Alineación

👉 Mostrá la palabra:

```
Python
```

📌 Condiciones:

* Debe estar **centrada en 20 caracteres**

💡 Tip:

* Usar `^` dentro del formato

---

## 🎮 Nivel 4 — Relleno

👉 Mostrá:

```
****Python****
```

📌 Condiciones:

* Usar f-string
* No escribir los `*` manualmente
* El relleno debe salir del formato

💡 Tip:

* Podés combinar alineación y caracteres de relleno

---

## 🎮 Nivel 5 — Debug

Dadas las variables:

```python
x = 10
y = 5
```

👉 Mostrá exactamente:

```
x=10, y=5, suma=15
```

📌 Condiciones:

* Usar f-string
* Mostrar nombre de variable y valor automáticamente

---

## 🚀 Extra (opcional)

👉 Probá modificar los ejercicios:

* Cambiar el ancho de alineación
* Usar otros caracteres de relleno
* Agregar más variables

---

## 💬 Conclusión

Los **f-strings** son una herramienta fundamental en Python para:

* Mostrar datos de forma clara
* Formatear texto
* Escribir código más limpio y legible

Practicar estos ejercicios te va a ayudar a dominarlos rápidamente.
