from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/upload", methods=["POST"])
def upload():
    text_data = request.form.get("text")
    image_data = request.files.get("image")

    if not text_data or not image_data:
        return "Both text and image data are required.", 400

    image_filename = os.path.join(app.config["UPLOAD_FOLDER"], image_data.filename)
    image_data.save(image_filename)

    with open(os.path.join(app.config["UPLOAD_FOLDER"], f"{image_data.filename}.txt"), "w") as text_file:
        text_file.write(text_data)

    return f"Image and text successfully uploaded and saved as {image_data.filename} and {image_data.filename}.txt", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
