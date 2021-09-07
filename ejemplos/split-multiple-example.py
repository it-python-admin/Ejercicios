import re
texto = "Ramón Bilbao#Santiago de Compostela#A Coruña*NIVEL 3*MEDIA"
print(re.split('#|\*',texto))