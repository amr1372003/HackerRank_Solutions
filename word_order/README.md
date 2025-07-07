# Word Order

## Problem Description
You are given `n` words. Some words may repeat. For each word, output its number of occurrences.  
The output order should correspond with the input order of appearance of the word.  
See the sample input/output for clarification.

> Note: Each input line ends with a `\n` character.

### Constraints

- The sum of the lengths of all the words does not exceed reasonable limits.
- All the words are composed of lowercase English letters only.

---

### Input Format

- The first line contains the integer `n`.
- The next `n` lines each contain a single word.

---

### Output Format

- Output **2 lines**:
  1. The number of distinct words from the input.
  2. The number of occurrences for each distinct word in the order they first appeared.

---

## Example Input/Output
```
### Sample Input
4
bcdef
abcdefg
bcde
bcdef

shell
Copy code

### Sample Output
3
2 1 1

markdown
Copy code

---

### Explanation

There are 3 distinct words:
- `"bcdef"` appears **twice**
- `"abcdefg"` appears **once**
- `"bcde"` appears **once**

The order of the first appearances is:
`bcdef`, `abcdefg`, `bcde` → corresponding to the output `2 1 1`.
```
