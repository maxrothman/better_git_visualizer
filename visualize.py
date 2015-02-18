#!/usr/bin/python
import git
from collections import namedtuple

Col = namedtuple('Col', ['width'])
cols = []

def load(path):
  nodes = {}
  to_traverse = [git.Repo(path).head.commit]

  while to_traverse:
    current = to_traverse.pop()
    if current.name_rev[:6] not in nodes:
      nodes[current.name_rev[:6]] = [c.name_rev[:6] for c in current.parents]
    else:
      raise Exception('Loop detected!')
    if current.parents:
      #to_traverse.append(current.parents[0])
      to_traverse.extend(current.parents)
      #watch out, there's a loop!

  return nodes


if __name__ == '__main__':
  import sys
  nodes = load(sys.argv[1])
  current, parents = nodes.popitem()
  while parents:
    current = parents[0]
    parents = nodes[current]
  
  print current

