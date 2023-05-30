class Tree:
    def __init__(self, root = None):
        self.root = root

    # Depth first 
    # def get_element_by_id(self, id):
    #     nodes_to_vist = [self.root]
    #     while len(nodes_to_vist) > 0:
    #         node = nodes_to_vist.pop(0)
    #         if node["id"] == id: 
    #             return node
    #         nodes_to_vist = node["children"] + nodes_to_vist
    #     return None

    # Breadth first 
    def get_element_by_id(self, id):
        nodes_to_vist = [self.root]
        while len(nodes_to_vist) > 0:
            node = nodes_to_vist.pop(0)
            if node["id"] == id: 
                return node
            nodes_to_vist = nodes_to_vist + node["children"]
        return None