from barcode import EAN13
from PIL import Image
number = '5901234123457'
my_code = EAN13(number)
my_code.save('C:/Users/JMS/Desktop/python_ex/barcode.png','new_code')

