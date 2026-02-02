# Computational Complexity — Complete Solutions Repository

This repository contains **complete, rigorous solutions to all problems** from:

Christos H. Papadimitriou  
*Computational Complexity*  
Addison–Wesley

The objective of this project is to provide **chapter-by-chapter solutions** to *all* problems in the book, written at a level appropriate for graduate study and research.

All solutions are:
- Fully formal and explicit
- Self-contained at the **chapter level**
- Faithful to the book’s definitions, notation, and proof style

---

## Repository Organization (IMPORTANT)

**The directory structure of this repository exactly mirrors the structure of the book.**

Key design principles:

- **Problems appear only at the end of each chapter**, exactly as in the book.
- Each chapter contains a single **`problems/` directory**.
- Each `problems/` directory is a **self-contained LaTeX project** that compiles **all solutions for that chapter together**, including:
  - all problem solutions of the chapter,
  - a chapter-specific bibliography,
  - a glossary / list of terms.

There are **no standalone solution files compiled independently**.

---

## Global Repository Structure

### PART I — ALGORITHMS

```
part-01-algorithms/
├── chapter-01-problems-and-algorithms/
│   ├── section-1.1-graph-reachability/
│   ├── section-1.2-maximum-flow-and-matching/
│   ├── section-1.3-the-traveling-salesman-problem/
│   └── problems/
├── chapter-02-turing-machines/
│   ├── section-2.1-turing-machine-basics/
│   ├── section-2.2-turing-machines-as-algorithms/
│   ├── section-2.3-turing-machines-with-multiple-strings/
│   ├── section-2.4-linear-speedup/
│   ├── section-2.5-space-bounds/
│   ├── section-2.6-random-access-machines/
│   ├── section-2.7-nondeterministic-machines/
│   └── problems/
├── chapter-03-computability/
│   ├── section-3.1-universal-turing-machines/
│   ├── section-3.2-the-halting-problem/
│   ├── section-3.3-more-undecidability/
│   └── problems/
```

---

### PART II — LOGIC

```
part-02-logic/
├── chapter-04-boolean-logic/
│   ├── section-4.1-boolean-expressions/
│   ├── section-4.2-satisfiability-and-validity/
│   ├── section-4.3-boolean-functions-and-circuits/
│   └── problems/
├── chapter-05-first-order-logic/
│   ├── section-5.1-the-syntax-of-first-order-logic/
│   ├── section-5.2-models/
│   ├── section-5.3-valid-expressions/
│   ├── section-5.4-axioms-and-proofs/
│   ├── section-5.5-the-completeness-theorem/
│   ├── section-5.6-consequences-of-the-completeness-theorem/
│   ├── section-5.7-second-order-logic/
│   └── problems/
├── chapter-06-undecidability-in-logic/
│   ├── section-6.1-axioms-for-number-theory/
│   ├── section-6.2-complexity-as-a-number-theoretic-concept/
│   ├── section-6.3-undecidability-and-incompleteness/
│   └── problems/
```

---

### PART III — P AND NP

```
part-03-p-and-np/
├── chapter-07-relations-between-complexity-classes/
│   ├── section-7.1-complexity-classes/
│   ├── section-7.2-the-hierarchy-theorem/
│   ├── section-7.3-the-reducibility-method/
│   └── problems/
├── chapter-08-reductions-and-completeness/
│   ├── section-8.1-reductions/
│   ├── section-8.2-completeness/
│   ├── section-8.3-logical-characterizations/
│   └── problems/
├── chapter-09-np-complete-problems/
│   ├── section-9.1-problems-in-np/
│   ├── section-9.2-variants-of-satisfiability/
│   ├── section-9.3-graph-theoretic-problems/
│   └── problems/
├── chapter-10-conp-and-function-problems/
│   ├── section-10.1-np-and-conp/
│   ├── section-10.2-primality/
│   ├── section-10.3-function-problems/
│   └── problems/
```

---

### PART IV — INSIDE P

```
part-04-inside-p/
├── chapter-11-randomized-computation/
│   ├── section-11.1-randomized-algorithms/
│   ├── section-11.2-randomized-complexity-classes/
│   ├── section-11.3-random-sources/
│   └── problems/
├── chapter-12-cryptography/
│   ├── section-12.1-one-way-functions/
│   ├── section-12.2-protocols/
│   └── problems/
├── chapter-13-approximability/
│   ├── section-13.1-approximation-algorithms/
│   ├── section-13.2-approximation-and-complexity/
│   └── problems/
├── chapter-14-on-p-vs-np/
│   ├── section-14.1-the-map-of-np/
│   ├── section-14.2-isomorphism-and-density/
│   ├── section-14.3-oracles/
│   └── problems/
```

---

### PART V — BEYOND NP

```
part-05-beyond-np/
├── chapter-17-the-polynomial-hierarchy/
│   ├── section-17.1-optimization-problems/
│   ├── section-17.2-the-hierarchy/
│   └── problems/
├── chapter-18-computation-that-counts/
│   ├── section-18.1-the-permanent/
│   ├── section-18.2-the-class-#p/
│   └── problems/
├── chapter-19-polynomial-space/
│   ├── section-19.1-alternation-and-games/
│   ├── section-19.2-games-against-nature-and-interactive-protocols/
│   ├── section-19.3-more-pspace-complete-problems/
│   └── problems/
├── chapter-20-a-glimpse-beyond/
│   ├── section-20.1-exponential-time/
│   └── problems/
```

---

## Internal Structure of Each `problems/` Directory

Each `problems/` directory is a **single LaTeX project** that compiles **all solutions for that chapter together**.

```
problems/
├── main.tex            # Entry point (compiled file)
├── preamble.tex        # Packages, theorem environments, macros
├── problems.tex        # Includes all problem solutions for the chapter
├── glossary.tex        # Chapter-specific glossary / list of terms
├── bibliography.bib    # Chapter-specific bibliography
├── problem-X.Y.Z.tex   # Individual problem solution (included by problems.tex)
└── figures/            # Figures used in this chapter
```

- Individual `problem-X.Y.Z.tex` files are **not standalone documents**.
- They are included via `\input{}` from `problems.tex`.
- Bibliography and glossary are resolved **at the chapter level**, not per problem.

---

## Status

This repository is a **work in progress**. Chapters are completed independently.

---

## Disclaimer

This repository is intended strictly for **educational and academic use**.  
All problem statements remain the intellectual property of the author and publisher.  
Only original solution texts are provided here.
