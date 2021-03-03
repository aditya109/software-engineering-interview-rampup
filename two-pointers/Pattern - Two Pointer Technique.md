# Pattern - Two Pointer Technique

## How do you identify ??

Two pointer technique is normally used for searching and it uses two pointer in one loop over the given data structure.

In order to use two pointers, most of the times the ***data structure needs to be ordered in some way***, which helps us to reduce the time complexity from **O(n<sup>2</sup>)** or **O(n<sup>3</sup>)** to **O(n)** of just one loop with two pointers and search each item just one time.

So depending on whether the input string is sorted or not, the two-pointer can take **O(n log n)** time complexity or even better which is **O(n)**.

## Types of two-pointers

1. **Opposite Directional**: One pointer starts from the beginning while the other pointer starts from the end. They move toward each other until they both meet or some condition satisfy.
2. **Equi-Directional**: Both start from the beginning, one slow-runner and the other is fast-runner.

