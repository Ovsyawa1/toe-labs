from csv import writer
from logging import getLogger
from abstract_class import AbstractCalculator


import math

from logger_setuper import MY_LOGGER_NAME


logger = getLogger(MY_LOGGER_NAME)


class CircuitCalculator(AbstractCalculator):
    def __init__(
        self,
        r_resistance,
        inductance,
        capacity,
        voltage,
    ):
        # Сопротивления
        self.r_resistance = r_resistance
        self.l_resistance = 0
        self.c_resistance = 0

        # Индуктивность, емкость и напряжение (вводимые параметры)
        self.inductance = inductance
        self.capacity = capacity
        self.voltage = voltage

        # f, Z, I, fi (Выводимые параметры)
        self.frequency = 0
        self.resistance = 0
        self.current = 0
        self.fi = 0

    def calc_react_res(self):
        self.l_resistance = 2 * math.pi * self.frequency * self.inductance
        try:
            self.c_resistance = 1 / (
                2 * math.pi * self.frequency * self.capacity
            )
        except ZeroDivisionError as e:
            logger.error(
                f"Ошибка! Деление на ноль при частоте {self.frequency} "
                "во время выполнения расчета сопротивления ёмкости. "
                "Программа досрочно завершает свою работу "
                f"\nОшибка: {e}"
            )
            raise ZeroDivisionError(
                "Обнаружено деление на ноль! Измените параметры емкости "
                "({self.capacity}), либо диапозон частоты "
                "(текущая частота - {self.frequency})."
                f"\nОшибка: {e}"
            )

    def calc_resistance(self):
        self.resistance = math.sqrt(
            self.r_resistance**2 + (self.l_resistance - self.c_resistance)**2
        )
        if abs(self.l_resistance - self.c_resistance) < 1e-6:
            logger.info(
                f"Обнаружен резонанс! Текущая частота {self.frequency}"
            )

    def calc_current(self):
        try:
            self.current = self.voltage / self.resistance
        except ZeroDivisionError as e:
            logger.error(
                f"Ошибка! Деление на ноль при частоте {self.frequency} "
                "во время выполнения расчета тока. "
                "Программа досрочно завершает свою работу. "
                f"\nОшибка: {e}"
            )
            raise ZeroDivisionError(
                "Обнаружено деление на ноль!"
                "Измените параметры сопротивления."
                f"\nОшибка: {e}"
            )

    def calc_fi(self):
        try:
            self.fi = math.degrees(
                math.atan(
                    (self.l_resistance - self.c_resistance) / self.r_resistance
                )
            )
        except ZeroDivisionError:
            logger.info(
                "Обнаружено деление на ноль во время вычисления арктангенса. "
                "Тангенс стремится к бесконечности, "
                "следовательно угол фи равен 90 градусов"
            )
            self.fi = 90

    def write_to_csv(self, csv_writer: writer):
        parameters = [self.frequency, self.resistance, self.current, self.fi]
        formatted_rows = []
        for parameter in parameters:
            formatted_rows.append(f"{parameter:.5g}")

        csv_writer.writerow(formatted_rows)
