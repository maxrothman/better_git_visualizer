#!/usr/bin/python
#import git
import networkx as nx
import matplotlib.pyplot as plt

#perhaps this would be easier to prototype with ipython

#git -C somewhere.git rev-list --parents --branches --tags --remotes > git.adjlist
#optional - shorten hashes: sed -i 's/\([a-zA-Z0-9]\{6\}\)[a-zA-Z0-9]*/\1/g' git.adjlist
#python visualize.py <(head -n100 git.adjlist)
#dot git.dot -Tpng -o git.png
#open git.png
def load(path):
  hist = nx.read_adjlist(path, create_using=nx.DiGraph())
  nx.write_dot(hist, 'git.dot')


# if __name__ == '__main__':
#   import sys
#   load(sys.argv[1])

#----------------------

nodes = [
        (1, {'branch': 'm'}),
        (2, {'branch': 'm'}),
        (3, {'branch': 'm'}),
        (4, {'branch': 'm'}),
        (5, {'branch': 'm'}),
        (6, {'branch': 'm'}),
        (7, {'branch': 'm'}),
        (8, {'branch': 'b1'}),
        (9, {'branch': 'b2'}),
        (10, {'branch': 'b3'}),
        (11, {'branch': 'b3'}),
        (12, {'branch': 'b3'}),
]

adjacency_list = [(1,2, {'branch': 'm'}), (2,3, {'branch': 'm'}), 
                  (3,4, {'branch': 'm'}), (4,5, {'branch': 'm'}), 
                  (5,6, {'branch': 'm'}), (6,7, {'branch': 'm'}), 
                  (2,10, {'branch': 'b3'}), (10,11, {'branch': 'b3'}), 
                  (11,12, {'branch': 'b3'}), (12,7, {'branch': 'b3'}), 
                  (3,8, {'branch': 'b1'}), (8,5, {'branch': 'b1'}), 
                  (4,9, {'branch': 'b2'}), (9,6, {'branch': 'b2'})]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(adjacency_list)

fig = plt.figure(1, figsize=(10,10))
ax = fig.add_subplot(1,1,1)
ax.set_xlim(0,100)
ax.set_ylim(0,100)

def point(x, y):
  c = plt.Circle((x,y), radius=1, color='g')
  ax.add_patch(c)

def line(x1, y1, x2, y2):
  l = plt.Line2D((x1, x2), (y1, y2))
  ax.add_line(l)

def delta(branchname):
  edges = [x for x in G.edges(data=True) if x['branch'] == branchname]
  nodes = edges2nodes(edges)
  master_nodes = sorted(n for n in nodes if n['branch']=='m')
  start = master_nodes[0]; finish = master_nodes[1]

  c=0; node = start
  while node != finish:
    c += 1
    node = [x for x in G.neighbors(node) if x['branch']=='m'][0]

  return c

def edges2nodes(edges):
  nodeset = set()
  for (n1, n2) in edges:
    nodeset.add(n1); nodeset.add(n2)
  return nodeset
