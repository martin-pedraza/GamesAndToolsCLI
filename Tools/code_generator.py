import qrcode
import barcode
from barcode.writer import ImageWriter

BARCODE = "1"
QRCODE = "2"
FILENAME = "code.png"

def generate_and_save_code():
    code_type = ask_for_code_type()
    code_data = ask_for_code_data(code_type)
    code_image = generate_code(code_type, code_data)
    save_code_image(code_image)
    print("The code has been generated in the file:", FILENAME)

def ask_for_code_type():
    while True:
        print("Would you like to generate a barcode or a QR code?")
        code_type = input("1. Barcode\n2. QR code\nOption: ")
        if code_type in (BARCODE, QRCODE):
            return code_type
        print("Invalid option. Please select 1 or 2.")

def ask_for_code_data(code_type):
    data = input("What data would you like to encode?\nYour input here: ")
    while (code_type == BARCODE and (len(data) < 12 or not data.isdecimal())):
        print("A minimum of 12 numeric characters is required for barcode.")
        data = input("What data would you like to encode?\nYour input here: ")
    return data

def generate_code(code_type, data):
    generator = generate_barcode if code_type == BARCODE else generate_qrcode
    return generator(data)

def generate_qrcode(data):
    return qrcode.make(data)

def generate_barcode(data):
    return barcode.get_barcode_class('ean13')(data, writer=ImageWriter())

def save_code_image(code_image):
    code_image.save(FILENAME)

if __name__ == '__main__':
    generate_and_save_code()
