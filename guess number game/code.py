import random




while True:
    from_ = int(input('from = '))
    to_ = int(input('to = '))

    random_number = random.randrange(from_,to_)  
    str(random_number)

    input_ = str(input('gess the number : '))


    if input_ == str(random_number) and input_ != '?':
        print('you win')
        break
    
    tip = str(input('do want a tip : y/n'))
    if tip == 'y':
            if str(random_number) >= input_:
                print('its bigger than',input_)
            if str(random_number) <= input_:
                print('its lower than ',input_)
    if tip == 'n':
        print('try agan ')

        

        


