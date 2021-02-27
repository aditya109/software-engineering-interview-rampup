# Floyd-Warshall Algorithm

- All pairs shortest path algorithm
  - single source is for 1 vertex
  - all pairs shortest path is for v vertices

![](D:\Work\go-workspace\src\github.com\aditya109\grokking-the-coding-interview\basics\floyd-warshall.svg)

- Dijkstra single source shortest path

  #minimum edges = v - 1 (minimum spanning tree)

  #maximum edges = v<sup>2</sup>

  > That every vertex v can make edges with remaining v-1 vertices
  >
  > #edges = v * (v-1) = O(v<sup>2</sup>)

  Time complexity for 1 vertex = E log v
  Time complexity for v vertices = v * (E log v) = v * v<sup>2</sup>(log v) = v<sup>3</sup> log v

  But, Floyd-Warshall has v<sup>3</sup> as time complexity.

  

  

