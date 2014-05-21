#!/usr/bin/python
# -*- coding: utf-8 -*-

mt = {

    'start': 's0',
    'stop': ['s3'],
    'empty_symbol': '□',

    'tab': {
        's0': {
            'a':	('s0',	'a',	'R'),
            'b':	('s0',	'b',	'R'),
            '□':	('s1',	'□',	'L'),
        },
        's1': {
            'a':	('s2',	'a',	'L'),
        },
        's2': {
            'b':	('s3',	'b',	'L'),
        }
    },

}

if __name__ == "__main__":
    import multituring
    multituring.interactive_test(mt)

