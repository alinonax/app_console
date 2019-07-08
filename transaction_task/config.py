import os

INFILE_NAME = os.path.join('data', 'magic_summer.txt')

LINE_LEN = 120
LINE_ENDING = '\r\n'

HEADER_ID = '01'
TRANS_ID = '02'
TRAILER_ID = '03'

ID = slice(0, 2)

NAME = slice(2, 30)
SURNAME = slice(30, 60)
PATRONYMIC = slice(60, 90)
ADDRESS = slice(90, 120)

TRANS_COUNTER = slice(2, 8)
TRANS_SUM = slice(8, 20)
CURRENCY_CODE = slice(20, 23)
TRANS_FILLER = slice(23, 120)

TRAILER_TRANS_NUMBER = slice(2, 8)
TRAILER_TRANS_AMOUNT = slice(8, 20)
TRAILER_FILLER = slice(20, 120)
