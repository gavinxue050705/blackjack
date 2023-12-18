from blackjack import begin_game, exit, value
import pytest

def main():
    test_begin_game()
    test_exit()
    test_value()


def test_begin_game():
    with open('balance.txt', 'r') as file:
        score = int(file.read())

    assert begin_game() == score


def test_exit():
    with open('balance.txt', 'r') as file:
        score = int(file.read())
        
    with pytest.raises(SystemExit):
        assert exit(score)


def test_value():
    assert value([1,2,3,4,5]) == 15


if __name__ == '__main__':
    main()