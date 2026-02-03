# Chapter 2 — Section 2.5: Space Bounds

## Why space is more delicate than time
At first glance, “space used by a TM” looks as straightforward as time:
- count how many tape cells are ever visited / written.

But the section highlights a real subtlety:
- the input itself occupies space,
- output may be written on the same tape,
- and careless definitions trivialize the measure (every machine uses at least n space if input counts naively).

So the book forces you to separate:
- the size of the input representation,
- the *additional workspace* the machine needs to solve the problem.

This is the first step toward space classes like L and NL.

## Space as a structural resource
Time is about how long computation runs; space is about how much information it can actively manipulate.
That difference becomes profound later:
- space-bounded computation can reuse memory,
- which makes reachability-style problems natural (configuration graphs have size exponential in space).

This is why the space chapter later will feel “graphy”: space bounds induce graph reachability problems over configuration graphs.

## The important classes introduced implicitly
The section’s palindrome example illustrates:
- you can do tasks with tiny workspace if you can make multiple passes over the input (log space vs linear time tradeoffs).

The class SPACE(log n) is called L.
Even if the book delays the full power of L until later, you should already see the shape of the subject:
- space is often a more stringent resource than time,
- and log-space is “the smallest nontrivial” regime that still admits interesting algorithms.

## Linear speedup for space (constants still don’t count)
The analog of time-speedup holds for space (up to additive constants):
- you can compress the tape alphabet,
- trading constant-factor reductions in used cells.

This is another justification for Big-O in space bounds and for treating “log n” as the canonical small workspace scale.

## Cross-source insight: why space-bounded complexity becomes “graph reachability”
A machine using s(n) space has at most exponentially many configurations in s(n).
Therefore:
- acceptance can be phrased as reachability in a directed graph of configurations,
- and many space results reduce to graph reachability (Savitch-style arguments, NL-completeness of reachability).

This connection is one of the best “mental bridges” from Chapter 1 reachability to later space theory.

---

## References
- Christos H. Papadimitriou, *Computational Complexity*, Addison–Wesley, 1994. (Chapter 2, Section 2.5)
- Michael Sipser, *Introduction to the Theory of Computation*, 3rd ed., Cengage, 2012. (SPACE classes; L and NL)
- Sanjeev Arora, Boaz Barak, *Computational Complexity: A Modern Approach*, Cambridge Univ. Press, 2009. (Space as configuration graph reachability)
- Walter J. Savitch, “Relationships Between Nondeterministic and Deterministic Tape Complexities,” *JCSS*, 1970. (Space vs reachability viewpoint)
