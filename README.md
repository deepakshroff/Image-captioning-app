# 🖼️ AI Image Captioning App

The **AI Image Captioning App** is a Flask-based web application that uses a deep learning model to generate intelligent captions for uploaded images. It analyzes the image and provides the best possible description along with a confidence score.

---

## 🔍 Screenshots

<table>
  <tr>
    <td><img src="Screenshot%202025-07-27%20162017.png" width="100%"/></td>
    <td><img src="Screenshot%202025-07-27%20161935.png" width="100%"/></td>
  </tr>
</table>

---

## 🚀 Features

- 📷 Upload any JPG/PNG image  
- 🧠 Automatically generates a descriptive caption  
- 📊 Displays prediction confidence percentage  
- 🎨 Smooth, responsive, and aesthetic UI  
- 💡 Built using Flask, Python, and a custom ML model  

---

## 🧪 Tech Stack

### 💻 Frontend
- HTML5
- CSS3
- Jinja2 (Flask template rendering)

### 🧠 Backend
- Python
- Flask
- Pre-trained image captioning model
- Custom module: `caption_model.py`

---

## 💡 How to Run Locally

### 🛠 Prerequisites
- Python 3.x  
- Pip  
- Virtualenv (optional but recommended)

### ⚙️ Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/AI-Image-Captioning.git
   cd AI-Image-Captioning

---

## 🔍 How It Works
- User uploads an image through the UI
- The image is saved to the /static/uploads/ directory
- The model (in caption_model.py) processes the image
- The generated caption and confidence score are returned and displayed

## 🔮 Future Enhancements
- 🖼️ Support for drag-and-drop image upload
- 🧠 Use more powerful models like BLIP or Vision Transformers
- 🌐 Add language translation for captions
- ☁️ Deploy on Render or HuggingFace Spaces

---