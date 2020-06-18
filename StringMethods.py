n = 0
s, a, b = (str(input()) for i in range(3))
for i in range(1001):
    if s.count(a) > 0:
        s = s.replace(a, b)
        n += 1
if s.count(a) > 0:
    print("Impossible")
else:
    print(n)
