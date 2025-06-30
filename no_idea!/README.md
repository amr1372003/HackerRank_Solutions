# No Idea!

## Problem Description
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. 

For each integer in the array:
- If the element is in A, you add 1 to your happiness.
- If the element is in B, you subtract 1 from your happiness.
- Otherwise, your happiness does not change.

You need to output your final happiness score.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

## Example Input/Output
```
Input Format
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers each — set A and set B.

Output Format
Output a single integer, your total happiness.

Sample Input
3 2
1 5 3
3 1
5 7

Sample Output
1
```
