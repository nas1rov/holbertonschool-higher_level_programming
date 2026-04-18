#!/usr/bin/python3
def safe_print_integer(value):
    """
    Funksiya daxil olan dəyərin tam ədəd (integer) olub-olmadığını yoxlayır 
    və onu formatlaşdırılmış şəkildə çap edir.
    """
    try:
        # Dəyəri integer formatında çap etməyə çalışırıq
        print("{:d}".format(value))
        # Əgər çap uğurlu oldusa, True qaytarırıq
        return True
    except (ValueError, TypeError):
        # Əgər formatlama zamanı xəta baş verərsə (məsələn, string gələrsə), 
        # False qaytarırıq
        return False
