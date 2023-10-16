numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sum_ = 0; index_of_none = 0
for i in range(len(numbers)):
    if numbers[i] is not None:
        sum_ += numbers[i]
    else:
        index_of_none = i
average_num = sum_ / len(numbers)
numbers[index_of_none] = average_num
print("Измененный список:", numbers)
