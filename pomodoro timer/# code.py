import time
# if you don't have windows the sonud not work 
import winsound
n = 0
print('wellcome to pomodoro timer !')
while n <= 0 :

    n = int(input('enter time in minutes  :'))

mm = n
ss = mm*60
s = 60
m = mm-1

for i in range(1,ss+1):
    time.sleep(1)
    s -=1
    if s == 0 and m != 0:

        m -= 1
        s = 60
    print(f'\r time remaing : {m}:{s}',end='')
winsound.MessageBeep(700)
print('\n time is up ! ')






