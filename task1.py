monet=int(input('Введите кол-во монет: '))
count=0
for i in range(1,monet+1):
    monetka=int(input('Введите монетка лежит решкой(0) или орлом(1): '))
    if monetka==0:
        count+=1
print(f'Необходимо перевернуть {count} монет чтоб все лежали орлом')