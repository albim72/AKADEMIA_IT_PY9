import os

f = open("dane.txt","r",encoding="utf-8")

print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
print(f.closed)

print("\ndrugie podejście:\n")
f = open("dane.txt","r",encoding="utf-8")
print(f.read())
f.close()
print(f.closed)

print("\ntrzecie podejście:\n")
f = open("dane.txt","r",encoding="utf-8")

for x in f:
    print(x)

f.close()
print(f.closed)

#tworzenie nowego pliku
g = open("message.txt","a",encoding="utf-8")
g.write("to jet istotna wiadomość: CCC45\n")
g.close()


print("\nzawartość pliku: message.txt\n")
f = open("message.txt","r",encoding="utf-8")
print(f.read())
f.close()

if os.path.exists("message.txt"):
    os.remove("message.txt")
    print("Plik został usunięty")
else:
    print("Plik nie istnieje")
