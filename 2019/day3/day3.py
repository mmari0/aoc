"""
AOC-2019
day: 3
story: 1&2
"""
from arepl_dump import dump



def split_cmd(cmd):
    direction = cmd[:1]
    assert direction.isalpha(), "direction: " + direction

    distance = cmd[1:].rstrip()
    assert distance.isnumeric(), "distance: [" + distance[:-1] + ']'
    distance = int(distance)

    return (direction, distance)

class Board():
    def __init__(self):
        self.start_point = [1, 1]
        self.point = [self.start_point[0], self.start_point[1]]
        self.board = {}
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0

    def set_central_point(self):
        self.point = [self.start_point[0], self.start_point[1]]

    def update_max(self):
        self.min_x = min(self.min_x, self.point[0])
        self.max_x = max(self.max_x, self.point[0])
        self.min_y = min(self.min_y, self.point[1])
        self.max_y = max(self.max_y, self.point[1])

    def move(self, coord):
        for i in range(coord[1]):
            if coord[0] == 'L':
                self.point[1] -= 1
            if coord[0] == 'R':
                self.point[1] += 1
            if coord[0] == 'U':
                self.point[0] += 1
            if coord[0] == 'D':
                self.point[0] -= 1
            self.update_max()

            point = str(self.point[0]) + 'x' + str(self.point[1])
            if point in self.board:
                value = self.board.get(point) + 1
            else:
                value = 1
         #   print(point)
            self.board.update({point : value})

    def print(self):
        for y in reversed(range(self.min_y - 2, self.max_y + 2)):
            dump(y)
            line = ""
            for x in range(self.min_x - 2, self.max_x + 2):
                point = str(x) + 'x' + str(y)
                if point in self.board:
                    value = self.board.get(point)
                elif point == (str(self.start_point[0]) + 'x' + str(self.start_point[1])):
                    value = 'o'
                else:
                    value = '.'
                line += str(value)
            print(line)

    def decode_point(self, point):
        x = int(point.split('x')[0])
        y = int(point.split('x')[1])
        return [x, y]

    def calc_dist_from_central_point(self, points):
        dist_list = []
        for point in points:
            point = self.decode_point(point)
            dist = abs(self.start_point[0] - point[0])
            dist += abs(self.start_point[1] - point[1])
            dist_list.append(dist)
        return dist_list

    def get_all_cross_point(self):
        points = []
        for key, value in self.board.items():
            if value > 1:
                points.append(key)
        return points

if __name__ == '__main__':
    TEST_VEC_1a = ['R8', 'U5', 'L5', 'D3']
    TEST_VEC_1b = ['U7', 'R6', 'D4', 'L4']

    board = Board()

    for cmd in TEST_VEC_1a:
        board.move(split_cmd(cmd))

    board.set_central_point()
    for cmd in TEST_VEC_1b:
        board.move(split_cmd(cmd))

    points = board.get_all_cross_point()
    dist = board.calc_dist_from_central_point(points)
    board.print()
    assert min(dist) == 6


    TEST_VEC_2a = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
    TEST_VEC_2b = ['U62','R66','U55','R34','D71','R55','D58','R83']
    board = Board()
    for cmd in TEST_VEC_2a:
        board.move(split_cmd(cmd))
    board.set_central_point()
    for cmd in TEST_VEC_2b:
        board.move(split_cmd(cmd))
    points = board.get_all_cross_point()
    dist = board.calc_dist_from_central_point(points)
    assert min(dist) == 157


    TEST_VEC_3a = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
    TEST_VEC_3b = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
    board = Board()
    for cmd in TEST_VEC_3a:
        board.move(split_cmd(cmd))
    board.set_central_point()
    for cmd in TEST_VEC_3b:
        board.move(split_cmd(cmd))
    points = board.get_all_cross_point()
    dist = board.calc_dist_from_central_point(points)
    assert min(dist) == 135


    f = open('input_day3.txt', 'r')
    VECT_a = f.readline().split(',')
    VECT_b = f.readline().split(',')
    f.close

    board = Board()
    for cmd in VECT_a:
        board.move(split_cmd(cmd))
    board.set_central_point()
    for cmd in VECT_b:
        board.move(split_cmd(cmd))
    points = board.get_all_cross_point()
    dist = board.calc_dist_from_central_point(points)
    print('ans for step1: ' + str(min(dist)))