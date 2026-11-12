# Fractal Tree

**Name:** Ayesha Kashaf Aslam<br>
**Registration No:** 515191<br>
**Course:** CS-370 : Artificial Intelligence
**Lab Title:** Lab 01 - Designing Using Fractals

## Description
A fractal tree drawn in Python using recursion. Each branch splits into two
smaller branches until the depth reaches zero.

## Fractal type
Fractal Tree

## Tools
- Python 3
- Turtle (built-in graphics library, no installation needed)

## How to run
1. Install Python 3.
2. Download or clone this repository.
3. Run:
```
python fractal_tree.py
```

## How it works
- `draw_tree(length, depth)` draws a branch, then calls itself twice for the
  left and right branches.
- Each new branch is 75% as long as the one before it.
- Branches turn 25 degrees left and right.
- Recursion stops when `depth` is 0.
- Thick branches are brown and thin ones are green.

## Output
![Output](output.png)
