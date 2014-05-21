#!/usr/bin/python
# -*- coding: utf-8 -*-

mt = {

    'start': 's0',
    'stop': ['sk'],
    'empty_symbol': '□',

    'tab': {
        's0': {
            '0':	('s0',	'0',	'R'),
            '□':	('s1',	'#',	'L'),
        },
        's1': {
            '0':	('s1',	'0',	'L'),
            '#':	('s1',	'#',	'L'),
            '□':	('s2',	'□',	'R'),
        },
        's2': {
            '0':	('s3',	'□',	'R'),
            '#':	('sk',	'□',	'R'),
        },
        's3': {
            '0':	('s4',	'□',	'R'),
            '#':	('sk',	'□',	'R'),
        },
        's4': {
            '0':	('s4',	'0',	'R'),
            '#':	('s4',	'#',	'R'),
            '□':	('s1',	'0',	'L'),
        },
    },
}

if __name__ == "__main__":
    import multituring
    import random
    import math

    def div2_test(n):
        print("Trying %s..." % (n))
        m = multituring.Multituring(mt, ('0' * n))
        m.run(False)
        expected = int(math.floor(n/2.0))
        assert(m.get_tape_contents().count('0') == expected)

    for n in range(101):
        div2_test(random.randint(0, 100))
    multituring.interactive_test(mt)

