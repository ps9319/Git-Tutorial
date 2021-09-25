import pprint as p
import numpy as np

A = np.array([[0, 0, 0, 2], [0, 0, 1, -4], [0, 1, 4, -1], [2, -4, -1, 6]], dtype=np.float64)
print("A:")
p.pprint(A)

print("dia_m:")
dia_m = np.eye(len(A), dtype=np.float64)
p.pprint(dia_m)
print("---------------------------------------------------------")
tmp = np.zeros((4, 4))

for i in range(4):
    count = 0
    for j in range(4):
        if A[i, j] == 0:
            count += 1
        else:
            break
    if count == 3:
        tmp[3] = A[i]
    elif count == 2:
        tmp[2] = A[i]
    elif count == 1:
        tmp[1] = A[i]
    elif count == 0:
        tmp[0] = A[i]

A = tmp

for i in range(4):
    if A[i, i] != 1:
        #  ↓ 대각행렬에 A를 나눈 수만큼 곱하는 식
        dia_m[i, i] *= A[i, i]
        # ↓ 행과 열이 같은 곳이 1이 아니면 1로 만들어주는 식
        A[i] /= A[i, i]
    for j in range(i+1):
        if i == 3:
            break
        if A[i+1, j] != 0:
            # ↓ 대각행렬을 하삼각행렬로 만들기 위해 더하는 식
            dia_m[i+1, j] += A[i+1, j]
            # ↓ A를 상삼각행렬로 만들기 위해 뺴는 식
            A[i+1] -= A[i+1, j]*A[j]

print("U:")
p.pprint(A)
print("L:")
p.pprint(dia_m)