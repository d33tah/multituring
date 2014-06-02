#!/usr/bin/python3
# -*- coding: utf-8 -*-

mt = {

    'start': 's0',
    'stop': [],
    'empty_symbol': '□',

    'tab': {
        's0': {
            'a':	('s0',	'a',	'R'),
            'b':	('s0',	'b',	'R'),
            '□':	('s1',	'#',	'R'),
        },
        's1': {
            'a':	('s1',	'a',	'L'),
            'b':	('s1',	'b',	'L'),
            '□':	('s2',	'□',	'R'),
        },
    },

}

if __name__ == "__main__":
    import multituring
    multituring.interactive_test(mt)

