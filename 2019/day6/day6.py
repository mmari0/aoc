"""
AOC-2019
day: 6
story: 1
"""
from arepl_dump import dump

1

class OrbitMap():
    def __init__(self):
        self.map = {}
        self.head = []
        # {planet : []}

    def add(self, coord):
        coord = coord.split(')')
        orbit = coord[0]
        planet = coord[1]

        if not orbit in self.map:
            self.map[orbit] = [planet]

        lists = self.map.get(orbit)
        lists.append(planet)

        if not planet in self.map:
            self.map[planet] = []


    def get_parent(self, planet):
        for el in self.map:
            if planet in self.map.get(el):
                return el

        return None

    def calc_orbits(self, planet):
        parent = self.get_parent(planet)
        if parent == None:
            return 0

        orbit = 0
        while parent:
            orbit += 1
            parent = self.get_parent(parent)

        return orbit

    def print(self):
        print(self.map)

    def calc_all_orbits(self):
        orbits = 0
        for el in self.map:
            orbits += self.calc_orbits(el)

        return orbits

if __name__ == '__main__':
    TEST_VEC = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
    #          G - H       J - K - L
    #        /           /
    # COM - B - C - D - E - F
    #                \
    #                 I

    om = OrbitMap()
    for el in TEST_VEC:
        om.add(el)
    assert om.get_parent('B') == 'COM'
    assert om.get_parent('D') == 'C'
    assert om.get_parent('L') == 'K'
    assert om.get_parent('F') == 'E'
    assert om.calc_orbits('COM') == 0
    assert om.calc_orbits('B') == 1
    assert om.calc_orbits('D') == 3
    assert om.calc_orbits('L') == 7
    assert om.calc_all_orbits() == 42

    # om.add('COM1)X')
    # om.print()


    om = OrbitMap()
    f = open('input_day6.txt', 'r')
    for line in f:
        om.add(line[:-1])
    f.close()
    print('read end')
    # total_orbits = om.calc_all_orbits()
    #print('ans for step1: ' + str(total_orbits))
    # assert total_orbits == 453028


