from servicios.inventario import Inventario
from modelos.producto import Producto


def mostrar_menu():
    print("\n" + "=" * 40)
    print("     SISTEMA DE GESTIÓN DE INVENTARIO")
    print("=" * 40)
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Listar inventario")
    print("6. Salir")
    print("=" * 40)


def obtener_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("¡Error! Debe ingresar un número entero.")


def obtener_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("¡Error! Debe ingresar un número decimal válido.")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = obtener_entero("Seleccione una opción (1-6): ")

        if opcion == 1:
            id_prod = obtener_entero("ID del producto: ")
            nombre = input("Nombre del producto: ").strip()
            while not nombre:
                print("El nombre no puede estar vacío.")
                nombre = input("Nombre del producto: ").strip()
            cantidad = obtener_entero("Cantidad inicial: ")
            precio = obtener_float("Precio unitario: $")

            producto = Producto(id_prod, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == 2:
            id_prod = obtener_entero("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_prod)

        elif opcion == 3:
            id_prod = obtener_entero("ID del producto a actualizar: ")
            print("Deje en blanco (Enter) los campos que NO desea actualizar.")
            cantidad_str = input("Nueva cantidad: ").strip()
            precio_str = input("Nuevo precio: $").strip()

            nueva_cantidad = int(cantidad_str) if cantidad_str else None
            nuevo_precio = float(precio_str) if precio_str else None

            inventario.actualizar_producto(id_prod, nueva_cantidad, nuevo_precio)

        elif opcion == 4:
            texto = input("Ingrese texto a buscar en el nombre: ").strip()
            if texto:
                resultados = inventario.buscar_por_nombre(texto)
                if resultados:
                    print(f"\nResultados encontrados ({len(resultados)}):")
                    for p in resultados:
                        print(p)

        elif opcion == 5:
            inventario.mostrar_todos()

        elif opcion == 6:
            print("\n¡Gracias por usar el sistema! Hasta luego.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()