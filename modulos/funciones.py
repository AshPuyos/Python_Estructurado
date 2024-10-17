import re

def ver_discos(inventario):
    """Muestra los discos disponibles en el inventario."""
    if not inventario:  # Verifica si el inventario está vacío
        print("\nNo hay discos disponibles actualmente.")
    else:
        print("\n--- Discos Disponibles ---")
        for idx, disco in enumerate(inventario):
            print(f"{idx + 1}. {disco['nombre']} - {disco['artista']} - Stock: {disco['stock']} - Precio: ${disco['precio']}")

def agregar_disco(inventario, disco):
    """Agrega un disco al inventario."""
    inventario.append(disco)
    print(f"Disco '{disco['nombre']}' agregado exitosamente.")
    return inventario

def eliminar_disco(inventario, indice):
    """Elimina un lote de discos del inventario por índice."""
    if 0 <= indice < len(inventario):
        disco_eliminado = inventario.pop(indice)
        print(f"Lote de discos '{disco_eliminado['nombre']}' eliminado exitosamente.")
    else:
        print("Índice inválido.")
    return inventario

def registrar_venta(inventario, indice, ventas_realizadas):
    """Registra una venta de un disco por índice y devuelve el precio de venta."""
    if 0 <= indice < len(inventario):
        disco_vendido = inventario[indice]
        if disco_vendido['stock'] > 0:
            disco_vendido['stock'] -= 1  
            print(f"Venta registrada: {disco_vendido['nombre']} - ${disco_vendido['precio']}. Stock restante: {disco_vendido['stock']}")
            ventas_realizadas.append(disco_vendido)  # Añadir a la lista de ventas
            return inventario, disco_vendido['precio']  # Devolver el inventario y el precio
        else:
            print("No hay stock disponible para vender.")
            return inventario, 0  # Devolver 0 si no se pudo vender
    else:
        print("Índice inválido.")
        return inventario, 0  # Devolver 0 si el índice es inválido

def ver_ventas(ventas_realizadas):
    """Muestra las ventas realizadas."""
    print("\n--- Ventas Realizadas ---")
    if not ventas_realizadas:
        print("No se han realizado ventas.")
    else:
        total_ventas = 0  # Variable para acumular el total
        for idx, venta in enumerate(ventas_realizadas):
            print(f"{idx + 1}. {venta['nombre']} - ${venta['precio']}")
            total_ventas += venta['precio']  # Acumular el total
        print(f"Total acumulado de ventas: ${total_ventas}")

def validar_precio(precio_input):
    """Valida que el precio sea un número positivo."""
    return re.match(r'^\d+(\.\d+)?$', precio_input) is not None

def validar_stock(stock_input):
    """Valida que el stock sea un número entero positivo."""
    return re.match(r'^\d+$', stock_input) is not None
