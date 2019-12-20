from day2 import *


def test_opcodes():
    oc = Opcodes(2,4)
    assert oc.get_next_cmd_offset() == 4
    assert oc.get_opcode() == 2