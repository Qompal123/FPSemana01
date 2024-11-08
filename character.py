character1 = str(input("What is your character name? "))
vida1=int(input("Health points? "))
nivel1=int(input("Level? "))

character2 = str(input("What is your character name? "))
vida2=int(input("Health points? "))
nivel2=int(input("Level? "))

character3 = str(input("What is your character name? "))
vida3=int(input("Health points? "))
nivel3=int(input("Level? "))


print(character1)
print(vida1)
print(nivel1)

print(character2)
print(vida2)
print(nivel2)

print(character3)
print(vida3)
print(nivel3)

array=[
    [character1,(vida1,nivel1)],
    [character2,(vida2,nivel2)],
    [character3,(vida3,nivel3)]
]

print(array)

def arrumação_characterlvl(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j][1][1]<array[j+1][1][1]:
                array[j],array[j+1] = array[j+1], array[j]

arrumação_characterlvl(array)

for i in array:
    print(i[0])