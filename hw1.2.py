 # -- coding: utf-8 --
x= input('Enter a number between 1 and 9 : ')
x = int(x)
if min(nubers) <= x <= max(nubers):
	i = 1
	s = input('Write a tex: ')
	n = int (input ('Write the number of text repeats: '))
	while i <= n:
		print (s)
		i = i + 1
elif min(nubers2) <= x <= max(nubers2):
	n = int (input('Введите степень в которую нужно ввести число: '))
	m = n
	print (x ** m)
elif min(nubers3) <= x <= max(nubers3):
	y=x+10
	while x < y:
		print (x)
		x = x + 1
else :
	print ('Ошибка ввода')
	
		

