# calculating average temprature and number of days which were above the average date

n = int(input("Enter the number of days :\t"))
arr= []
sumis =0
def average(array,n):
    count = 0
    for i in range(n):
        val = float(input(f"Enter the temperature of day {i+1}:\t"))
        array.append(val)
    sumis = sum(array)
    avg = sumis/n
    print("The average temperature of days is :\t",avg)
    for j in array:
        if(j > avg): count += 1
    print("the number of days that were above the average date is :",count)

average(arr,n)


