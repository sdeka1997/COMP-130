"""
Swapnav Deka
COMP 130
Assignment 8: Social Graphs
"""
class Graph:
    """
    Directed graph stored as an adjacency list.
    A graph is a dictionary mapping nodes to sets of neighbors.
    A node can be of any immutable type.
    """
    
    def __init__(self):
        """Create an empty graph."""
        self._graph = {}

    def __str__(self):
        """
        Returns a printable string version of the graph
        in the form
        Graph(set([...]), set([...]))
        where the node set is printed first, then the
        edge set.
        """
        return 'Graph(' + str(self.get_nodes()) + ', ' + str(self.get_edges()) + ')'
    
    def add_node(self, name):
        """
        Adds the named node to the graph, if it doesn't already exist.
        Returns nothing.
        """
        if name not in self._graph.keys():
            self._graph[name] = set()
    
    def add_edge(self, name_from, name_to):
        """
        Adds an edge from/to the named nodes, if it doesn't already exist.
        Also adds each of the named nodes, if they don't exist.
        Returns nothing.
        """
        if name_from not in self._graph.keys():
            self.add_node(name_from)
        if name_to not in self._graph.keys():
            self.add_node(name_to)
        if name_to not in self._graph[name_from]:
            self._graph[name_from].add(name_to)
        
    def get_nodes(self):
        """Returns a set of all the node names."""
        return set(self._graph.keys())
        
    def get_node_neighbors(self, name_from):
        """
        Returns a set of all the named node's neighbors.
        The neighbors are those nodes that this node has an edge to.
        Returns an empty set if the node doesn't exist.
        """
        if name_from not in self._graph.keys():
            return set()
        return self._graph[name_from]
    
    def get_edges(self):
        """
        Returns a set of all the edges.
        Each edge is a pair (tuple) of its source node,
        where it comes from, and its destination node,
        where it goes to.
        """
        output = set()
        for node_from in self._graph:
            for node_to in self._graph[node_from]:
                output.add((node_from, node_to))
        return output
           
    def is_neighbor(self, name_from, name_to):
        """
        Returns whether the named destination node is
        a neighbor of the named source node.
        """
        return name_to in self._graph[name_from]

class Graph2:
    """
    Graph stored as an adjacency matrix and a list of names.
    """
    
    def __init__(self):
        """
        Create an empty graph.
        """
        
        # The graph currently has no nodes, therefore no rows or columns.
        self._adjmatrix = []
        
        # Users of this class consider that each node has a string name.
        # Since the adjacency matrix (both rows and columns)
        # must be indexed by integers 0..n-1, we will internally assign
        # each node an integer 0..n-1.  self.names will be an array
        # that maps from this internal integer to the external name.
        # I.e., self.names[i] = the name for the ith node.
        # Each node name must be unique.
        #
        # The graph currently has no nodes, therefore no names of nodes.
        self._names = []
        
        # NO OTHER ATTRIBUTES SHOULD BE DEFINED.

    def __str__(self):
        """
        Returns a printable string version of the graph in the form
        Graph(set([...]), set([...]))
        where the node set is printed first, then the edge set.
        """
        return ("Graph(" +
                str(self.get_nodes()) + ", " + 
                str(self.get_edges()) + ")")
    
    def add_node(self, name):
        """
        Adds the named node to the graph, if it doesn't already exist.
        Returns nothing.
        """
        if name not in self._names:
            self._names.append(name)
            for node in self._adjmatrix:
                node.append(0)
            self._adjmatrix.append([0] * len(self._names))
    
    def add_edge(self, name_from, name_to):
        """
        Adds an edge from/to the named nodes, if it doesn't already exist.
        Also adds each of the named nodes, if they don't exist.
        Returns nothing.
        """
        if name_from not in self._names:
            self.add_node(name_from)
        if name_to not in self._names:
            self.add_node(name_to)
        if self._adjmatrix[self._names.index(name_from)][self._names.index(name_to)] == 0:
            self._adjmatrix[self._names.index(name_from)][self._names.index(name_to)] = 1
    
    def get_nodes(self):
        """Returns a set of all the node names."""
        return set(self._names)
        
    def get_node_neighbors(self, name_from):
        """
        Returns a set of all the named node's neighbors.
        The neighbors are those nodes that this node has an edge to.
        Returns an empty set if the node doesn't exist.
        """
        neighbors_set = set([])
        if name_from in self._names:
            index_from = self._names.index(name_from)
            for node_to in range(len(self._adjmatrix[index_from])):
                if self._adjmatrix[index_from][node_to] == 1:
                    neighbors_set.add(self._names[node_to])
        return neighbors_set

    def get_edges(self):
        """
        Returns a set of all the edges.
        Each edge is a pair (tuple) of its source node,
        where it comes from, and its destination node,
        where it goes to.
        """
        edge_set = set([])
        for out_node_index in range(len(self._adjmatrix)):
            for in_node_index in range(len(self._adjmatrix[out_node_index])):
                if self._adjmatrix[out_node_index][in_node_index] == 1:
                    edge_set.add((self._names[out_node_index], self._names[in_node_index]))
        return edge_set
    
    def is_neighbor(self, name_from, name_to):
        """
        Returns whether the named destination node is
        a neighbor of the named source node.
        """
        
        # This serves as an example of how we can use self.names
        # to map between the external node name and the internal
        # node integer.
        # We can use .index() since node names are unique.
        node_from = self._names.index(name_from)
        node_to = self._names.index(name_to)
        return self._adjmatrix[node_from][node_to]

def not_empty(set1):
    """
    Returns whether a set of nodes is empty or not.
    """
    return len(set1) > 0

def is_disjoint(set1, set2):
    """ 
    Retursn whether two sets of nodes are disjoint or not.
    """
    for node in set1:
        if node in set2:
            return False
    return True

def is_equivalent(graph, set1, set2):
    """
    Returns whether the set of nodes from a graph is equivalent to 
    the union of the two input sets of nodes.
    """
    union = set1.union(set2)
    for node in graph.get_nodes():
        if node not in union:
            return False
    return True

def is_partition(graph, set1, set2):
    """
    Returns whether the given node sets partition the graph.
    """
    if not not_empty(set1) or not not_empty(set2):
        return False
    if not is_disjoint(set1, set2):
        return False
    if not is_equivalent(graph, set1, set2):
        return False
    for node1 in set1:
        for node2 in set2:
            if graph.is_neighbor(node1, node2):
                return False
            if graph.is_neighbor(node2, node1):
                return False
    return True
    
def make_empty_graph():
    """
    Returns an empty graph.
    """
    return Graph()

def connect_all(graph, nodes):
    """
    Returns a modified graph by adding edges between all the nodes, except for 
    self-edges. It also adds any of these nodes that are not already in the graph.  
    """
    for o_node in nodes:
        if o_node not in graph.get_nodes():
            graph.add_node(o_node)
        for i_node in nodes:
            if i_node != o_node:
                if graph.is_neighbor(o_node, i_node) == False:
                    graph.add_edge(o_node, i_node)
    return graph


def create_graph_and_partition(nodes):
    """
    Returns three values: a graph consisting of the given nodes, and two sets 
    of nodes. Those two sets of nodes should form a partition of the graph.
    """
    graph = make_empty_graph()
    nodelist = list(nodes)
    nodelist1 = []
    nodelist2 = []
    for idx in range(len(nodelist)):
        graph.add_node(nodelist[idx])
        if idx % 2:
            nodelist1.append(nodelist[idx])
        else:
            nodelist2.append(nodelist[idx])
    nodelist1 = set(nodelist1)
    nodelist2 = set(nodelist2)
    graph = connect_all(graph, nodelist1)
    graph = connect_all(graph, nodelist2)
    return graph, nodelist1, nodelist2


def create_graph_without_partition(nodes):
    """
    Returns a graph consisting of the given nodes. The graph should not be 
    able to be partitioned.
    """
    graph = make_empty_graph()
    for node in nodes:
        graph.add_node(node)
    graph = connect_all(graph, nodes)
    return graph

