# Load the dataset
file_path = "life-expectancy.csv" #I dont know if I need to submit this file, but you can if you want.

overall_min_life_expectancy = float('inf')
overall_max_life_expectancy = float('-inf')
overall_min_country = ""
overall_max_country = ""
overall_min_year = 0
overall_max_year = 0

data = []

with open(file_path, 'r', encoding='utf-8') as file:
    next(file) 
    for line in file:
        parts = line.strip().split(',') 
        
        try:
            country = parts[0]
            year = int(parts[2])
            life_expectancy = float(parts[3])
        except ValueError:
            continue
        
        data.append((country, year, life_expectancy))
        
        if life_expectancy < overall_min_life_expectancy:
            overall_min_life_expectancy = life_expectancy
            overall_min_country = country
            overall_min_year = year
        if life_expectancy > overall_max_life_expectancy:
            overall_max_life_expectancy = life_expectancy
            overall_max_country = country
            overall_max_year = year

print(f"The overall min life expectancy is: {overall_min_life_expectancy} from {overall_min_country} in {overall_min_year}")
print(f"The overall max life expectancy is: {overall_max_life_expectancy} from {overall_max_country} in {overall_max_year}")

user_year = int(input("Enter the year of interest: "))
year_life_expectancies = [entry for entry in data if entry[1] == user_year]

if year_life_expectancies:
    avg_life_expectancy = sum(entry[2] for entry in year_life_expectancies) / len(year_life_expectancies)
    min_entry = min(year_life_expectancies, key=lambda x: x[2])
    max_entry = max(year_life_expectancies, key=lambda x: x[2])
    
    print(f"For the year {user_year}:")
    print(f"The average life expectancy across all countries was {avg_life_expectancy:.2f}")
    print(f"The min life expectancy was in {min_entry[0]} with {min_entry[2]:.3f}")
    print(f"The max life expectancy was in {max_entry[0]} with {max_entry[2]:.3f}")
else:
    print(f"No data available for the year {user_year}.")
