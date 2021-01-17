#!/usr/bin/env python3
""" Code to represent a family from a file of people and node IDs """

import sys


class Family(object):
    """ class to represent the family """
    def __init__(self, parent_id, node_id, node_name):
        self.parent_id = parent_id
        self.node_id = node_id
        self.children = []
        self.node_name = node_name

def dotree(person, level):
    """ recursive tree walk function to display family structure --
        trees of this structure are much easier to code recursively
        than iteratively """
    for x in range(level):
        print(' ', end='')
    print(person.node_name)
    for c in person.children:
        dotree(c, level+1)

def main():

    nodez = {}     # quick access to each Family object
    try:
        fyle = sys.argv[1]
    except IndexError:
        print('usage: ./hierarchy.py data.in')
        sys.exit(1)

    eldest = None  # the root 'grandfather' object

    f = open(fyle)


    for line in f:
        fields = line.rstrip().split('|')
        for field in fields:
            try:
                (parent, node, name) = field.split(',')
            except ValueError:
                continue
            fam = Family(parent, node, name)
            nodez[node] = fam
            if parent == 'null':
                eldest = fam
            else:
                nodez[parent].children.append(fam)



    dotree(eldest, 0)

if __name__ == "__main__":
    main()
