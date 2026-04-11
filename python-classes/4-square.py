#!/usr/bin/python3
"""Kvadratın property-lərini təyin edən modul."""


class Square:
    """Kvadratı təmsil edən klass."""

    def __init__(self, size=0):
        """Yeni kvadrat instansiyası yaradır.
        Qeyd: Burada birbaşa self.__size yazmaq əvəzinə, 
        setter-i işə salmaq üçün self.size istifadə edirik.
        """
        self.size = size

    @property
    def size(self):
        """Getter: __size dəyərini qaytarır."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter: __size dəyərini təyin edir və yoxlayır."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Kvadratın sahəsini qaytarır."""
        return self.__size ** 2
