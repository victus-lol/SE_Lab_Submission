# Scenario 14: 2048

A small terminal version of 2048. Use W, A, S, and D to move the tiles. Type U to undo the last successful move, and Q to quit.

## Run

```bash
python main.py
```

Python's standard library is enough; no packages need to be installed.

## What changed

- Each tile can merge only once in a move. For example, four 2s become two 4s, not an 8.
- New tiles appear only after a move changes the board. The game ends on a 2048 tile or when no legal moves remain.
- U restores the board and score from the previous successful move. The best score is tracked for the current run.
- A successful move reports its direction and any merges. Invalid and unchanged moves don't report a successful move.

## Check the game logic

Run `python -m unittest -v` from this directory. The checks cover normal movement, merge boundaries, unchanged moves, win and no-move states, undo, invalid input, and quitting.

## Lab submission recordings

The original-bug recording must be made before changing the starter files. A recording made after the fix cannot honestly show that earlier state. The supplied before recording is therefore still needed from the student. Record a 10-second after clip after running this version; show a merge, the score/feedback, and undo if possible.

The assignment asks for a personal-account copy of the assigned repository. This folder contains the updated code; copy it into your personal fork and push it there. Do not open a pull request against SETAPESU26.
