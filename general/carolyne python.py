Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> = range(0,10)
SyntaxError: invalid syntax
>>> = range(0,10)
SyntaxError: invalid syntax
>>> x= range(0,10)
>>> for a %3==0:
	
SyntaxError: invalid syntax
>>> for a in x:
	if a %3 ==0:
		print(a)

		
0
3
6
9
>>> for a in x:
	if a%!=0:
		
SyntaxError: invalid syntax
>>> for a in x:
	if a%3!=0:
		print(a)

		
1
2
4
5
7
8
>>> for a in x:
	if a%3!=0:
		print(a)

		
1
2
4
5
7
8
>>> 
>>> 
>>> 
>>> for a in x:
	if a%3 ==0:
		print("{} is divisible by 3".format(a))
		else:
			
SyntaxError: invalid syntax
>>> for a in x:
	if a%3 ==0:
		print("{} is divisible by 3".format(a))
	else:
		print("{} is not divisible by 3".format(a))

		
0 is divisible by 3
1 is not divisible by 3
2 is not divisible by 3
3 is divisible by 3
4 is not divisible by 3
5 is not divisible by 3
6 is divisible by 3
7 is not divisible by 3
8 is not divisible by 3
9 is divisible by 3
>>> x = range(0,20)
>>>  for a in x:
	
SyntaxError: unexpected indent
>>> x = range(0,20)
>>> for a in x:
	if a %3 ==0:
		print("{} is divisible by 3".format(a))
	elif a %5 ==0:
		print("{} is divisible by 5".format(a))
	else:
		print("{} is not divisible by 3 or 5".format(a))

		
0 is divisible by 3
1 is not divisible by 3 or 5
2 is not divisible by 3 or 5
3 is divisible by 3
4 is not divisible by 3 or 5
5 is divisible by 5
6 is divisible by 3
7 is not divisible by 3 or 5
8 is not divisible by 3 or 5
9 is divisible by 3
10 is divisible by 5
11 is not divisible by 3 or 5
12 is divisible by 3
13 is not divisible by 3 or 5
14 is not divisible by 3 or 5
15 is divisible by 3
16 is not divisible by 3 or 5
17 is not divisible by 3 or 5
18 is divisible by 3
19 is not divisible by 3 or 5
>>> x = range(0,20)for a in x:
	if a %3 ==0:
		print("{} is divisible by 3".format(a))
	elif a %5 ==0:
		print("{} is divisible by 5".format(a))
	elif a %7==0:
		print("{} is divisible by 7".format(a))
		
	else:
		print("{} is not divisible by 3 or 5 or 7".format(a))
		
SyntaxError: invalid syntax
>>> 
>>> x = range(0,20)
for a in x:
	if a %3 ==0:
		print("{} is divisible by 3".format(a))
	elif a %5 ==0:
		print("{} is divisible by 5".format(a))
	elif a %7==0:
		print("{} is divisible by 7".format(a))

	else:
		print("{} is not divisible by 3 or 5 or 7".format(a))
		
SyntaxError: multiple statements found while compiling a single statement
>>> x = range(0,20)
>>> for a in x:
	if a %3 ==0:
		print("{} is divisible by 3".format(a))
	elif a %5 ==0:
		print("{} is divisible by 5".format(a))
	elif a %7 ==0:
		print("{} is divisible by 7".format(a))
		
	else:
		print("{} is not divisible by 3 or 5 or 7".format(a))

		
0 is divisible by 3
1 is not divisible by 3 or 5 or 7
2 is not divisible by 3 or 5 or 7
3 is divisible by 3
4 is not divisible by 3 or 5 or 7
5 is divisible by 5
6 is divisible by 3
7 is divisible by 7
8 is not divisible by 3 or 5 or 7
9 is divisible by 3
10 is divisible by 5
11 is not divisible by 3 or 5 or 7
12 is divisible by 3
13 is not divisible by 3 or 5 or 7
14 is divisible by 7
15 is divisible by 3
16 is not divisible by 3 or 5 or 7
17 is not divisible by 3 or 5 or 7
18 is divisible by 3
19 is not divisible by 3 or 5 or 7
>>> 
>>> for a in x:
	if a %3 ==0 and a % 5==0:
		print (a)

		
0
15
>>> for a in x:
	if a %3 ==0 or a % 5==0:
		print (a)

		
0
3
5
6
9
10
12
15
18
>>> True and True
True
>>> True and False
False
>>> True or False
True
>>> False or False
False
>>> False and True
False
>>> False or True
True
>>> 
>>>  for a in x:
	
SyntaxError: unexpected indent
>>> for a in x:
	if a %3 <2:
		print ("{} is divisible by 3".format(a))
	elif a %5>2:
		print ("{} is ivisible by 5".format(a))
	else :
		print ("{} is not divisible by 3 or 5".format(a))

		
0 is divisible by 3
1 is divisible by 3
2 is not divisible by 3 or 5
3 is divisible by 3
4 is divisible by 3
5 is not divisible by 3 or 5
6 is divisible by 3
7 is divisible by 3
8 is ivisible by 5
9 is divisible by 3
10 is divisible by 3
11 is not divisible by 3 or 5
12 is divisible by 3
13 is divisible by 3
14 is ivisible by 5
15 is divisible by 3
16 is divisible by 3
17 is not divisible by 3 or 5
18 is divisible by 3
19 is divisible by 3
>>>  "using a for loop range if else create two list a and b where a is all the numbers btn 0,100 that are divisible by 9 and b by 11"
SyntaxError: unexpected indent
>>> 
>>> 
>>> x= range (0,100)
>>> 
>>> x
range(0, 100)
>>> a=( x %3 for a in x)
>>> a
<generator object <genexpr> at 0x01EC85F0>
>>> 
>>> 
>>> a = []
>>> b=[]
>>> 
>>> for a in x:
	a==0:
		
SyntaxError: invalid syntax
>>> 
>>> for a in x:
	a=x%9
	 a.append
	 
SyntaxError: unexpected indent
>>> for a in x:
	a=x%9
	a.append(x)

	
Traceback (most recent call last):
  File "<pyshell#86>", line 2, in <module>
    a=x%9
TypeError: unsupported operand type(s) for %: 'range' and 'int'
>>> for a in x:
	a=x%9
	a.append(x)

	
Traceback (most recent call last):
  File "<pyshell#88>", line 2, in <module>
    a=x%9
TypeError: unsupported operand type(s) for %: 'range' and 'int'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> x= range (0,100)
>>> 
>>> a=[]
>>> 
>>> for a in x:
	if a %3 ==0:
		a.append

		
Traceback (most recent call last):
  File "<pyshell#103>", line 3, in <module>
    a.append
AttributeError: 'int' object has no attribute 'append'
>>> for a in x:
	if a %3 ==0:
	a.append
	
SyntaxError: expected an indented block
>>> for a in x:
	if a %3 ==0:
		a.append(x)

		
Traceback (most recent call last):
  File "<pyshell#106>", line 3, in <module>
    a.append(x)
AttributeError: 'int' object has no attribute 'append'
>>> for a in x:
	if a %3 ==0:
		a.append(a)

		
Traceback (most recent call last):
  File "<pyshell#108>", line 3, in <module>
    a.append(a)
AttributeError: 'int' object has no attribute 'append'
>>> for a in x:
	if a %3 ==0:
		a.append(x)
	elif:
		
SyntaxError: invalid syntax
>>> for a in x:
	if a % 9 ==0:
		
	elif b % 11==0:
		
SyntaxError: expected an indented block
>>> for a in x:
	if a % 9 ==0:
		a.append (x)
	elif b % 11==0:
		b.append(x)

		
Traceback (most recent call last):
  File "<pyshell#117>", line 3, in <module>
    a.append (x)
AttributeError: 'int' object has no attribute 'append'
>>> for l in x:
	if a % 9 ==0:
		a.append (x)
	elif b % 11==0:
		b.append(x)

		
Traceback (most recent call last):
  File "<pyshell#119>", line 3, in <module>
    a.append (x)
AttributeError: 'int' object has no attribute 'append'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> k = range (0,100)
>>> 
>>> a=[]
>>> b=[]
>>>  for l in k:
	
SyntaxError: unexpected indent
>>> 
>>> for l in k:
	if l % 9==0:
		a.append(l)
	elif m % 11==0:
		b.append(m)

		
Traceback (most recent call last):
  File "<pyshell#145>", line 4, in <module>
    elif m % 11==0:
NameError: name 'm' is not defined
>>> 
>>> 
>>> 
>>> using the range
SyntaxError: invalid syntax
>>> 
