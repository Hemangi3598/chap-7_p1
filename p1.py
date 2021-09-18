# wapp to demo list

# declare
d1 = []
print(d1, type(d1))

d2 = [10, 30, 10, 40, 20, 20]
print(d2, type(d2))

d3 = ["amit", "neha", "pooja"]

# display
print(d3)

for d in d3:
	print(d)

# operators
r1 = d2 + d3
print(r1)

r2 = d3 * 2
print(r2)

print("amit" in d3)
print(" Pooja" in d3)
# since python is case sensitive so Pooja wont show in list bcoz P is capital