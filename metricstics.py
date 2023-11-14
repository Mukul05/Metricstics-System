# This is the metricstics.py file

class Metricstics:
    def __init__(self, data):
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("All items in the data must be numeric (int or float).")
        self.data = data

    def iterative_sum(self, lst):
        total = 0
        for num in lst:
            total += num
        return total

    def iterative_len(self, lst):
        length = 0
        for _ in lst:
            length += 1
        return length

    def mean(self):
        if not self.data:
            raise ValueError("Mean is undefined for an empty dataset.")
        return self.iterative_sum(self.data) / self.iterative_len(self.data)

    def sort_data(self, lst):
        return sorted(lst)

    def median(self):
        if not self.data:
            raise ValueError("Median is undefined for an empty dataset.")
        sorted_data = self.sort_data(self.data)
        n = self.iterative_len(sorted_data)
        middle = n // 2
        if n % 2 == 1:
            return sorted_data[middle]
        else:
            return (sorted_data[middle - 1] + sorted_data[middle]) / 2

    def mode(self):
        if not self.data:
            raise ValueError("Mode is undefined for an empty dataset.")
        frequency = {}
        for num in self.data:
            frequency[num] = frequency.get(num, 0) + 1
        max_frequency = max(frequency.values())
        mode_value = [num for num, freq in frequency.items() if freq == max_frequency]
        return mode_value

    def min(self):
        if not self.data:
            raise ValueError("Min is undefined for an empty dataset.")
        return min(self.data)

    def max(self):
        if not self.data:
            raise ValueError("Max is undefined for an empty dataset.")
        return max(self.data)
