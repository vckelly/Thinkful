#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", help="the base", type = int)
parser.add_argument("y", help="the exponent", type=int)

parser.add_argument("-v",'--verbosity', help="increase output verbosity", action = 'count', default=0)
args = parser.parse_args()

answer = args.x**args.y

if args.verbosity >= 2:  # TODO: verbosity should be a true/flase flag, not value oriented
  print " {} to the power of {} equals {}".format(args.x, args.y, answer)
elif args.verbosity >=1:
  print "{}^{} == {}".format(args.x, args.y, answer)
else:
  print answer

#print args.square**2

