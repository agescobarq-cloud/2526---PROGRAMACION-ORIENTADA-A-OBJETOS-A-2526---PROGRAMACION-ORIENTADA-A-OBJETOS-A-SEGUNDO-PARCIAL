from modelos.producto import Producto
from typing import List, Optional


class Inventario:
    """
    Clase que gestiona la colección de productos.
    Implementa las operaciones principales del sistema.
    """

    def __init__(self):
        self._productos: List[Producto] = []

    def agregar_producto(self, producto: Producto) -> bool:
        """
        Añade un nuevo producto si el ID no está repetido.
        Retorna True si se agregó con éxito, False si el ID ya existe.
        """
        if any(p.id == producto.id for p in self._productos):
            print(f"¡Error! Ya existe un producto con ID {producto.id}")
            return False

        self._productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado correctamente.")
        return True

    def eliminar_producto(self, id_producto: int) -> bool:
        """Elimina un producto por su ID. Retorna True si se eliminó."""
        for i, producto in enumerate(self._productos):
            if producto.id == id_producto:
                eliminado = self._productos.pop(i)
                print(f"Producto '{eliminado.nombre}' (ID: {id_producto}) eliminado.")
                return True
        print(f"No se encontró producto con ID {id_producto}")
        return False

    def actualizar_producto(self, id_producto: int, cantidad: Optional[int] = None,
                            precio: Optional[float] = None) -> bool:
        """Actualiza cantidad y/o precio de un producto por ID."""
        for producto in self._productos:
            if producto.id == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print(f"Producto ID {id_producto} actualizado correctamente.")
                return True
        print(f"No se encontró producto con ID {id_producto}")
        return False

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        """Busca productos cuyo nombre contenga el texto (insensible a mayúsculas)"""
        texto = texto.lower()
        resultados = [p for p in self._productos if texto in p.nombre.lower()]

        if not resultados:
            print(f"No se encontraron productos que contengan '{texto}'")
        return resultados

    def mostrar_todos(self) -> None:
        """Muestra todos los productos registrados"""
        if not self._productos:
            print("El inventario está vacío.")
            return

        print("\n=== INVENTARIO ACTUAL ===")
        print("-" * 60)
        for producto in self._productos:
            print(producto)
        print("-" * 60)