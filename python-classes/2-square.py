#!/usr/bin/python3
"""Square klassı üçün validasiya modulu."""


class Square:
    """Kvadrat klassı."""

    def __init__(self, size=0):
        """İnistilizasiya zamanı məlumatın doğruluğunu yoxlayırıq.
        
        Args:
            size (int): Kvadratın tərəfi (default 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
