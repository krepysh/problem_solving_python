numbers = [int(n) for n in open("day1.txt").read().split()]

left = numbers[0::2]
right = numbers[1::2]
left.sort()
right.sort()

part1 = part2 = 0

for l, r in zip(left, right):
    part1 += abs(l - r)
    part2 += l * right.count(l)

print(part1, part2)
