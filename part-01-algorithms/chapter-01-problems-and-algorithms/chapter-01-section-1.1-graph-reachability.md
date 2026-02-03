# Chapter 1 — Section 1.1: Graph Reachability

## What this section is really setting up
Graph reachability is being used as the “hello world” of algorithmic problem-solving in complexity theory:
- You get a crisp problem definition (input → yes/no).
- You get a clean algorithm (search).
- You get a first serious encounter with *resource measures* (time and space) and how they depend on representation.

It is also a prototype for later complexity-theoretic ideas: reachability sits near the boundary between what is easy in time and what is easy in space.

## Core problem
**Instance:** A directed graph \(G=(V,E)\) and two distinguished vertices \(s,t\).  
**Question:** Is there a directed path from \(s\) to \(t\)?

Equivalent viewpoint: compute the set of all vertices reachable from \(s\), then check membership of \(t\).

## The search algorithm: invariant-driven thinking
The algorithm maintains a set of “discovered” vertices \(S\) and repeatedly adds a vertex that has an incoming edge from \(S\).

Two invariants matter (they become explicit in the end-of-chapter problems):
1. **Soundness:** Whenever a vertex \(v\) is added to \(S\), there exists a path from \(s\) to \(v\).
2. **Completeness:** If there exists a path from \(s\) to \(v\), the algorithm eventually adds \(v\) to \(S\).

This is the first place in the book where you can see the “complexity style” of proof:
- correctness by induction on the order vertices are discovered;
- termination by finiteness;
- runtime by counting *primitive events* (“each edge/entry is processed at most once”).

## Representation matters (and this is intentional)
The section implicitly teaches a crucial lesson: runtime claims depend on the input encoding.

- With an **adjacency matrix**, scanning a row is \(O(|V|)\) and scanning all visited rows is \(O(|V|^2)\).
- With **adjacency lists**, scanning outgoing edges from visited vertices is \(O(|V|+|E|)\).

This matters later when “polynomial time” is treated as a robust notion: you want claims that survive reasonable encodings, and you want to be honest when they do not.

## BFS vs DFS is an implementation detail with semantic consequences
The section emphasizes that the search is correct no matter how you choose the next frontier vertex, but:
- a queue yields **BFS**, which discovers shortest paths in number of edges;
- a stack yields **DFS**, which is often better for building depth-first structures (spanning trees, topological tests, etc.).

The complexity angle: both are linear-time in adjacency lists, but they behave very differently as *exploration policies*. This foreshadows later themes where “which witness you find” matters (e.g., which augmenting path, which certificate).

## Complexity-theory connections (beyond what the section explicitly says)
- **Directed s–t reachability** is complete for **NL** under logspace reductions (a canonical space-bounded problem). This is why reachability keeps returning throughout complexity theory.
- **Undirected reachability** is in **L** (Reingold), which is a striking “space vs randomness” milestone.

So: this “simple” problem is actually a landmark when you switch from time to space.

## Practical notes / pitfalls
- Directed vs undirected reachability are different problems; don’t silently swap them.
- If you claim \(O(|E|)\) time but you’re using a matrix, you are counting the wrong primitive operation.
- In proofs, explicitly name what is processed once: matrix entries vs list edges.

---

## References
- Christos H. Papadimitriou, *Computational Complexity*, Addison–Wesley, 1994. (Chapter 1, Section 1.1)
- Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein, *Introduction to Algorithms* (CLRS), 3rd ed., MIT Press, 2009. (BFS/DFS; graph representations)
- Christos H. Papadimitriou, “On the Complexity of the Parity Argument and Other Inefficient Proofs of Existence,” *JCSS*, 1984. (Context for reachability-style completeness phenomena)
- Omer Reingold, “Undirected Connectivity in Log-Space,” *J. ACM*, 2008. (Undirected reachability in L)
