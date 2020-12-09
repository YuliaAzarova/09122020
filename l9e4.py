vvod = input()
delet = len(vvod)//2
if len(vvod) == 1:
    print(vvod)
if len(vvod) % 2 == 0:
    print(vvod[delet:]+vvod[:delet])
elif len(vvod) % 2 != 0:
    print(vvod[delet+1:]+vvod[:-delet])