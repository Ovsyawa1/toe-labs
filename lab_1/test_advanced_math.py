import io
import math
import pytest
import advanced_math as am
from math import isclose, sin, cos, tan, radians, log


class TestMySin:
    @pytest.mark.parametrize(
        "a, res",
        [
            (30, sin(radians(30))),
            (0, 0),
            (-30, sin(radians(-30))),
            (360, sin(radians(360))),
            (45.5, sin(radians(45.5))),
            (90, 1),
            (180, 0),
        ]
    )
    def test_my_sin_ok(self, monkeypatch, a, res):
        inputs = f"{a}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(am.my_sin(), res, abs_tol=1e-15)

    def test_my_sin_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid\nexit"))
        am.my_sin()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_sin_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = am.my_sin()
        assert result is None


class TestMyCos:
    @pytest.mark.parametrize(
        "a, res",
        [
            (60, cos(radians(60))),
            (0, 1),
            (-60, cos(radians(-60))),
            (90, 0),
            (180, -1),
        ]
    )
    def test_my_cos_ok(self, monkeypatch, a, res):
        inputs = f"{a}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(am.my_cos(), res, abs_tol=1e-15)

    def test_my_cos_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid\nexit\n"))
        am.my_cos()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_cos_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = am.my_cos()
        assert result is None


class TestMyTan:
    @pytest.mark.parametrize(
        "a, res",
        [
            (45, tan(radians(45))),
            (0, 0),
            (-45, tan(radians(-45))),
            (180, tan(radians(180))),
        ]
    )
    def test_my_tan_ok(self, monkeypatch, a, res):
        inputs = f"{a}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(am.my_tan(), res)

    def test_my_tan_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid\nexit\n"))
        am.my_tan()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_tan_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = am.my_tan()
        assert result is None


class TestMyCtg:
    @pytest.mark.parametrize(
        "a, res",
        [
            (45, 1 / tan(radians(45))),
            (-45, 1 / tan(radians(-45))),
            (30, 1 / tan(radians(30))),
        ]
    )
    def test_my_ctg_ok(self, monkeypatch, a, res):
        inputs = f"{a}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(am.my_ctg(), res)

    def test_my_ctg_zero_tan(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("0\nexit\n"))
        result = am.my_ctg()
        captured = capsys.readouterr()
        assert "Обнаружено деление на 0!" in captured.out
        assert result is None

    def test_my_ctg_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid\nexit\n"))
        am.my_ctg()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_ctg_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = am.my_ctg()
        assert result is None


class TestMyFactorial:
    @pytest.mark.parametrize(
        "a, res",
        [
            (5, 120),
            (0, 1),
            (1, 1),
            (10, 3628800),
            (5.9, 120),  # int(5.9) = 5
        ]
    )
    def test_my_factorial_ok(self, monkeypatch, a, res):
        inputs = f"{a}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(am.my_factorial(), res)

    def test_my_factorial_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid\nexit\n"))
        am.my_factorial()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_factorial_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = am.my_factorial()
        assert result is None


class TestMyLn:
    @pytest.mark.parametrize(
        "a, res",
        [
            (2.718281828459045, 1.0),
            (1, 0),
            (10, log(10)),
        ]
    )
    def test_my_ln_ok(self, monkeypatch, a, res):
        inputs = f"{a}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(am.my_ln(), res)

    def test_my_ln_zero(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("0\nexit\n"))
        result = am.my_ln()
        captured = capsys.readouterr()
        assert "Логарифма с аргументов" in captured.out
        assert result is None

    def test_my_ln_negative(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("-5\nexit\n"))
        result = am.my_ln()
        captured = capsys.readouterr()
        assert "Логарифма с аргументов" in captured.out
        assert result is None

    def test_my_ln_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid\nexit\n"))
        am.my_ln()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_ln_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = am.my_ln()
        assert result is None


class TestMyGcdAndLcm:
    @pytest.mark.parametrize(
        "a, b, gcd_res, lcm_res",
        [
            (12, 18, 6, 36),
            (7, 11, 1, 77),
            (15, 15, 15, 15),
            (-12, 18, 6, 36),
        ]
    )
    def test_my_gcd_and_lcm_ok(self, monkeypatch, a, b, gcd_res, lcm_res):
        inputs = f"{a} {b}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = am.my_gcd_and_lcm()
        assert math.isclose(result[0], gcd_res)  # НОД
        assert math.isclose(result[1], lcm_res)  # НОК

    def test_my_gcd_and_lcm_float_values(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("12.5 18.7\nexit\n"))
        result = am.my_gcd_and_lcm()
        captured = capsys.readouterr()
        assert "Обнаружена дробная часть" in captured.out
        assert math.isclose(result[0], 6)  # НОД от int(12.5)=12 и int(18.7)=18
        assert math.isclose(result[1], 36)  # НОК

    def test_my_gcd_and_lcm_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid 2\nexit\n"))
        am.my_gcd_and_lcm()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_gcd_and_lcm_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = am.my_gcd_and_lcm()
        assert result is None


class TestConvertBase:
    @pytest.mark.parametrize(
        "from_base, number, to_base, res",
        [
            (10, "255", 16, "FF"),
            (2, "1010", 10, "10"),
            (10, "15", 2, "1111"),
            (16, "ABC", 10, "2748"),
        ]
    )
    def test_convert_base_ok(
        self,
        monkeypatch,
        from_base,
        number,
        to_base,
        res
    ):
        inputs = f"{from_base}\n{number}\n{to_base}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert am.convert_base() == res

    def test_convert_base_invalid_input(self, monkeypatch, capsys):
        inputs = "10\ninvalid\n16\n10\n255\n16"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        am.convert_base()
        captured = capsys.readouterr()
        assert "Произошла ошибка" in captured.out


class TestFindSquare:
    @pytest.mark.parametrize(
        "n, side, expected",
        [
            (3, 5.0, 3 * 25 / 4 * (1 / tan(radians(60)))),
            (4, 6.0, 4 * 36 / 4 * (1 / tan(radians(45)))),
            (6, 4.0, 6 * 16 / 4 * (1 / tan(radians(30)))),
        ]
    )
    def test_find_square_param(self, monkeypatch, n, side, expected):
        # Подготавливаем ввод
        inputs = f"{n}\n{side}\n"
        monkeypatch.setattr("sys.stdin", io.StringIO(inputs))

        result = am.find_square()
        assert math.isclose(result, expected, rel_tol=1e-9, abs_tol=1e-12)

    def test_find_square_invalid_input(self, monkeypatch, capsys):
        inputs = "invalid555\naaaa"
        monkeypatch.setattr("sys.stdin", io.StringIO(inputs))

        am.find_square()

        captured = capsys.readouterr()
        assert "Произошла ошибка" in captured.out


class TestSolveEquation:
    def test_solve_equation_two_roots(self, monkeypatch):
        inputs = "1 -5 6"  # x^2 - 5x + 6 = 0, корни: 2 и 3
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = am.solve_equation()

        roots = sorted(result)
        assert isclose(roots[0], 2.0)
        assert isclose(roots[1], 3.0)

    def test_solve_equation_one_root(self, monkeypatch):
        inputs = "1 -4 4"  # x^2 - 4x + 4 = 0, корень: 2
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = am.solve_equation()
        assert abs(result - 2.0) < 0.001

    def test_solve_equation_complex_roots(self, monkeypatch):
        # Уравнение x^2 + 1 = 0
        monkeypatch.setattr('sys.stdin', io.StringIO("1 0 1\n"))

        result = am.solve_equation()

        expected_roots = [1j, -1j]

        assert set(result) == set(expected_roots)

    def test_solve_equation_linear(self, monkeypatch):
        inputs = "1 2 -3"  # x^2 + 2x - 3 = 0, корни: 1 и -3
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = am.solve_equation()
        assert isinstance(result, list)
        assert len(result) == 2

    def test_solve_equation_invalid_input(self, monkeypatch, capsys):
        inputs = "invalid input\n1 -5 6"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        am.solve_equation()
        captured = capsys.readouterr()
        assert "Произошла ошибка" in captured.out

    def test_solve_equation_exit(self, monkeypatch):
        inputs = "exit"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = am.solve_equation()
        assert result is None
