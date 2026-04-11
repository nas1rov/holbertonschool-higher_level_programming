#!/usr/bin/python3
"""Kvadratı çap edən Square klassı modulu."""


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
        """Kvadratın ölçüsünü əldə edir."""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü təyin edir.

        Args:
            value (int): Yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər value integer deyilsə.
            ValueError: Əgər value 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini hesablayır və qaytarır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı stdout-da # işarəsi ilə çap edir.
        
        Əgər size 0-dırsa, boş bir sətir çap edir.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
