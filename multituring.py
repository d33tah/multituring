#!/usr/bin/python

import collections
import copy

def print_state(current_state, symbol, direction, tape, pos, empty_symbol):

    print('(%s,\t%s,\t%s)' % (current_state, symbol, direction))

    our_tape = copy.deepcopy(tape)
    if pos not in our_tape:
        our_tape[pos] = empty_symbol
    our_tape[pos] = "\033[4m%s\033[0m" % our_tape[pos]

    if our_tape != {}:
        min_key = min(our_tape.keys())
        max_key = max(our_tape.keys())
        our_tape_contents = [our_tape[i] if i in our_tape else empty_symbol
                         for i in range(min_key-3, max_key+4)]
        print(' '.join(our_tape_contents))
    else:
        print("")

    print("")

def main(mt_start, tape_start):

    current_state = mt['start']
    empty_symbol = mt['empty_symbol']

    tape = dict(enumerate(tape_start))

    pos = 0
    direction = 'S'

    while True:
        symbol = tape.get(pos, empty_symbol)

        print_state(current_state, symbol, direction, tape, pos, empty_symbol)

        if current_state in mt['stop']:
            return True

        if not current_state in mt['tab']:
            raise Exception('Entered an unknown state:' % current_state)

        if not symbol in mt['tab'][current_state]:
            error = 'Symbol not defined for state %s: %s' % (current_state,
                                                             symbol)
            raise Exception(error)

        current_state, symbol, direction = mt['tab'][current_state][symbol]

        if direction == 'R':
            offset = 1
        elif direction == 'L':
            offset = -1
        else:
            assert(direction == 'S')
            offset = 0

        tape[pos] = symbol
        pos += offset

if __name__ == "__main__":
    from ex1_a import mt
    tape_start = raw_input("Enter the tape contents: ")
    print("")
    main(mt, tape_start)
    print("The tape was accepted.")
