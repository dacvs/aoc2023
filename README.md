# Advent of Code 2023
## Solutions by David Smith
## dsmith@alumni.caltech.edu

I participated in Advent of Code 2023,
competing with 17 other participants on a private leaderboard.
I entered the contest a couple weeks late,
and I missed out on the opportunity to gain some early points.

On March 31, 2024, I was first on our leaderboard to solve all 50
problems, with 660 points. I was first to finish, but only second
place in points when I finished.

Here are my solutions, cleaned up, straightened out, and edited for
consistency. I used **Python** only.
Occasionally I experimented with other tools, including SymPy and
Sage Mathematics, before I switched back to Python.

The only library I really needed was NumPy.
In places where I used other libraries (`import sys`, `import math`,
`import random`), I have edited my solutions to use **NumPy only**.

TODO verify claim NumPy only.

This was my first time participating in Advent of Code. Problems were
easy at first. I solved many of them that first Saturday.
I solved many problems before I ever received a "wrong answer" message.
I solved many problems before I ever defined a function.
I defined only one class, and I could easily do without that definition.
I edited my solutions to use **no classes**.

TODO verify claim no classes.

- Problem 24 part 2 was hardest for me.

- Problem __ (TODO the infinite grid one) was tough, as there were
many little details to worry about.

- Problem 25 is the one where I had to learn something new
(Karger's algorithm).

TODO hyperlinks to selected problems

If you want to run my scripts, you will need Python.
I used Python 3.10, but any recent Python should work.
You should find the problem statement and problem inputs at the
Advent of Code web site.
Record your problem input in a file named
"input.txt" so that my script can find it.
TODO update input loc

Congratulations to Eric Wastl on creating a nice set of problems
for this competition. The visual presentation is impressive.

## Comments

### Day 2

We don't need regular expressions. Python's `str.split()` is fine.

### Day 3

NumPy arrays. Why not?

### Day 4

Keep it simple.

### Day 12

Please see the Advent of Code site for the problem statement.

Let C be the set of characters '.', '#', and '?'.
Let W be a string of characters from C.
Let G be a list of positive integers, the group sizes of springs.
Let N(W, G) be the number of possible arrangements within W of springs
whose group sizes are in G.

We may evaluate N(W, G) recursively by counting:
1. those arrangements where the last group of G is at the end of W, plus
2. all the other arrangements.

Memoization allows us to evaluate N efficiently.
My simple implementation uses memoization.

Dynamic programming is also possible.

### Day 14

In part 1, we may tally the load without moving any rocks around.

In part 2, we have to move rocks around, as far as I can tell.
We can do a northward tilt in linear time.

### Day 25

I don't recall ever reading about Karger's algorithm until my first efforts toward
solving this problem were too slow.
