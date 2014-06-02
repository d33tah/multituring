#!/usr/bin/python3
# -*- coding: utf-8 -*-

mt = {

    'start': 's0',
    'stop': ['sk'],
    'empty_symbol': '□',

    'tab': {
        's0': {
            '0':	('s1',	'□',	'R'),
            '1':	('sk',	'□',	'R'),
        },
        's1': {
            '0':	('s1',	'0',	'R'),
            '1':	('s2',	'1',	'R'),
        },
        's2': {
            '0':	('s2',	'0',	'R'),
            '□':	('s3',	'□',	'L'),
        },
        's3': {
            '0':	('s4',	'□',	'L'),
            '1':	('sk',	'0',	'L'),
        },
        's4': {
            '0':	('s4',	'0',	'L'),
            '1':	('s4',	'1',	'L'),
            '□':	('s0',	'□',	'R'),
        },
    },

}

if __name__ == "__main__":
    import multituring
    import random

    def substract_test(i, j):
        print("Trying %s and %s..." % (i, j))
        m = multituring.Multituring(mt, ('0' * i) + '1' + ('0' * j))
        m.run(False)
        assert(m.get_tape_contents().count('0') == i-j)

    substract_test(1, 0)
    substract_test(1, 1)
    substract_test(2, 1)
    substract_test(2, 2)
    substract_test(3, 2)
    substract_test(4, 2)
    max_length = 100
    for _ in range(10):
        j = random.randint(1, max_length)
        i = random.randint(j, max_length)
        substract_test(i, j)
    #multituring.interactive_test(mt)

