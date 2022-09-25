#!/usr/bin/env python3

class Clause(object):

    def __init__(self, head, body=[]):

        self.head = head
        self.body = body

    def __str__(self):

        if self.body:

            chained_body = " ^ ".join(self.body)
            clause       = f"{self.head} <- {chained_body}."
            return clause

        else:
            
            clause = f"{self.head}."
            return clause
