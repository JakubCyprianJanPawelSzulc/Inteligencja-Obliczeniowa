import math


def f_act(x):
    return 1 / (1 + math.exp(-x))


def forward_pass(age, weight, height):
    hidden1 = -0.46122 * age + 0.97314 * weight - 0.39203 * height + 0.80109
    hidden1_po_aktywacji = f_act(hidden1)

    hidden2 = 0.78548 * age + 2.10584 * weight + -0.57847 * height + 0.43529
    hidden2_po_aktywacji = f_act(hidden2)

    output = -0.81546 * hidden1_po_aktywacji + \
        1.03775 * hidden2_po_aktywacji - 0.2368
    return output

print(forward_pass(23, 75, 176))
print(forward_pass(28, 120, 180))