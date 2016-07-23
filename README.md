# Apriori
A simple implementation of the [apriori algorithm](https://en.wikipedia.org/wiki/Apriori_algorithm). A method for extracting frequent substructures in a set of sequences of ordered events.

## How To

`Apriori` takes a list of strings, representing number sequences, and an integer, representing the percentage of sequences the pattern must match for being considered.

```python
>> import apriort
>> data = ['1,2, 4, 5', '2, 4,5', '4,5', '1, 2, 3']
>> patterns = apriori.Apriori(data, 34)
>> patterns
{'1, 2': 2,
 '2, 4': 2,
 '4, 5': 3,
 '2, 4, 5': 2}
 ```

## References

+ "Mining Frequent Patterns, Associations, and Correlations" (Chap. 5) *in* Han, J., Kamber, M., & Pei, J. (2006). **Data mining: concepts and techniques.** Morgan kaufmann.

+ Mooney, C. H., & Roddick, J. F. (2013). **Sequential pattern mining--approaches and algorithms.** ACM Computing Surveys (CSUR), 45(2), 19.

+ Original repo: https://github.com/mazieres/apriori
