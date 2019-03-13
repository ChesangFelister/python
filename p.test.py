                *Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=[0,1,2,3,4,5,6,7,8,9]
>>> x.append(12)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
>>> x.extend([34,45])
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 34, 45]
>>> x.pop()
45
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 34]
>>> x.insert(3,3.5)
>>> x
[0, 1, 2, 3.5, 3, 4, 5, 6, 7, 8, 9, 12, 34]
>>> x.reverse()
>>> x
[34, 12, 9, 8, 7, 6, 5, 4, 3, 3.5, 2, 1, 0]
>>> x.remove(34)
>>> x
[12, 9, 8, 7, 6, 5, 4, 3, 3.5, 2, 1, 0]
>>> x.sort()
>>> x
[0, 1, 2, 3, 3.5, 4, 5, 6, 7, 8, 9, 12]
>>> x.remove(3.5)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
>>> x.index(7)
7
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12]
>>> x.remove(12)
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x.count(5)
1
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> y=[p*10 for p in x]
>>> y
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
>>> for p in x:
	print(p*10)

	
0
10
20
30
40
50
60
70
80
90
>>> k=x[:5]
>>> k
[0, 1, 2, 3, 4]
>>> v=[5:]
SyntaxError: invalid syntax
>>> v=x[5:]
>>> v
[5, 6, 7, 8, 9]
>>> 
>>> 
>>> 
>>> n=[[1,2,3],[4,5,6],[7,8,9]]
>>> m=[]
>>> for sublist in n:
	for x in sublist:
		m.append()

		
Traceback (most recent call last):
  File "<pyshell#41>", line 3, in <module>
    m.append()
TypeError: append() takes exactly one argument (0 given)
>>> for sublist in n:
	for x in sublist:
		m.append(x)

		
>>> m
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
