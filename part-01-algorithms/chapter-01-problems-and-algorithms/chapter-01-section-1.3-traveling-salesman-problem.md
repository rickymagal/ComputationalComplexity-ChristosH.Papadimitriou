# Chapter 1 — Section 1.3: The Traveling Salesman Problem (TSP)

## Why TSP is placed here
Reachability and max flow are “happy stories”: clean polynomial-time algorithms with strong certificates.
TSP is introduced as the counterweight:
- a natural, simple-to-state problem,
- a strong algorithmic tradition,
- and still no known polynomial-time exact algorithm in general.

TSP is one of the key motivational engines behind the emergence of complexity theory: it forces you to ask whether “efficient” always exists, or whether some tasks are inherently intractable.

## The problem (optimization and decision)
**Optimization (TSP):** find the minimum-length Hamiltonian cycle (tour).  
**Decision (TSP(D)):** given a bound \(B\), does there exist a tour of length at most \(B\)?

The decision form is the one that fits best into complexity classes and reductions later, but algorithm design often starts from the optimization form.

## The Held–Karp dynamic program: what it teaches
The classical dynamic program uses states \((S,j)\):
- \(S\) is the set of visited cities,
- \(j\) is the last city,
- the recurrence removes \(j\) and tries all possible predecessors.

This is a canonical “subset DP” pattern:
- correctness from optimal substructure (last step decomposition),
- exponential state space (\(2^{n}\)),
- polynomial work per state (\(O(n)\)).

The headline bound is \(O(n^2 2^n)\) time and \(O(n 2^n)\) space: dramatically better than \(n!\), but still exponential.

Complexity insight: this is the first explicit demonstration that “cleverness” can cut factorial to exponential, yet still fail to reach polynomial time.

## Cross-source insight: metric vs general TSP
Papadimitriou states TSP in a complete graph with symmetric distances, but algorithmic behavior changes drastically depending on additional structure:
- **Metric TSP** (triangle inequality) admits constant-factor approximation (e.g., Christofides’ 3/2-approx).
- **General TSP** (no triangle inequality) is much harder to approximate; strong inapproximability results are known unless P=NP.

So when you see “TSP,” always ask: what assumptions on distances are in force? That question becomes central in approximation and hardness chapters.

## Complexity-theory connection
TSP(D) is NP-complete (via Karp’s reductions). This is not proven in Chapter 1, but this section is clearly preparing the reader to accept that some “simple” problems may encode vast combinatorial search spaces.

---

## References
- Christos H. Papadimitriou, *Computational Complexity*, Addison–Wesley, 1994. (Chapter 1, Section 1.3)
- Michael Held and Richard M. Karp, “A Dynamic Programming Approach to Sequencing Problems,” *J. SIAM*, 1962. (Held–Karp DP)
- Richard M. Karp, “Reducibility Among Combinatorial Problems,” in *Complexity of Computer Computations*, Plenum Press, 1972. (NP-completeness of TSP(D))
- Nicos Christofides, “Worst-case analysis of a new heuristic for the travelling salesman problem,” 1976. (3/2-approx for metric TSP; widely cited technical report)
- CLRS, *Introduction to Algorithms*, 3rd ed., MIT Press, 2009. (TSP discussion; approximation pointers)
