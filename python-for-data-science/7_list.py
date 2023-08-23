l = []

l.append("hello")
l.insert(0, "world")
l.extend(["22", "23"])

print(l)
print(len(l))
print(l[1])
print(l.count(l[1]))
print(reversed(l))
print(24, 24 in l)
print(l.pop())
l.remove("22")
print(l)
l.clear()
print(l)