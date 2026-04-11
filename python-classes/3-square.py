#!/usr/bin/python3
"""Kvadratın sahəsini hesablayan Square klassı modulu."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0):
        """Klassı inisializasiya edir və size-ı yoxlayır.

        Args:
            size (int): Kvadratın tərəfi.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Kvadratın cari sahəsini hesablayır və qaytarır.

        Returns:
            Kvadratın sahəsi (size * size).
        """
        return self.__size ** 2
