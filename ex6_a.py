#!/usr/bin/python
# -*- coding: utf-8 -*-

mt = {

    'start': 's0',
    'stop': ['sk'],
    'empty_symbol': '□',

    'tab': {
        's0': {
            'a':	('s1',	'*',	'R'),
            '□':	('sk',	'□',	'R'),
            '*':	('s0',	'*',	'R'),
        },
        's1': {
            'a':	('s1',	'a',	'R'),
            'b':	('s2',	'*',	'R'),
            '*':	('s1',	'*',	'R'),
        },
        's2': {
            'b':	('s2',	'b',	'R'),
            '*':	('s2',	'*',	'R'),
            'c':	('s3',	'*',	'R'),
        },
        's3': {
            'c':	('s3',	'c',	'R'),
            '□':	('s4',	'□',	'L'),
        },
        's4': {
            'a':	('s4',	'a',	'L'),
            'b':	('s4',	'b',	'L'),
            'c':	('s4',	'c',	'L'),
            '*':	('s4',	'*',	'L'),
            '□':	('s0',	'□',	'R'),
        },
    },
}

if __name__ == "__main__":
    import multituring
    while True:
        multituring.interactive_test(mt)
