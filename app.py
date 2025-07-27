from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from caption_model import generate_caption

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    caption = None
    confidence = None
    filename = None
    if request.method == 'POST':
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
            caption, confidence = generate_caption(image_path)
    return render_template('index.html', caption=caption, confidence=confidence, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)