start_range = int(input("Enter the starting number of the range: "))
end_range = int(input("Enter the ending number of the range: "))

print("Special number in the range [", start_range, ",", end_range, "] are:")

for num in range(start_range, end_range + 1):
    temp = num
    num_digits = 0
    while temp > 0:
        num_digits += 1
        temp //= 10
    
    temp = num
    sum_of_powers = 0
    while temp > 0:
        digit = temp % 10
        sum_of_powers =+ digit ** num_digits
        temp //= 10

    if num == sum_of_powers:
        print(num)