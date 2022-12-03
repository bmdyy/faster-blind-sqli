C = 77 # 'M' = 77
answer = 0

print("Is C & 1 true?")
if C & 1:
    print("Yes => answer |= 1")
    answer |= 1
else:
    print("No")

print("Is C & 2 true?")
if C & 2:
    print("Yes => answer |= 2")
    answer |= 2
else:
    print("No")

print("Is C & 4 true?")
if C & 4:
    print("Yes => answer |= 4")
    answer |= 4
else:
    print("No")

print("Is C & 8 true?")
if C & 8:
    print("Yes => answer |= 8")
    answer |= 8
else:
    print("No")

print("Is C & 16 true?")
if C & 16:
    print("Yes => answer |= 16")
    answer |= 16
else:
    print("No")

print("Is C & 32 true?")
if C & 32:
    print("Yes => answer |= 32")
    answer |= 32
else:
    print("No")

print("Is C & 64 true?")
if C & 64:
    print("Yes => answer |= 64")
    answer |= 64
else:
    print("No")

print("Answer is %d" % answer)