#!/usr/bin/env python3

from utils import ask

def bottom_up_procedure(clauses, assumables, verbose=False):

    fixed_point = []

    for assumable in assumables:

        if ask(assumable, verbose=False):
            fixed_point.append(assumable)

    added = True

    while added:
        added = False

        for clause in clauses:
            if clause.head not in fixed_point:
                if all(body in fixed_point for body in clause.body):

                    fixed_point.append(clause.head)
                    added = True

                    if verbose:
                        print(f"`{clause.head}` added to fixed point due to clause: {clause}")

    return fixed_point
