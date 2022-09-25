#!/usr/bin/env python3

from Clause import Clause
from Bottom_Up import bottom_up_procedure

def abduction(clauses, assumables, observations, verbose=False):

    need_to_explain = list()

    for observation in observations:

        if observation in assumables:
            continue

        for clause in clauses:

            if observation == clause.head:

                explain = Clause(clause.head, clause.body)
                
                need_to_explain.append(explain)

                if verbose:
                    print(f'need_to_explain: {explain}')


    for clause in clauses:
        for explain in need_to_explain:
            for item in explain.body:

                if clause.head in item:
                    if item not in need_to_explain:

                        follows = Clause(str(clause.head), clause.body)
                        
                        need_to_explain.append(follows)

    if verbose:
        for item in need_to_explain[len(observations):]:
            print(f'\tfollows: {item}')
    

    minimal_explanations = []

    for explain in need_to_explain:
        for item in explain.body:

            fixed_point = bottom_up_procedure([explain], [item], verbose=True)

            minimal_explanation = set()

            if fixed_point != []:
                if item in assumables:
                    if item not in minimal_explanations:

                            minimal_explanation.add(item)

            if minimal_explanation != set():
                    if minimal_explanation not in minimal_explanations:
                        minimal_explanations.append(minimal_explanation)
    
    return minimal_explanations
