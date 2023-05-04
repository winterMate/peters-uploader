from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__, template_folder='.')
app.config['UPLOAD_FOLDER'] = './uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file'}), 400
    image = request.files['image']
    text = request.form.get('text', '')

    if image.filename == '':
        return jsonify({'error': 'No image selected'}), 400

    if image and allowed_file(image.filename):
        timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S.%fZ')
        file_ext = os.path.splitext(image.filename)[1]
        filename = f'{timestamp}{file_ext}'
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        # Save text data alongside the image
        text_filename = f'{timestamp}.txt'
        text_path = os.path.join(app.config['UPLOAD_FOLDER'], text_filename)
        with open(text_path, 'w') as text_file:
            text_file.write(text)

        return jsonify({'message': 'Image and text uploaded successfully'}), 200
    else:
        return jsonify({'error': 'Invalid file format'}), 400

@app.route('/', methods=['GET'])
def serve_frontend():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
