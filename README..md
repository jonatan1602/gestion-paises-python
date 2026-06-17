# Gestión de Datos de Países en Python

## 📝 Descripción
Este proyecto fue desarrollado para el **Trabajo Práctico Integrador de Programación 1** de la *Tecnicatura Universitaria en Programación*.

La aplicación permite gestionar información de países almacenada en un archivo CSV mediante operaciones de búsqueda, filtrado, ordenamiento y generación de estadísticas.

---

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3
* **Persistencia:** Archivo CSV (`paises.csv`)
* **Estructuras de Datos:** Listas y Diccionarios
* **Paradigma:** Programación Estructurada y Modular (Funciones)

---

## 🚀 Funcionalidades
El sistema cuenta con un menú interactivo que permite realizar las siguientes acciones:
* 📊 **Mostrar países:** Listado completo de los registros.
* 🔍 **Buscar país por nombre:** Localización exacta de un país.
* ➕ **Agregar país:** Inserción de nuevos registros al sistema.
* 🔄 **Actualizar población y superficie:** Modificación de datos existentes.
* ❌ **Eliminar país:** Borrado de registros.
* 🗺️ **Filtrar por continente:** Agrupación de países por su región.
* 👥 **Filtrar por rango de población:** Búsqueda segmentada por cantidad de habitantes.
* 📐 **Filtrar por rango de superficie:** Búsqueda segmentada por extensión territorial.
* 🔤 **Ordenar por nombre:** Ordenamiento alfabético.
* 📈 **Ordenar por población:** Ordenamiento numérico por habitantes.
* 📉 **Ordenar por superficie:** Ordenamiento numérico (ascendente o descendente).
* 📋 **Mostrar estadísticas generales:** Cálculos y métricas globales sobre los datos.

---

## 📊 Estructura de Datos

Los países son almacenados internamente dentro de una **lista de diccionarios**. Cada país se representa mediante un diccionario con los siguientes campos:

* `nombre` (String)
* `poblacion` (Integer)
* `superficie` (Float/Integer)
* `continente` (String)

### Ejemplo de registro en el archivo CSV:
```csv
Argentina,45376763,2780400,América
```

## Ejecución
* Abrir una terminal
* Ubicarse en la carpeta del proyecto
* Ejecutar: main.py

## Link video
https://drive.google.com/file/d/1WamgND2Q6ULbgz0XWC96Za-EfYezr--V/view?usp=sharing

Jonatan Farfán
