data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
#1-Rename column names using function. "First Name" --> "first_name", "Age" --> "age
df = df.rename(columns={"First Name":"first_name","Age":"age"})
#2-Print the first 3 rows of the DataFrame
df.head(3)
#3-Find the mean age of the individuals
df["age"].mean() #mean returns avg number of the column that u want
#4-Select and print only the 'Name' and 'City' columns
df[["first_name","City"]]
#5-Add a new column 'Salary' with random salary values
Salary = [2000,3000,2500,1750]
df["Salary"]= Salary
df
#6-Display summary statistics of the DataFrame
df.describe() #describe uses to return statistic of mean, std , min ,etcs
df.info() #info method uses to return all information about data frame like how many columns ,nulls , types
#7-Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
data  = ({"Month": ["Jan", "Feb","Mar","Apr"],"Sales":[5000,6000,7500,8000],"Expenses":[3000,3500,4000,4500]})
sales_and_expenses = pd.DataFrame(data)
#8-Calculate and display the maximum sales and expenses.
sales_and_expenses[["Sales","Expenses"]].max()  #man() method returns maximum values from columns that u chosed
#9-Calculate and display the minimum sales and expenses.
sales_and_expenses[["Sales","Expenses"]].min()  #min() method returns minimum valuses from columns  that u chosed 
#10-Calculate and display the average sales and expenses.
sales_and_expenses[["Sales","Expenses"]].mean() #mean() method uses to calculate avarage of chosen column 
#11-Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
data = {"Category":["Rent","Utilities","Groceries","Entertaiment"],"January":[1200,200,300,150],"February":[1300,220,320,160],"March":[1400,240,330,170],"April":[1500,250,350,180]}
Expenses = pd.DataFrame(data)
#12-Calculate and display the maximum expense for each category.
Expenses["Max Expense"] = Expenses[["January", "February", "March", "April"]].max(axis=1)
#13-Calculate and display the minimum expense for each category.
Expenses["Min Expense"] = Expenses[["January", "February", "March", "April"]].min(axis=1)
#14-Calculate and display the average expense for each category.
Expenses["Avg Expense"] = Expenses[["January", "February", "March", "April"]].mean(axis=1)


