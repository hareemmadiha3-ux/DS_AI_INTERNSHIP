# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

# -------------------------------
# Task 1: Customer Click Analysis
# -------------------------------

def customer_click_probability():
    actions = ["Click", "Scroll", "Exit"]
    
    # Define sample space S
    S = [(a1, a2) for a1 in actions for a2 in actions]
    
    # Define event E: at least one Click
    E = [outcome for outcome in S if "Click" in outcome]
    
    probability = len(E) / len(S)
    
    print("Sample Space S:")
    print(S)
    
    print("\nEvent E (at least one Click):")
    print(E)
    
    print("\nProbability of at least one Click:")
    print(probability)


# -------------------------------
# Task 2: Dice Simulation
# -------------------------------

def dice_simulation(trials=1000):
    count_sum_7 = 0
    
    for _ in range(trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        
        if die1 + die2 == 7:
            count_sum_7 += 1
    
    experimental_probability = count_sum_7 / trials
    
    print("\nDice Simulation Results")
    print("Number of trials:", trials)
    print("Number of times sum was 7:", count_sum_7)
    print("Experimental probability:", experimental_probability)


# -------------------------------
# Main Execution
# -------------------------------

if __name__ == "__main__":
    customer_click_probability()
    dice_simulation(1000)


# --------------------------------
# Task 2: Independent vs Dependent Events
# --------------------------------

def independent_events():
    # Coin toss and dice roll
    p_heads = 1 / 2
    p_six = 1 / 6

    p_independent = p_heads * p_six

    print("Independent Event:")
    print("P(Heads and 6) =", p_independent)


def dependent_events():
    # Drawing two red marbles without replacement
    total_marbles = 10
    red_marbles = 5

    p_red1 = red_marbles / total_marbles
    p_red2 = (red_marbles - 1) / (total_marbles - 1)

    p_dependent = p_red1 * p_red2

    print("\nDependent Event:")
    print("P(Both Red) =", p_dependent)


# -------------------------------
# Main Execution
# -------------------------------

if __name__ == "__main__":
    independent_events()
    dependent_events()

# --------------------------------
# Task 3: Bayes' Theorem (Spam Detection)
# --------------------------------

def bayes_spam_classifier():
    # Prior probabilities
    P_spam = 0.1
    P_ham = 0.9

    # Likelihood probabilities
    P_free_given_spam = 0.9
    P_free_given_ham = 0.05

    # Total probability of the word "Free"
    P_free = (P_free_given_spam * P_spam) + (P_free_given_ham * P_ham)

    # Bayes' Theorem
    P_spam_given_free = (P_free_given_spam * P_spam) / P_free

    print("Total Probability of 'Free':", round(P_free, 4))
    print("Probability the email is Spam given it contains 'Free':",
          round(P_spam_given_free, 4))


# -------------------------------
# Main Execution
# -------------------------------

if __name__ == "__main__":
    bayes_spam_classifier()
