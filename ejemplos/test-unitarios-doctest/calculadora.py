import doctest
"""
>>> restar(3,1)
2
"""
def sumar(s1, s2):
    """
    >>> sumar(3,4)
    7
    >>> sumar(8,12)
    20
    """
    return s1+s2

def restar(r1, r2):
    return r1-r2

def multiplicar_no_cero(m1, m2):
    return m1*m2

def dividir(d1, d2):
    return d1/d2

doctest.testmod(verbose=True) #Sin el parametro verbose=True sólo muestros errores