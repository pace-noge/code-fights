
"""
With which foot should I step on the nth crack?

Ever since I was young, I used a pattern to decide with which foot I should step on the next crack in the ground. My goal was to 'balance', to the greatest extent possible, the number of times I stepped on cracks with each foot.

If the first time I stepped on a crack it was with my left foot, then the next time I stepped on the crack it would have to be with my right foot, so that I 'balanced' the fact that the left foot had already stepped on one.

Then the third time I stepped on a crack, it was again with my right foot, since even though each foot had had a turn, I had stepped with my left foot first, which was not completely 'balanced.' Now I had stepped twice with my right foot and once with my left foot, so in order to 'balance', the fourth time I would again step with my left foot.

Only when I was 21 years old and sitting in a course called Chaos Theory and Fractal Geometry in college, did I learn that this was actually a special pattern: the Thue-Morse sequence.

Given the first foot with which I stepped on a crack, find the foot with which I should step on the nth crack.

Example

For step = "left" and n = 2, the output should be
stepOnCrack(step, n) = "right".
For step = "right" and n = 3, the output should be
stepOnCrack(step, n) = "left".
Since the first time I step on the crack with my right leg, the second and the third steps will be made with my right leg.

[input] string first

The first foot with which I stepped on a crack. Either "left" or "right".

[input] integer n

The 1-based number of the crack on which I will step, 2 ≤ n ≤ 50.

[output] string

The foot with which I should step on the nth crack. Either "left" or "right".
"""

def stepOnCrack(f, n):
    x = [f]
    while len(x) < n:
        x += ["right" if i == "left" else "left" for i in x]
    return x[n-1]