"""
AOC-2019
day: 2
story: 1
"""
from arepl_dump import dump
import copy

class BaseOpcode():
    def __init__(self, opcode, size):
        self.opcode = opcode
        self.size = size
        self.params = 0

    def get_next_cmd_offset(self):
        return self.size

    def get_opcode(self):
        return self.opcode

    def set_params(self, code):
        self.params = code[:self.size]

    def is_end(self):
        return self.opcode == 99

class AddOpcode(BaseOpcode):
    def __init__(self):
        super().__init__(1, 4)

    def set_params(self, code):
        dump(code)
        assert len(code) == 3
        super().set_params(code)

    def calc(self, code):
        dump(self.params)
        dump(code)
        code[self.params[2]] = code[self.params[0]] + code[self.params[1]]
        dump(code)

class MulOpcode(BaseOpcode):
    def __init__(self):
        super().__init__(2, 4)

    def set_params(self, code):
        assert len(code) == 3
        super().set_params(code)

    def calc(self, code):
        dump(self.params)
        code[self.params[2]] = code[self.params[0]] * code[self.params[1]]
        dump(code)

class EofOpcode(BaseOpcode):
    def __init__(self):
        super().__init__(99, 1)

    def set_params(self, code):
        assert not code

    def calc(self, code):
        pass

OPCODES = {
    1 : AddOpcode,
    2 : MulOpcode,
    99: EofOpcode
}

class Parser():
    def __init__(self, program):
        self.program = program
        self.cursor = 0

    def print_line(self, opcode):
        #print('line: ' + str(self.program[self.cursor : self.cursor + opcode.get_next_cmd_offset()]))
        pass

    def decode_opcode(self):
        cur_val = self.program[self.cursor]
        if cur_val in OPCODES:
            opcode = OPCODES.get(cur_val)()
            opcode.set_params(self.program[self.cursor + 1: self.cursor + opcode.get_next_cmd_offset()])
            return opcode

        return None

    def move_cursor(self, opcode):
        self.cursor += opcode.get_next_cmd_offset()

    def is_finish(self, opcode):
        if not opcode:
            return True
        if opcode.is_end():
            return True
        return False

    def execute(self):
        while True:
            opcode = self.decode_opcode()
            self.print_line(opcode)
            if self.is_finish(opcode):
                break
            opcode.calc(self.program)
            self.move_cursor(opcode)

    def get_program(self):
        return self.program

if __name__ == "__main__":
    TEST_VEC_1 = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
    parser = Parser(TEST_VEC_1)
    parser.execute()
    assert parser.get_program() == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]

    TEST_VEC_2 = [1, 0, 0, 0, 99]
    parser = Parser(TEST_VEC_2)
    parser.execute()
    assert parser.get_program() == [2, 0, 0, 0, 99]

    TEST_VEC_3 = [2, 3, 0, 3, 99]
    parser = Parser(TEST_VEC_3)
    parser.execute()
    assert parser.get_program() == [2, 3, 0, 6, 99]

    TEST_VEC_4 = [2, 4, 4, 5, 99, 0]
    parser = Parser(TEST_VEC_4)
    parser.execute()
    assert parser.get_program() == [2, 4, 4, 5, 99, 9801]

    TEST_VEC_5 = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    parser = Parser(TEST_VEC_5)
    parser.execute()
    assert parser.get_program() == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    str_val = open('input_day2.txt', 'r').readline().split(',')

    memory = []
    for val in str_val:
        memory.append(int(val))

    memory_s1 = copy.deepcopy(memory)
    memory_s1[1] = 12
    memory_s1[2] = 2
    parser = Parser(memory_s1)
    parser.execute()
    print('ans for step1: ' + str(parser.get_program()[0]))


    for noun in range(100):
        for verb in range(100):
            memory_s2 = copy.deepcopy(memory)
            memory_s2[1] = noun
            memory_s2[2] = verb
            parser = Parser(memory_s2)
            parser.execute()
            if parser.get_program()[0] == 19690720:
                print('pos 0 is ' + str(parser.get_program()[0]))
                print('nount is:' + str(noun))
                print('verb is:' + str(verb))
                print('ans for step2: ' + str(noun*100 + verb))
                break
    print("EOF")