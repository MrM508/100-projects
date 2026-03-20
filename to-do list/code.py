

my_list = []
print('welcome to my to-do list !\n ------------------ ')
while True:
    print('------------------------')
    print('[1] add task ')
    print('[2] show all tasks ')
    print('[3] delete task  ')
    print('[4] save as txt file')
    print('[5] exit ')
    print('------------------------')
    input1 = str(input('choic : '))
    if input1 == '1':
        input2 = str(input('add name of task : '))
        my_list.append(input2)
        print('the task added \n ----------------------- \n  ')
    if input1 == '2':
        print(my_list)
    if input1 == '3':
        input3 = str(input('enter task name : '))
        for i in my_list:
            if input3 == i:
                o = my_list.index(i)
                del my_list[o]
                print('task deleted ')
    if input1 == '4':
        with open('to-do list\\my to-do list .txt','a+') as l :
            for i in my_list:
                l.write(i+'\n')
    if input1 == '5':
        break       


