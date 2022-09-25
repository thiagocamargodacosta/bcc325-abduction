#!/usr/bin/env python3

from Clause import Clause

def medical_diagnostic_assistant_kb():

    bronchitis_1 = Clause('bronchitis',['influenza'])
    bronchitis_2 = Clause('bronchitis', ['smokes'])
    coughing     = Clause('coughing', ['bronchitis'])
    wheezing     = Clause('wheezing', ['bronchitis'])
    fever_1      = Clause('fever', ['influenza'])
    fever_2      = Clause('fever', ['infection'])
    sore_throat  = Clause('sore_throat', ['influenza'])
    false        = Clause('false', ['smokes','nonsmoker'])

    clauses = [bronchitis_1, bronchitis_2, coughing, wheezing, fever_1, fever_2, sore_throat, false]

    assumables = ['smokes', 'nonsmoker', 'influenza', 'infection']

    return clauses, assumables
