def sumar(s1, s2):
    return s1+s2

def test_sumar():
    rdo = sumar(3,8)
    if (rdo==11):
        pass
    else:
        print("La función sumar da un resultado erróneo")

    rdo = sumar(-3,8)
    if (rdo==5):
        pass
    else:
        print("La función sumar da un resultado erróneo")


test_sumar()