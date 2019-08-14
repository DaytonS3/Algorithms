#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  outcomes = []
  hands = ["rock", "paper", "scissors"]

  def findOutCome(n, results):
    if n == 0:
      outcomes.append(results)
    else:
          for p in range(len(hands)):
            findOutCome((n-1), (results+[hands[p]]))
  findOutCome(n, [])     
  return outcomes

print(len(rock_paper_scissors(4)))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

