Please see the Advent of Code site for the problem statement.

Let C be the set of characters '.', '#', and '?'.
Let W be a string of characters from C.
Let G be a list of positive integers, the group sizes of springs.
Let N(W, G) be the number of possible arrangements within W of springs
whose group sizes are in G.

We may evaluate N(W, G) recursively by counting:
    1, those arrangements where the last group of G is at the end of W, plus
    2. all the other arrangements.

Memoization allows us to evaluate N efficiently.
I did a simple version with memoization.

Dynamic programming is also possible.
