# statistics
```main.py```

```py
import stati

data1 = [1, 2, 3, 4, 5]
data2 = [6, 7, 8, 9, 10]
result = compare(data1, data2)
print(result)

start_num = 1
end_num = 50

prime_result = prime_numbers(start_num, end_num)

print("素数:", prime_result['primes'])
print("開始数:", prime_result['start_num'])
print("終了数:", prime_result['end_num'])

```


```stati.py```

```py
import math

def calculate_statistics(data):
  if type(data) == str:
    data = data.strip('[]').split(',')
    data = [float(x) for x in data]
  sorted_data = sorted(data)
  length = len(sorted_data)
  half = length // 2
  box, Outlier = [], []
  count, box_count, Total, R25, max_count = 0,0,0,0,0
  mode_value = None
  Total = sum(sorted_data)
  Average = Total / length
  for number in range(length):
    if Average * 3 <= sorted_data[number]:
      Outlier.append(sorted_data[number])
  if length % 2 == 0: R50 = (sorted_data[half - 1] + sorted_data[half]) / 2
  else: R50 = sorted_data[half]
  if (half / 2).is_integer():
    for h in range(half):
      if h == (half // 2) - 1:count += sorted_data[h]
      elif h == half // 2:count += sorted_data[h]
    R25 = count / 2
    for j in range(length):
      if j >= half + 1:
        box.append(sorted_data[j])
        box_count += 1
    R75 = (box[box_count // 2] + box[(box_count // 2) - 1]) / 2
  else:
    for h in range(half):
      if h == half // 2:R25 += sorted_data[h]
    for j in range(length):
      if j >= half:
        box.append(sorted_data[j])
        box_count += 1
    R75 = box[box_count // 2]
  Scope = sorted_data[length - 1] - sorted_data[0]
  Quartilerange = R75 - R25
  Min_value, Max_value = sorted_data[0], sorted_data[length - 1]
  for d in sorted_data:
    data_count = sorted_data.count(d)
    if data_count > max_count:max_count,mode_value = data_count,d
  result = {
    'len': length,
    'total': Total,
    'average': Average,
    'max': Max_value,
    'min': Min_value,
    'median': R50,
    'IQR': Quartilerange,
    'range': Scope,
    'mode': mode_value,
    'outliers': Outlier,
    'Q1': R25,
    'Q2': R50,
    'Q3': R75,
    'Q': {
      'Q1': R25,
      'Q2': R50,
      'Q3': R75
    }
  }
  return result

def calculate_deviation(data):
  if type(data) == str:
    data = data.strip('[]').split(',')
    data = [float(x) for x in data]
  sorted_data = sorted(data)
  length = len(sorted_data)
  total = sum(sorted_data)
  average = total / length
  deviation_list = [value - average for value in sorted_data]
  deviation_squared_list = [deviation ** 2 for deviation in deviation_list]
  deviation_total = sum(deviation_squared_list)
  variance = deviation_total / length
  standard_deviation = math.sqrt(variance)
  result = {
    'sorted_data': sorted_data,
    'total': total,
    'len': length,
    'average': average,
    'variance': variance,
    'deviation_list': deviation_list,
    'standard_deviation': standard_deviation,
    'deviation_squared_list': deviation_squared_list
  }
  return result

def compare(a,b):
  result = {
    'a':{
      'statistics': calculate_statistics(a),
      'deviation': calculate_deviation(a)
    },
    'b':{
      'statistics': calculate_statistics(b),
      'deviation': calculate_deviation(b)
    }
  }
  return result

def prime_numbers(start, end):
  numbers = range(start, end + 1)
  def is_prime(num):
    if num <= 1: return False
    for x in range(2, int(math.sqrt(num)) + 1):
      if (num % x) == 0: return False
    return True
  primes = list(filter(is_prime, numbers))
  result = {
    'primes': primes,
    'start_num': start,
    'end_num': end,
  }
  return result
```
