#reportlab canvas PyPDF2

import PyPDF2 as pypdf
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors as colors
import time

def save_pdf(age = '0', sex = '', image = '', prediction = ''):
    file_name = str(hash(time.time())) + '.pdf'

    canvas = Canvas('pdf/' + file_name, pagesize=(300, 400))

    canvas.setFont("Times-Roman", 30)
    canvas.setFillColor(colors.blue)

    canvas.drawString(30, 350, "ISKINcare")

    canvas.setFont("Times-Roman", 12)
    canvas.setFillColor(colors.blue)
    canvas.drawString(30, 330, "Digitizing your skin care")


    canvas.setFillColor(colors.black)
    canvas.setFont("Times-Roman", 12)

    canvas.drawString(40, 280, "Age: " + age)

    canvas.drawString(40, 260, "Sex: " + sex)

    if image != '':

        canvas.drawString(40, 240, "image: ")

        canvas.drawImage(image,60, 130, 100, 100)

    canvas.drawString(40, 110, "prediction: " + 'epylispy')

    canvas.save()
    
    data = { 
        'url' : 'pdf/' + file_name,
     }

    return data



