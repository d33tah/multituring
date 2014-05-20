#!/usr/bin/python

import collections

def main(mt_start, tape_start):

    current_state = mt['start']

    tape = collections.defaultdict(lambda: None)
    # load tape_start onto the tape
    tape.update(dict(enumerate(list(tape_start))))

    pos = 0
    direction = 'S'

    while True:
        symbol = tape[pos]

        to_print = tuple(map(repr, (current_state, symbol, direction)))
        print('(%s,\t%s,\t%s)' % to_print)

        current_state, symbol, direction = mt['tab'][current_state][symbol]

        if current_state in mt['stop']:
            return True

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
    main(mt, tape_start)
    print("The tape was accepted.")
