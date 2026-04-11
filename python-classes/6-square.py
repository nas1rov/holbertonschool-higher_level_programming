#!/usr/bin/python3
"""
Bu modul bir kvadratı təmsil edən Square klassını təqdim edir.
Burada ölçü (size) və koordinat (position) idarəetməsi, həmçinin
validasiya və vizual çap funksiyaları cəmlənmişdir.
"""


class Square:
    """
    Kvadratı təmsil edən və onun xüsusiyyətlərini idarə edən klass.

    Attributes:
        __size (int): Kvadratın tərəfinin ölçüsü.
        __position (tuple): Kvadratın çap olunacağı (x, y) koordinatları.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Yeni bir Square instansiyasını inisializasiya edir.

        Args:
            size (int): Kvadratın ölçüsü, susmaya görə 0-dır.
            position (tuple): Kvadratın koordinatları, susmaya görə (0, 0)-dır.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Kvadratın cari ölçüsünü (size) əldə etmək üçün istifadə olunur."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Kvadratın ölçüsünü təyin edir və onun tam ədəd olmasını yoxlayır.

        Args:
            value (int): Kvadrat üçün yeni təyin ediləcək ölçü dəyəri.

        Raises:
            TypeError: Əgər daxil edilən dəyər tam ədəd (integer) deyilsə.
            ValueError: Əgər daxil edilən dəyər 0-dan kiçikdirsə.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Kvadratın koordinatlarını (position) əldə etmək üçün istifadə olunur."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Kvadratın koordinatlarını təyin edir və onun doğruluğunu yoxlayır.

        Args:
            value (tuple): İki müsbət tam ədəddən ibarət tuple.

        Raises:
            TypeError: Əgər position formatı 2 müsbət tam ədəd olan tuple deyilsə.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Kvadratın sahəsini (size kvadratını) hesablayır və qaytarır.

        Returns:
            int: Hesablanmış sahə dəyəri.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Kvadratı # simvolları ilə standart çıxışa (stdout) çap edir.
        
        Metod position[1] qədər şaquli boşluq (yeni sətir) və 
        position[0] qədər üfüqi boşluq (space) buraxır.
        Əgər size 0-dırsa, sadəcə boş bir sətir çap edir.
        """
