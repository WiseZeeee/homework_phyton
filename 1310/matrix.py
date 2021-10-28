class Matrix():
    def __init__(one, b):
        a = 1
        for i in range(1, len(b)):
            if len(b[0]) == len(b[i]):
                a += 1
        if a == len(b):
            one.b = b
        else:
            print("Невозможно решить")
        one.b = b
    def transpose(one):
        new_b = [[] for _ in one.b [0]]
        for i in range(len(one.b[0])):
            for j in range(len(one.b)):
                new_b[i].append(one.b[j][i])
        one.b = new_b
        return one.b

b1 = Matrix([[8, 2, 7], [9, 3, 5], [6, 1, 4]])
print(b1.transpose())
