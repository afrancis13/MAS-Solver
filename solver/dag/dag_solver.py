class DAGSolver(object):

    def __init__(self, adj_matrix):
        self.sorted_nodes = []
        self.nodes = [i for i in range(len(adj_matrix))]
        self.adj_matrix = adj_matrix
        self.previsited = [0 for i in range(len(adj_matrix))]
        self.postvisited = [0 for i in range(len(adj_matrix))]

    def topological_sort(self):
        while len(self.unmarked_nodes) > 0:
            node = self.unmarked_nodes.pop()
            if self.visit(node) is None:
                return None
        return self.sorted_nodes

    def visit(self, node):
        if self.is_previsited(node):
            return None
        if not self.is_postvisited(node):
            self.previsit(node)
            for adj_node in range(len(self.adj_matrix[node])):
                if self.adj_matrix[adj_node] == 1:
                    self.visit(adj_node)
            self.postvisit(node)
            self.sorted_nodes.append(node)

    def previsit(self, node):
        self.previsited[node] = 1

    def postvisit(self, node):
        self.postvisited[node] = 1

    def is_previsited(self, node):
        return self.previsited[node] == 1

    def is_postvisited(self, node):
        return self.postvisited[node] == 1
