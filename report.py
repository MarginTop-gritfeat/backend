#reportlab canvas PyPDF2

import PyPDF2 as pypdf
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors as colors
import time

disease_dict = [
    "Actinic keratoses and intraepithelial carcinoma / Bowen's disease",
    "Basal cell carcinoma",
    "Benign keratosis-like lesions",
    "Dermatofibroma",
    "Melanoma",
    "Vascular lesions",
    "Melanocytic nevi"
]

sex_dict = [
    'Others',
    'female',
    'male'
]

location_dict = [
    'Others',
    'abdomen',
    'back',
    'chest',
    'face',
    'foot',
    'hand',
    'lower extremity',
    'neck',
    'scalp',
    'trunk', 
    'upper extremity'
]


def save_pdf(age = '', sex = -1, image = '', prediction = -1, location = -1):
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

    canvas.drawString(40, 280, "Age: " + str(age))

    canvas.drawString(40, 260, "Sex: " + sex_dict[sex])


    # canvas.drawString(40, 260, "Sex: " + 'बकफमषवबकफ')

    if prediction >= 0:
        location = location_dict[location]
    
    else:
        location = ''

    canvas.drawString(40, 240, "location: " + location)

    if prediction >= 0:

        disease = disease_dict[prediction]
    
    else:
        disease = ''

    if image != '':

        canvas.drawString(40, 220, "image: ")

        canvas.drawImage(image,60, 110, 100, 100)

        canvas.drawString(40, 90, "prediction: " + disease)

    else:

        canvas.drawString(40, 220, "prediction: " + disease)

    canvas.save()

    return 'pdf/' + file_name  #return url of pdf

print(save_pdf(22, 1, '', 4, 6))



