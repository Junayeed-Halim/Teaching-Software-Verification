class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.out_edges = set()

    def get_node_id(self):
        return self.node_id

    def get_out_edges(self):
        return self.out_edges

    def add_out_edge(self, edge):
        self.out_edges.add(edge)


class Edge:
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def get_src(self):
        return self.src

    def get_dst(self):
        return self.dst


class Graph:
    def __init__(self):
        self.nodes = set()

    def get_nodes(self):
        return self.nodes

    def add_node(self, node):
        self.nodes.add(node)

class GraphTraversal:
    def __init__(self):
        self.visited = set()
        self.path = []
        self.paths = set()


    def print_path(self, path):
        path_str = "START: " + "->".join(str(node.get_node_id()) for node in path) + "->END"
        print(path_str)
        self.paths.add(path_str)

    def dfs(self, src_edge, dst):
        src = src_edge.get_dst()
        self.visited.add(src)
        self.path.append(src)

        if src == dst:
            self.print_path(self.path)
        else:
            for edge in src.get_out_edges():
                if edge.get_dst() not in self.visited:
                    self.dfs(edge, dst)

        self.visited.remove(src)
        self.path.pop()

    def get_paths(self):
        return self.paths




if __name__ == "__main__":
    # Initialize nodes
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    # Initialize edges
    edge0 = Edge(node0, node1)
    edge1 = Edge(node1, node2)
    edge2 = Edge(node1, node3)
    node1.add_out_edge(edge1)
    node1.add_out_edge(edge2)
    edge3 = Edge(node2, node4)
    edge4 = Edge(node3, node4)
    node2.add_out_edge(edge3)
    node3.add_out_edge(edge4)
    edge5 = Edge(node4, node5)
    node4.add_out_edge(edge5)

    # Initialize graph
    g = Graph()
    g.add_node(node1)
    g.add_node(node2)
    g.add_node(node3)
    g.add_node(node4)
    g.add_node(node5)

    # Expected answer
    expected_answer = {"START: 1->2->4->5->END", "START: 1->3->4->5->END"}

    # Test
    dfs = GraphTraversal()
    dfs.dfs(edge0, node5)
    assert dfs.get_paths() == expected_answer, "Test case failed!"
    print("Test case passed!")
