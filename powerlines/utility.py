from system_classes import Element, Node


def create_nodes_from_data(nodes_data: dict) -> list[Node]:
    """Создает список объектов Node из данных JSON"""
    nodes = []
    for node_id, node_info in nodes_data.items():
        node = Node(
            node_id=node_id,
            voltage=node_info["voltage"],
            active_power=node_info["active_power"],
            reactive_power=node_info["reactive_power"]
        )
        node.check_node_data()
        nodes.append(node)
    return nodes


def create_elements_from_data(elements_data: dict) -> list[Element]:
    """Создает список объектов Element из данных JSON"""
    elements = []
    for element_id, element_info in elements_data.items():
        element = Element(
            element_id=element_id,
            element_type=element_info["type"],
            circuit_number=element_info["circuit_number"],
            r0=element_info["R0"],
            x0=element_info["X0"],
            b0=element_info["B0"],
            length=element_info["L"]
        )
        element.check_element_data()
        elements.append(element)
    return elements
