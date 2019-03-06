def call_by_reference(n):
 n += 5
 return n
h = 5
z = call_by_reference(h)
print(h)
print(z)

