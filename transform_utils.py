from PIL import Image

def convert_grayscale_to_rgb(image):
    if image.mode == 'RGB':
        return image
    return image.convert('RGB')