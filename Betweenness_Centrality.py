import sys
import os
import pdb
import timeit
import collections
from assignemnt1 import bfs

try:
	first_arg = sys.argv[1]
	start1 = timeit.default_timer()
	d = {}

	def main_program (data=first_arg):
	  status={}
	  node=[]
	  with open(data, 'r') as f:
	    for line in f:
	       (key, val) = line.strip().split('\t')
	       if key not in d:
	           d[key] = [val]     
	       else:
	       #if key in d and val not in d[key]:
	           d[key].append(val)
	       if val not in d:
	           d[val]=[key]
	       #if val in d and key not in d[val]:
	       else:
	           d[val].append(key)
	       node=d.keys()
	       #pdb.set_trace()
	  Betweenness, time=BC(d, node)
	  od = collections.OrderedDict(sorted(Betweenness.items()))
	  for key, item in od.items():
	  	print("[{0}]\t{1}".format(key,item))
	  print ("running time of this algorithm is "+ str(time))

	def BC(graph,node):
		Betweenness={float(u): 0.0 for u in node}
		#pdb.set_trace()
		for s in node:
			dist={}
			weight={}
			weight[s]=1
			dist[s]=0
			prev={u: [] for u in node}
			q=[]
			q.append(s)
			source=[]
			while q:
				#pdb.set_trace()
				v=q.pop(0)
				source.append(v)
				for u in graph[v]:
					if u not in dist:
						dist[u]=dist[v]+1
						q.append(u)
						weight[u]=weight[v]
						prev[u]=[v]
					elif dist[u]==dist[v]+1:
						weight[u]=weight[v]+weight[u]
						prev[u].append(v)
			#pdb.set_trace()
			d={z: 0 for z in source}
			# pdb.set_trace()
			while source:
				n=source.pop()
				c=(1 + d[n])/float(weight[n])
				for u in prev[n]:
					d[u]=d[u]+(weight[u]*c)
				if n != s:
					Betweenness[float(n)]=Betweenness[float(n)]+d[n]
		stop1 = timeit.default_timer()
		runtime= float(stop1) - float(start1)
		# pdb.set_trace()
		component=bfs(graph, node)[1]
		for vertex in Betweenness:
			for key, items in component.items():
				if vertex in items:
					Betweenness[vertex]+=((len(items)-1)*2)+1
		return (Betweenness, runtime)

	if __name__ == '__main__':
		main_program()

except Exception as e:
  	print ("please give an input as edgelist")
  	sys.stdout.flush()
