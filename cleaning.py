def clean_heartrate_data(data: list) -> tuple:
    clearned = []
    skipped = 0

    for line in data:
      line = line.strip()

      if line.isdigit():
          cleaned.append(int(line))
      else:
          skipped += 1
    return cleaned, skipped