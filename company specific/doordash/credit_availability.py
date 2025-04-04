"""
A growing number of companies have chosen Doordash as partners to feed their employees as free perks. One way is to give the employees a limited-time availability credit that employees can use to order on Doordash. The administrator can determine credit amount and availability time before issuing the credits to their employees.

The customer can use multiple credits when placing one order. We would like to know the maximum credit available the customer can use when placing one order. You will be given a list of time intervals and credit amounts to determine the maximum credit that the customer can use.

Example 1:

[["10:00-11:00", "5"], ["13:00-15:00", "10"]] (Python Array format)

{{"10:00-11:00", "5"}, {"13:00-15:00", "10"}} (Java Array format)
Output: Max credit available is 10 dollars when using the credit from 13:00 to 15:00.

Example 2:

[["09:00-11:00", "10"], ["10:00-12:00", "15"], ["13:00-14:00", "20"]]  # Python Array format
Output: Max credit available is 25 dollars. 
Explanation: The intervals 09:00-11:00 and 10:00-12:00 overlap between 10:00-11:00. 
The combined credit is 10 + 15 = 25. 
The 13:00-14:00 interval doesn't overlap but has a credit of 20. 
The maximum available credit is 25.

"""