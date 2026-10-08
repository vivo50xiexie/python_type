jihe = {'xigua' , 'pingguo' , 'putao' , 'xiangjiao' , 'mangguo' , 'caomei' , 'boluo' , 'li' , 'juzi' , 'yingtao'}
if 'pingguo' in jihe:
    print('pingguo bu zai jihe')
else:
    print('pingguo zai jihe')

a = set('2nd8thl40a')
b = set('l4j8sbe03')
print(a - b)       # a 和 b 的差集（在 a 中但不在 b 中）
print(a | b)       # a 和 b 的并集（在 a 或 b 中）
print(a & b)       # a 和 b 的交集（同时在 a 和 b 中）
print(a ^ b)       # a 和 b 的对称差集（在 a 或 b 中，但不同时存在）