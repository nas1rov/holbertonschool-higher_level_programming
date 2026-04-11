#!/usr/bin/python3
"""Bu modul kvadratı təyin edən Square klassını saxlayır."""


class Square:
    """Kvadratı təmsil edən klass.
    
    Attributes:
        __size (int): Kvadratın tərəfinin ölçüsü.
    """

    def __init__(self, size):
        """Klassın yeni instansiyasını (obyektini) yaradır.
        
        Args:
            size (int): Yeni kvadratın ölçüsü.
        """
        self.__size = size
