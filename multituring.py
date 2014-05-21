import collections
import copy

class Multituring:

    def __init__(self, mt, tape_start):
        self.mt = mt
        self.tape = dict(enumerate(tape_start))
        self.current_state = self.mt['start']
        self.empty_symbol = self.mt['empty_symbol']
        self.pos = 0
        self.direction = 'S'
        self.symbol = self.empty_symbol

    def _get_tape_contents(self, sep='', highlight_pos=False, offset=0):
        our_tape = copy.deepcopy(self.tape)
        if self.pos not in our_tape:
            our_tape[self.pos] = self.empty_symbol
        if highlight_pos:
            our_tape[self.pos] = "\033[4m%s\033[0m" % our_tape[self.pos]

        if our_tape != {}:
            min_key = min(our_tape.keys())
            max_key = max(our_tape.keys())
            our_tape_contents= []
            for i in range(min_key-offset, max_key+offset+1):
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

        print('(%s,\t%s,\t%s)' % (self.current_state, self.symbol,
                                  self.direction))
        print(self._get_tape_contents(sep=' ', highlight_pos=True, offset=3))
        print("")

    def run(self, print_progress=True):

        while True:
            self.symbol = self.tape.get(self.pos, self.empty_symbol)

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
            self.direction = turing_tuple[2]

            if self.direction == 'R':
                offset = 1
            elif self.direction == 'L':
                offset = -1
            else:
                assert(self.direction == 'S')
                offset = 0

            self.tape[self.pos] = self.symbol
            self.pos += offset

def interactive_test(mt):
    tape_start = raw_input("Enter the tape contents: ")
    print("")
    mt = Multituring(mt, tape_start)
    mt.run()
    print("The tape was accepted.")

