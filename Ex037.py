lista=[]
num=int(input('Digite umm numero inteiro: '))

print('Digite 1 para transformar em binário')
print('Digite 2 para transformar em octal')
print('Digite 3 para transformar em Hexadecimal')

opcao=int(input())

if opcao == 1:
    while(num>=1) :   
        x=num%2
        lista.insert(0,x)
        num=num//2
    print(lista)

elif opcao == 2:
    while(num>=1) :   
        x=num%8
        lista.insert(0,x)
        num=num//8
    print(lista)

elif opcao == 3:
    while(num>=1) :   
        x=num%16
        
        if x==10:
            x='A'
        elif x==11:
            x='B'
        elif x==12:
            x='C'
        elif x==13:
            x='D'
        elif x==14:
            x='E'
        elif x==15:
            x='F'
        else:
            pass
        lista.insert(0,x)
        num=num//16
    print(lista)