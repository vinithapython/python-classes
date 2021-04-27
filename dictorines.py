#dict methods
d = {"v":7, "age": 22}
print(d["v"])
#print(d.get("b"),"not found")
print(d.keys())
print(d.values())
print(d.items())
print(d.update(age=23))
#practice
s = {"Name": "vv", "native": "vellore"}
a = {}
for v,b in s.items():
	a[v] = b
print(a)