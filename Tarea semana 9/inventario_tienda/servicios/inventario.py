from modelos.producto import Producto
from typing import List, Optional


class Inventario:
    """
    Clase que gestiona la colección de productos.
    Utiliza una lista como estructura principal de almacenamiento.
    """

    def __init__(self):
        self._productos: List[Producto] = []

    def agregar_producto(self, producto: Producto) -> bool:
        """
        Añade un nuevo producto al inventario.
        Valida que el ID no esté repetido.

        Returns:
            bool: True si se agregó correctamente, False si el ID ya existe
        """
        if any(p.id == producto.id for p in self._productos):
            return False

        self._productos.append(producto)
        return True

    def eliminar_producto(self, id_producto: int) -> bool:
        """Elimina un producto por su ID. Retorna True si se eliminó."""
        for i, producto in enumerate(self._productos):
            if producto.id == id_producto:
                del self._productos[i]
                return True
        return False

    def actualizar_producto(self, id_producto: int, cantidad: Optional[int] = None,
                            precio: Optional[float] = None) -> bool:
        """
        Actualiza cantidad y/o precio de un producto por ID.
        Solo actualiza los campos que se proporcionen (no None).
        """
        for producto in self._productos:
            if producto.id == id_producto:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                return True
        return False

    def buscar_por_nombre(self, texto: str) -> List[Producto]:
        """Busca productos cuyo nombre contenga el texto (búsqueda parcial, sin importar mayúsculas)."""
        texto = texto.lower().strip()
        return [p for p in self._productos if texto in p.nombre.lower()]

    def obtener_todos(self) -> List[Producto]:
        """Retorna todos los productos ordenados por ID."""
        return sorted(self._productos, key=lambda p: p.id)

    def esta_vacio(self) -> bool:
        return len(self._productos) == 0