import json
from utility import create_elements_from_data, create_nodes_from_data


def load_system():
    with open("powerlines/system.json", "r", encoding="utf-8") as file:
        return json.load(file)


def print_info(nodes: list, elements: list):
    print("Итого. Получились следующие элементы сети:")
    print("-" * 50)
    for i in range(len(nodes)):
        print(nodes[i])
        print(elements[i])


def main():
    system = load_system()
    results = dict()
    try:
        source_voltage = int(system["source_voltage"])
        elements_data = system["elements"]
        nodes_data = system["nodes"]
    except (TypeError, ValueError) as e:
        raise Exception(
            f"JSON был неправильно сформирован. Ошибка {e}"
        )

    # Создаем объекты из данных JSON
    nodes = create_nodes_from_data(nodes_data)
    elements = create_elements_from_data(elements_data)

    if len(nodes) != len(elements):
        raise Exception(
            "Со схемой что-то не так. Программа не способна её решить"
        )
    print_info(nodes, elements)
    for i in range(len(elements) - 1, 0, -1):
        results[f"{elements[i].element_id}"] = dict()

        # Зарядная мощность в конце элемента
        results[f"{elements[i].element_id}"]["jQ''/2"] = (
            nodes[i].voltage ** 2 * elements[i].b / 2
        )

        # Зарядная мощность в начале элемента
        if (i > 1):
            results[f"{elements[i].element_id}"]["jQ'/2"] = (
                nodes[i - 1].voltage ** 2 * elements[i].b / 2
            )
        else:
            results[f"{elements[i].element_id}"]["jQ'/2"] = (
                source_voltage ** 2 * elements[i].b / 2
            )

        results[f"{elements[i].element_id}"]["Q''"] = (
            nodes[i].reactive_power -
            results[f"{elements[i].element_id}"]["jQ''/2"]
        )

        results[f"{elements[i].element_id}"]["P''"] = nodes[i].active_power


if __name__ == "__main__":
    main()
