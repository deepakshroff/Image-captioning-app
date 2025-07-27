from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    image = Image.open(image_path).convert('RGB')
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs, num_return_sequences=1, output_scores=True, return_dict_in_generate=True)
    caption = processor.decode(out.sequences[0], skip_special_tokens=True)

    # Confidence estimation (approx.)
    probs = torch.nn.functional.softmax(out.scores[0], dim=-1)
    confidence = torch.max(probs).item()
    return caption, round(confidence * 100, 2)