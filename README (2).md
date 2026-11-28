# Фрактал Мандельброта 
В цьому репозиторії розміщений Python-файл який створює схематичне зображення фракталу Мандельброта
---
## А яка ж його функціональність?
- можливість показувати на парах під вичення теми фракталів
    - на основах комп'ютерної графіки
    - алгоритмізації
    *я вважаю це універсальний код для вивчення у сфері ІТ для початківців*
- огляд користувацьких фунцій у коді
- можливість розглянути приклад фракталу, не маючи інтернету
## 
1. Клонуйте репозиторій:
``````bash
git clone https://github.com/krisllixs/mandelbrot-fractal-project.git
``````
2. Перейдіть у папку проєкту:
``````bash
cd mandelbrot-fractal-project
``````
3. Запустіть програму:
``````bash
python script.py
``````
### ***Приклад коду***
``````python
def escape_time(c, max_iter=50):
    """Скільки кроків точка c 'тримається' в множині Мандельброта."""
    z = 0
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return i
    return max_iter


def pick_char(i, max_iter=50):
    """Перетворює кількість ітерацій на символ: чим далі, тим 'щільніше'."""
    if i == max_iter:
        return "█"
    palette = " .:-=+*#%@"
    return palette[i * len(palette) // max_iter]


def render(width=80, height=32):
    """Малює фрактал рядок за рядком."""
    rows = []
    for y in range(height):
        row = ""
        for x in range(width):
            c = complex(-2.2 + 3.2 * x / width, -1.2 + 2.4 * y / height)
            row += pick_char(escape_time(c))
        rows.append(row)
    return "\n".join(rows)


print(render())
#author Khrystyna Prykhodko
``````
![Зображення виконаного коду] (fractal.png)
### Чи було виконане завдання автором?
- [x] Виконане завдання
- [ ] Невиконане завдання
- [ ] Ще одне завдання
## Автор
Приходько Христина КН-21
## Посилання на lокументування функцій
[DOCUMENTION.md] (https://github.com/krisllixs/mandelbrot-fractal-project/blob/main/DOCUMENTION.md)
