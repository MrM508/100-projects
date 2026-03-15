# set input var 

input_ = 0 


# print welcome massage
print('  welcome to age in deys calculator !  ')


# make the user enter number greater than zero 
while input_ <= 0:

    input_ = int(input('enter you age : '))

# calculate the number of days and print the massage 
days = input_ * 365

print(f'you lived {days} days')
