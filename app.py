from flask import * 
from OpenSSL import SSL
from flask_cors import CORS
import predict as predict_disease
import log
import time
from codecs import encode
import base64
import json
import report
import monitor as monitor_disease

app = Flask(__name__)
CORS(app)


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

@app.route('/')
def index():
    return [1]

@app.route('/predictdisease' , methods = ['GET', 'POST'])
def predictdisease():
    if request.method == 'POST':
        img = request.form['image']
        # img = request.files['image']
        age = request.form['age']
        sex = request.form['sex']
        location = request.form['location']
        print(age, sex, location)
        bytes_img = encode(img, 'utf-8')
        binary_img = base64.decodebytes(bytes_img)
        image_file = 'images/' + str(hash(time.time())) + '.jpg'
        with open(image_file, "wb") as fh:
            fh.write(binary_img)
        disease = predict_disease.predict(image_file , int(sex), int(location), int(age))#, sex, location, age)
        report_file = report.save_pdf(age, sex, image_file, disease, location)
        log.store(result = disease, report = report_file, image = image_file)
        disease['report'] = report_file
        return jsonify(disease)
        # return jsonify({
        #     'report' : report_file,
        #     'disease' : disease,
        #     # 'age' : age,
        #     # 'sex' : report.sex_dict[int(sex)],
        #     # 'location' : report.location_dict[int(location)]
        # })
    return [0]

@app.route('/monitor' , methods = ['GET', 'POST'])
def monitor():
    if request.method == 'POST':
        # img = request.form['image']
        # # img = request.files['image']
        # bytes_img = encode(img, 'utf-8')
        # binary_img = base64.decodebytes(bytes_img)
        # image_file = 'images/monitor/' + str(hash(time.time())) + '.jpg'
        # with open(image_file, "wb") as fh:
        #     fh.write(binary_img)
        # relation = monitor_disease.predict(image_file)#, sex, location, age)
        
        # report_file = report.save_pdf(age, sex, image_file, disease, location)
        monitor_disease.store(relation = 'relation', image = 'image_file')
        return jsonify({
            monitor_disease.retrieve_all()
        })
    return [0]

server_ip = '100.64.131.174'
# server_ip = '127.0.0.1'

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run(server_ip, '8000' ,debug = True, ssl_context = context)