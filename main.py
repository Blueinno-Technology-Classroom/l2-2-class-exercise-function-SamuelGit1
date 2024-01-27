##################################################
'''
Q1: 
'''

def greet(name):
   print(f'Hi, {name}!')

greet('Alice')
greet('Bob')

##################################################
'''
Q2:
'''

def greet(name1, name2):
   print(f'Hi, {name1} and {name2}')


greet(name2='Bob', name1='Alex')

##################################################
'''
Q3:
'''

def find_rect_area(width, height):
    print(f'the rectangle  area is {width * height}')


find_rect_area(width=12.3, height=45.6)

##################################################
'''
Q4:
'''

def bought_and_fed(animal):
    print(f'Bought me a {animal} and the {animal} pleased me, I fed my {animal} under yonder tree.', end=' ')
    
def fiddle_cat():
    print('Cat goes fiddle-i-fee.', end='\n')

def hen_chimmy_chuck():
    print('Hen goes chimmy-chuck, chimmy-chuck,', end=' ')
    fiddle_cat()

def duck_quack():
    print('Duck goes quack, quack,', end=' ')
    hen_chimmy_chuck()

def goose_hissy():
    print('Goose goes hissy, hissy,', end=' ')
    duck_quack()

bought_and_fed('cat')
fiddle_cat()
bought_and_fed('hen')
hen_chimmy_chuck()
bought_and_fed('duck')
duck_quack()
bought_and_fed('goose')
goose_hissy()

##################################################
