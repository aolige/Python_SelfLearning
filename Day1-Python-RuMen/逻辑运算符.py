#逻辑运算符：and   or   not


a,b,c,d = 10,20,3,5

#and条件比较严格,左右两边都为true,则为true
print(a + b > c and c < d)
#or，一方为真，true，则为true
print(a > c or a < c)
#not 取反，真假切换
print(not a < b)

#优先级
#()->not->and->or

print(2>1 and 1<4 or 2<3 and 9>6 or 2<4 and 3<2)