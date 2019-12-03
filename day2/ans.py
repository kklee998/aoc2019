opcode_input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 6, 19, 1, 9, 19, 23, 2, 23, 10, 27, 1, 27, 5, 31, 1, 31, 6, 35, 1, 6, 35, 39, 2, 39, 13, 43, 1, 9, 43, 47, 2, 9, 47, 51, 1, 51, 6, 55, 2, 55, 10, 59, 1, 59, 5, 63, 2, 10, 63, 67, 2, 9, 67, 71, 1, 71, 5, 75, 2, 10, 75, 79, 1, 79, 6, 83, 2, 10, 83, 87, 1, 5, 87, 91, 2, 9, 91, 95, 1, 95, 5, 99, 1, 99, 2, 103, 1, 103, 13, 0, 99, 2, 14, 0, 0
                ]

opcode_input[1] = 12
opcode_input[2] = 2


def opcode_one(a, b):
    return opcode_input[a] + opcode_input[b]


def opcode_two(a, b):
    return opcode_input[a] * opcode_input[b]


for k, v in enumerate(opcode_input):
    if k % 4 == 0:
        if v == 99:
            break
        a, b, c = opcode_input[k + 1], opcode_input[k + 2], opcode_input[k + 3]
        if v == 1:
            replace = opcode_one(a, b)
            opcode_input[c] = replace
        if v == 2:
            replace = opcode_two(a, b)
            opcode_input[c] = replace

print(opcode_input)
print(opcode_input[0])


"""
Part Two
Found the answer, but not sure about coding the solution yet.
Answer found by guessing from the given number: 19690720
That is the date of Apollo 11. Can start guessing by setting noun and verb to 69,69
This gives us: 19690710
by adjusting the verb (which increases the output by 1 every time you increase) to 79,
you'll get 19690720

TODO: two loops, outer loop for noun and inner loop for verb.

LOOP Steps:
0
[0 .. 99]

1
[0 .. 99]

2
[0 .. 99]
"""
