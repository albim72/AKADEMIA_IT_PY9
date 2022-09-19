import math

print("To jest pierwsza aplikacja...")

a = 78
print(a)
print(type(a))

a = "jedynka"
print(a)
print(type(a))

b:str
b = "Henio"
print(b)
print(type(b))

b = 99.56
print(b)
print(type(b))

d = "pora roku - lato"
e = "kolejna pora: jesień"
f = "a teraz zima"

print(d,e,f,sep=" -> ")

print(12*b)

c = "4.6"
print(12*c)
#komentarz  --> CTRL + D -> powielenie linii lub bloku
print(12*eval(c))
print(12*float(c))

g1 = 10
g2 = 11

print(g1+g2,g1-g2,g1*g2,g1/g2,g1%g2,g1**g2,sep="      ")

print(round(4.678239))
print(round(4.678239,2))
print(5**2)
print(pow(5,2))
print(pow(7,0.5))
print(math.sqrt(7))

i = 1
i+=6 #i_1 = i_0+1
print(i)

i = i + 1 #matematyka dyskretna
print(i)

i*=3
print(i)

s = "lajkonik"
print(s)
print(s[0])
print(s[1])
print(s[2:5])
print(s[2:])
print(s[:6])
print(s[-1])
print(s[len(s)-3:])
print(s[-3:])


