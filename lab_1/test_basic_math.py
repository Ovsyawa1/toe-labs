import io
import math
import pytest
import basic_math as bm


class TestMySum:
    @pytest.mark.parametrize(
        "a, b, res",
        [
            (1, 2, 3),
            (4, 5, 9),
            (0, 0, 0),
            (0.35, 0.75, 1.1),
        ]
        )
    def test_my_sum_ok(self, monkeypatch, a, b, res):
        inputs = f"{a} {b}"

        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))

        assert math.isclose(bm.my_sum(), res)

    def test_my_sum_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("a 2\nexit\n"))
        bm.my_sum()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_sum_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = bm.my_sum()
        assert result is None


class TestMySub:
    @pytest.mark.parametrize(
        "a, b, res",
        [
            (10, 3, 7),
            (3, 10, -7),
            (5, 0, 5),
            (-5, -3, -2),
            (5.7, 2.3, 3.4),
            (0, 0, 0),
        ]
    )
    def test_my_sub_ok(self, monkeypatch, a, b, res):
        inputs = f"{a} {b}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(bm.my_sub(), res)

    def test_my_sub_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid 2\nexit\n"))
        bm.my_sub()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_sub_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = bm.my_sub()
        assert result is None


class TestMyMult:
    @pytest.mark.parametrize(
        "a, b, res",
        [
            (4, 5, 20),
            (5, 0, 0),
            (-4, 5, -20),
            (-4, -5, 20),
            (2.5, 4.0, 10.0),
            (1000, 1000, 1000000),
        ]
    )
    def test_my_mult_ok(self, monkeypatch, a, b, res):
        inputs = f"{a} {b}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(bm.my_mult(), res)

    def test_my_mult_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid 2\nexit\n"))
        bm.my_mult()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_mult_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = bm.my_mult()
        assert result is None


class TestMyDiv:
    @pytest.mark.parametrize(
        "a, b, res",
        [
            (10, 2, 5.0),
            (7, 2, 3.5),
            (-10, 2, -5.0),
            (0, 5, 0.0),
            (0.1, 0.01, 10.0),
        ]
    )
    def test_my_div_ok(self, monkeypatch, a, b, res):
        inputs = f"{a} {b}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(bm.my_div(), res)

    def test_my_div_zero_divisor(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("5 0\nexit\n"))
        result = bm.my_div()
        captured = capsys.readouterr()
        assert "Обнаружено деление на 0!" in captured.out
        assert result is None

    def test_my_div_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid 2\nexit\n"))
        bm.my_div()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_div_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = bm.my_div()
        assert result is None


class TestMyRaise:
    @pytest.mark.parametrize(
        "a, b, res",
        [
            (2, 3, 8),
            (5, 0, 1),
            (5, 1, 5),
            (2, -2, 0.25),
            (4, 0.5, 2.0),
            (2, 10, 1024),
        ]
    )
    def test_my_raise_ok(self, monkeypatch, a, b, res):
        inputs = f"{a} {b}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(bm.my_raise(), res)

    def test_my_raise_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid 2\nexit\n"))
        bm.my_raise()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_my_raise_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = bm.my_raise()
        assert result is None
