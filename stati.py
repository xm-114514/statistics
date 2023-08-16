import math

def statistics(data):
  if type(data) == str:
    data = data.strip('[]').split(',')
    data = [float(x) for x in data]
  sorted_data = sorted(data)
  length = len(sorted_data)
  half = length // 2
  box, Outlier = [], []
  count, box_count, Total, Range25per, max_count = 0,0,0,0,0
  mode_value = None
  Total = sum(sorted_data)
  Average = Total / length
  for number in range(length):
    if Average * 3 <= sorted_data[number]:
      Outlier.append(sorted_data[number])
  if length % 2 == 0: Range50per = (sorted_data[half - 1] + sorted_data[half]) / 2
  else: Range50per = sorted_data[half]
  if (half / 2).is_integer():
    for h in range(half):
      if h == (half // 2) - 1:count += sorted_data[h]
      elif h == half // 2:count += sorted_data[h]
    Range25per = count / 2
    for j in range(length):
      if j >= half + 1:
        box.append(sorted_data[j])
        box_count += 1
    Range75per = (box[box_count // 2] + box[(box_count // 2) - 1]) / 2
  else:
    for h in range(half):
      if h == half // 2:Range25per += sorted_data[h]
    for j in range(length):
      if j >= half:
        box.append(sorted_data[j])
        box_count += 1
    Range75per = box[box_count // 2]
  Scope = sorted_data[length - 1] - sorted_data[0]
  Quartilerange = Range75per - Range25per
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
    'median': Range50per,
    'IQR': Quartilerange,
    'range': Scope,
    'mode': mode_value,
    'outliers': Outlier,
    'Q1': Range25per,
    'Q2': Range50per,
    'Q3': Range75per,
    'Q': {
      'Q1': Range25per,
      'Q2': Range50per,
      'Q3': Range75per
    }
  }
  return result

def Difference(data):
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

def merge(x,y):
  difference1,Quartile1 = Difference(x),statistics(x)
  difference2,Quartile2 = Difference(y),statistics(y)
  result = {
    'data[1]': {
      'Quartile': Quartile1,
      'deviation': difference1,
    },
    'data[2]': {
      'Quartile': Quartile2,
      'deviation': difference2,
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
