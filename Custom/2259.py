class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        index = -1

        for i in range(len(number) - 1):
          if number[i] == digit and number[i] < number[i + 1]:
            index = i
            break

        if index == -1: index = number.rindex(digit)
        return number[:index] + number[index + 1:]
