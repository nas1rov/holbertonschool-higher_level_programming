#!/usr/bin/python3
"""Square klassını təyin edən modul."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0):
        """Yeni bir Square instansiyasını inisializasiya edir.

        Args:
            size (int): Yeni kvadratın ölçüsü.
        Raises:
            TypeError: Əgər size integer deyilsə.
            ValueError: Əgər size < 0 olarsa.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
