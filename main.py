#!/usr/bin/env python3

from Abduction import abduction

from Examples import medical_diagnostic_assistant_kb

if __name__ == '__main__':

    clauses, assumables = medical_diagnostic_assistant_kb()

    minimal_explanations = abduction(clauses, assumables, ['wheezing'], verbose=True)

    print(minimal_explanations)
