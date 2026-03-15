from random import *
while True:
    output = ['rock','peper','scissor']
    choice_ = choice(output)
    print('choice : rock , paper , scissor')
    n = str(input('your choice :'))
    print('my choice is',choice_)
    if n == 'rock':
        if choice_ == 'rock':
            print('=')
        elif choice_ == 'paper':
            print('you lose !')
        elif choice_ == 'scissor':
            print('you win !')        
    if n == 'paper':
        if choice_ == 'rock':
            print('you win')
        elif choice_ == 'paper':
            print('=')
        elif choice_ == 'scissor':
            print('you lose !')    
    if n == 'scissor':
        if choice_ == 'rock':
            print('you lose')
        elif choice_ == 'paper':
            print('you win')
        elif choice_ == 'scissor':
            print('=')            
         