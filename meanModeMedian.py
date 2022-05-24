list_of_numbers = [0, 1, 2, 3, 4, 5, 6] # put in here the list of numbers

# function for mean
def mean(list_of_numbers):
    if len(list_of_numbers) == 0: # even
        return 0
    else:
        total = 0
        for num in list_of_numbers: # odd
            total += num
        mean = total / len(list_of_numbers)
        return mean

# function for mode
def mode(list_of_numbers):
    max = (0, 0)
    for num in list_of_numbers:
        frequency = list_of_numbers.count(num)
        if frequency > max[0]:
            max = (frequency, num)
    return max

# function for median
def median(list_of_numbers):
    list_of_numbers.sort()
    if len(list_of_numbers) % 2 != 0: # odd
        middle = int((len(list_of_numbers) - 1) / 2)
        return middle
    elif len(list_of_numbers) % 2 == 0: # even
        middle1 = int(len(list_of_numbers) / 2)
        middle2 = int(len(list_of_numbers) / 2) - 1
        return mean([list_of_numbers[middle1], list_of_numbers[middle2]])


mean = mean(list_of_numbers)
mode = mode(list_of_numbers)
median = median(list_of_numbers)

print("The mean of the list of numbers is ", mean)
print("The mode of the list of numbers is ", mode[1], " with a frequency of ", mode[0])
print("The median of the list of numbers is ", median)
