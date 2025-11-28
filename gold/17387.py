def line_coeff(x1,y1,x2,y2):
    A = y2 - y1
    B = x1 - x2
    C = A*x1 + B*y1
    return A, B, C

def between(a, b, x):
    return min(a,b) <= x <= max(a,b)

def intersect(x1,y1,x2,y2,x3,y3,x4,y4):

    # -------- 특수 케이스 1 : 둘 다 수평 --------
    if y1 == y2 and y3 == y4:
        if y1 != y3:
            return 0
        return int(not (x2 < x3 or x4 < x1))

    # -------- 특수 케이스 2 : 한쪽 수평 + 한쪽 수직 --------
    if y1 == y2 and x3 == x4:
        return int(between(x1,x2,x3) and between(y3,y4,y1))

    if y3 == y4 and x1 == x2:
        return int(between(x3,x4,x1) and between(y1,y2,y3))

    # -------- 특수 케이스 3 : 둘 다 수직 --------
    if x1 == x2 and x3 == x4:
        if x1 != x3: return 0
        return int(not (max(y1,y2) < min(y3,y4) or max(y3,y4) < min(y1,y2)))

    # -------- 일반 케이스 : 정수 직선식 A x + B y = C --------

    A1,B1,C1 = line_coeff(x1,y1,x2,y2)
    A2,B2,C2 = line_coeff(x3,y3,x4,y4)

    det = A1*B2 - A2*B1

    # ---- 평행 또는 일치 ----
    if det == 0:
        # 일직선인지 검사: 한 점이 다른 직선 위에 있는지
        if A1*x3 + B1*y3 != C1:
            return 0
        # 선분이 겹치는지 검사
        # x축 기준으로 정렬
        if max(x1,x2) < min(x3,x4): return 0
        if max(x3,x4) < min(x1,x2): return 0
        return 1

    # ---- det != 0 : 교점 존재 ----
    # x = (C1*B2 - C2*B1) / det
    # y = (A1*C2 - A2*C1) / det
    # → 범위 비교 시 분모 det을 곱해 정수 비교

    x_num = C1*B2 - C2*B1
    y_num = A1*C2 - A2*C1

    # 선분1 범위 검사
    if not (min(x1,x2)*det <= x_num <= max(x1,x2)*det):
        return 0
    if not (min(y1,y2)*det <= y_num <= max(y1,y2)*det):
        return 0

    # 선분2 범위 검사
    if not (min(x3,x4)*det <= x_num <= max(x3,x4)*det):
        return 0
    if not (min(y3,y4)*det <= y_num <= max(y3,y4)*det):
        return 0

    return 1


# -------- Main --------
import sys
input = sys.stdin.readline
x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

print(intersect(x1,y1,x2,y2,x3,y3,x4,y4))
