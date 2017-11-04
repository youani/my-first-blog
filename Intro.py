Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2+3
5
>>> 4*5
20
>>> 5-1
4
>>> 40/2
20.0
>>> 2**3
8
>>> 4+5**4
629
>>> '0la'
'0la'
>>> 'Hi there' + 'Ola'
'Hi thereOla'
>>> "Hi there" + "Ola"
'Hi thereOla'
>>> 'Ola' * 8
'OlaOlaOlaOlaOlaOlaOlaOla'
>>> "Runnin' down the hill"
"Runnin' down the hill"
>>> 'Runnin\' down the hill'
"Runnin' down the hill"
>>> 'Ola'.upper
<built-in method upper of str object at 0x03256120>
>>> 'Ola'.upper()
'OLA'
>>> 'Ola'.lower()
'ola'
>>> len('olo')
3
>>> len('rachael')
7
>>> len(458929)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    len(458929)
TypeError: object of type 'int' has no len()
>>> len(str(6739937670))
10
>>> name m= 'ola'
SyntaxError: invalid syntax
>>> name = 'ola'
>>> name
'ola'
>>> len(name)
3
>>> name = 'rachael'
>>> len(name)
7
>>> 
>>> a = 7
>>> b = 4
>>> a*b
28
>>> b**a
16384
>>> 	city = Lagos
	
SyntaxError: unexpected indent
>>> city = Lagos
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    city = Lagos
NameError: name 'Lagos' is not defined
>>> city = 'Lagos'
>>> cyti
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    cyti
NameError: name 'cyti' is not defined
>>> 
>>> name = 'peace'
>>> name
'peace'
>>> print(name)
peace
>>> []
[]
>>> lottery = [3, 10, 70, 5, 7, 2, 100, 87]
>>> len(lottery)
8
>>> lottery.sort()
>>> lottery
[2, 3, 5, 7, 10, 70, 87, 100]
>>> lottery.reverse()
>>> lottery
[100, 87, 70, 10, 7, 5, 3, 2]
>>> lottery.append(67)
>>> lottery
[100, 87, 70, 10, 7, 5, 3, 2, 67]
>>> lottery.sort
<built-in method sort of list object at 0x03261BE8>
>>> lottery.sort()
>>> lottery.reverse()
>>> lottery
[100, 87, 70, 67, 10, 7, 5, 3, 2]
>>> print(lottery)
[100, 87, 70, 67, 10, 7, 5, 3, 2]
>>> print(lottery[0])
100
>>> print(lottery[5])
7
>>> print(lottery[4])
10
>>> lottery.pop(4)
10
>>> print(lottery)
[100, 87, 70, 67, 7, 5, 3, 2]
>>> 
>>> game = [10, -5, 9, 100, -1000, 50, 95, 45]
>>> game
[10, -5, 9, 100, -1000, 50, 95, 45]
>>> game.sort()
>>> game.reverse()
>>> game
[100, 95, 50, 45, 10, 9, -5, -1000]
>>> game.append(6)
>>> game.sort()
>>> game.reverse()
>>> print(game)
[100, 95, 50, 45, 10, 9, 6, -5, -1000]
>>> 
>>> {}
{}
>>> {'name': 'Grace', 'country': 'Nigeria', 'age': '25', 'favorite_number': [5, 10, 7, 25, 9]}
{'name': 'Grace', 'country': 'Nigeria', 'age': '25', 'favorite_number': [5, 10, 7, 25, 9]}
>>> participant = {'name': 'Grace', 'country': 'Nigeria', 'age': '25', 'favorite_number': [5, 10, 7]}
>>> participant
{'name': 'Grace', 'country': 'Nigeria', 'age': '25', 'favorite_number': [5, 10, 7]}
>>> len(participant)
4
>>> participant('state') = 'Oyo'
SyntaxError: can't assign to function call
>>> participant['state'] = 'Kwara'
>>> len(participant)
5
>>> print(participant[name])
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    print(participant[name])
KeyError: 'peace'
>>> print(participant['name'])
Grace
>>> participant['name'] = 'Rachael'
>>> participant
{'name': 'Rachael', 'country': 'Nigeria', 'age': '25', 'favorite_number': [5, 10, 7], 'state': 'Kwara'}
>>> print(participant['state'])
Kwara
>>> participant.pop('state')
'Kwara'
>>> participant
{'name': 'Rachael', 'country': 'Nigeria', 'age': '25', 'favorite_number': [5, 10, 7]}
>>> 
>>> 5>2
True
>>> 5!=5
False
>>> 10==5
False
>>> 5!=6 or 4==3
True
>>> 5!= and 4==3
SyntaxError: invalid syntax
>>> 6>=3
True
>>> 5!=6 and 4==3
False
>>> a =True
>>> a
True
>>> a = 2>5
>>> a
False
>>> True or True
True
>>> True or False
True
>>> True and False
False
>>> 
