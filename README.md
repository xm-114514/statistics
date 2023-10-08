# statistics
```main.py```

```py
import stati

stats = Statistics()

data1 = [1, 2, 3, 4, 5]
data2 = [6, 7, 8, 9, 10]

result = stats.compare_data(data1, data2)
print(result)

start_num = 1
end_num = 50

prime_result = stats.find_primes(start_num, end_num)

print("素数:", prime_result['primes'])
print("開始数:", prime_result['start_num'])
print("終了数:", prime_result['end_num'])

```


```stati.py```

```py
import math

class Statistics:
  def __init__(self, data=None):
    self.data = data

  def set_data(self, data):
    self.data = data

  def calculate_statistics(self):
    if isinstance(self.data, str):
      self.data = self.data.strip('[]').split(',')
      self.data = [float(x) for x in self.data]
    sorted_data = sorted(self.data)
    length = len(sorted_data)
    half = length // 2
    box, outliers = [], []
    count, box_count, total, range_25per, max_count = 0, 0, 0, 0, 0
    mode_value = None
    total = sum(sorted_data)
    average = total / length
    for number in range(length):
      if average * 3 <= sorted_data[number]:
        outliers.append(sorted_data[number])
    if length % 2 == 0:
      range_50per = (sorted_data[half - 1] + sorted_data[half]) / 2
    else:
      range_50per = sorted_data[half]
    if (half / 2).is_integer():
      for h in range(half):
        if h == (half // 2) - 1:
          count += sorted_data[h]
        elif h == half // 2:
          count += sorted_data[h]
      range_25per = count / 2
      for j in range(length):
        if j >= half + 1:
          box.append(sorted_data[j])
          box_count += 1
      range_75per = (box[box_count // 2] + box[(box_count // 2) - 1]) / 2
    else:
      for h in range(half):
        if h == half // 2:
          range_25per += sorted_data[h]
      for j in range(length):
        if j >= half:
          box.append(sorted_data[j])
          box_count += 1
      range_75per = box[box_count // 2]
    scope = sorted_data[length - 1] - sorted_data[0]
    quartile_range = range_75per - range_25per
    min_value, max_value = sorted_data[0], sorted_data[length - 1]
    for d in sorted_data:
      data_count = sorted_data.count(d)
      if data_count > max_count:
        max_count, mode_value = data_count, d
    result = {
      'length': length,
      'total': total,
      'average': average,
      'max': max_value,
      'min': min_value,
      'median': range_50per,
      'IQR': quartile_range,
      'range': scope,
      'mode': mode_value,
      'outliers': outliers,
      'Q1': range_25per,
      'Q2': range_50per,
      'Q3': range_75per,
      'Q': {'Q1': range_25per, 'Q2': range_50per, 'Q3': range_75per}
    }
    return result

  def calculate_deviation(self):
    if isinstance(self.data, str):
      self.data = self.data.strip('[]').split(',')
      self.data = [float(x) for x in self.data]
    sorted_data = sorted(self.data)
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
      'length': length,
      'average': average,
      'variance': variance,
      'deviation_list': deviation_list,
      'standard_deviation': standard_deviation,
      'deviation_squared_list': deviation_squared_list
    }
    return result

  @staticmethod
  def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
      if num <= 1:
        continue
      is_prime = True
      for x in range(2, int(math.sqrt(num)) + 1):
        if (num % x) == 0:
          is_prime = False
          break
      if is_prime:
        primes.append(num)
    result = {
      'primes': primes,
      'start_num': start,
      'end_num': end,
    }
    return result

  def compare_data(self, data1, data2):
    self.set_data(data1)
    quartile1 = self.calculate_statistics()
    deviation_result1 = self.calculate_deviation()
    self.set_data(data2)
    quartile2 = self.calculate_statistics()
    deviation_result2 = self.calculate_deviation()
    result = {
      'data1': {
        'statistics': quartile1,
        'deviation': deviation_result1,
      },
      'data2': {
        'statistics': quartile2,
        'deviation': deviation_result2,
      }
    }
    return result
```
