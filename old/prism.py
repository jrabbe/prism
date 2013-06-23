#!/usr/bin/python

import argparse
import json
import requests
from numpy import matrix
from numpy import matlib
from numpy import dtype

ACCESS_TOKEN = ""
HOST = "https://graph.facebook.com/"

def getFriends():
    url = "me/friends"
    query = {'access_token': ACCESS_TOKEN}

    print "-> Fetching friends..."

    r = requests.get(HOST + url, params=query);

    try:
        return json.loads(r.text)['data']
    except:
        print "ERROR! Could not read data from ", r.url
        print ""
        print r.text
        exit(2)


def getGroupsForFriend(friend):
    url = "/groups"
    query = {'access_token': ACCESS_TOKEN}

    print "=> Fetching groups for ", friend['name'], "..."

    r = requests.get(HOST + friend['id'] + url, params=query)

    try:
        return json.loads(r.text)['data']
    except:
        print "ERROR! Could not read data from ", r.url
        print ""
        print r.text
        exit(2)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="prism", description="Runs PRISM analysis on my friends from facebook.")
    parser.add_argument("-g", "--groups", type=file, default=None, help="The file containing json for the groups.")
    parser.add_argument("-f", "--friends", type=file, default=None, help="The file containing json for the friends.")
    parser.add_argument("-o", "--output", default=None, help="The base to use for output files, will be prepended to *_groups.json & *_friends.json.")
    parser.add_argument("-m", "--matrices", action='store_true', help="Set option to output matrix files.")

    args = parser.parse_args()

    if args.groups == None or args.friends == None:
        # data gathering
        groups = {}
        friends = getFriends()

        print "Found ", len(friends), " friends..."

        for friend in friends:
            friend['groupIds'] = []
            g = getGroupsForFriend(friend)
            for group in g:
                friend['groupIds'].append(group['id'])
                print "++ Adding group ", group['name'], " to ", friend['name'], "..."
                if group['id'] not in groups.keys():
                    print "!! and to groups..."
                    groups[group['id']] = group

        print "Your friends are in ", len(groups), " groups..."

        if args.output != None:
            print "writing friends to ", args.output, "_friends.json..."
            json.dump(friends, open(args.output + "_friends.json", "w"))

            print "writing groups to ", args.output, "_groups.json..."
            json.dump(groups, open(args.output + "_groups.json", "w"))

    else:
        print "Loading ", args.groups.name, " into groups..."
        groups = json.load(args.groups)

        print "Loading ", args.friends.name, " into friends..."
        friends = json.load(args.friends)

    # build matrix
    print "Building matrix..."
    f2g = matlib.zeros((len(groups), len(friends)), dtype(int))
    print "built a ", f2g.shape, " matrix..."

    for fi, friend in enumerate(friends):
        for gi, groupId in enumerate(groups.keys()):
            if groupId in friend['groupIds']:
                f2g[gi, fi] += 1

    if args.matrices and args.output != None:
        print "writing friend 2 group matrix to " + args.output + "_f2g.txt..."
        f2g.tofile(open(args.output + "_f2g.txt", "w"), ",")

    print "Calculating friend 2 friend matrix..."
    f2f = f2g.T * f2g

    if args.matrices and args.output != None:
        print "writing friend 2 friend matrix to " + args.output + "_f2f.txt..."
        f2f.tofile(open(args.output + "_f2f.txt", "w"), ",")

    print "Calculating group 2 group matrix..."
    g2g = f2g * f2g.T

    if args.matrices and args.output != None:
        print "writing group 2 group matrix to " + args.output + "_g2g.txt..."
        g2g.tofile(open(args.output + "_g2g.txt", "w"), ",")

    print "Writing dot graph for friend 2 friend..."
    dot = open(args.output + "_f2f.dot", 'w')
    dot.write("graph f2f {\n")
    length = range(len(friends))
    visited = []
    for x in length:
        for y in range(x):
            if x == y:
                continue

            if f2f[x, y] > 0:
                f1 = friends[x]
                f2 = friends[y]

                if not f1['id'] in visited:
                    dot.write("    " + f1['id'].encode('utf8') + " [label=\"" + f1['name'].replace('"', '\\"').encode('utf8') + "\"];\n")
                if not f2['id'] in visited:
                    dot.write("    " + f2['id'].encode('utf8') + " [label=\"" + f2['name'].replace('"', '\\"').encode('utf8') + "\"];\n")

                width = f2f[x,y].astype('str')
                weight = str(int(width) * 10)
                dot.write("    " + f1['id'].encode('utf8') + " -- " + f2['id'].encode('utf8') + " [penwidth=" + width + "];\n")

    dot.write("}\n")
    dot.close()

    print "Writing dot graph for group 2 group..."
    dot = open(args.output + "_g2g.dot", 'w')
    dot.write("graph g2g {\n")
    length = range(len(groups))
    visited = []
    for x in length:
        for y in range(x):
            if x == y:
                continue

            if g2g[x, y] > 0:
                k1 = groups.keys()[x]
                k2 = groups.keys()[y]
                g1 = groups[k1]
                g2 = groups[k2]

                if not g1['id'] in visited:
                    dot.write("    " + g1['id'].encode('utf8') + " [label=\"" + g1['name'].replace('"', '\\"').encode('utf8') + "\"];\n")
                if not g2['id'] in visited:
                    dot.write("    " + g2['id'].encode('utf8') + " [label=\"" + g2['name'].replace('"', '\\"').encode('utf8') + "\"];\n")

                width = g2g[x,y].astype('str')
                weight = str(int(width) * 10)
                dot.write("    " + g1['id'].encode('utf8') + " -- " + g2['id'].encode('utf8') + " [penwidth=" + width + "];\n")

    dot.write("}\n")
    dot.close()

    print "the end..."
    exit(0)

