# TURING-SIM

This repository includes a small single-tape Turing machine simulator that follows the conventions used in Chapter 2 of Papadimitriou.

## Conventions implemented

The simulator matches the book's setup:

- The tape is a right-infinite string whose first cell (cell 0) is the left-end marker **`[>`**.
- The head starts on cell 0, scanning **`[>`**.
- The blank symbol is **`u`**.
- The input is a finite string `x` placed immediately to the right of `[>`; the input contains no blanks (`u`).
- The left-end marker `[>` is never erased and always moves the head to the right.
- Halting states are:
  - `yes` (accept),
  - `no` (reject),
  - `h` (halt with string output).

The output `M(x)` is printed exactly as defined in the book:
- `yes` or `no` if the machine halts in the accepting/rejecting state,
- otherwise, if it halts in `h`, it outputs the tape contents after `[>` up to the last nonblank symbol,
- `/` if it does not halt (approximated by a step limit).

## Files

- `turing_sim.py` — the simulator
- `*.tm` — machine descriptions (plain text)

## Machine file format (`.tm`)

A `.tm` file is designed to be easy to write by hand.

### Directives

All directives are optional; defaults match the book:

- `@blank u`
- `@left [>`
- `@start s`
- `@accept yes`
- `@reject no`
- `@halt h`

Example:

```
@blank u
@left [>
@start s
@accept yes
@reject no
@halt h
```

### Transitions

Each transition is one line:

```
state read -> next write move
```

- `move` is one of `L`, `R`, `S` (also accepts `LEFT`, `RIGHT`, `STAY`, `<`, `>`, `-`).
- Comments start with `#`.

Example:

```
s 0 -> s 0 R
s 1 -> s 1 R
s u -> q u L
q 0 -> h 1 S
```

#### Left-end marker rule

If `read` is `[>`, the simulator enforces the book's constraint:

- you must write `[>` and move `R`.

So this is valid:

```
s [> -> s [> R
```

And this is rejected as invalid:

```
s [> -> s 0 L
```

## Running the simulator

### Basic run

```
python3 turing_sim.py path/to/machine.tm --input 0101
```

Input handling:
- If `--input` contains no spaces, it is treated as a sequence of single-character symbols.
- If `--input` contains spaces, it is treated as a space-separated list of symbols.

Examples:

```
python3 turing_sim.py succ.tm --input 11011
python3 turing_sim.py some.tm --input "a a b b a"
```

### Trace mode

Trace prints a window around the head at each step (or every k steps):

```
python3 turing_sim.py succ.tm --input 11011 --trace --radius 20
python3 turing_sim.py succ.tm --input 11011 --trace --dump-every 10
```

### Step limit and strictness

- `--max-steps N`: stop after N steps; if not halted, output is `/`.
- `--strict`: missing transitions become an error (useful for debugging).

By default, if a transition is missing, the simulator halts in `h` without changing the tape.
This is convenient when you omit transitions that are unreachable on legal inputs.

## Notes

- The simulator is deterministic and single-tape.
- The tape is one-way (no negative indices): the left marker prevents falling off the left end, matching the book.
- Tomorrow, when you draw machines in LaTeX, you can keep the `.tm` file as the source of truth and derive the TikZ/LaTeX diagram from it.
