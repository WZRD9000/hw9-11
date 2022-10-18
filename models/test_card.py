from card import Card, CardNumber, CardNotContainceError
from pytest import raises


class TestCardNumber:

    def setup(self):
        self.number = CardNumber(3)
        self.other = CardNumber(4)

    def test_str(self):
        assert str(self.number) == '3'
        self.number.is_cross_out = True
        assert str(self.number) == '-'

    def test_gt_lt(self):
        assert self.other > self.number
        assert self.number < self.other

    def test_eq(self):
        eq_number = CardNumber(3)
        assert eq_number == self.number
        assert self.other != self.number


class TestCards:

    def setup(self):
        self.numbers_list = [9, 43, 62, 74, 90, 2, 27, 75, 78, 82, 41, 56, 63, 76, 86]
        self.card = Card(self.numbers_list)

    def test_is_empty(self):
        assert not self.card.is_empty()
        for i in self.numbers_list:
            self.card.cross_out(i)
        assert self.card.is_empty()


    def test_str(self):
        result = """
        --------------------------
            9 43 62          74 90
         2    27    75 78    82
           41 56 63     76      86
        --------------------------
        """
        assert result == str(self.card)

    def test_contains(self):
        assert 9 in self.card
        assert 99 not in self.card
        assert CardNumber(9) in self.card
        assert CardNumber(99) not in self.card

    def test_cross_out(self):
        self.card.cross_out(43)
        result = """
        --------------------------
            9 - 62          74 90
         2    27    75 78    82
           41 56 63     76      86
        --------------------------
        """
        assert str(self.card) == result

        with raises(CardNotContainceError):
            self.card.cross_out(CardNumber(99))