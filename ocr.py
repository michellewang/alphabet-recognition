try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename), lang='eng', config='--psm 10')
    return text

print(ocr_core('letter.jpg'))
