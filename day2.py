report = [[int(n) for n in line.split()] for line in open("day2.txt").readlines()]


def is_safe(levels):
    deltas = [a - b for a, b in zip(levels, levels[1:])]
    return all([- 1 >= d >= -3 for d in deltas]) or all([1 <= d <= 3 for d in deltas])


part_1 = 0
part_2 = 0
for levels in report:
    if is_safe(levels):
        part_1 = part_1 + 1
    for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i + 1:]):
            part_2 += 1
            break

print(part_1)
print(part_2)
