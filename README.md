# Advent of Code 2023
## Solutions by David Smith
## dsmith@alumni.caltech.edu

I participated in Advent of Code 2023,
competing with 17 others on a private leaderboard.
I entered the contest a couple weeks late,
and I missed out on some early points.

On March 31, 2024, I was first on our leaderboard to solve all 50
problems, with 660 points. First to finish, but only second
place in points when I finished.

## Python + NumPy only, no classes

Here are my solutions, cleaned up, straightened out, and edited for
consistency. I used **Python only**.
Occasionally I experimented with other tools, including SymPy and
Sage Mathematics, before I switched back to Python.

The only library I really needed was NumPy. In places where I used other libraries,
I have edited my solutions to use **NumPy only**.

To be clear, I spell out my arbitrary "NumPy only" rule with a few examples:
- `import sys` is forbidden. No libraries but NumPy, not even imports of the standard library.
- `import math` is forbidden. Same reason.
- `import random` is forbidden. Same reason.
- `import d03` is ok. This module `d03` contains my code for day 3 that is shared by my solutions to parts 1 and 2 of day 3.
- `import lib` is ok. This module `lib` contains my code that is available to all my solutions.

TODO verify claim NumPy only.

This was my first time participating in Advent of Code. Problems were
easy at first. I solved many of them that first Saturday.
I solved many problems before I ever received a "wrong answer" message.
I solved many problems before I ever defined a function.
I defined only one class, and I could easily do without that definition, so
I have edited my solutions to use **no classes**.

TODO verify claim no classes.

- [Problem 24 part 2](#day-24) was hardest for me.

- [Problem 21](#day-21) was tough, as there were many little details to worry about.

- For [problem 25](#day-25), I had to learn something new.

Congratulations to Eric Wastl on creating a nice set of problems
for this competition. The visual presentation is impressive.

## Running

If you want to run my scripts, you will need Python.
I used Python 3.10, but any recent Python should work.
You should find the problem statement and problem inputs at the
Advent of Code web site.
Record your problem inputs, one file per day, in files named
"input/01.txt", "input/02.txt", and so on.
Then run `python3 d01p1.py`, for example.

## Comments

### Day 2

We don't need regular expressions. Python's `str.split()` is fine.

### Day 3

NumPy arrays. Why not?

### Day 4

Keep it simple.

### Day 6

In part 2, some of the numbers involved are fairly large, possibly too large
for 64-bit floats.
This worked fine for me:

```python
D = t * t - 4 * d
R = (t + np.sqrt(D)) / 2
r = (t - np.sqrt(D)) / 2
print("ans", int(np.floor(R) - np.ceil(r) + 1))
```

But this may not work well for (larger) inputs other than mine.
Plain old Python's `math.isqrt()` (integer square root) may work,
but my (arbitrary) policy allows no libraries but NumPy.
I wrote my own `isqrt()` as in [Wikipedia](https://en.wikipedia.org/wiki/Integer_square_root#Algorithm_using_binary_search).

### Day 12
Please see the Advent of Code site for the [problem statement](https://adventofcode.com/2023/day/12).

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

### Day 19

In part 2, we begin with a large 4D ("xmas") space and chop it up just enough
to follow the rules.

### Day 20

Each pulse is Hi or Lo.
When a module sends a pulse, it sends that type of pulse to each of its
destination modules.

Flip-flop module (prefix "%") is on or off, initially off.
 When it receives Hi, it does nothing.
 When it receives Lo, it flips between on, off.
 If it was off, it turns on and sends Hi.
 If it was on, it turns off and sends Lo.

Conjunction module (prefix "&") remembers the type of the most recent pulse
received from each input module.
Initially remembers Lo.
When a pulse is received, the module first updates its memory for that input.
Then if it remembers all Hi, it sends Lo. Otherwise sends Hi. (Like Nand).

Broadcast module (only one exists).
When it receives a pulse, sends the same pulse to all its destinations.

Button module when pushed emits Lo to broadcast module.
After pushing button, must wait till all pulses delivered before pushing again.

Pulses processed in the order sent.

### Day 23

The following example input is given in the problem statement.
Enter at the top and exit at the bottom, obeying the arrows.

    #.#####################
    #.......#########...###
    #######.#########.#.###
    ###.....#.>.>.###.#.###
    ###v#####.#v#.###.#.###
    ###.>...#.#.#.....#...#
    ###v###.#.#.#########.#
    ###...#.#.#.......#...#
    #####.#.#.#######.#.###
    #.....#.#.#.......#...#
    #.#####.#.#.#########v#
    #.#...#...#...###...>.#
    #.#.#v#######v###.###v#
    #...#.>.#...>.>.#.###.#
    #####v#.#.###v#.#.###.#
    #.....#...#...#.#.#...#
    #.#########.###.#.#.###
    #...###...#...#...#.###
    ###.###.#.###v#####v###
    #...#...#.#.>.>.#.>.###
    #.###.###.#.###.#.#v###
    #.....###...###...#...#
    #####################.#

To make things clearer at start and finish, I add two arrows as follows.

    #v#####################
    #.......#########...###
    #######.#########.#.###
    ###.....#.>.>.###.#.###
    ###v#####.#v#.###.#.###
    ###.>...#.#.#.....#...#
    ###v###.#.#.#########.#
    ###...#.#.#.......#...#
    #####.#.#.#######.#.###
    #.....#.#.#.......#...#
    #.#####.#.#.#########v#
    #.#...#...#...###...>.#
    #.#.#v#######v###.###v#
    #...#.>.#...>.>.#.###.#
    #####v#.#.###v#.#.###.#
    #.....#...#...#.#.#...#
    #.#########.###.#.#.###
    #...###...#...#...#.###
    ###.###.#.###v#####v###
    #...#...#.#.>.>.#.>.###
    #.###.###.#.###.#.#v###
    #.....###...###...#..v#
    #####################.#

In part 2, I keep the weights of heaviest paths over a large domain
(vertex sets with a spanning path to the End).
This takes a lot of memory, nearly 4 GB on my machine.
It would be nice to shrink that down without complicating the algorithm.
On the other hand, most people these days have 4 GB lying around.

### Day 24

Part 2 wasn't obvious to me.
I tried many ideas before I found one that worked.

The solution trajectory traces a line that meets the trajectory lines of all the inputs.
There should be a unique line containing the solution trajectory, provided the input is
"nondegenerate." (It is easy to verify that the input is nondegenerate.) It should be
straightforward to derive the solution trajectory from the unique line, so the hard part
is to find the (unique) line.

This problem (of finding a line that meets many other given lines in 3D space) seems like
a least-squares problem. I did not manage to cast it as a least-squares problem. However,
if we consider it as a more general problem of optimization (find a line near as possible
to many other lines), it is easy to imagine that there are only a few independent variables
(I brought it down to 2 real variables), and there should be a well-behaved objective
function, so that a simple method like gradient descent should work.

I cooked up an objective function. I went to compute the gradient exactly, but this
was nontrivial. Instead I did an axis-aligned search, constrained to the nonnegative
quadrant, in the plus and minus directions along each axis at distances
1, 10, ..., 1 billion or so, and this method of search quickly found the solution.

### Day 25

My first efforts toward solving this problem ran too slowly.
I searched for algorithms that find small cuts.
I found Karger's algorithm, which is remarkably simple.
