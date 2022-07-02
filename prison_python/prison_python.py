#import numpy as np
import random

def random_algorithm(verbose, size):
    boxes = list(range(size))
    random.shuffle(boxes)
    if verbose:
        print("Random Algorithm:")
        print("Number of Prisoners:", size)
        print("Boxes:", boxes)
    failed = 1
    for prisoner in range(size):
        failed = 1
        if verbose:
            print("Prisoner:", prisoner)
        choices = random.choices(range(size), k=size//2)
        if verbose:
            print("Choices:", choices)
        for choice in choices:
            #import ipdb; ipdb.set_trace()
            if verbose:
                print("Trying Choice:", choice, "Contains:", boxes[choice])
            if boxes[choice] == prisoner:
                if verbose:
                    print("Success Prisoner:", prisoner)
                failed = 0
                break
        if failed:
            if verbose:
                    print("Failed Prisoner:", prisoner)
            break
    return not failed

def tryloop_algorithm(verbose, size):
    boxes = list(range(size))
    random.shuffle(boxes)
    if verbose:
        print("TryLoop Algorithm:")
        print("Number of Prisoners:", size)
        print("Boxes:", boxes)
    failed = 1
    for prisoner in range(size):
        failed = 1
        if verbose:
            print("Prisoner:", prisoner)
        tries = range(size//2)
        choice = prisoner
        for tryy in tries:
            if verbose:
                print("Try:", tryy, " Box:", choice, "Contains:", boxes[choice])
            if boxes[choice] == prisoner:
                failed = 0
                break
            choice = boxes[choice]
        if failed:
            if verbose:
                    print("Failed Prisoner:", prisoner)
            break
    return not failed

def main(algorithm, verbose=True):
    if algorithm == 'random':
        return random_algorithm(verbose, 100)
    elif algorithm == 'tryloop':
        return tryloop_algorithm(verbose, 100)