from random import *


latters_s = ['q','w','e','r','t','y','u',
    'i','o','p','a','s','d','f','g','h',
    'j','k','l','z','x','c','v','b','n','m',
]
latters_c = ['Q','W','E','R','T','U',
    'I','O','P','A','S','D','F','G','H',
    'J','K','L','Z','X','C','V','B','N','M'
]
numbers = ['1','2','3','4','5','6','7','8','9','0']
marks = ['[',']','@','#','$','%','^','&','*','(',')','-','_','=','+','/',';',',','.','/']
while True:
    i = int(input('enter number of latters in password : '))
    print('''what do you want to use :
    [ls == small latters ]
    [lc == captal latters]
    [n == numbers]
    [m == marks]''')
    e = str(input('write like this ls-lc-n-m in the same way: '))
    ls=[]
    lc=[]
    n=[]
    m=[]    
    def ls_():
        for q in range(i):
            p = choice(latters_s)
            ls.append(p)
    def lc_():
        for q in range(i):
            o = choice(latters_c)
            lc.append(o) 
    def n_():
        for q in range(i):
            u = choice(numbers)
            n.append(u)               
    def m_():
        for q in range(i):
            y = choice(marks)
            m.append(y)   
    def print_password():
        pas = lc+ls+n+m
        mypassword = ''
        passwor = []
        for c in range(i):
            password_ = choice(pas)
            passwor.append(password_)
        print('this is your pass word :',mypassword.join(passwor))    
    if e == 'ls':
        ls_()
        print_password()                   
    if e == 'lc':
        lc_()
        print_password()
    if e == 'n':
        n_()
        print_password()
    if e == 'm':
        m_()
        print_password()

    if e == 'ls-lc-n-m':
        ls_()
        lc_()
        n_()
        m_()
        print_password()

    if e == 'ls-lc':
        ls_()
        lc_()
        print_password()
    if e == 'ls-n':
        ls_()
        n_()
        print_password()
    if e == 'ls-m':
        ls_()
        m_()
        print_password()
    if e == 'ls-lc-n':
        ls_()
        lc_()
        n_()
        print_password()
    if e == 'ls-lc-m':
        ls_()
        lc_()
        m_()
        print_password()
    if e == 'ls-n-m':
        ls_()
        n_()
        m_()
        print_password()

    if e == 'lc-n':
        lc_()
        n_()  
        print_password()
    if e == 'lc-m':
        lc_()
        m_()
        print_password()        
    if e == 'lc-n-m':
        lc_()
        n_()   
        m_()
        print_password()
    if e == 'n-m':
        n_()
        m_()
        print_password()        
    input_ = str(input('do you want generate another password y/n : '))
    if input_ == 'n':
        break


