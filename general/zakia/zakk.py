Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 3+3
6
>>> 5-3
2
>>> 3*3
9
>>> 3x3
SyntaxError: invalid syntax
>>> 9/3
3.0
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> 10%3
1
>>> 2^^3
SyntaxError: invalid syntax
>>> 2**3
8
>>> 3==3
True
>>> 3==4
False
>>> 3!=3
False
>>> 3!=4
True
>>> 3<4
True
>>> 4<3
False
>>> 3>4
False
>>> 4>3
True
>>> 3<=3
True
>>> 3<=4
True
>>> 3<=2
False
>>> 4>=3
True
>>> 4>=5
False
>>> akirachix
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    akirachix
NameError: name 'akirachix' is not defined
>>> "akirachix"
'akirachix'
>>> "a"+"b"
'ab'
>>> "a"-"b"
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    "a"-"b"
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> "a"*5
'aaaaa'
>>> "a"*100
'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
>>> "ha"*10
'hahahahahahahahahaha'
>>> "hello"+"akirachix"
'helloakirachix'
>>> "hello" + "akirachix"
'helloakirachix'
>>> "girl"=="girl"
True
>>> 
>>> "hello "+"akirachix "
'hello akirachix '
>>> "girl"=="boy"
False
>>> "girl">"boy"
True
>>> "boy">"girl"
False
>>> "b">"a"
True
>>> "a">"b"
False
>>> "a"=3
SyntaxError: can't assign to literal
>>> "a"
'a'
>>> "a"=3
SyntaxError: can't assign to literal
>>> a=3
>>> a=3
>>> a
3
>>> a="girl"
>>> a
'girl'
>>> b=10
>>> b
10
>>> a*b
'girlgirlgirlgirlgirlgirlgirlgirlgirlgirl'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'int'>
>>> c=5
>>> d=7
>>> e=c*d
>>> l=d%c
>>> e>l
True
>>> l>e
False
>>> c*d<d-c*12
False
>>> first name="zakia"
SyntaxError: invalid syntax
>>> firstname="zakia"
>>> number="0774731946"
>>> "hello "+ firstname +"your number is" + number
'hello zakiayour number is0774731946'
>>> "hello "+ firtname +" your number is "+ number
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    "hello "+ firtname +" your number is "+ number
NameError: name 'firtname' is not defined
>>> firstname= "zakia"
>>> lastname="Mohamed"
>>> school="AkiraChix"
>>> firstname
'zakia'
>>> lastname
'Mohamed'
>>> school
'AkiraChix'
>>> 'hello "+ firstname +lastname +" welcome to"+ school
SyntaxError: EOL while scanning string literal
>>> "hello "+ firstname+ lastname +"welcome to" + school
'hello zakiaMohamedwelcome toAkiraChix'
>>> "hello " + firstname + lastname+" welcome to"+ school
'hello zakiaMohamed welcome toAkiraChix'
>>> 
'hello zakiaMohamed welcome toAkiraChix'
'hello zakiaMohamed welcome toAkiraChix'
>>> "hello "+ firstname+" "+lastname+ " welcome to "+ school
'hello zakia Mohamed welcome to AkiraChix'
>>> 
