import easyocr

def text_ocr(file_name):
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(file_name)
    print(result)
    return result


file_name = input("Введите имя файла: ")
print(text_ocr(file_name=file_name))