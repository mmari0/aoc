"""
AOC-2019
day: 1
story: 1
"""
from arepl_dump import dump

def fuel_counter(mass):
    """Calculate fuel"""
    return int(mass / 3) - 2

if __name__ == "__main__":
    assert fuel_counter(12) == 2
    assert fuel_counter(14) == 2
    assert fuel_counter(1969) == 654
    assert fuel_counter(100756) == 33583



