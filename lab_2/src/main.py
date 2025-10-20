import csv
import json
from pathlib import Path

from circuit_class import CircuitCalculator
from logger_setuper import setup_log


def load_options(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def all_calc(csv_path, logger, lower_freq_limit, upper_freq_limit, calculator):
    try:
        with open(csv_path, 'w', newline='') as csv_file:
            logger.info("Файл найден. Создание объекта типа 'writer'")
            csv_writer = csv.writer(
                csv_file,
                delimiter=' ',
                quotechar='|',
                quoting=csv.QUOTE_MINIMAL
            )
            logger.info("Объект 'writer' успешно создан. Начало расчета\n")
            for curr_freq in range(lower_freq_limit, upper_freq_limit):
                logger.info(f"Рассматриваемая частота: {curr_freq}")
                calculator.frequency = curr_freq

                # Расчет индуктивных и емкостных сопротивлений
                calculator.calc_react_res()
                logger.info(
                    "Получившиеся сопротивления: "
                    f"x_l = {calculator.l_resistance:.4f}; "
                    f"x_c = {calculator.c_resistance:.4f}"
                )

                # Вычисление суммарного сопротивления
                calculator.calc_resistance()
                logger.info(
                    f"Суммарное сопротивление: "
                    f"Z = {calculator.resistance:.4f}"
                )

                # Вычисление тока
                calculator.calc_current()
                logger.info(
                    "Рассчитанный ток: "
                    f"I = {calculator.current:.4f}"
                )

                # Расчет угла фи
                calculator.calc_fi()
                logger.info(
                    "Рассчитанный fi: "
                    f"fi = {calculator.fi:.4f}"
                )

                # Запись в csv-файл
                calculator.write_to_csv(csv_writer)
                logger.info("Результаты расчета записаны в csv-файл\n")
            logger.info("Программа успешно отработала!")

    except FileNotFoundError as e:
        logger.error("Файл или папка для csv-файла не были найдены!"
                     f"Программа досрочно завершает свою работу. Ошибка {e}")

        raise FileNotFoundError(
            "Файл или папка для csv-файла не были найдены!"
        )


def main():
    Path("lab_2", "output").mkdir(parents=True, exist_ok=True)
    logger = setup_log()
    logger.info("Инициализация переменных")
    file_path = Path("lab_2", "options.json")
    csv_path = Path("lab_2", "output", "output.csv")
    parameters = load_options(file_path)
    calculator = CircuitCalculator(
        parameters["R"],
        parameters["L"],
        parameters["C"],
        parameters["U"]
    )
    lower_freq_limit = parameters["frequencies"]["lower_limit"]
    upper_freq_limit = parameters["frequencies"]["upper_limit"]

    all_calc(
        csv_path,
        logger,
        lower_freq_limit,
        upper_freq_limit,
        calculator
    )


if __name__ == "__main__":
    main()
