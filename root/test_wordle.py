from byu_pytest_utils import dialog, max_score, this_folder, test_files


@max_score(10)
@dialog(
    test_files / "one_guess_win.txt",
    this_folder / "wordle.py",
    test_files / "crane.txt",
    1
)
def test_wordle_one_try_one_guess_win(): ...


@max_score(10)
@dialog(
    test_files / "one_guess_win.txt",
    this_folder / "wordle.py",
    test_files / "crane.txt",
    5
)
def test_wordle_5_tries_one_guess_win(): ...


@max_score(10)
@dialog(
    test_files / "two_tries_two_guesses_win.txt",
    this_folder / "wordle.py",
    test_files / "crane.txt",
    2
)
def test_wordle_two_tries_two_guesses_win(): ...


@max_score(10)
@dialog(
    test_files / "two_tries_two_guesses_win.txt",
    this_folder / "wordle.py",
    test_files / "crane.txt",
    2
)
def test_wordle_two_tries_two_guesses_win(): ...


@max_score(10)
@dialog(
    test_files / "three_tries_three_guesses_loss.txt",
    this_folder / "wordle.py",
    test_files / "crane.txt",
    3
)
def test_wordle_three_tries_three_guesses_loss(): ...


@max_score(10)
@dialog(
    test_files / "correct_letters_but_wrong_spots.txt",
    this_folder / "wordle.py",
    test_files / "crane.txt",
    1
)
def test_wordle_correct_letters_but_wrong_spots(): ...


@max_score(10)
@dialog(
    test_files / "duplicate_letters_one_correct_one_close.txt",
    this_folder / "wordle.py",
    test_files / "slope.txt",
    1
)
def test_wordle_duplicate_letters_one_correct_one_close(): ...


@max_score(10)
@dialog(
    test_files / "duplicate_letters_one_correct_one_wrong.txt",
    this_folder / "wordle.py",
    test_files / "tooth.txt",
    1
)
def test_wordle_correct_word_has_doubles(): ...


@max_score(10)
@dialog(
    test_files / "numbers_and_symbols.txt",
    this_folder / "wordle.py",
    test_files / "crane.txt",
    2
)
def test_wordle_numbers_and_symbols(): ...


@max_score(10)
@dialog(
    test_files / "six_guesses_loss.txt",
    this_folder / "wordle.py",
    test_files / "abcde.txt",
    5
)
def test_wordle_six_guesses_loss(): ...


@max_score(10)
@dialog(
    test_files / "real_game.txt",
    this_folder / "wordle.py",
    test_files / "upset.txt",
    6
)
def test_wordle_real_game(): ...
