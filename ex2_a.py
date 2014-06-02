#!/usr/bin/python3
# -*- coding: utf-8 -*-

mt = {

    'start': 's0',
    'stop': ['s0'],
    'empty_symbol': '□',

    'tab': {
        's0': {
            'a':	('s0',	'a',	'R'),
            'b':	('s0',	'□',	'R'),
        },
    },

}

if __name__ == "__main__":
    import multituring
    multituring.interactive_test(mt)

