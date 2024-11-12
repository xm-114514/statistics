import math

def Stats(data):
  if type(data) == str:
    data = data.strip('[]').split(',')
    data = [float(x) for x in data]
  sorted_data = sorted(data)
  length = len(sorted_data)
  half = length // 2
  box, Outlier = [], []
  count, box_count, Total, R25, max_count = 0, 0, 0, 0, 0
  mode_value = None
  Total = sum(sorted_data)
  Average = Total / length
  if length % 2 == 0: R50 = (sorted_data[half - 1] + sorted_data[half]) / 2
  else: R50 = sorted_data[half]
  if (half / 2).is_integer():
    for h in range(half):
      if h == (half // 2) - 1: count += sorted_data[h]
      elif h == half // 2: count += sorted_data[h]
    R25 = count / 2
    for j in range(length):
      if j >= half + 1:
        box.append(sorted_data[j])
        box_count += 1
    R75 = (box[box_count // 2] + box[(box_count // 2) - 1]) / 2
  else:
    for h in range(half):
      if h == half // 2: R25 += sorted_data[h]
    for j in range(length):
      if j >= half:
          box.append(sorted_data[j])
          box_count += 1
    R75 = box[box_count // 2]
  Range = sorted_data[length - 1] - sorted_data[0]
  Quartilerange = R75 - R25
  Min_value, Max_value = sorted_data[0], sorted_data[length - 1]
  for d in sorted_data:
    data_count = sorted_data.count(d)
    if data_count > max_count: max_count, mode_value = data_count, d
  for _, number in enumerate(sorted_data):
    if number < R25 - Quartilerange * 1.5 or number > R75 + Quartilerange * 1.5:
      Outlier.append(number)
  result = {
    'sorted_data': sorted_data,
    'length': length,
    'total': Total,
    'average': Average,
    'max': Max_value,
    'min': Min_value,
    'median': R50,
    'IQR': Quartilerange,
    'range': Range,
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

def deviation(data):
  r = lambda path: Stats(data)[path]
  sorted_data = r("sorted_data")
  _x = r("average")
  length = r("length")

  variance = sum((x - _x) ** 2 for x in sorted_data) / length
  std_deviation = math.sqrt(variance)

  deviations = [(i+1, x - _x) for i, x in enumerate(sorted_data)]
  total_deviation = sum(d[1] for d in deviations)

  result = {
      "deviations": deviations,
      "total_deviation": total_deviation,
      "variance": variance,
      "standard_deviation": std_deviation
  }

  return result

def covariance(x_data, y_data):
    if len(x_data) != len(y_data):
      return "要素数不一致"
    length = len(x_data)

    _x = sum(x_data) / length
    _y = sum(y_data) / length
    Sxy = sum((x - _x) * (y - _y) for x, y in zip(x_data, y_data)) / length

    result = {
        '_x': _x,
        '_y': _y,
        'covariance': Sxy
    }
    return result
