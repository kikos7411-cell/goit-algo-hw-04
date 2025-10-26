def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()


            cats_info = []

            for line in lines:

                part = line.strip().split(',')

                if len(part) == 3:
                    id, name, age = part
                    person = {f"id: {id}, name: {name}, age: {age}"}
                    # try:
                    if age <= '0':
                        print(f"Помилка: некоректний рядок '{line.strip()}'")
                        continue

                    cats_info.append(person)

                else:
                    print(f"Помилка: некоректний рядок '{line.strip()}'")
                    continue
                try:
                    int(age)

                except ValueError:
                    print(f"Помилка: некоректний рядок '{line.strip()}'")
                    continue


            return cats_info


    except FileNotFoundError:
            print("Помилка: файл не знайдено.")
            return 0, 0


cats_info = get_cats_info("cats_id.txt")
print(f"{cats_info}")
