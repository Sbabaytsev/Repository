s, t = (str(input()) for i in range(2))
count = 0
for i in range(len(s) - len(t) + 1):
    if s.startswith(t, i):
        count += 1
print(count)
