#!/usr/bin/python3
"""
Bu modul bir kvadratı təmsil edən Square klassını müəyyən edir.
Klass ölçü və koordinat validasiyası, həmçinin vizual çap imkanlarına malikdir.
"""


class Square:
    """
    Kvadratı təmsil edən klass.

    Bu klass həm ölçünü (size), həm də kvadratın ekrandakı
    yerini (position) idarə etmək üçün istifadə olunur.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Yeni bir Square obyektini inisializasiya edir.

        Args:
            size (int): Kvadratın bir tərəfinin ölçüsü.
            position (tuple): Kvadratın x və y koordinatları.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Kvadratın cari ölçüsünü (size) əldə etmək üçün getter."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Kvadratın ölçüsünü təyin etmək üçün setter.

        Args:
            value (int): Təyin olunacaq yeni ölçü dəyəri.

        Raises:
            TypeError: Əgər daxil edilən dəyər tam ədəd deyilsə.
            ValueError: Əgər daxil edilən dəyər 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Kvadratın koordinatlarını (position) əldə etmək üçün getter."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Kvadratın koordinatlarını təyin etmək üçün setter.

        Args:
            value (tuple): İki müsbət tam ədəddən ibarət tuple.

        Raises:
            TypeError: Əgər position formatı tələblərə uyğun deyilsə.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Kvadratın sahəsini hesablayır.

        Returns:
            int: Kvadratın sahəsi (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Kvadratı # işarələri ilə standart çıxışa (stdout) çap edir.
        
        Position[1] qədər boş sətir və position[0] qədər boşluq qoyur.
        Əgər size 0-dırsa, sadəcə bir boş sətir çap edir.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
