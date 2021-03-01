
'''
Poker.. probability and chance
'''

# the probability of drawing an Ace from a poker deck:

    
# Sample Space
cards = 52

# Outcomes
aces = 4

# Divide possible outcomes by the sample set
ace_probability = aces / cards

# Print probability rounded to two decimal places
print(round(ace_probability, 2))

# Ace Probability Percent Code
ace_probability_percent = ace_probability * 100

# Print probability percent rounded to one decimal place
print(str(round(ace_probability_percent, 0)) + '%')



# Create function that returns probability percent rounded to one decimal place

def event_probability(event_outcomes, sample_space):
    probability = round((event_outcomes / sample_space) * 100,2)
    
    return(probability)

    
# Sample Space
cards = 52

# Determine the probability of drawing a heart
hearts = 13
heart_probability = event_probability(hearts, cards)

# Determine the probability of drawing a face card
face_cards = 12
face_card_probability = event_probability(face_cards, cards)

# Determine the probability of drawing the queen of hearts
queen_of_hearts = 1
queen_of_hearts_probability = event_probability(queen_of_hearts, cards)

# Print each probability
print(str(heart_probability) )
print(str(face_card_probability) )
print(str(queen_of_hearts_probability) )


#Probability with Combinations and Permutations
# =============================================

# Permutations Code
import math
n = 4
k = 2

# Determine permutations and print result
Permutations = math.factorial(n) / math.factorial(k)

print(Permutations)

'''
finding the number of starting hand combinations 
that can be dealt in Texas Hold’em.
'''



# Combinations Code
n = 52
k = 2

# Determine Permutations
Permutations = math.factorial(n) / math.factorial(n - k)

# Determine Combinations and print result
Combinations = Permutations / math.factorial(k)
print(Combinations)


'''
the probability of drawing an Ace on the second draw, 
if the first card drawn was either a King or an Ace:

'''

# Sample Space
cards = 52
cards_drawn = 1 
cards = cards - cards_drawn 

# Determine the probability of drawing an Ace after drawing a King on the first draw
aces = 4
ace_probability1 = event_probability(aces, cards)

# Determine the probability of drawing an Ace after drawing an Ace on the first draw
aces_drawn = 1
aces = aces - aces_drawn
ace_probability2 = event_probability(aces, cards)

# Print each probability
print(ace_probability1)
print(ace_probability2)



#### simulating a coin toss
import random
def coin_trial():
    heads = 0
    for i in range(100):
        if random.random() <= 0.5:
            heads +=1
    return heads

def simulate(n):
    trials = []
    for i in range(n):
        trials.append(coin_trial())
    return(sum(trials)/n)

simulate(10)
