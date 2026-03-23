def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    cleaned = []
    skipped = 0

    for line in data:
        line = line.strip()
    
        if line.isdigit():
            cleaned.append(int(line))
        else:
            skipped = skipped + 1

    return cleaned, skipped

    

def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """
    total = 0
    count = 0

    for number in data:
        total = total + number
        count = count + 1

    avg = total / count
    return round(avg, 2)


def median(data: list) -> float:
    """
    """
    sorted_data = sorted(data)
    n = len(sorted_data)

    middle = n // 2

    if n % 2 == 1:
        med = sorted_data[middle]
    else:
        med = (sorted_data[middle - 1] + sorted_data[middle]) / 2

    return round(med, 2)


def range(data: list) -> float:
    """
    """
    max_value = data[0]
    min_value = data[0]

    for number in data:
        if number > max_value:
            max_value = number
        if number < min_value:
            min_value = number
    
    return round(max_value - min_value, 2)

def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
    


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    with open(file, 'r') as f:
        data = f.readlines()
        
    print("raw data:")
    print(data)

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_values = clean_heartrate_data(data)
    print("cleaned data:")
    print(cleaned_list)
    print("Skipped values:", removed_values)

    # calculate the average, median, and range of this file using the functions you've wrote
    avg = average(cleaned_list)
    med = median(cleaned_list)

    

    # print out your data quality measure to the console
    print("average heart rate:", avg)
    print("median hearth rate:", med)
  

    # print out your descriptive statistics to the console
 


if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
