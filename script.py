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