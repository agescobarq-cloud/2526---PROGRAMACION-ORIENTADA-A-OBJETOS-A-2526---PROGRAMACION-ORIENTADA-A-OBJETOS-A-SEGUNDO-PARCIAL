class Producto:
    """
    Clase que representa un producto en el inventario.
    Contiene los atributos básicos y métodos para acceder/modificarlos (getters y setters).
    """
    
    def __init__(self, id_producto: int, nombre: str, cantidad: int, precio: float):
        """
        Constructor de la clase Producto
        
        Args:
            id_producto (int): Identificador único del producto
            nombre (str): Nombre del producto
            cantidad (int): Cantidad disponible en stock
            precio (float): Precio unitario del producto
        """
        self._id = id_producto          # Atributo protegido
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio
    
    # Getters
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def cantidad(self) -> int:
        return self._cantidad
    
    @property
    def precio(self) -> float:
        return self._precio
    
    # Setters
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = nuevo_nombre.strip()
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad: int):
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = nueva_cantidad
    
    @precio.setter
    def precio(self, nuevo_precio: float):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = nuevo_precio
    
    def __str__(self) -> str:
        """Representación en string del producto (útil para imprimir)"""
        return (f"ID: {self._id} | Nombre: {self._nombre} | "
                f"Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}")
