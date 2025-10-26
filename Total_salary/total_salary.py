def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            total = 0
            count = 0
            for line in lines:
                parts = line.strip().split(',')
                if(len(parts) == 2):
                    try:
                        name, salary = parts
                        total += round(float(salary), 2)
                        count += 1

                    except ValueError:
                        print(f"Помилка: некоректний рядок '{line.strip()}'")
                        continue

            if count == 0:
                print('Файл порожній або не має коректних даних')
            average = round(float(total / count), 2)
            return total, average
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено")
    except ZeroDivisionError:
        return 0, 0

total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
