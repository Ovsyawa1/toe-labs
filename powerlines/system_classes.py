class Node:
    """Класс для представления узла энергосистемы"""

    def __init__(
        self,
        node_id: str,
        voltage: float,
        active_power: float,
        reactive_power: float
    ):
        self.node_id = node_id
        self.voltage = voltage
        self.active_power = active_power
        self.reactive_power = reactive_power

    def __str__(self):
        return f"=== Узел: {self.node_id} ===\
            \nНапражение в узле: {self.voltage}\
            \nПриведенная активная мощность: {self.active_power}\
            \nПриведенная реактивна мощность: {self.reactive_power}"

    def check_node_data(self):
        if (not bool(self.node_id)) or (not isinstance(self.node_id, str)):
            raise Exception("У узла нет названия")

        try:
            self.voltage = float(self.voltage)
            self.active_power = float(self.active_power)
            self.reactive_power = float(self.reactive_power)
        except (TypeError, ValueError) as e:
            raise Exception(f"Были получены получени некорректные данные \
                            для узла {self.node_id}: {e}")


class Element:
    """Класс для представления элемента энергосистемы"""

    def __init__(
        self,
        element_id: str,
        element_type: str,
        circuit_number: int,
        r0: float,
        x0: float,
        b0: float,
        length: float
    ):
        self.element_id = element_id
        self.element_type = element_type
        self.circuit_number = circuit_number
        self.r = r0 * length / circuit_number
        self.x = x0 * length / circuit_number
        self.b = b0 * length * circuit_number

    def __str__(self):
        return f"=== Элемент: {self.element_id} === \
            \nМарка провода: {self.element_type} \
            \nАктивное сопротивление с учетом цепности: {self.r:.3f} \
            \nРеактивное сопротивление с учетом цепности: {self.x:.3f} \
            \nЕмкостная проводимость с учетом цепности: {self.b:g}"

    def check_element_data(self):
        if (
            not bool(self.element_id) or
            not isinstance(self.element_id, str)
        ):
            raise Exception("У элемента нет названия")

        try:
            self.element_type = str(self.element_type)
            self.circtuit_number = int(self.circuit_number)
            self.r = float(self.r)
            self.x = float(self.x)
            self.b = float(self.b)
        except (TypeError, ValueError) as e:
            raise Exception(f"Были получены получени некорректные данные: {e}")
