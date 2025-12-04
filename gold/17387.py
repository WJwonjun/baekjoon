def ccw(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


def intersect(a, b, c, d):
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)

    if ab == 0 and cd == 0:  # 일직선인 경우
        if a > b: a, b = b, a
        if c > d: c, d = d, c
        return not (b < c or d < a)  # 구간이 겹침
    return ab <= 0 and cd <= 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

print(1 if intersect((x1,y1),(x2,y2),(x3,y3),(x4,y4)) else 0)

## CCW 알고리즘 -> 선분과 점의 방향 구하기