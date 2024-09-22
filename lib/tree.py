class Tree:
    def __init__(self, root):
        self.root = root

    def breadth_first_traversal(self, node):
        result = []
        nodes_to_visit = [node]

        while len(nodes_to_visit) > 0:
            # 1. Remove the first node
            node = nodes_to_visit.pop(0)
            # 2. Add its value to the result list
            result.append(node['value'])
            # 3. Add its children to the end of the list
            nodes_to_visit.extend(node['children'])

        return result

    def depth_first_traversal(self, node):
        result = []
        nodes_to_visit = [node]

        while len(nodes_to_visit) > 0:
            # 1. Remove the first node
            node = nodes_to_visit.pop(0)
            # 2. Add its value to the result list
            result.append(node['value'])
            # 3. Add its children to the beginning of the list
            nodes_to_visit = node['children'] + nodes_to_visit

        return result

    def depth_first_traversal_recursive(self, node, result=None):
        if result is None:
            result = []
        result.append(node['value'])
        for child in node['children']:
            self.depth_first_traversal_recursive(child, result)
        return result

    def get_element_by_id(self, element_id):
        return self._dfs(self.root, element_id)

    def _dfs(self, node, element_id):
        if node['id'] == element_id:
            return node
        for child in node['children']:
            result = self._dfs(child, element_id)
            if result:
                return result
        return None

    def get_element_by_id_bfs(self, element_id):
        nodes_to_visit = [self.root]
        while nodes_to_visit:
            node = nodes_to_visit.pop(0)
            if node['id'] == element_id:
                return node
            nodes_to_visit.extend(node['children'])
        return None

# Example usage:
if __name__ == "__main__":
    child_1 = {'value': 2, 'id': 'child_1', 'children': []}
    child_2 = {'value': 3, 'id': 'child_2', 'children': []}
    child_3 = {'value': 4, 'id': 'child_3', 'children': []}
    root = {'value': 1, 'id': 'root', 'children': [child_1, child_2, child_3]}

    tree = Tree(root)

    print("BFS Traversal:", tree.breadth_first_traversal(root))  # Output: [1, 2, 3, 4]
    print("DFS Traversal:", tree.depth_first_traversal(root))    # Output will vary based on tree structure
    print("Recursive DFS Traversal:", tree.depth_first_traversal_recursive(root))  # Output will vary
    print("Get Element by ID (DFS):", tree.get_element_by_id('child_2'))  # Output: {'value': 3, 'id': 'child_2', 'children': []}
    print("Get Element by ID (BFS):", tree.get_element_by_id_bfs('child_2'))  # Same output as above


# class Tree:
#   def __init__(self, root = None):
#     self.root = root

#   def breadth_first_traversal(node):
#     result = []
#     nodes_to_visit = [node]

#     while len(nodes_to_visit) > 0:
#       # 1. Remove the first node from the `nodes_to_visit` list
#       node = nodes_to_visit.pop(0)
#       # 2. Add its value to the result list
#       result.append(node['value'])
#       # 3. Add its children (if any) to the END of the `nodes_to_visit` list
#       nodes_to_visit = nodes_to_visit + node['children']

#     return result

#   def get_element_by_id(self, id):
#     pass


