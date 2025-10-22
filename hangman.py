import random

def draw_hangman(attempts):
    """Рисует виселицу"""
    hangman = [
        "  +---+\n  |   |\n      |\n      |\n      |\n      |",
        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |",
        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |",
        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |",
        "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |"
    ]
    print(hangman[attempts])


def play_hangman():
    """Игра "Виселица"."""

    words = ["виселица", "программа", "программирование", "компьютер", "алгоритм", "сервер", "нейросеть"]
    word = random.choice(words)
    guessed_letters = set()
    attempts = 0
    max_attempts = 6

    print("Добро пожаловать в игру 'Виселица'!\n Категория: IT")

    while attempts < max_attempts:
        # текущее слово
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print(display)

        draw_hangman(attempts)

        if "_" not in display:
            print("Поздравляю! Вы угадали слово:", word)
            break

        # ввод буквы
        guess = input("Введите букву: ").lower()

        # Проверка ввода
        if not guess.isalpha() or len(guess) != 1:
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже угадывали эту букву.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts += 1
            print("Неверно!")
            print(f"Осталось попыток: {max_attempts - attempts}")

    else:
        draw_hangman(attempts)  # Рисуем виселицу в последний раз
        print("Вы проиграли! Слово было:", word)

if __name__ == "__main__":
    play_hangman()
