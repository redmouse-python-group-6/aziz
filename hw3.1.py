def func1(*args):
	temp_var=args[0]
	print(temp_var**1)
	for i in args[1:]:
		print(i**temp_var)
		temp_var = i 
