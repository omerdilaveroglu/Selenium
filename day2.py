faiz = 1.59
vade = "36"
krediAdi ="İhtiyac Kredisi"

print(faiz+float(vade))

print("selam {name}".format(name="Omer"))

print("Selam # ".replace("#","Omer"))

metin = f"Hosgeldiniz {vade}"

print(metin)

krediler = ["İhtiyaç Kredisi","Taşıt Kredisi","Konut Kredisi"]

print(krediler[0])


print("*************")

for i in range(10):
    print(i)


print("*************")

for i in range(5,10):
    print(i)

    print("*************")

for i in range(5,35,5):
    print(i)

print("*************")

for kredi in krediler:
    print(kredi)

print("*************")

for i in range(len(krediler)):
    print(krediler[i])

print("*******While*********")

while i < len(krediler):
    print(krediler[i])
    i += 1

print("*************")


while i < 10:
    print("x")
    i += 1
print("y")

print("*************")




