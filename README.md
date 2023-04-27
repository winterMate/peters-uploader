# Web Photo and Text Uploader
A simple web application that allows users to take a photo with their webcam and submit it along with text data to a server.

## Prerequisites
- Python 3.6 or newer
- pip (Python package installer)

## Installation
Clone the repository or download the source files.

```bash
git clone https://github.com/winterMate/peters-uploader.git
```

Change to the project directory.

```bash
cd peters-uploader
```

Create a virtual environment (optional, but recommended).

```bash
python -m venv venv
```

Activate the virtual environment.
On Windows:
```bash
venv\Scripts\activate
```
On macOS and Linux:
```bash
source venv/bin/activate
```

Install the required dependencies.
```bash
pip install -r requirements.txt
```

## Running the Application

Start the server by running the following command:
```bash
python server.py
```

Open a web browser and navigate to http://localhost:8080.

Use the webcam capture button to take a photo.

Enter the text data in the input field.

Click the "Submit" button to upload the photo and text to the server.