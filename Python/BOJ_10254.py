import sys

def solve():
    read = sys.stdin.read().split()
    iterator = iter(read)
    T = int(next(iterator))


    def ccw(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    

    def dist(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    

    for tc in range(T):
        N = int(next(iterator))
        point_list = []

        for _ in range(N):
            x, y = int(next(iterator)), int(next(iterator))
            point_list.append((x, y))
        
        point_list.sort(key = lambda x:(x[0], x[1]))

        down_shell = []
        for point in point_list:
            while len(down_shell) >= 2 and ccw(down_shell[-2], down_shell[-1], point) <= 0:
                down_shell.pop()
            
            down_shell.append(point)
        
        up_shell = []
        for point in reversed(point_list):
            while len(up_shell) >= 2 and ccw(up_shell[-2], up_shell[-1], point) <= 0:
                up_shell.pop()
            
            up_shell.append(point)
        
        down_shell.pop()
        up_shell.pop()
        shell = down_shell + up_shell


        # --- 회전하는 캘리퍼스 ---
        M = len(shell)
        l_index = 0
        r_index = 0
        
        # x좌표 기준으로 볼록껍질 제작했으니, x좌표가 가장 큰 점을 r_index로 설정
        for i in range(M):
            if shell[i][0] > shell[r_index][0]:
                r_index = i
        
        max_len = 0
        answer_l, answer_r = 0, 0
        for _ in range(M * 2):
            length = dist(shell[l_index], shell[r_index])

            if max_len < length:
                max_len = length
                answer_l, answer_r = l_index, r_index

            next_l = (l_index + 1) % M
            next_r = (r_index + 1) % M

            # 두 포인트를 벡터로 변환
            u = (shell[next_l][0] - shell[l_index][0], shell[next_l][1] - shell[l_index][1])
            v = (shell[next_r][0] - shell[r_index][0], shell[next_r][1] - shell[r_index][1])

            # 기존의 ccw 재사용
            if ccw((0, 0), u, v) > 0:
                r_index = next_r
            elif ccw((0, 0), u, v) < 0:
                l_index = next_l
            else:
                r_index = next_r
                l_index = next_l
        
        print(*shell[answer_l], *shell[answer_r])


if __name__ == "__main__":
    solve()