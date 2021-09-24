from fpdf import FPDF

def generar_pdf(fichero_salida : str, textos : list, fichero_imagen : str):
    pdf = FPDF(orientation='P', unit='mm', format='A4') #Instanciar(crear) documento
    pdf.add_page() #Agregar página al documento
    pdf.set_font('Arial', 'B', 16)
    pdf.set_text_color(0, 0, 0) #Color del texto
    #Imagen (BACKGROUND)
    pdf.image('./src/bg.jpg', x = 0, y = 0, w = 210, h = 297)
    #Imagen
    pdf.image(fichero_imagen, x = 30, y = 30, w = 75)
    #Texto
    for i in range(len(textos)):
        pdf.text(120, 10*i+40, textos[i])
    #Generación del fichero
    pdf.output(fichero_salida)

