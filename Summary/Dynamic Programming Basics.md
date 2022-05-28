
## Steps:
1. Express **Recursive Approach:**  
    a. Express problem in turns of index.  
    b. Do all possible ops on the index.  
    c. Return min of rec calls.  
  
2. **Memoization (Top-Down)** for TC reduction:  
    a. Declare dp array.  
    b. If `dp[n]` is calculated, return value.    
        Else calculate and store the value.  
    c. Return `dp[n]`  
  
3. **Tabulation (Bottom-Up)** for SC reduction:  
    a. Assign base cases using for loop.  
    b. Use for loop to convert recursive calls to iterative calls.  
    c. Return last element of the array.  
  
4. **Space optimization**:  
    a. If you are only using the previous index, assign the value to a prev-variable.  
    b. Get rid of the array.    

---

## Reference:
[Striver's DP Series.](https://www.youtube.com/playlist?list=PLgUwDviBIf0qUlt5H_kiKYaNSqJ81PMMY)