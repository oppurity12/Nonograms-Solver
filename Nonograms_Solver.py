class Nonograms_Solver():
    def __init__(self,size,row_hint,col_hint):
        self.size = size
        self.row_hint = row_hint
        self.col_hint = col_hint
        self.matrix = [['-1']*size for _ in range(size)]
        self.answer = []

    #각 row 마다 조건에 부합한 배열 생성
    def possible_nums(self,row_hint):
        from itertools import combinations_with_replacement
        from collections import Counter
        base = ['']
        pos = [0]
        total = []
        s = 0
        # 기본 베이스 설정
        for i in range(len(row_hint)):
            base += ['1'] * row_hint[i]
            base += ['']
            s += row_hint[i] + 1
            pos.append(s)

        # 사이 사이에 숫자 넣어주기
        extra_count = self.size - len(base) + 2
        extra_arrays = list(combinations_with_replacement(pos, extra_count))
        for array in extra_arrays:
            tmp = base[:]
            dic = Counter(array)
            for idx in pos:
                if idx == 0 or idx == pos[-1]:
                    tmp[idx] = '0' * dic.setdefault(idx, 0)
                else:
                    tmp[idx] = '0' * (dic.setdefault(idx, 0) + 1)
            total.append(list(''.join(tmp)))
        return total

    # idx는 현재 검사하고자 하는 컬럼의 위치
    # col_pos 는 어느 row 까지 넣었는지
    def check(self,idx,col_pos):
        count = 0
        pos = 0
        hint = self.col_hint[col_pos]
        for i in range(idx + 1):
            # 당연한 조건들
            if hint == [0] and self.matrix[i][col_pos] == '1':
                return False
            if hint == [self.size] and self.matrix[i][col_pos] == '0':
                return False
            if self.matrix[i][col_pos] == '-1':
                return False

            if self.matrix[i][col_pos] == '1':
                count += 1
                if pos == len(hint):
                    return False
                if count > hint[pos]:
                    return False
            elif self.matrix[i][col_pos] == '0':
                if count == 0:
                    continue
                if count != hint[pos]:
                    return False
                pos += 1
                count = 0
        if idx == self.size - 1:
            if pos != len(hint):
                if count != hint[pos]:
                    return False

        return True

    def solver(self,idx):
        import copy
        if idx == self.size:
            self.answer = copy.deepcopy(self.matrix)
        else:
            if self.answer:
                return
            possibe_array = self.possible_nums(self.row_hint[idx])
            for array in possibe_array:
                self.matrix[idx] = array
                for i in range(self.size):
                    if self.check(idx, i) == False:
                        break
                else:
                    self.solver(idx + 1)
                self.matrix[idx] = ['-1'] * self.size

    def solve(self):
        self.solver(0)
        for i in self.answer:
            print(i)

    def show(self):
        if not self.answer:
            print('답을 먼저 구하세요')
        else:
            import turtle as t
            t.speed(200000)
            q = (50 - len(self.answer)) // 4
            t.penup()
            t.goto(-15 * (q + 1), 10 * q + 30)
            t.pendown()

            for k in range(len(self.answer)):
                t.penup()
                t.goto(-15 * (q + 1), 30 + 10 * q - 2 * q * k)
                t.pendown()
                for j in range(len(self.answer)):
                    if self.answer[k][j] == '1':
                        t.begin_fill()
                        for i in range(4):
                            if i % 2 == 0:
                                t.forward(2 * q * ((-1) ** i))
                                t.right(90)
                            else:
                                t.forward(2 * q * ((-1) ** i))
                                t.right(90)
                        t.end_fill()
                        t.forward(2 * q)
                    else:
                        for i in range(4):
                            if i % 2 == 0:
                                t.forward(2 * q * ((-1) ** i))
                                t.right(90)
                            else:
                                t.forward(2 * q * ((-1) ** i))
                                t.right(90)
                        t.forward(2 * q)





# size = 15
# row_hint = [[3],[5],[4,3],[7],[5],[3],[5],[1,8],[3,3,3],[7,3,2],[5,4,2],[8,2],[10],[2,3],[6]]
# col_hint = [[3],[4],[5],[4],[5],[6],[3,2,1],[2,2,5],[4,2,6],[8,2,3],[8,2,1,1],[2,6,2,1],[4,6],[2,4],[1]]


# size = 30
# row_hint = [[6],[4,2,4,4],[1,1,2,7,1,1],[1,1,11,1,1],[2,2,4,3,2,2],
#             [2,2,3,1,1,3,2,2],[4,1,1,3],[4,1,2],[1,2,1,3],[1,2,3,3,1],
#             [1,3,4,1,5],[1,4,3,1,2,1],[6,2,1,1,1],[1,4,4,3,2],[1,4,4,2,3,1],
#             [9,2,2,2,1],[6,4,1,1],[2,4,4,3,1,1],[2,4,2,3,3,1],[2,7,2,1,1,2],
#             [2,1,4,1,2,1,1,1],[1,2,1,4,2,2,1,1],[1,2,6,1,1,1,2],[2,3,2,2,1,1,1,2],[3,2,4,2],
#             [4,2,3,3,2],[1,4,2,1,3],[2,2,1],[2,7],[6,1]]
#
# col_hint = [[2,4],[5,2,2],[1,2,1,1],[1,2,2,2,2],[5,2,1,1,3],
#             [11,1,1,1,1,2],[6,1,6,1,1,2],[20,1,1,1],[2,18,1,1,1],[1,3,11,2,1,1],
#             [1,2,2,2,5,1,2,2,1],[4,1,1,1,2,2,2,3],[4,2,1,1,1,2,4,3],[4,6,1,4,2,1],[6,7,1,1,1,1],
#             [9,2,2,2,1],[13,1,1,1,1],[4,10],[2,2,2],[2,1,2],
#             [2,1,3,1],[1,2,1,2],[1,1,3,2],[1,2,2],[2,1,3,8],
#             [5,2,3],[1,1,1],[1,2,1,2,2],[5,1,1,1,5],[3,1,1]]



# size = 20
# row_hint = [[3],[4,4,2],[7,4,2],[7,5,3],[11,4],
#             [4,8],[3,6],[4,5],[4,1,1,3],[5,2],
#             [5,2,2,1],[5,2,2,5],[3,2,4,6],[2,3,6],[1,5,7],
#             [10],[4,5],[3,7],[2,7],[2,7]]
#
# col_hint = [[1,6],[2,6],[3,6],[4,5,4],[18],
#             [7,8],[5,1,4,1],[3,1,2],[1,1,2,3],[2,2,1,4],
#             [5,1,5],[4,1,2,5],[5,2,6],[5,1,2,3],[3,3,3],
#             [10,2],[1,11,1],[8,4],[6,4],[3,3]]






# size = 10
# row_hint = [[10],[2,3],[1,5,2],[1,2,2],[4,1,2],
#             [4,1],[1,2],[1,5],[1,5],[1,5]]
# col_hint = [[4,4],[2,2],[1,1,2,3],[1,1,2,3],[1,1,2,3],
#             [1,2,4],[1,8],[2],[5],[5]]


#
# size = 20
# row_hint = [[1,1],[3,3],[4,4],[4,4],[5,3],
#             [5,3],[5,4],[3,4],[5],[7],
#             [9],[3,7],[11],[11],[11],
#             [9],[6],[7],[10],[12]]
# col_hint = [[0],[0],[0],[2],[4],
#             [5,4],[5,6],[5,7],[4,2,5,1],[15],
#             [14],[12],[14],[18],[7,6,3],
#             [7,4,3],[4,2],[2],[2],[1]]
# #
#
# size = 15
# row_hint = [[15],[3,4],[2,4,3],[1,2,1,2],[1,1,1,1,1,1],
#             [1,1,1,1,3,1],[1,1,1,3,1],[1,2,1,1,1,1],[1,1,4,1,1,1],[1,2,6,1],
#             [1,4,1,1,1],[1,2,2,1],[2,5,2],[3,3],[15]]
# col_hint = [[15],[3,3],[2,2],[1,7,1],[1,2,1,2,1],
#             [1,1,1,1,2,1],[1,1,1,3,1],[1,9,1,1],[1,2,1,1],[1,4,1],
#             [1,6,2,1],[2,2,2,1],[3,6,2],[4,3],[15]]

# size = 15
# row_hint = [[1],[1,1,1],[1,1,1],[4,1],[2],
#             [10],[1,2,2],[1,2,5,1],[1,4,2,1],[1,3,1,1,1],
#             [3,5,1],[4,2,2],[1,7],[15],[15]]
#
# col_hint = [[4,2],[3,2],[12],[9,2],[3,1,4,2],
#             [1,2,4],[1,1,2,3],[1,1,1,3],[1,1,5],[1,2,5],
#             [1,3,3],[2,4],[6,2],[2],[4,2]]

size = 20
row_hint = [[3],[4,4,2],[7,4,2],[7,5,3],[11,4],
            [4,8],[3,6],[4,5],[4,1,1,3],[5,2],
            [5,2,2,1],[5,2,2,5],[3,2,4,6],[2,3,6],[1,5,7],
            [10],[4,5],[3,7],[2,7],[2,7]]

col_hint = [[1,6],[2,6],[3,6],[4,5,4],[18],
            [7,8],[5,1,4,1],[3,1,2],[1,1,2,3],[2,2,1,4],
            [5,1,5],[4,1,2,5],[5,2,6],[5,1,2,3],[3,3,3],
            [10,2],[1,11,1],[8,4],[6,4],[3,3]]






Solver = Nonograms_Solver(size,row_hint,col_hint)
Solver.solve()
Solver.show()