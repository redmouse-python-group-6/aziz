 # -- coding: utf-8 --
print ('Общество в начале XXI века')
age = int(input('Сколько вам лет?: '))
if age > 0 and age < 7:
	print ('Вам в детский сад')
elif age > 7 and age < 18:
	print ('Вам в школу"')
elif age > 18 and age < 25:
	print ('Вам в профессиональное учебное заведение')
elif age > 25 and age < 60:
	print ('Вам на работу')
elif age > 60 and age < 120:
	print ('Вам предоставляется выбор')
else:
	print ('Ошибка! Это программа для людей!' * 5 )