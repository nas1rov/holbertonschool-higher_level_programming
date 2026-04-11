#!/usr/bin/python3
"""Singly linked list üçün Node və LinkedList klassları."""


class Node:
    """Linked list-in düyününü (Node) təmsil edən klass."""

    def __init__(self, data, next_node=None):
        """Node-u inisializasiya edir."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data getter-i."""
        return self.__data

    @data.setter
    def data(self, value):
        """Data setter-i (mütləq tam ədəd olmalıdır)."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Next_node getter-i."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Next_node setter-i (Node obyekti və ya None olmalıdır)."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list-i idarə edən klass."""

    def __init__(self):
        """Boş bir list yaradır."""
        self.__head = None

    def __str__(self):
        """List-i çap etmək üçün mətni formalaşdırır."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """
        Yeni Node-u listin daxilinə artan sıra ilə əlavə edir.
        
        Args:
            value (int): Əlavə olunacaq rəqəm.
        """
        new_node = Node(value)
        
        # Əgər list boşdursa və ya yeni dəyər başdakından kiçikdirsə
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Düzgün mövqeyi tapmaq üçün listi gəzirik
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node
