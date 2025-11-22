import pytesseract
from PIL import Image
from pathlib import Path
from pdf2image import convert_from_path

class ProcessModule:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def ReadImage(self) -> str:
        text = pytesseract.image_to_string(self.file_path)
        return text
    
    def ReadPDF(self) -> str:
        pages = convert_from_path(self.file_path)
        text = ""
        for page in pages:
            text += pytesseract.image_to_string(page)
        return text
    
if __name__ == '__main__':
    process_file_path = '/PythonScript/BM-Notice-12.11.2025.pdf'
    ext = Path(process_file_path).suffix[1:].lower()
    ProcessModuleInstance = ProcessModule(file_path=process_file_path)

    if ext in ('jpg', 'png'):
        text = ProcessModuleInstance.ReadImage()
    elif ext in ('pdf'):
        text = ProcessModuleInstance.ReadPDF()
    else:
        text = "Can't Process this extention file"
    print(text)
