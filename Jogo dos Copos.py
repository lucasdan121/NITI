A = 0
B = 0
C = 0
m = int(input())
v = input()
if v == "A":
    A = 1
elif v == "B":
    B = 1
elif v == "C":
    C = 1
for x in range(0, m, 1):
    y = int(input())
    if y == 1:
        A, B = B, A
    elif y == 2:
        B, C = C, B
    elif y == 3:
        C, A = A, C
if A == 1:
    print("A")
elif B == 1:
    print("B")
elif C == 1:
    print("C")