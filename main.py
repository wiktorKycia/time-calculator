print("Kalkulator godzin, minut i sekund")
sekundy = 0
minuty = 0
godziny = 0

while True:
    while True:
        x = input("Podaj ilość godzin: ")
        if not x == '': x = int(x);break
        else: continue
    if x < 0:
        break
    godziny += x
    while True:
        x = input("Podaj ilość minut: ")
        if not x == '':
            x = int(x);break
        else:
            continue
    if x < 0:
        break
    minuty += x
    # while True:
    #     x = input("Podaj ilość sekund: ")
    #     if not x == '':
    #         x = int(x);break
    #     else:
    #         continue
    # if x < 0:
    #     break
    # sekundy += x

# while sekundy > 60:
#     sekundy -= 60
#     minuty += 1

while minuty > 60:
    minuty -= 60
    godziny += 1

print(f"Całkowita długość to: {godziny}:{minuty}:{sekundy}")