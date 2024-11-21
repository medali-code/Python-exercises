a = 100 > 10 and 5>20
print(a)
a = 100 > 10 and 5<20
print(a)


a = 100 > 10 or 5<20
print(a)
a = 100 > 10 or 5>20
print(a)
a = 100 < 10 or 5>20
print(a)

a = 100 > 10 and (5 < 20 or 5 > 10)
print(a)
  #  True  + True ==> True         