import networkx as nx
with open(".\\ego_facebook\\facebook\\0.edges",'rb') as fh:
    G_roadNet=nx.read_edgelist(fh)
print(nx.density(G_roadNet))
print("No.nodes:",nx.number_of_nodes(G_roadNet))
print("No.edges:",nx.number_of_edges(G_roadNet))
