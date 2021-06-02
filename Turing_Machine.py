# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:19:13 2021

@author: Arthur Querido Lopes
"""

def turing_machine(transitions, state, acceptance_state, strip, pos):

    #verify if state is in acceptance state and stop if it is
    if state in acceptance_state:
        return True
    
    for transition in transitions:
        if state == transition[0] and strip[pos] == transition[1]:
            state = transition[2]
            strip[pos] = transition[3]
            if transition[4] == 'D':
                pos = pos+1
            if transition[4] == 'E':
                pos = pos-1
            if turing_machine(transitions, state, acceptance_state, strip, pos):
                return True
    
    return False


#Receiving number of states from user
n = int(input())

#Receiving alphabet symbols
n = input()

#Receiving strip symbols
strip_symbols = input().split()
strip_symbols.pop(0)

#Receiving acceptance states from user
acceptance_state = set(input())

#Receiving number of transitions from user
t = int(input())

transitions = []
#Receiving transitions from user
for i in range(t):
    trans = input().split()
    transitions.append(trans)

#Receiving number of strings to be tested
c = int(input())
 
#Receiving strings one by one
tape = []
for i in range(c):
    tape.append(str(input()))
    
#Testing all strings
for strip in tape:
    if (turing_machine(transitions, '0', acceptance_state, strip, 0)):
        print("aceita")
    else:
        print("rejeita")