import math

a = [[".", ".", ".", "#", ".", "#", ".", ".", ".", "."],
     [".", ".", "#", ".", ".", "#", ".", "#", ".", "#"],
     ["s", ".", "#", ".", "#", ".", "#", ".", ".", "."],
     [".", "#", "#", ".", ".", ".", ".", ".", "#", "."],
     [".", ".", ".", ".", "#", "#", ".", ".", "#", "."],
     [".", "#", ".", ".", ".", ".", "#", ".", ".", "."],
     [".", "#", ".", ".", ".", "#", "#", ".", "#", "."],
     [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
     [".", "#", "#", ".", ".", ".", "#", ".", ".", "."],
     [".", ".", ".", "#", "#", "#", ".", ".", "#", "f"],
     ["#", "#", ".", ".", "#", "#", "#", ".", "#", "."],
     [".", "#", "#", ".", ".", ".", "#", ".", ".", "."],
     [".", ".", ".", ".", "#", "#", ".", ".", "#", "."]]



class Node:
    def __init__(self, x, y, heu=None, parent=None, is_closed=None):
        self.x = x
        self.y = y
        self.heu = heu
        self.parent = parent
        self.is_closed = is_closed

    def heuristic(self, start, goal):
        stoself = math.sqrt(pow((self.x - start.x), 2) + pow((self.y - start.y), 2))
        selftog = math.sqrt(pow((goal[0] - self.x), 2) + pow((goal[1] - self.y), 2))
        f = stoself + selftog
        return f


def move(direction, x, y):
    if direction == "r":
        x += 1
    elif direction == "l":
        x -= 1
    elif direction == "d":
        y -= 1
    elif direction == "u":
        y += 1
    elif direction == "ur":
        x += 1
        y += 1
    elif direction == "ul":
        x -= 1
        y += 1
    elif direction == "dl":
        x -= 1
        y -= 1
    elif direction == "dr":
        x += 1
        y -= 1

    return x, y


def if_possible(x, y):
    if 0 <= x <= 12 and 0 <= y <= 10:  # array size x = 12 y = 10
        return True
    else:
        return False


def pick_min(arr, cl):
    m = 999
    for i in range(len(arr)):
        if arr[i].is_closed:
            continue
        else:
            m = min(m, arr[i].heu)
    for j in arr:
        if j.heu == m:
            k = arr.index(j)
            v = arr.pop(k)
            cl.append(v)
            return v


def in_closed(obj, arr):
    for i in arr:
        if obj[0] == i.x and obj[1] == i.y:
            return True
    return False


def find_start_goal(arr):
    i = -1
    j = -1
    for row in a:
        i += 1
        for el in row:
            j += 1
            if el == 's':
                start = (i, j)
            if el == 'f':
                goal = (i, j)
        j = -1
    return start, goal


def find_point_parent_heu(x, y, arr):
    for i in arr:
        if x == i.x and y == i.y:
            return i

stf = find_start_goal(a)

start = Node(stf[0][0], stf[0][1])  # input data 
finish = (stf[1][0], stf[1][1])

moves = ("r", "l", "u", "d", "ul", "ur", "dl", "dr")
open = []
closed = []
curr = start
flag = True


while flag:
    for dir in moves:
        step = move(dir, curr.x, curr.y)
        if if_possible(step[0], step[1]):
            if a[step[0]][step[1]] == "f":
                heuristic_total = 0


                while curr.parent != start:

                    heuristic_total += curr.heu
                    a[curr.x][curr.y] = 'X'
                    curr = curr.parent
                    for row in a:
                        for el in row:
                            print(el, end=' ')
                        print()
                    print()
                    print('curr = ', curr.heu, 'total = ', heuristic_total)
 
                a[curr.x][curr.y] = 'X'
                print(heuristic_total)
                flag = False

            if a[step[0]][step[1]] == ".":
                if in_closed(step, closed):
                    continue
                node = Node(step[0], step[1])
                a[step[0]][step[1]] = "o"
                node.heu = node.heuristic(start, finish)
                node.parent = curr
                open.append(node)
            elif a[step[0]][step[1]] == "o":
                obj = find_point_parent_heu(step[0], step[1], open)
                if obj is not None and curr.heu < obj.heu:
                    obj.parent = curr
                else:
                    continue

    curr.is_closed = True
    curr = pick_min(open, closed)
    for row in a:
        for el in row:
            print(el, end=' ')
        print()
    print()
