# Chapter 1 — Section 1.2: Maximum Flow (and Matching)

## Why this section matters for complexity
This section introduces a second algorithmic “paradigm,” very different from plain search:
- **Optimization by local improvement** (augmenting a feasible solution).
- **Correctness via a global certificate** (cuts and the max-flow min-cut theorem).
- A first encounter with the “polynomial vs not obviously polynomial” phenomenon: the same-looking algorithm can be polynomial or not depending on a choice rule.

This is a template you will see repeatedly later: define a *relaxation space* (residual network), then walk inside it by local moves (augmentations).

## Problem statement in the complexity style
There are two versions:
- **Optimization:** compute a maximum \(s\)-\(t\) flow value.
- **Decision:** given \(K\), decide whether there exists a flow of value at least \(K\).

A recurring complexity trick appears here: decision and optimization are often polynomially inter-reducible (binary search + decision oracle, or direct reconstruction).

## Residual networks: the real object the algorithm operates on
Given a flow \(f\), the residual network \(N(f)\) encodes exactly how you can change \(f\):
- forward residual edge if capacity remains;
- backward residual edge if you can cancel some sent flow.

Augmenting along an \(s\)-\(t\) path in \(N(f)\) increases the flow value by the minimum residual capacity on that path (the bottleneck).

The conceptual point: you are not “guessing” a better flow; you are performing a certified local move that preserves feasibility.

## Why the choice of augmenting paths matters (polynomial vs pseudo-polynomial)
The Ford–Fulkerson augmentation idea is correct, but without a path-selection rule its number of iterations can depend on the *numerical values* of capacities (pseudo-polynomial), and can even fail to terminate with irrational capacities.

A disciplined rule (choose a shortest augmenting path in number of edges) yields the Edmonds–Karp strategy:
- distances in the residual network are monotone nondecreasing;
- each edge becomes “critical” only \(O(|V|)\) times;
- total augmentations are \(O(|V||E|)\), leading to a polynomial bound.

This is the first place the book pushes you to separate:
- **algorithmic idea** (augment);
- **complexity guarantee** (how you choose the augmenting path).

## Max-flow min-cut: certificate viewpoint
A cut \((S,T)\) upper-bounds the value of any flow. The theorem says the best flow meets the best cut:
- when the algorithm stops (no augmenting path), the reachable set from \(s\) in \(N(f)\) defines a cut whose capacity equals the current flow value.

That is a beautiful pattern: *algorithm termination produces a dual certificate*. Later, this becomes the normal way to think about polynomial-time algorithms in combinatorial optimization (strong duality, complementary slackness).

## Matching as a reduction to flow
The section ties flow to bipartite matching:
- create a source connected to left-part vertices (capacity 1);
- keep original bipartite edges (capacity 1);
- connect right-part vertices to sink (capacity 1);
- maximum integral flow corresponds exactly to a maximum matching.

Two important insights:
1. **Integrality:** With integer capacities, augmenting-path algorithms produce integer flows (no rounding).
2. **Reduction mindset:** you solve a new problem by compiling it into one you already know how to solve.

This is early preparation for reductions as the main language of complexity theory.

---

## References
- Christos H. Papadimitriou, *Computational Complexity*, Addison–Wesley, 1994. (Chapter 1, Section 1.2)
- L. R. Ford Jr. and D. R. Fulkerson, *Flows in Networks*, Princeton University Press, 1962. (Foundational flow theory)
- Jack Edmonds and Richard M. Karp, “Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems,” *J. ACM*, 1972. (Edmonds–Karp analysis)
- Ravindra K. Ahuja, Thomas L. Magnanti, James B. Orlin, *Network Flows: Theory, Algorithms, and Applications*, Prentice Hall, 1993. (Modern flow viewpoint; reductions; implementations)
- CLRS, *Introduction to Algorithms*, 3rd ed., MIT Press, 2009. (Max flow and bipartite matching)
