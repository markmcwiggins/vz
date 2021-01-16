#!/usr/bin/env python3

import sys

fyle = sys.argv[1]

nodez = {}  # quick access to each node
eldest = None

class Family(object):
    global nodez, eldest
    def __init__(self, parent_id,node_id,node_name):
        self.parent_id = parent_id
        self.node_id = node_id
        self.node_name = node_name

def main():

    f = open(fyle)

    members = []
    maxnode = -1
    for line in f:
        fields = line.rstrip().split('|')
        print(fields)
        for field in fields:
            try:
                (parent, node, name) = field.split(',')
            except:
                continue
            fam = Family(parent,node,name)
            nodez[node] = fam
            if int(node) > maxnode:
                maxnode = int(node)
            if parent == 'null':
                print('ELDEST')
                eldest = fam

            members.append(fam)


    #bottom = nodez[maxnode]


    print(eldest.node_name)
    for parid in range(0,6):
        print('level ', parid)
        for mem in members:
            if mem.parent_id != 'null':
                if int(mem.parent_id) == parid:
                    print(mem.node_name,end = ' ')
        print('\n')

if __name__ == "__main__":
    main()


        
