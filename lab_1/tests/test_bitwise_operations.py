import io
import math
import pytest
import lab_1.src.bitwise_operations as bo


class TestBitwiseAnd:
    @pytest.mark.parametrize(
        "a, b, res",
        [
            (5, 3, 1),  # 101 & 011 = 001
            (10, 6, 2),  # 1010 & 0110 = 0010
            (0, 0, 0),
            (15, 7, 7),  # 1111 & 0111 = 0111
            (255, 170, 170),  # 11111111 & 10101010 = 10101010
            (-1, 5, 5),  # -1 & 5 = 5 (в двоичном представлении)
        ]
    )
    def test_bitwise_and_ok(self, monkeypatch, a, b, res):
        inputs = f"{a} {b}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(bo.bitwise_and(), res)

    def test_bitwise_and_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid 2\nexit\n"))
        bo.bitwise_and()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_bitwise_and_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = bo.bitwise_and()
        assert result is None


class TestBitwiseOr:
    @pytest.mark.parametrize(
        "a, b, res",
        [
            (5, 3, 7),  # 101 | 011 = 111
            (10, 6, 14),  # 1010 | 0110 = 1110
            (0, 0, 0),
            (15, 0, 15),  # 1111 | 0000 = 1111
            (255, 0, 255),  # 11111111 | 00000000 = 11111111
            (170, 85, 255),  # 10101010 | 01010101 = 11111111
        ]
    )
    def test_bitwise_or_ok(self, monkeypatch, a, b, res):
        inputs = f"{a} {b}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(bo.bitwise_or(), res)

    def test_bitwise_or_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid 2\nexit\n"))
        bo.bitwise_or()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_bitwise_or_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = bo.bitwise_or()
        assert result is None


class TestBitwiseXor:
    @pytest.mark.parametrize(
        "a, b, res",
        [
            (5, 3, 6),  # 101 ^ 011 = 110
            (10, 6, 12),  # 1010 ^ 0110 = 1100
            (0, 0, 0),
            (15, 7, 8),  # 1111 ^ 0111 = 1000
            (255, 170, 85),  # 11111111 ^ 10101010 = 01010101
            (170, 85, 255),  # 10101010 ^ 01010101 = 11111111
        ]
    )
    def test_bitwise_xor_ok(self, monkeypatch, a, b, res):
        inputs = f"{a} {b}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(bo.bitwise_xor(), res)

    def test_bitwise_xor_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid 2\nexit\n"))
        bo.bitwise_xor()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_bitwise_xor_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = bo.bitwise_xor()
        assert result is None


class TestBitwiseNot:
    @pytest.mark.parametrize(
        "a, res",
        [
            (0, -1),  # ~0 = -1
            (5, -6),  # ~5 = -6
            (255, -256),  # ~255 = -256
            (-1, 0),  # ~(-1) = 0
            (127, -128),  # ~127 = -128
        ]
    )
    def test_bitwise_not_ok(self, monkeypatch, a, res):
        inputs = f"{a}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(bo.bitwise_not(), res)

    def test_bitwise_not_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid\nexit\n"))
        bo.bitwise_not()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_bitwise_not_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = bo.bitwise_not()
        assert result is None


class TestBitwiseToLeft:
    @pytest.mark.parametrize(
        "a, n, res",
        [
            (5, 1, 10),  # 5 << 1 = 10
            (3, 2, 12),  # 3 << 2 = 12
            (1, 8, 256),  # 1 << 8 = 256
            (0, 5, 0),  # 0 << 5 = 0
            (15, 3, 120),  # 15 << 3 = 120
        ]
    )
    def test_bitwise_to_left_ok(self, monkeypatch, a, n, res):
        inputs = f"{a} {n}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(bo.bitwise_to_left(), res)

    def test_bitwise_to_left_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid 2\nexit\n"))
        bo.bitwise_to_left()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_bitwise_to_left_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = bo.bitwise_to_left()
        assert result is None


class TestBitwiseToRight:
    @pytest.mark.parametrize(
        "a, n, res",
        [
            (10, 1, 5),  # 10 >> 1 = 5
            (12, 2, 3),  # 12 >> 2 = 3
            (256, 8, 1),  # 256 >> 8 = 1
            (0, 5, 0),  # 0 >> 5 = 0
            (120, 3, 15),  # 120 >> 3 = 15
        ]
    )
    def test_bitwise_to_right_ok(self, monkeypatch, a, n, res):
        inputs = f"{a} {n}"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        assert math.isclose(bo.bitwise_to_right(), res)

    def test_bitwise_to_right_stdout(self, monkeypatch, capsys):
        monkeypatch.setattr('sys.stdin', io.StringIO("invalid 2\nexit\n"))
        bo.bitwise_to_right()
        captured = capsys.readouterr()
        assert "Ввод неверный. Ошибка:" in captured.out

    def test_bitwise_to_right_exit(self, monkeypatch):
        monkeypatch.setattr('sys.stdin', io.StringIO("exit\n"))
        result = bo.bitwise_to_right()
        assert result is None


# Тесты на граничные случаи
class TestBitwiseEdgeCases:
    def test_large_numbers_and(self, monkeypatch):
        inputs = "2147483647 1"  # Максимальное 32-битное число
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = bo.bitwise_and()
        assert math.isclose(result, 1)

    def test_large_numbers_or(self, monkeypatch):
        inputs = "2147483647 1"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = bo.bitwise_or()
        assert math.isclose(result, 2147483647)

    def test_large_shift_left(self, monkeypatch):
        inputs = "1 31"  # Сдвиг на 31 позицию влево
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = bo.bitwise_to_left()
        assert math.isclose(result, 2**31)

    def test_large_shift_right(self, monkeypatch):
        inputs = f"{2**31} 31"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = bo.bitwise_to_right()
        assert math.isclose(result, 1)

    def test_negative_numbers_and(self, monkeypatch):
        inputs = "-1 5"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = bo.bitwise_and()
        assert math.isclose(result, 5)

    def test_negative_numbers_or(self, monkeypatch):
        inputs = "-1 0"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = bo.bitwise_or()
        assert math.isclose(result, -1)

    def test_float_conversion(self, monkeypatch):
        # Тестируем что float числа преобразуются в int
        inputs = "5.7 3.2"
        monkeypatch.setattr('sys.stdin', io.StringIO(inputs))
        result = bo.bitwise_and()
        assert math.isclose(result, 1)  # int(5.7) & int(3.2) = 5 & 3 = 1
