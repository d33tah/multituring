#!/usr/bin/python
# -*- coding: utf-8 -*-

mt = {

    'start': 's0',
    'stop': ['s3'],
    'empty_symbol': '□',

    'tab': {
        's0': {
            'a':	('s1',	'a',	'R'),
            'b':	('s1',	'b',	'R'),
        },
        's1': {
            'a':	('s2',	'a',	'R'),
        },
        's2': {
            '□':	('s3',	'□',	'R'),
        }
    },

}

if __name__ == "__main__":
    import multituring
    multituring.interactive_test(mt)

