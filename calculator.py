import math


class Leksema:
    def __init__(self, type, value=0):
        self.type = type
        self.value = value


class Calculator:
    def __init__(self):
        self.Pi = math.pi

    def Sin(self, x):
        return round(math.sin(x) * 10000000) / 10000000

    def Cos(self, x):
        return round(math.cos(x) * 10000000) / 10000000

    def Ctg(self, x):
        a = self.Cos(x)
        b = self.Sin(x)
        return a / b

    def Tan(self, x):
        a = self.Cos(x)
        b = self.Sin(x)
        return b / a

    def Maths(self, Stack_n, Stack_o, item):
        if not Stack_n:
            return False
        a = Stack_n[-1].value
        Stack_n.pop()

        if not Stack_o:
            return False

        op_type = Stack_o[-1].type

        if op_type == '+':
            if not Stack_n:
                return False
            b = Stack_n[-1].value
            Stack_n.pop()
            c = a + b
            item.type = '0'
            item.value = c
            Stack_n.append(item)
            Stack_o.pop()

        elif op_type == '-':
            if not Stack_n:
                return False
            b = Stack_n[-1].value
            Stack_n.pop()
            c = b - a
            item.type = '0'
            item.value = c
            Stack_n.append(item)
            Stack_o.pop()

        elif op_type == '^':
            if not Stack_n:
                return False
            b = Stack_n[-1].value
            Stack_n.pop()
            c = math.pow(b, a)
            item.type = '0'
            item.value = c
            Stack_n.append(item)
            Stack_o.pop()

        elif op_type == '*':
            if not Stack_n:
                return False
            b = Stack_n[-1].value
            Stack_n.pop()
            c = a * b
            item.type = '0'
            item.value = c
            Stack_n.append(item)
            Stack_o.pop()

        elif op_type == '/':
            if not Stack_n:
                return False
            b = Stack_n[-1].value
            if a == 0:
                print("\nНа 0 делить нельзя!\n")
                return False
            else:
                Stack_n.pop()
                c = b / a
                item.type = '0'
                item.value = c
                Stack_n.append(item)
                Stack_o.pop()

        elif op_type == 's':
            c = self.Sin(a)
            item.type = '0'
            item.value = c
            Stack_n.append(item)
            Stack_o.pop()

        elif op_type == 'c':
            c = self.Cos(a)
            item.type = '0'
            item.value = c
            Stack_n.append(item)
            Stack_o.pop()

        elif op_type == 't':
            if self.Cos(a) == 0:
                print("\nНеверный аргумент для тангенса!\n")
                return False
            else:
                c = self.Tan(a)
                item.type = '0'
                item.value = c
                Stack_n.append(item)
                Stack_o.pop()

        elif op_type == 'g':
            if self.Sin(a) == 0:
                print("\nНеверный аргумент для котангенса!\n")
                return False
            else:
                c = self.Ctg(a)
                item.type = '0'
                item.value = c
                Stack_n.append(item)
                Stack_o.pop()

        elif op_type == 'e':
            c = math.exp(a)
            item.type = '0'
            item.value = c
            Stack_n.append(item)
            Stack_o.pop()

        else:
            print("\nОшибка!\n")
            return False

        return True

    def getRang(self, Ch):
        if Ch in ['s', 'c', 't', 'g', 'e']:
            return 4
        if Ch == '^':
            return 3
        if Ch in ['+', '-']:
            return 1
        if Ch in ['*', '/']:
            return 2
        return 0


def main():
    calc = Calculator()

    while True:
        print("\n")
        print("   Привет! Это программа - калькулятор!")
        print("   Для использования числа Пи введите 'p', для использования числа Е введите 'exp(1)'")
        print("   Пример выражения: 3+4-tan(p/4)+exp(2)")
        print("   Введите выражение: ", end="")

        try:
            str_input = input().strip()
        except EOFError:
            break

        if not str_input:
            continue

        Stack_n = []
        Stack_o = []
        flag = True
        i = 0

        while i < len(str_input):
            Ch = str_input[i]

            if Ch == ' ':
                i += 1
                continue

            if Ch in ['s', 'c', 't', 'e']:
                if i + 2 < len(str_input):
                    foo = str_input[i:i + 3]
                    if foo == 'sin':
                        item = Leksema('s', 0)
                        Stack_o.append(item)
                        i += 3
                        continue
                    elif foo == 'cos':
                        item = Leksema('c', 0)
                        Stack_o.append(item)
                        i += 3
                        continue
                    elif foo == 'tan':
                        item = Leksema('t', 0)
                        Stack_o.append(item)
                        i += 3
                        continue
                    elif foo == 'ctg':
                        item = Leksema('g', 0)
                        Stack_o.append(item)
                        i += 3
                        continue
                    elif foo == 'exp':
                        item = Leksema('e', 0)
                        Stack_o.append(item)
                        i += 3
                        continue

            if Ch == 'p':
                item = Leksema('0', calc.Pi)
                Stack_n.append(item)
                flag = False
                i += 1
                continue

            if Ch.isdigit() or (Ch == '-' and flag):
                j = i
                if Ch == '-':
                    j += 1
                while j < len(str_input) and (str_input[j].isdigit() or str_input[j] == '.'):
                    j += 1
                try:
                    value = float(str_input[i:j])
                    item = Leksema('0', value)
                    Stack_n.append(item)
                    flag = False
                    i = j
                    continue
                except ValueError:
                    print("\nНеверно введено выражение!\n")
                    input("Нажмите Enter для продолжения...")
                    return

            if Ch in ['+', '-', '*', '/', '^'] and (Ch != '-' or not flag):
                if not Stack_o:
                    item = Leksema(Ch, 0)
                    Stack_o.append(item)
                    i += 1
                    continue

                if Stack_o and calc.getRang(Ch) > calc.getRang(Stack_o[-1].type):
                    item = Leksema(Ch, 0)
                    Stack_o.append(item)
                    i += 1
                    continue

                if Stack_o and calc.getRang(Ch) <= calc.getRang(Stack_o[-1].type):
                    item = Leksema('0', 0)
                    if not calc.Maths(Stack_n, Stack_o, item):
                        input("Нажмите Enter для продолжения...")
                        return
                    continue

            if Ch == '(':
                item = Leksema('(', 0)
                Stack_o.append(item)
                i += 1
                continue

            if Ch == ')':
                while Stack_o and Stack_o[-1].type != '(':
                    item = Leksema('0', 0)
                    if not calc.Maths(Stack_n, Stack_o, item):
                        input("Нажмите Enter для продолжения...")
                        return
                if Stack_o and Stack_o[-1].type == '(':
                    Stack_o.pop()
                i += 1
                continue

            else:
                print("\nНеверно введено выражение!\n")
                input("Нажмите Enter для продолжения...")
                return

            i += 1

        while Stack_o:
            item = Leksema('0', 0)
            if not calc.Maths(Stack_n, Stack_o, item):
                input("Нажмите Enter для продолжения...")
                return

        if Stack_n:
            print(f"   Ответ: {Stack_n[-1].value}")
        else:
            print("   Ошибка вычисления")

        input("Нажмите Enter для продолжения...")


if __name__ == "__main__":
    main()