names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
for name in names:
    print(f'Hello, {name}!')
    

data = 0
for x in range(101):
    data = data + x
print(data)

sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 2
print(sum)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
