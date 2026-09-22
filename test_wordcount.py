from wordcount import count_words


def test_single_word():
    assert count_words("hello") == 1


def test_multiple_words():
    assert count_words("hello world") == 2


def test_multiple_spaces():
    assert count_words("hello   world") == 2
