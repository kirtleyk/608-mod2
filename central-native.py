""" In this file, we will use native Python programming to calculate measures of central tendency. 
Using the data provided in the Self Check on p 110-111, question 4, calculate:
Count
Sum
Mean
Median 
Mode
"""
values = [47,95,88,73,88,84]
valuesCount = len(values)
sumTotal = sum(values)
medianItem = 0  #list position for median calculation

medianList = sorted(values)  #sort list for median calculation
medianPosition = int(abs(valuesCount/2-1)) #find middle value index
medianItem = medianList[medianPosition]  #get middle value in list

if valuesCount % 2 == 0:  # even number get average of two middle values
    medianItem = (medianItem + medianList[medianPosition+1]) / 2

meanVal = sumTotal/valuesCount #average value

# Uses key function that selects max value based on the number with the highest count
mode = max(values, key=values.count)  

print(f'Values: {values}')
print(f'Count: {valuesCount}')
print(f'Sum: {sumTotal}')
print(f'Mean: {meanVal}')
print(f'Median: {medianItem}')
print(f'Mode: {mode}')