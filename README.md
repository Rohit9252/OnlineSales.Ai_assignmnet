# OnlineSales.Ai Assignment

## Task 1: SQL Query

To fetch the top 3 departments along with their name and average monthly salary, you can execute the following SQL query:
``` sql
SELECT d.NAME AS DEPT_NAME, AVG(s.AMT) AS AVG_MONTHLY_SALARY
FROM departments d
JOIN employees e ON d.ID = e.DEPT_ID
JOIN salaries s ON e.ID = s.EMP_ID
GROUP BY d.ID, d.NAME
ORDER BY AVG_MONTHLY_SALARY DESC
LIMIT 3;
```


The query will retrieve the department names and their corresponding average monthly salaries, sorted in descending order by average salary. The result will be limited to the top 3 departments.

## Task 2: Scripting

To generate the same report using CSV files as the data source, you can use the provided Python script `Index.py`. The script reads data from `departments.csv`, `employees.csv`, and `salaries.csv` files, calculates the average monthly salary for each department, and generates a report displaying the top 3 departments along with their average salaries.

To run the script, execute the following command in the terminal:


Ensure that the CSV files (`departments.csv`, `employees.csv`, `salaries.csv`) are present in the same directory as the script.

## Task 3: Debugging

1. The provided Python script computes different values based on the input number `n`. It calculates the square of `n` </br>
2. if it is less than 10, the factorial of `(n-10)` </br>
3. if it is between 10 and 20, and the sum of integers between 1 and `(n-20)` if `n` is greater than 20.

The bugs in the script have been fixed. Here's the updated code:

``` python
def compute(n):
    if n < 10:
        out = n ** 2
    elif n < 20:
        out = 1
        for i in range(1, n - 9):  # Fixed the range starting from 1
            out *= i
    else:
        lim = n - 20
        out = (lim * (lim + 1)) // 2  # Fixed the calculation for sum of integers
    print(out)

n = int(input("Enter an integer: "))
compute(n)



Now, when you run the script and provide an integer input, it will correctly
compute the square, factorial, or sum based on the given conditions.
```

---

## Conclusion

This assignment covered SQL querying, scripting with CSV files, and debugging a code snippet. By completing these tasks, you gained practical experience in data analysis, data manipulation, and problem-solving with programming.

Feel free to explore and modify the code according to your specific requirements. If you have any questions or need further assistance, please don't hesitate to reach out.

Happy coding!







