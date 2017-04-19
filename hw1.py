 # -- coding: utf-8 --

x= int(input('Enter a number between 1 and 9 : '))

if x > 1 and x <= 3:
	i = 1
	s = input('Write a tex: ')
	n = int (input ('Write the number of text repeats: '))
	while i <= n:
		print (s)
		i = i + 1
elif x > 4 and x <= 6:
	n = int (input('Введите степень в которую нужно ввести число: '))
	m = n
	print (x ** m)
elif x > 7 and x <=9:
	y=x+10
	while x < y:
		print (x)
		x = x + 1
else :
	print ('Ошибка ввода')