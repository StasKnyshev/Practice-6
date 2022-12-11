print('Введите последовательность скобок через запятую:')
x = input().split()
c = []
k = []
f = False
for i in range(len(x)):
    if x[i] == '(':
        c.append(x[i])
        k.append(i)
    if x[i] == ')':
        if len(c) == 0:
            print ('Скобка находится на', i, 'позиции')
            f = True
            break
        if len(c) > 0:
            if c[-1] == '(':
                c.pop()
                k.pop()
if len(c) == 0 and f == False:
    print('Верно')
if len(c) > 0 and f == False:
    print ('Скобка не закрылась на позиции: ',k[-1])
