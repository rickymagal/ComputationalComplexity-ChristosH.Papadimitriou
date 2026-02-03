# Chapter 2 — Section 2.4: Linear Speedup

## The purpose of linear speedup in this book
Linear speedup is the formal justification for a cultural norm in complexity theory:
- constant factors are not the point,
- growth rates are.

The section is not claiming constants are uninteresting in engineering; it is claiming they do not support a clean, stable *theory*.

## What the theorem is buying you
The theorem says (informally): if a language is decidable in time f(n), then it is decidable in essentially ε·f(n) time for any constant ε>0, up to lower-order additive terms.

This implies:
- TIME(f(n)) is insensitive to constant factors (above some baseline),
- Big-O is the right equivalence class for time bounds,
- “polynomial time” can be treated as “n^k for some k” without caring about coefficients.

This is the key step that makes P a clean mathematical object rather than a fragile artifact of the chosen hardware.

## Technique: packing to do more work per step
Speedup proofs typically work by:
- compressing the tape representation (packing multiple symbols per cell),
- simulating multiple original steps in a single new step by decoding/encoding blocks.

The take-away is not the exact encoding, but the general method:
- represent a neighborhood of the head at higher “density”,
- pay a one-time preprocessing cost,
- amortize it over many steps.

This is an early “constant-factor amortization” argument in the book.

## Cross-source insight: speedup is not universal across all models
Linear speedup is a TM theorem. It is one reason “P” is stable under TM variants.
But constant factors reappear whenever the model is changed in stronger ways, for example:
- in fine-grained complexity (SETH-style analysis),
- in hardware-aware models (I/O complexity, cache complexity),
- in circuit complexity where depth and fan-in constants can matter structurally.

So: speedup justifies ignoring constants in *classical* asymptotic complexity, not in every modern subfield.

---

## References
- Christos H. Papadimitriou, *Computational Complexity*, Addison–Wesley, 1994. (Chapter 2, Section 2.4)
- Juris Hartmanis, Richard E. Stearns, “On the Computational Complexity of Algorithms,” *Transactions of the AMS*, 1965. (Early complexity measures)
- Fred C. Hennie, Richard E. Stearns, “Two-Tape Simulation of Multitape Turing Machines,” *J. ACM*, 1966. (Classical speed/simulation analyses)
- Sanjeev Arora, Boaz Barak, *Computational Complexity: A Modern Approach*, Cambridge Univ. Press, 2009. (Why constants are ignored in P)
