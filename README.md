# Aplicación de Gestión de Ventas para Disquería con Python

Este proyecto es una aplicación de consola desarrollada para gestionar el inventario y las ventas de una disquería. Permite a los empleados agregar discos, ver el inventario, eliminar discos y registrar ventas. El sistema lleva un registro de las ventas realizadas y permite consultar el total de las transacciones.

## Características

- **Funciones Modulares**: El código está organizado en funciones para que cada una cumpla con una tarea específica, manteniendo la modularidad y legibilidad del sistema.
- **Estructura del Proyecto**: Se separa la lógica principal en dos archivos: `main.py`, que contiene el flujo del programa, y `funciones.py`, que almacena todas las funciones relacionadas con la gestión del inventario y las ventas.
- **Gestión de Inventario**: Permite agregar, eliminar y visualizar discos en el inventario, donde cada disco se representa mediante un diccionario con atributos como nombre, artista, precio y stock.
- **Registro de Ventas**: Los empleados pueden registrar ventas de discos, actualizando el stock y acumulando el total de las transacciones realizadas.
- **Validación de Datos**: Se utilizan expresiones regulares para validar las entradas de precio y stock, asegurando que sean valores numéricos válidos.
- **Interfaz de Usuario**: Menú interactivo que facilita la selección de opciones y la interacción con el sistema.
- **Reportes de Ventas**: Visualiza el total de ventas realizadas y el inventario disponible, permitiendo un análisis fácil de las transacciones.
- **Manejo de Errores**: Captura de excepciones en toda la aplicación para garantizar una experiencia de usuario fluida.

## Tecnologías Utilizadas

- Python
- Librería `math`
- Expresiones Regulares (`re`)

## Uso de Programación Estructurada

La aplicación aplica principios de programación estructurada, dividiendo el código en funciones lógicas y procedimientos que abordan tareas específicas. Este enfoque ayuda a mantener el código organizado y facilita la comprensión del sistema.
