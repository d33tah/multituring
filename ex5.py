#!/usr/bin/python3
# -*- coding: utf-8 -*-

mt = {

    'start': 's0',
    'stop': ['sk'],
    'empty_symbol': '□',

    'tab': {
        's0': {
            'α':	('s0',	'0',	'R'),
            'β':	('s0',	'1',	'R'),
            '0':	('s1',	'a',	'R'),
            '1':	('s2',	'b',	'R'),
            '□':	('sk',	'□',	'R'),
        },
        's1': {
            'α':	('s1',	'α',	'R'),
            'β':	('s1',	'β',	'R'),
            '0':	('s1',	'0',	'R'),
            '1':	('s1',	'1',	'R'),
            'a':	('s1',	'a',	'R'),
            'b':	('s1',	'b',	'R'),
            '□':	('s3',	'α',	'L'),
        },
        's2': {
            'α':	('s2',	'α',	'R'),
            'β':	('s2',	'β',	'R'),
            '0':	('s2',	'0',	'R'),
            '1':	('s2',	'1',	'R'),
            'a':	('s2',	'a',	'R'),
            'b':	('s2',	'b',	'R'),
            '□':	('s3',	'β',	'L'),
        },
        's3': {
            '0':	('s3',	'0',	'L'),
            '1':	('s3',	'1',	'L'),
            'α':	('s3',	'α',	'L'),
            'β':	('s3',	'β',	'L'),
            'a':	('s0',	'0',	'R'),
            'b':	('s0',	'1',	'R'),
        },
    },
}

if __name__ == "__main__":
    import multituring
    testcase = '0010'
    m = multituring.Multituring(mt, testcase)
    m.run(False)
    print(m.get_tape_contents())
    assert(m.get_tape_contents() == testcase*2)
    multituring.interactive_test(mt)

