# Chapter 2 — Section 2.2: Turing Machines as Algorithms

This section makes a foundational complexity move:
- an “algorithmic problem” is represented as a language (a set of strings),
- “solving” the problem means deciding membership.

This is not only a formal convenience. It is what makes reductions and complexity classes possible later:
- problems become objects,
- transformations between problems become proofs.

## Encoding is not an afterthought; it is part of the theory
Papadimitriou emphasizes that “mathematical objects of interest” are encoded as strings:
- numbers in binary,
- tuples with delimiters,
- graphs via adjacency matrices or adjacency lists, etc.

This matters because asymptotic bounds are statements about input length |x|, not about some informal “n”.

A useful working discipline:
- always state what parameter n means (number of vertices? bits? matrix dimension?),
- and check that the encoding length is polynomially related to the intended parameter.

That discipline is one reason complexity results survive changes of representation.

## Correctness proofs by invariant + induction
The section’s example machines (e.g., palindrome recognition) illustrate a proof pattern that becomes standard:
- define an invariant about what remains to be checked,
- show each loop iteration preserves it,
- show termination implies correctness.

This is already complexity-flavored correctness: you prove correctness and complexity together, because the invariant often explains why the algorithm makes progress.

## Time as number of steps: what gets counted
The section pushes you to treat “time” as a *primitive counter*:
- one transition is one unit,
- runtime is the number of transitions before halting.

Later, when you compare models, you will be forced to argue that “one RAM instruction” corresponds to “polylog steps on a TM” (or similar). This is where the bookkeeping begins.

## Cross-source insight: why “language” is the right abstraction
If you compare with computability texts (Sipser, Hopcroft–Ullman), you’ll see that “language” is the natural abstraction for:
- decidability and undecidability,
- reductions,
- complexity classes.

The same abstraction supports everything from SAT to factoring to graph isomorphism—once you accept “everything is a string,” complexity becomes a unifying theory rather than a zoo of ad hoc problems.

---

## References
- Christos H. Papadimitriou, *Computational Complexity*, Addison–Wesley, 1994. (Chapter 2, Section 2.2)
- Michael Sipser, *Introduction to the Theory of Computation*, 3rd ed., Cengage, 2012. (Encodings; decision problems as languages)
- Oded Goldreich, *P, NP and NP-Completeness*, Cambridge Univ. Press, 2010. (Why decision problems/languages are central)
- Sanjeev Arora, Boaz Barak, *Computational Complexity: A Modern Approach*, Cambridge Univ. Press, 2009. (Robustness under encodings)
