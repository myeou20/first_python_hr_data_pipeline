def average(data: list) -> float:
  total = 0
  for num in data:
      total += num
  return total / len(data)


def median(data):
  sorted_data = sorted(data)
  n = len(sorted_data)
  mid = n // 2

  if n % 2 == 1:
      return sorted_data[mid]
  else:
      return (sorted_data)[mid - 1] + sorted_data[mid] / 2


      def data_range(data):
          return max(data) - min(data)