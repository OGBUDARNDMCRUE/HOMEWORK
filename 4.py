s = str(input('Введите слово:'))
a = s[::-1]
if s == a:
    print('Слово палиндром')
else:
    print('Слово не палиндром')