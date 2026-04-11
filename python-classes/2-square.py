#!/usr/bin/python3
"""Bu modul validasiyası olan Square klassını saxlayır."""


class Square:
    """Kvadratı təmsil edən klass.
    
    Attributes:
        __size (int): Kvadratın tərəfinin ölçüsü.
    """

    def __init__(self, size=0):
        """Klassın yeni instansiyasını yaradır və dəyəri yoxlayır.
        
        Args:
            size (int): Yeni kvadratın ölçüsü (default 0).
            
        Raises:
            TypeError: Əgər size integer deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
