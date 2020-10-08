#Zadanie 1
def zad1(x,y):
    z=x+'.'+y
    return z

#print(zad1('J','Kowalski'))

#Zadanie 2
def zad2(x,y):
    c=x.capitalize()
    v=y.capitalize()
    z=c[0]+'.'+v
    return z

#print(zad2('jan','kowalski'))

#zadanie 3
def zad3(x,y,z):
    c=str(x)
    v=str(y)
    b=int(c+v)
    return b-z


#print(zad3(20,20,20))

#Zadanie 4
def zad4(x,y,z):
    return z(x,y)

#print(zad4('Jan','Kowalski',zad2))

#Zadanie 5
def zad5(x,y):
    if x>0 and y>0:
        return x/y

#print(zad5(4,2))

#zadanie 6
def zad6():
    x=0
    while x!=100:
        y=int(input())
        x+=y
        print('suma=')
        print(x)

#zad6()

#Zadanie 7
def zad7(x):
    z=tuple(x)
    return z


a=[4,5,6,7,78,9,0]
#print(zad7(a))

#Zadanie 8
def zad8():
    x=[]
    c=0
    print('Aby zakonczyc dodawanie liczb wpisz "koniec"')
    while c!='koniec':
        c=input()
        if c!='koniec':
            x.append(c)
    x=tuple(x)
    return x
#print(zad8())

#Zadanie 9
def zad9(x):
    dz=['poniedzialek','wtorek','sroda','czwartek','piatek','sobota','niedziela']
    return dz[x-1]

#print(zad9(7))

#Zadanie 10
def zad10(x):
    if x == x[::-1]:
        return 'Wyraz jest palindromem'
    else:
        return 'Wyraz nie jest palindromem'

print(zad10('kot'))