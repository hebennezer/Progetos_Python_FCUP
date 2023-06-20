a = [3, 2, 1]
b = [1, 2, 3, 4]
c = [5, 6, 7]

def is_contained(a, b):
    for elemento in a:
        if elemento not in b:
            return False
    return True

print(is_contained(a, c))
print(is_contained(a, b))
