#include <stdio.h>
#include <string.h>

int main() {
    char king[3], stone[3], cmd[3];
    int N;

    scanf("%s %s %d", king, stone, &N);

    while (N--) {
        scanf("%s", cmd);

        int kx = king[0];
        int ky = king[1] - '0';
        int sx = stone[0];
        int sy = stone[1] - '0';

        int dx = 0, dy = 0;

        if (!strcmp(cmd, "R")) dx = 1;
        else if (!strcmp(cmd, "L")) dx = -1;
        else if (!strcmp(cmd, "B")) dy = -1;
        else if (!strcmp(cmd, "T")) dy = 1;
        else if (!strcmp(cmd, "RT")) dx = 1, dy = 1;
        else if (!strcmp(cmd, "LT")) dx = -1, dy = 1;
        else if (!strcmp(cmd, "RB")) dx = 1, dy = -1;
        else if (!strcmp(cmd, "LB")) dx = -1, dy = -1;

        int nkx = kx + dx;
        int nky = ky + dy;

        // 왕이 범위 안일 때만 이동
        if (nkx >= 'A' && nkx <= 'H' && nky >= 1 && nky <= 8) {

            // 돌을 치는 경우
            if (nkx == sx && nky == sy) {
                int nsx = sx + dx;
                int nsy = sy + dy;
                if (nsx >= 'A' && nsx <= 'H' && nsy >= 1 && nsy <= 8) {
                    sx = nsx;
                    sy = nsy;
                    kx = nkx;
                    ky = nky;
                }
            } else {
                kx = nkx;
                ky = nky;
            }
        }

        king[0] = kx;
        king[1] = ky + '0';
        king[2] = 0;

        stone[0] = sx;
        stone[1] = sy + '0';
        stone[2] = 0;
    }

    printf("%s\n%s\n", king, stone);
    return 0;
}
