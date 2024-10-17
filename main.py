import modulos.funciones as f
import math

def main():
    inventario = []
    ventas_realizadas = []
    continuar = True

    while continuar:
        print("\n--- Disquería Indie Symphony ---")
        print("1. Agregar Disco")
        print("2. Ver Discos")
        print("3. Eliminar lote de Discos")
        print("4. Registrar Venta")
        print("5. Ver Ventas")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del disco: ")
            artista = input("Ingrese el artista del disco: ")

            # Validar el precio
            precio = None
            while precio is None:
                precio_input = input("Ingrese el precio del disco: ")
                if f.validar_precio(precio_input):
                    precio = float(precio_input)
                else:
                    print("Formato no válido, por favor intente nuevamente.")

            # Validar el stock
            stock = None
            while stock is None:
                stock_input = input("Ingrese el stock del disco: ")
                if f.validar_stock(stock_input):
                    stock = int(stock_input)
                else:
                    print("Formato no válido, por favor intente nuevamente.")

            nuevo_disco = {'nombre': nombre, 'artista': artista, 'precio': precio, 'stock': stock}
            inventario = f.agregar_disco(inventario, nuevo_disco)

        elif opcion == "2":
            f.ver_discos(inventario)

        elif opcion == "3":
            f.ver_discos(inventario)
            indice = int(input("Seleccione el número del lote de discos a eliminar: ")) - 1
            inventario = f.eliminar_disco(inventario, indice)

        elif opcion == "4":
            total_venta = 0
            comprar_mas = 's'
            while comprar_mas.lower() == 's':
                f.ver_discos(inventario)
                indice = int(input("Seleccione el número del disco a vender: ")) - 1
                inventario, precio = f.registrar_venta(inventario, indice, ventas_realizadas)
                total_venta += precio
                comprar_mas = input("¿Desea comprar otro disco? (s/n): ")

            total_venta = math.floor(total_venta * 100) / 100  # Redondeamos el total a dos decimales
            print(f"Total gastado en esta compra: ${total_venta}")

        elif opcion == "5":
            f.ver_ventas(ventas_realizadas)

        elif opcion == "6":
            print("Saliendo del sistema...")
            continuar = False

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()