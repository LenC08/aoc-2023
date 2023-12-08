from math import gcd
a = [11911, 13019, 16897, 18559, 19667, 21883]   
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)