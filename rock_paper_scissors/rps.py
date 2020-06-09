#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  plays = [['rock'], ['paper'], ['scissors']]
  if n == 0:
    return [[]]
  else:
    return [p + r for p in plays for r in rock_paper_scissors(n-1)]
  # Your code here

  pass


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')