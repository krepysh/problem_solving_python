t = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

total = 0
do = True
for start in range(len(t)):
    for shift in range(15):
        cmd = t[start: start + shift]
        if cmd == "do()":
            do = True
        if cmd == "don't()":
            do = False
        if do and cmd.startswith("mul(") and cmd.endswith(")"):
            args = cmd[4:-1]
            try:
                a, b = args.split(",")
                a = int(a)
                b = int(b)
                total += a * b
                break
            except:
                pass

print(total)
