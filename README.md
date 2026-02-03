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
- Each chapter contains a single **`problems/` directory** and may contain notes in markdown format.
- Each `problems/` directory is a **self-contained LaTeX project** that compiles **all solutions for that chapter together**, including:
  - all problem solutions of the chapter,
  - a chapter-specific bibliography,
  - a glossary / list of terms.
- The compiled PDF for each chapter is placed at the **repository root**.

There are **no standalone solution files compiled independently**.

---

## Global Repository Structure

### PART I — ALGORITHMS

```
part-01-algorithms/
├── chapter-01-problems-and-algorithms/
│   └── problems/
├── chapter-02-turing-machines/
│   └── problems/
├── chapter-03-computability/
│   └── problems/
```

---

### PART II — LOGIC

```
part-02-logic/
├── chapter-04-boolean-logic/
│   └── problems/
├── chapter-05-first-order-logic/
│   └── problems/
├── chapter-06-undecidability-in-logic/
│   └── problems/
```

---

### PART III — P AND NP

```
part-03-p-and-np/
├── chapter-07-relations-between-complexity-classes/
│   └── problems/
├── chapter-08-reductions-and-completeness/
│   └── problems/
├── chapter-09-np-complete-problems/
│   └── problems/
├── chapter-10-conp-and-function-problems/
│   └── problems/
```

---

### PART IV — INSIDE P

```
part-04-inside-p/
├── chapter-11-randomized-computation/
│   └── problems/
├── chapter-12-cryptography/
│   └── problems/
├── chapter-13-approximability/
│   └── problems/
├── chapter-14-on-p-vs-np/
│   └── problems/
```

---

### PART V — BEYOND NP

```
part-05-beyond-np/
├── chapter-17-the-polynomial-hierarchy/
│   └── problems/
├── chapter-18-computation-that-counts/
│   └── problems/
├── chapter-19-polynomial-space/
│   └── problems/
├── chapter-20-a-glimpse-beyond/
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
