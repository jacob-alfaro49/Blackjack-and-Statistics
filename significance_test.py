import auto_blackjack
import math
from scipy.stats import norm

auto_blackjack

x = auto_blackjack.player_wins
y = auto_blackjack.y
alpha = float(input("What alpha level? (ex: 0.05)"))

sample_prop = (x/y)
pop_prop = 0.4608
print(" ")
print(" ")
print(" ")
print(" ")
print("----------------------------------")

#hypotheses
print("Ho: p = 0.4608")
print("Ha: p != 0.4608")
print("Alpha = " + str(alpha))
print("")

#condition check
#random
print("Random Met:")
print("Random is used")
print("")

#independent
if y < 100000:
    print("Independence Met:")
    print("n < 0.10N")
    print("")
else:
    print("Independence Not Met")
    print("n > 0.10N")
    print("")

#large counts
if (sample_prop*y) > 10 and ((1-sample_prop)*y) > 10:
    print("Large Counts Met:")
    print("p*N > 10 and (1-p)*N > 10")
    print("")
else:
    print("Large Counts Not Met")
    print("p*N < 10 and/or (1-p)*N < 10")
    print("")

#do
sd = math.sqrt((pop_prop * (1-pop_prop))/y)
z = (sample_prop - 0.4608)/sd
if z > 0:
    p = 2*(1 - norm.cdf(z))
else:
    p = 2*(norm.cdf(z))
print("Sample Proportion = " + str(sample_prop))
print("Z = " + str(z))
print("Standard Deviation = " + str(sd))
print("P-value = " + str(p))
print("")

print("Conclusion:")
if p > alpha:
    print("Since the P-value " + str(p) + " is greater than alpha = " + str(alpha) + " we fail to reject the null.")
    print("There is not significant evidence that the true percent chance to win a blackjack game is different from " + str(pop_prop) + ".")
else:
    print("Since the P-value " + str(p) + " is less than alpha = " + str(alpha) + " we reject the null.")
    print("There is significant evidence that the true percent chance to win a blackjack game is different from " + str(pop_prop) + ".")