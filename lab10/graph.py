import networkx as nx
import csv
import matplotlib.pyplot as plt
f = open('/Users/Kylee/secu2002_master/data/london_gang.csv','r' )
r = csv.DictReader(f, delimiter =',')

f1 = open('/Users/Kylee/secu2002_master/data/london_gang_attr.csv','r' )
r1 = csv.DictReader(f1, delimiter =',')

ranking_data = {}
for rows in r1:
    ranking_data[rows['ID']] = int(rows['Ranking'])

spreadsheet = []
for row in r:
    spreadsheet.append(row)

nodes = []
graph = nx.Graph()
for row in spreadsheet:
    graph.add_node(row['\xef\xbb\xbf'])
    graph.node[row['\xef\xbb\xbf']]['Ranking'] = ranking_data[row['\xef\xbb\xbf']]

for i in range(0,len(spreadsheet)):
    for k in spreadsheet[i]:
        if spreadsheet[i][k] != '0':
            graph.add_edge(i,k)

print graph
nx.draw(graph)
plt.show()

