# -*- coding: utf-8 -*-
"""
Author:Ruben Bustamante
Instructor: Diego Aguirre
TA:Gerarado Barraza
Course: CS 2302
Assigment: lab 7-unit test
Date of last modification: 12/02/2019
Purpose of program:test edit_distance.py file with hard code strings
"""
from edit_distance import edit_distance

def main():
    print("min number of steps:",edit_distance('miner','money'))
    print("min number of steps:",edit_distance('a', ''))
    print("min number of steps:",edit_distance('turn', 'ta'))
    print("min number of steps:",edit_distance('cat','Doggz'))
    print("min number of steps:",edit_distance('zzz', 'sleepz'))
    print("min number of steps:",edit_distance('xzyzyzabc', 'y'))
    print("min number of steps:",edit_distance('albertsons','walmart'))
    print("min number of steps:",edit_distance('bye', 'hellworld'))
    print("min number of steps:",edit_distance('time', 'money'))
    print("min number of steps:",edit_distance('" "', '" "'))
main()