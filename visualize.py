#!/usr/bin/python
import git
import networkx as nx

#git --git-dir=somewhere.git rev-list --parents --branches --tags --remotes > git.adjlist
#optional - shorten hashes: sed -ir 's/([a-zA-Z0-9]{6})[a-zA-Z0-9]*/\1/g' git.adjlist
#python visualize.py <(head -n100 git.adjlist)
#dot git.dot -Tpng -o git.png
#open git.png
def load(path):
  hist = nx.read_adjlist(path, create_using=nx.DiGraph())
  nx.write_dot(hist, 'git.dot')


if __name__ == '__main__':
  import sys
  load(sys.argv[1])

