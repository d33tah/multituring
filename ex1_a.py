#!/usr/bin/python3
# -*- coding: utf-8 -*-

mt = {

    'start': 's0',
    'stop': ['s3'],
    'empty_symbol': '□',

    'tab': {
        's0': {
            'a':	('s1',	'a',	'R'),
            '□':	('s3',	'□',	'R'),
        },
        's1': {
            'a':	('s2',	'a',	'R'),
        },
        's2': {
            'b':	('s3',	'b',	'R'),
        }
    },

}

if __name__ == "__main__":
    import multituring
    multituring.interactive_test(mt)

