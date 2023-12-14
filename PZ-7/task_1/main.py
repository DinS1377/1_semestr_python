from string import ascii_letters

rus_alphabet = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
lat = 0
rus = 0
qwerty = 'QаавчолWDCHKвддфHI'


for i in qwerty:
    if i in ascii_letters:
        lat = lat + 1
    elif i in rus_alphabet:
        rus = rus + 1

print(lat)
print(rus)



