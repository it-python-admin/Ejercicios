def sumar(s1, s2, s3=10):
    resultado = s1+s2+s3
    return resultado
rdo = sumar(5,7)
print(rdo)

def restar(r1, r2=None):
    if (r2 is None):
        resultado = r1
    else:
        resultado = r1 - r2
    return resultado
rdo = restar(5)
print(rdo)
rdo = restar(5,4)
print(rdo)