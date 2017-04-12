#!/usr/bin/env python
"""
This Module takes user input and writes SymbiotCode that is read by the Symbiot software. Each script
with the suffix -Generator creates one line of SymbiotCode. MakeMethod receives user input, generates SymbiotCode
by calling the various Generator files, and outputs a finished Test.

There can be many tests per group, and many steps per test. Drawing liquid and Dropping liquid are operations that
can be utilized within a step.
"""