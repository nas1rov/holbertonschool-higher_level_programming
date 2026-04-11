#!/usr/bin/python3
"""Kvadratın koordinatlarını idarə edən modul."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0, position=(0, 0)):
        """İnisializasiya metodu."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size getter-i."""
        return self.__size

    @size.setter
    def size(self, value):
        """Size setter-i və validasiyası."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Position getter-i."""
        return self.__position

    @size.setter
    @position.setter
    def position(self, value):
        """Position setter-i və validasiyası."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Sahəni hesablayır."""
        return self.__size ** 2

    def my_print(self):
        """Kvadratı koordinatlara uyğun çap edir."""
        if self.__size == 0:
            print("")
            return

        # Y koordinatı (boş sətirlər)
        [print("") for i in range(self.__position[1])]

        # X koordinatı (boşluqlar) və kvadratın özü
        for
