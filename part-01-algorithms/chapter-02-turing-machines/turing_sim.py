#!/usr/bin/env python3
"""
Single-tape deterministic Turing machine simulator following Papadimitriou's conventions.

Conventions implemented:
- Tape is a right-infinite string that starts with the left-end marker "[>" at cell 0.
- The head starts on cell 0 (scanning "[>").
- The blank symbol is "u". Input contains no blanks.
- The left-end marker "[>" is never erased and always moves the head to the right.
- Halting states are: h (halt), yes (accept), no (reject).
- Output M(x):
  - "yes" if machine halts in state yes
  - "no"  if machine halts in state no
  - y     (the tape contents after "[>" up to the last nonblank symbol) if halts in h
  - "/"   if it does not halt (approximated by a step limit)
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Dict, Tuple, List, Optional


Symbol = str
State = str
Move = str  # "L", "R", "S"
Key = Tuple[State, Symbol]
Val = Tuple[State, Symbol, Move]


DEFAULT_BLANK = "u"
DEFAULT_LEFT = "[>"
DEFAULT_START = "s"
DEFAULT_ACCEPT = "yes"
DEFAULT_REJECT = "no"
DEFAULT_HALT = "h"


def _strip_comment(line: str) -> str:
    i = line.find("#")
    return line if i < 0 else line[:i]


def _tokenize(line: str) -> List[str]:
    line = _strip_comment(line).strip()
    if not line:
        return []
    return line.split()


def _parse_move(tok: str) -> Move:
    t = tok.strip().upper()
    if t in ("L", "LEFT", "<"):
        return "L"
    if t in ("R", "RIGHT", ">"):
        return "R"
    if t in ("S", "STAY", "-", "0"):
        return "S"
    raise ValueError(f"invalid move: {tok!r} (expected L/R/S)")


@dataclass
class Spec:
    blank: Symbol = DEFAULT_BLANK
    left: Symbol = DEFAULT_LEFT
    start: State = DEFAULT_START
    accept: List[State] = None
    reject: List[State] = None
    halt: List[State] = None
    transitions: Dict[Key, Val] = None

    def __post_init__(self) -> None:
        if self.accept is None:
            self.accept = [DEFAULT_ACCEPT]
        if self.reject is None:
            self.reject = [DEFAULT_REJECT]
        if self.halt is None:
            self.halt = [DEFAULT_HALT]
        if self.transitions is None:
            self.transitions = {}

    @staticmethod
    def from_tm_file(path: str) -> "Spec":
        spec = Spec()
        transitions: Dict[Key, Val] = {}

        with open(path, "r", encoding="utf-8") as f:
            for lineno, raw in enumerate(f, start=1):
                toks = _tokenize(raw)
                if not toks:
                    continue

                # Directives: @blank, @left, @start, @accept, @reject, @halt
                if toks[0].startswith("@"):
                    directive = toks[0][1:].lower()
                    args = toks[1:]

                    if directive == "blank":
                        if len(args) != 1:
                            raise ValueError(f"{path}:{lineno}: @blank expects 1 argument")
                        spec.blank = args[0]
                    elif directive == "left":
                        if len(args) != 1:
                            raise ValueError(f"{path}:{lineno}: @left expects 1 argument")
                        spec.left = args[0]
                    elif directive == "start":
                        if len(args) != 1:
                            raise ValueError(f"{path}:{lineno}: @start expects 1 argument")
                        spec.start = args[0]
                    elif directive == "accept":
                        if len(args) < 1:
                            raise ValueError(f"{path}:{lineno}: @accept expects at least 1 state")
                        spec.accept = args[:]
                    elif directive == "reject":
                        if len(args) < 1:
                            raise ValueError(f"{path}:{lineno}: @reject expects at least 1 state")
                        spec.reject = args[:]
                    elif directive == "halt":
                        if len(args) < 1:
                            raise ValueError(f"{path}:{lineno}: @halt expects at least 1 state")
                        spec.halt = args[:]
                    else:
                        raise ValueError(f"{path}:{lineno}: unknown directive @{directive}")
                    continue

                # Transition rule:
                #   state read -> next write move
                # Example:
                #   s 0 -> s 0 R
                if len(toks) != 6 or toks[2] != "->":
                    raise ValueError(
                        f"{path}:{lineno}: expected transition: state read -> next write move"
                    )

                st, rd, _, nxt, wr, mv = toks
                mv_parsed = _parse_move(mv)

                key = (st, rd)
                if key in transitions:
                    raise ValueError(f"{path}:{lineno}: duplicate transition for ({st}, {rd})")
                transitions[key] = (nxt, wr, mv_parsed)

        spec.transitions = transitions
        spec._validate()
        return spec

    def _validate(self) -> None:
        # Enforce the book's convention for the left marker.
        # If delta(q, left) = (p, sym, D) then sym == left and D == R.
        for (st, rd), (nxt, wr, mv) in self.transitions.items():
            if rd == self.left:
                if wr != self.left or mv != "R":
                    raise ValueError(
                        f"invalid transition on left marker: ({st}, {self.left}) -> ({nxt}, {wr}, {mv}); "
                        f"must write {self.left} and move R"
                    )
        # Sanity: blank and left must be distinct.
        if self.blank == self.left:
            raise ValueError("blank symbol and left marker must be distinct")


class TM:
    def __init__(self, spec: Spec, input_symbols: List[Symbol]) -> None:
        self.spec = spec
        self.state: State = spec.start
        self.head: int = 0
        self.steps: int = 0

        # Tape is right-infinite; we store a sparse dictionary for nonblank cells.
        # Cell 0 always stores the left marker.
        self.tape: Dict[int, Symbol] = {0: spec.left}

        # Input x begins at cell 1, and contains no blanks or left markers.
        for i, sym in enumerate(input_symbols, start=1):
            self.tape[i] = sym

        # Track the rightmost cell ever visited (for nicer dumps).
        self.rightmost: int = max(0, len(input_symbols))

    def _read(self) -> Symbol:
        if self.head == 0:
            return self.spec.left
        return self.tape.get(self.head, self.spec.blank)

    def _write(self, sym: Symbol) -> None:
        if self.head == 0:
            # Left marker is immutable by convention.
            self.tape[0] = self.spec.left
            return
        if sym == self.spec.blank:
            self.tape.pop(self.head, None)
        else:
            self.tape[self.head] = sym

    def _is_accept(self) -> bool:
        return self.state in self.spec.accept

    def _is_reject(self) -> bool:
        return self.state in self.spec.reject

    def _is_halt(self) -> bool:
        return self.state in self.spec.halt

    def _halted(self) -> bool:
        return self._is_accept() or self._is_reject() or self._is_halt()

    def step(self, *, strict: bool) -> Optional[Tuple[State, Symbol, Move]]:
        """
        Perform one transition.
        Returns the applied (next_state, written_symbol, move) or None if halted due to missing transition.
        """
        if self._halted():
            return None

        rd = self._read()
        tr = self.spec.transitions.get((self.state, rd))
        if tr is None:
            if strict:
                raise RuntimeError(f"missing transition for ({self.state}, {rd!r})")
            # Default behavior: halt in h without changing the tape.
            self.state = self.spec.halt[0] if self.spec.halt else DEFAULT_HALT
            return None

        nxt, wr, mv = tr

        self._write(wr)

        if mv == "L":
            # By construction, the head never goes below 0 because left marker transitions always move R.
            if self.head > 0:
                self.head -= 1
        elif mv == "R":
            self.head += 1
            if self.head > self.rightmost:
                self.rightmost = self.head
        elif mv == "S":
            pass
        else:
            raise RuntimeError(f"internal error: bad move {mv!r}")

        self.state = nxt
        self.steps += 1
        return (nxt, wr, mv)

    def output_M_of_x(self) -> str:
        """
        Return M(x) following the book's definition.
        - "yes" or "no" if halted in accept/reject
        - otherwise the tape string y after the left marker, up to the last nonblank symbol
        """
        if self._is_accept():
            return "yes"
        if self._is_reject():
            return "no"
        # Halt state: output y (may contain blanks internally; trailing blanks are removed).
        # Find the rightmost cell >= 1 that is nonblank.
        last = 0
        for pos, sym in self.tape.items():
            if pos >= 1 and sym != self.spec.blank and pos > last:
                last = pos
        if last == 0:
            return ""
        out: List[str] = []
        for pos in range(1, last + 1):
            out.append(self.tape.get(pos, self.spec.blank))
        return "".join(out)

    def tape_as_string(self, *, max_len: int = 200) -> str:
        """
        Return a compact tape string for display:
        [> followed by cells 1..min(rightmost, max_len) with blanks shown explicitly.
        """
        hi = min(self.rightmost, max_len)
        cells = [self.spec.left]
        for pos in range(1, hi + 1):
            cells.append(self.tape.get(pos, self.spec.blank))
        if self.rightmost > hi:
            cells.append("...")
        return "".join(cells)

    def window(self, radius: int) -> Tuple[int, int, List[str], List[str]]:
        """
        A local tape view around the head for tracing.
        Returns (lo, hi, cells, markers).
        """
        lo = max(0, self.head - radius)
        hi = self.head + radius
        cells: List[str] = []
        marks: List[str] = []
        for pos in range(lo, hi + 1):
            sym = self.spec.left if pos == 0 else self.tape.get(pos, self.spec.blank)
            cells.append(sym)
            marks.append("^" if pos == self.head else " ")
        return lo, hi, cells, marks


def parse_input(s: str, *, blank: str, left: str) -> List[Symbol]:
    """
    Input convention: x in (Sigma - {u})*.
    - If s contains whitespace, it is treated as a space-separated list of symbols.
    - Otherwise, it is treated as a sequence of single-character symbols.
    """
    raw = s.strip()
    if raw == "":
        return []
    if any(ch.isspace() for ch in raw):
        syms = [t for t in raw.split() if t]
    else:
        syms = list(raw)

    for sym in syms:
        if sym == blank:
            raise ValueError("input contains the blank symbol")
        if sym == left:
            raise ValueError("input contains the left-end marker")
    return syms


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Single-tape TM simulator (Papadimitriou conventions)"
    )
    ap.add_argument("machine", help="Path to .tm machine file")
    ap.add_argument("--input", default="", help="Input x (chars or space-separated symbols)")
    ap.add_argument("--max-steps", type=int, default=200000, help="Step limit")
    ap.add_argument("--strict", action="store_true", help="Error on missing transitions")
    ap.add_argument("--trace", action="store_true", help="Print per-step trace (slow)")
    ap.add_argument("--radius", type=int, default=25, help="Trace window radius")
    ap.add_argument("--dump-every", type=int, default=1, help="Trace: print every k steps")
    args = ap.parse_args()

    spec = Spec.from_tm_file(args.machine)
    x = parse_input(args.input, blank=spec.blank, left=spec.left)
    tm = TM(spec, x)

    if args.trace:
        print(f"machine={args.machine}")
        print(f"blank={spec.blank} left={spec.left} start={spec.start}")
        print(f"accept={spec.accept} reject={spec.reject} halt={spec.halt}")
        print(f"input={args.input!r}")
        print()

        for _ in range(args.max_steps):
            if tm._halted():
                break
            if tm.steps % max(1, args.dump_every) == 0:
                lo, hi, cells, marks = tm.window(args.radius)
                print(f"step={tm.steps} state={tm.state} head={tm.head} window=[{lo}..{hi}]")
                print("".join(cells))
                print("".join(marks))
                print()
            tm.step(strict=args.strict)

        if not tm._halted():
            print("RESULT: / (did not halt within step limit)")
        else:
            print(f"RESULT: {tm.output_M_of_x()}")
        print(f"STEPS: {tm.steps}")
        print(f"FINAL STATE: {tm.state}")
        print(f"TAPE: {tm.tape_as_string(max_len=200)}")
        return

    # Non-trace mode: run quietly
    for _ in range(args.max_steps):
        if tm._halted():
            break
        tm.step(strict=args.strict)

    if not tm._halted():
        print("/")
        return

    print(tm.output_M_of_x())


if __name__ == "__main__":
    main()
