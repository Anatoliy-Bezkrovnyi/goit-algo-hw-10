## Сomparison of two different approaches to find the square of the figure with curve lines

**Approaches selected for comparison:**

 - Integral calculation with "quad" function from "integrate" module of SciPy library 
 - Monte Carlo method

**Test strategy:** 
Calculation the square of the figure using two different approaches. 

**Test results:** 
| Method| Result|
| ------ | ---------- |
|**Quad**|2.666666666666667 |
|**Monte Carlo**|2.666248 |


**Conclusions:**
As can be seen from the provided testing results, **Monte Carlo** method gave acceptable results with very good level of accuracy. Accuracy of **Monte Carlo** method depends on quantity of experimwnts as higher quantity as more accurate results you will get. Awesome and very interesting experiment.