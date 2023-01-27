from flask import * 
from OpenSSL import SSL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

@app.route('/')
def index():
    return [1]

# server_ip = '192.168.43.164'
server_ip = '127.0.0.1'

if __name__ == "__main__":
    context = ('cert.pem', 'key.pem')
    app.run( server_ip, '8000')# ,debug=True, ssl_context = context)