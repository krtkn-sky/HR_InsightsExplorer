import pandas as pd
import random
import faker

# Create a Faker instance for generating fake data
fake = faker.Faker()

# Generate a list of department names
departments = ['HR', 'Finance', 'IT', 'Marketing', 'Sales', 'Operations']

# Create an empty DataFrame to store the data
data = []

# Generate data for 500 employees
for _ in range(500):
    employee_id = _ + 1
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    hire_date = fake.date_between(start_date='-10y', end_date='today')
    department = random.choice(departments)
    salary = random.randint(40000, 120000)
    performance_score = random.uniform(2.0, 5.0)
    training_hours = random.randint(10, 40)

    data.append([employee_id, first_name, last_name, email, hire_date, department, salary, performance_score, training_hours])

# Create a DataFrame from the generated data
df = pd.DataFrame(data, columns=['Employee_ID', 'First_Name', 'Last_Name', 'Email', 'Hire_Date', 'Department', 'Salary', 'Performance_Score', 'Training_Hours'])

# Save the DataFrame to a CSV file
df.to_csv('hr_data.csv', index=False)
