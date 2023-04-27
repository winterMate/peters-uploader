import os
import base64
import time
from flask import Flask, request
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'photo' not in request.form or 'text' not in request.form:
        return 'Invalid request', 400

    photo = request.form['photo']
    text = request.form['text']

    if photo == '' or text == '':
        return 'No photo or text provided', 400

    img_data = base64.b64decode(photo.split(',')[1])
    filename = secure_filename(f"photo_{time.time()}.jpeg")
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    with open(filepath, 'wb') as f:
        f.write(img_data)

    with open(os.path.join(app.config['UPLOAD_FOLDER'], f"{filename}_text.txt"), 'w') as f:
        f.write(text)

    return 'Upload successful', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

