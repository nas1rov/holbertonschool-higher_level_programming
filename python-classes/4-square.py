#!/usr/bin/python3
"""Square klassı üçün getter və setter modulu."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0):
        """Yeni bir Square instansiyasını inisializasiya edir.

        Args:
            size (int): Kvadratın ölçüsü.
        """
        self.size = size

    @property
    def size(self):
        """Kvadratın ölçüsünü (size) əldə edir."""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü (size) təyin edir.

        Args:
            value (int): Təyin olunacaq yeni ölçü.

        Raises:
            TypeError: Əgər value tam ədəd (integer) deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın cari sahəsini hesablayır və qaytarır.

        Returns:
            int: Kvadratın sahəsi.
        """
        return self.__size ** 2
