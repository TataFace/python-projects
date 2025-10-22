class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def phone_num_form(self):
        if self.is_valid_phone_number():
            if self.phone_number.startswith("+"):
                country_code = self.phone_number[1:len(self.phone_number) - 10]
                num = self.phone_number[len(self.phone_number) - 10:]
                return f"+{country_code} {num[:3]}-{num[3:6]}-{num[6:]}"
            elif self.phone_number.startswith("8"):
                num = self.phone_number[1:]
                return f"+7 {num[:3]}-{num[3:6]}-{num[6:]}"
        return "incorrect number"

    def is_valid_phone_number(self):
        if self.phone_number.startswith("+"):
            if len(self.phone_number) < 11 or len(self.phone_number) > 13:
                return False
        elif self.phone_number.startswith("8"):
            if len(self.phone_number) != 11:
                return False
        else:
            return False
        return True


def main():
    print("=== Форматирование телефонных номеров ===")
    """print("Примеры номеров:")
    print("  +79175655655 → +7 917-565-5655")
    print("  89175655655  → +7 917-565-5655")
    print("  +104289652211 → +104 289-652-211")
    print()"""

    while True:
        print("\n" + "=" * 40)
        phone_input = input("Введите номер телефона (или 'exit' для выхода): ").strip()

        if phone_input.lower() == 'exit':
            print("Выход из программы...")
            break

        if not phone_input:
            print("Ошибка: введите номер телефона")
            continue

        phone = PhoneNumber(phone_input)
        result = phone.phone_num_form()

        print(f"Результат: {result}")

        # Примеры при ошибке ввода
        if result == "incorrect number":
            print("\nПодсказка:")
            print("  - Номер должен начинаться с '+' или '8'")
            print("  - Для номеров с '+': длина 11-13 символов")
            print("  - Для номеров с '8': длина 11 символов")
            print("  Пример: +79175655655 или 89175655655")


if __name__ == "__main__":
    main()