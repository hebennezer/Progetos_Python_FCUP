d = {"apples": 15, "bananas": 35, "grapes": 12}
print(d,"\n")

print(d["bananas"],"\n")

d["oranges"] = 20

print("grapes" in d, "\n")

d["pears"] = 0
d.get("pears", 0)
print(d["pears"], "\n")

print(len(d), "\n")

print(sorted(d), "\n")

del d["apples"]
print(d, "\n")

print("apples" in d)