number_input = [4, 3, 2, 2, 5]
pattern = [[0 for _ in range(18)] for _ in range(14)]
height = 5
rows = 14
lines = 0


def figure(height, lines, nums):
    print(nums)
    for i in range(len(nums)):
        if i % 2 == 0:
            for j in range(nums[i]):
                pattern[rows-height-1][lines] = '/'
                height += 1
                lines += 1
            height -= 1
        elif i % 2 == 1:
            for j in range(nums[i]):
                pattern[rows-height-1][lines] = '\\'
                height -= 1
                lines += 1
            height += 1


figure(height, lines, number_input)
for line in pattern:
    for i, num in enumerate(line):
        if num == 0:
            line[i] = ' '
    print(*line)
