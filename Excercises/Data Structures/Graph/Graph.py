from collections import deque

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print(self.graph_dict)

    def get_path(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)

        return paths

    def get_shortest_paths(self, start, end):
        queue = deque([[start]])
        shortest_paths = []
        min_length = None

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == end:
                if min_length is None or len(path) == min_length:
                    shortest_paths.append(path)
                    min_length = len(path)
                elif len(path) < min_length:
                    shortest_paths = [path]
                    min_length = len(path)
            else:
                for next_node in self.graph_dict.get(node, []):
                    if next_node not in path:
                        queue.append(path + [next_node])

        return shortest_paths


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    print(route_graph.get_path("Mumbai", "New York"))
    print(route_graph.get_shortest_paths("Mumbai", "New York"))
