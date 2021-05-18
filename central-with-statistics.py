""" In this file, we will use native Python programming to calculate measures of central tendency. 
Using the data provided in the Self Check on p 110-111, question 4, calculate:
Count
Sum
Mean
Median 
Mode
"""
import statistics

values = [47,95,88,73,88,84]
valuesCount = len(values)
sumTotal = sum(values)
meanValue = statistics.mean(values)
medianValue = statistics.median(values)
modeValue = statistics.mode(values)

print(f'Values: {values}')
print(f'Count: {valuesCount}')
print(f'Sum: {sumTotal}')
print(f'Mean: {meanValue}') 
print(f'Median: {medianValue}') 
print(f'Mode: {modeValue}')