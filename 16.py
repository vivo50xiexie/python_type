a = 16
if a >= 18:
    print("a是成年人")
elif a >= 6:
    print("a是青少年")
else:
    print("a是儿童")


height = 1.75
weight = 80.5

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")

age = 14

match age:
    case x if x < 10:
        print(f'< 10 years old: {x}')
    case 10:
        print("10 years old")
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print(f'11-18 years old')
    case 19:
        print("19 years old")
    case _:
        print("not sure.")
