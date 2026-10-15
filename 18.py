d = {'liuyipeng': 18, 'zhanjiadong': 20, 'panqiwei': 22}
print(d['zhanjiadong'])

d['zhongyiming'] = 19
print(d['zhongyiming'])
d['zhongyiming'] = 78
print(d['zhongyiming'])

print('mayun' in d)

d.pop('liuyipeng')
print(d)

s = {1, 2, 3}
s.add(4)
print(s)
s.remove(2)
print(s)