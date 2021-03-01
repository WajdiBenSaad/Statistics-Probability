
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
