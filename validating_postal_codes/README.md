# Validating Postal Codes

## Problem Description
A valid postal code must fulfill both of the following requirements:

✅ 1. Must be a number in the range 100000 to 999999 (inclusive)
It should be a 6-digit number.

The first digit cannot be 0.

✅ 2. Must not contain more than one alternating repetitive digit pair
Alternating repetitive digits are digits that repeat immediately after one digit.

In other words, an alternating repetitive digit pair is formed by two equal digits with exactly one digit in between them.

## Example Input/Output
```
📥 Input Format
The stub code reads a single string P from standard input and applies the expression above using your regex patterns.

📤 Output Format
You don’t need to print anything manually — the stub code will handle that.

🧪 Sample Input 0
Copy
Edit
110000
✅ Sample Output 0
graphql
Copy
Edit
False
📘 Explanation
In 110000, there are two alternating repetitive digit pairs:

0_0

Another 0_0

Since we’re only allowed one, the result is False.

⚠️ Note
Do not use if conditions — doing so may reduce your score.

You must pass all test cases to receive a positive score.
```
