#!/usr/bin/env python3

def ask(askable, verbose=True):

    if verbose:

        ans = input(f'Is `{askable}` true? ')

        if ans.lower() in ['y']:
            return True
        else:
            return False
    
    else:
        return True
