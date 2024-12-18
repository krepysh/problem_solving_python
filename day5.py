import contextlib

top, bottom = open("day5.txt").read().split("\n\n")

rules = set()
for line in top.splitlines():
    a, b = line.split("|")
    rules.add((int(a), int(b)))


updates = [list(map(int, line.split(","))) for line in bottom.splitlines()]

res = 0


def weird_sort(update):
    run_one_more_time = True
    while run_one_more_time:
        run_one_more_time = False
        for rule in rules:
            before, after = rule
            with contextlib.suppress(ValueError):
                lower_index = update.index(before)
                higher_index = update.index(after)
                if lower_index < higher_index:
                    update[lower_index], update[higher_index] = update[higher_index], update[lower_index]
                    run_one_more_time = True
    return True



for update in updates:
    middle = (len(update) - 1) // 2 # 3 -> 1, 5 -> 2
    if weird_sort(update):
        res += update[middle]

print(res)