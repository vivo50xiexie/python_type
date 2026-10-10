# 之前是在runoob上学习的，现在在liaoxuefeng学习，同学推荐
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Bob!'''

print(s4)

print(ord('就'))
print(chr(20129))
print('\u4d2d\u6537')
print('DSB'.encode('ascii'))
print('六十'.encode('utf-8'))

print('你好，%s，你有%d块钱' % ('小明', 3))

s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print(f'小明的成绩提升了{r:.1f}%')
