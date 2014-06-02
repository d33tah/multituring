import collections
import copy
import sys

if sys.version >= '3':
    raw_input = input

class Multituring:

    def __init__(self, mt, tape_start):
        self.mt = mt
        self.num_tapes = mt.get('num_tapes', 1)
        self.tapes = ([dict(enumerate(tape_start))] +
                      [{} for i in range(self.num_tapes-1)])
        self.current_state = self.mt['start']
        self.empty_symbol = self.mt['empty_symbol']
        self.tapes_pos = [0 for i in range(self.num_tapes)]
        self.directions = 'S' * self.num_tapes
        self.symbol = self.empty_symbol

    def _get_tape_contents(self, tape_number=0, sep='', highlight_pos=False,
                           left_offset=0, right_offset=None):
        if right_offset is None:
            right_offset = left_offset
        our_tape = copy.deepcopy(self.tapes[tape_number])
        if self.tapes_pos[tape_number] not in our_tape:
            our_tape[self.tapes_pos[tape_number]] = self.empty_symbol
        if highlight_pos:
            our_tape[self.tapes_pos[tape_number]] = ("\033[4m%s\033[0m" %
                our_tape[self.tapes_pos[tape_number]])

        if our_tape != {}:
            min_key = min(our_tape.keys())
            max_key = max(our_tape.keys())
            our_tape_contents= []
            for i in range(min_key-left_offset, max_key+right_offset+1):
                if i in our_tape:
                    our_tape_contents += [our_tape[i]]
                else:
                    our_tape_contents += [self.empty_symbol]
            return sep.join(our_tape_contents)
        else:
            return ""

    def get_tape_contents(self):
        return self._get_tape_contents().rstrip(self.empty_symbol)

    def print_state(self):

        print('(%s,\t%s,\t%s,\t%s)' % (self.current_state, self.symbol,
                                  self.directions, self.tapes_pos))
        for tape_number in range(len(self.tapes)):
            print(self._get_tape_contents(tape_number, sep=' ',
                                          highlight_pos=True, left_offset=3))
        print("")

    def _step(self, print_progress):
        self.symbol = ""
        for i in range(len(self.tapes)):
            self.symbol += self.tapes[i].get(self.tapes_pos[i],
                                             self.empty_symbol)

        if print_progress:
            self.print_state()

        if self.current_state in self.mt['stop']:
            return True

        if not self.current_state in self.mt['tab']:
            raise Exception('Entered an unknown state: %s'
                            % self.current_state)

        if not self.symbol in self.mt['tab'][self.current_state]:
            error = 'Symbol not defined for state %s: %s' % (
                        self.current_state, self.symbol)
            raise Exception(error)

        turing_tuple = self.mt['tab'][self.current_state][self.symbol]
        self.current_state = turing_tuple[0]
        self.symbol = turing_tuple[1]
        self.directions = turing_tuple[2]
        for i in range(len(self.directions)):

            if self.directions[i] == 'R':
                offset = 1
            elif self.directions[i] == 'L':
                offset = -1
            else:
                assert(self.directions[i] == 'S')
                offset = 0

            self.tapes[i][self.tapes_pos[i]] = self.symbol[i]
            self.tapes_pos[i] += offset

    def run(self, print_progress=True):

        while True:
            ret = self._step(print_progress)
            if ret:
                return ret

def interactive_test(mt):
    tape_start = raw_input("Enter the tape contents: ")
    print("")
    mt = Multituring(mt, tape_start)
    mt.run()
    print("The tape was accepted.")

