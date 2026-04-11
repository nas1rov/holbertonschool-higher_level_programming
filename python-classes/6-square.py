#!/usr/bin/python3
"""Kvadratı təyin edən Square sinfi modulu."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0, position=(0, 0)):
        """Yeni Square obyektini inisializasiya edir.

        Args:
            size (int): Kvadratın tərəfinin ölçüsü.
            position (int, int): Kvadratın koordinatları (tuple).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Kvadratın ölçüsünü geri qaytarır."""
        return self.__size

    @size.setter
    def size(self, value):
        """Kvadratın ölçüsünü təyin edir və yoxlayır."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Kvadratın mövqeyini (koordinatlarını) geri qaytarır."""
        return self.__position

    @position.setter
    def position(self, value):
        """Kvadratın mövqeyini təyin edir və yoxlayır."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Kvadratın sahəsini hesablayır və qaytarır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı '#' simvolu ilə çap edir, mövqeyini nəzərə alır."""
        if self.__size == 0:
            print("")
            return

        # Şaquli boşluq (position[1])
        [print("") for i in range(self.__position[1])]

        # Kvadratın sətirləri
        for i in range(self.__size):
            # Üfüqi boşluq (position[0])
            print(" " * self.__position[0], end="")
            # Kvadratın özü
            print("#" * self.__size)
