# Matrix Script

## Problem Description
🧩 Problem: Matrix Script Decoder
Neo has a complex matrix script. The matrix script is a n × m grid of strings. It consists of alphanumeric characters, spaces, and symbols like !, @, #, $, %, and &.

To decode the script, Neo needs to:

Read each column from top to bottom, starting from the leftmost column.

Concatenate only alphanumeric characters into the result.

If there are symbols or spaces between two alphanumeric characters, replace them with a single space (' ') for readability.

Neo insists on solving this without using any if conditions.
Note: You may lose points if you use if statements in your implementation.

✨ Alphanumeric Characters:
A-Z, a-z, 0-9

📥 Input Format
The first line contains two space-separated integers:
n — number of rows
m — number of columns

The next n lines each contain a string of length m, representing a row of the matrix.

📤 Output Format
Print the decoded string with symbols replaced by spaces when they appear between two alphanumerics.

🔢 Constraints
0 < n, m < 100

## Example Input/Output

🧪 Sample Input
```
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
```
✅ Sample Output
```
This is Matrix#  %!
```
🧠 Explanation
If we read the matrix column-wise, we get this decoded string:
```
This$#is% Matrix#  %!
```
Neo then replaces the symbols and spaces that appear between alphanumeric characters with a single space, resulting in:
```
This is Matrix#  %!
```
