"""
Program Name: trivia game
Author: zachary ostheimer
Purpose: Single player trivia game covering the content  I have  learned pursing my b.s. in ChemE. The player picks a category then answers ten
         questions of increasing difficulty to earns points with a streak bonus and loses a life for each wrong answer. The game tracks stats across 
         rounds and prints a summary when the player quits.
Starter Code: None
Date: 06/28/2026

"""

import random

quiz = {
    "Math": [
        {"question": "What is the derivative of x^3 with respect to x?",
         "options": ["3x^2", "x^2", "3x", "x^4/4"], "answer": "3x^2"},
        {"question": "What is the integral of 1/x dx?",
         "options": ["x^-2 + C", "ln|x| + C", "1 + C", "-1/x^2 + C"], "answer": "ln|x| + C"},
        {"question": "What is the value of the limit of sin(x)/x as x -> 0?",
         "options": ["0", "Infinity", "1", "Undefined"], "answer": "1"},
        {"question": "Which method solves a system of linear equations using matrices?",
         "options": ["Euler's method", "Gaussian elimination", "Newton's method", "Simpson's rule"], "answer": "Gaussian elimination"},
        {"question": "The Taylor series of e^x around 0 has what general term?",
         "options": ["x^n", "x^n / n!", "n! / x^n", "(-1)^n x^n"], "answer": "x^n / n!"},
        {"question": "What is the general solution form for dy/dx = ky?",
         "options": ["y = kx + C", "y = Ce^(kx)", "y = C/x", "y = k ln(x)"], "answer": "y = Ce^(kx)"},
        {"question": "For a function f(x,y), what does the partial derivative df/dx hold constant?",
         "options": ["x", "y", "Both x and y", "Neither"], "answer": "y"},
        {"question": "What does the divergence of a vector field measure?",
         "options": ["Rotation", "Net outward flux per unit volume", "Arc length", "Curvature"], "answer": "Net outward flux per unit volume"},
        {"question": "A 2nd-order linear ODE with constant coefficients is solved using which equation?",
         "options": ["The characteristic equation", "The continuity equation", "Bernoulli's equation", "The secant equation"], "answer": "The characteristic equation"},
        {"question": "The Laplace transform of the derivative f'(t) equals what (with f(0))?",
         "options": ["F(s)/s", "sF(s) - f(0)", "s^2 F(s)", "F(s) + f(0)"], "answer": "sF(s) - f(0)"},
    ],
    "Chemistry": [
        {"question": "What is the pH of a neutral aqueous solution at 25 C?",
         "options": ["0", "7", "14", "1"], "answer": "7"},
        {"question": "What is Avogadro's number (approximately)?",
         "options": ["6.022 x 10^23", "3.14 x 10^8", "1.602 x 10^-19", "8.314"], "answer": "6.022 x 10^23"},
        {"question": "In an exothermic reaction, what is the sign of the enthalpy change?",
         "options": ["Positive", "Negative", "Zero", "Undefined"], "answer": "Negative"},
        {"question": "What type of bond involves the sharing of electron pairs?",
         "options": ["Ionic", "Covalent", "Metallic", "Hydrogen"], "answer": "Covalent"},
        {"question": "Which quantum number describes the shape of an orbital?",
         "options": ["Principal (n)", "Azimuthal (l)", "Magnetic (m_l)", "Spin (m_s)"], "answer": "Azimuthal (l)"},
        {"question": "According to Le Chatelier's principle, increasing pressure shifts equilibrium toward what?",
         "options": ["More moles of gas", "Fewer moles of gas", "No change ever", "Solid phase only"], "answer": "Fewer moles of gas"},
        {"question": "What is the rate law order overall for rate = k[A][B]^2?",
         "options": ["First order", "Second order", "Third order", "Zero order"], "answer": "Third order"},
        {"question": "In an SN2 reaction, the rate depends on what?",
         "options": ["Substrate only", "Nucleophile only", "Both substrate and nucleophile", "Neither"], "answer": "Both substrate and nucleophile"},
        {"question": "The Nernst equation relates cell potential to what?",
         "options": ["Temperature only", "Reaction quotient and concentration", "Pressure only", "Bond energy"], "answer": "Reaction quotient and concentration"},
        {"question": "Which functional group characterizes a carboxylic acid?",
         "options": ["-OH", "-CHO", "-COOH", "-NH2"], "answer": "-COOH"},
    ],
    "Physics": [
        {"question": "What is Newton's second law of motion?",
         "options": ["F = ma", "E = mc^2", "F = mv", "P = IV"], "answer": "F = ma"},
        {"question": "What is the SI unit of force?",
         "options": ["Joule", "Watt", "Newton", "Pascal"], "answer": "Newton"},
        {"question": "What quantity is conserved in an elastic collision?",
         "options": ["Only momentum", "Only kinetic energy", "Both momentum and kinetic energy", "Neither"], "answer": "Both momentum and kinetic energy"},
        {"question": "What is the kinetic energy of an object of mass m moving at speed v?",
         "options": ["mv", "(1/2)mv^2", "mgh", "mv^2"], "answer": "(1/2)mv^2"},
        {"question": "Ohm's law relates voltage, current, and what?",
         "options": ["Power", "Resistance", "Capacitance", "Charge"], "answer": "Resistance"},
        {"question": "What does Gauss's law relate electric flux to?",
         "options": ["Magnetic field", "Enclosed charge", "Current", "Inductance"], "answer": "Enclosed charge"},
        {"question": "For simple harmonic motion, the period of a mass-spring system depends on mass and what?",
         "options": ["Amplitude", "Spring constant", "Gravity", "Velocity"], "answer": "Spring constant"},
        {"question": "What is the moment of inertia a rotational analog of?",
         "options": ["Velocity", "Mass", "Force", "Energy"], "answer": "Mass"},
        {"question": "Faraday's law states that an induced EMF is proportional to the rate of change of what?",
         "options": ["Electric field", "Magnetic flux", "Charge", "Resistance"], "answer": "Magnetic flux"},
        {"question": "In the Bohr model, electron energy levels are described as what?",
         "options": ["Continuous", "Quantized", "Random", "Zero"], "answer": "Quantized"},
    ],
    "Statistics": [
        {"question": "What measure of central tendency is the most frequent value?",
         "options": ["Mean", "Median", "Mode", "Range"], "answer": "Mode"},
        {"question": "What does standard deviation measure?",
         "options": ["Central value", "Spread of data", "Sample size", "Correlation"], "answer": "Spread of data"},
        {"question": "A probability value must fall between which two numbers?",
         "options": ["-1 and 1", "0 and 1", "0 and 100", "1 and 10"], "answer": "0 and 1"},
        {"question": "The normal distribution is also commonly known as what?",
         "options": ["Uniform curve", "Bell curve", "Skewed curve", "Step function"], "answer": "Bell curve"},
        {"question": "What does a p-value below 0.05 typically indicate?",
         "options": ["Accept the null hypothesis", "Statistical significance", "No effect", "A measurement error"], "answer": "Statistical significance"},
        {"question": "In linear regression, R^2 represents what?",
         "options": ["Slope of the line", "Fraction of variance explained", "Sample mean", "The intercept"], "answer": "Fraction of variance explained"},
        {"question": "The Central Limit Theorem states that sample means approach what distribution?",
         "options": ["Uniform", "Normal", "Exponential", "Binomial"], "answer": "Normal"},
        {"question": "Which distribution models the number of successes in fixed independent trials?",
         "options": ["Poisson", "Binomial", "Normal", "Geometric"], "answer": "Binomial"},
        {"question": "A Type I error in hypothesis testing is what?",
         "options": ["Rejecting a true null hypothesis", "Accepting a false null", "A sampling bias", "A rounding error"], "answer": "Rejecting a true null hypothesis"},
        {"question": "The Poisson distribution is best used to model what?",
         "options": ["Continuous heights", "Rare events over an interval", "Coin flips", "Paired t-tests"], "answer": "Rare events over an interval"},
    ],
    "Thermodynamics": [
        {"question": "What does the first law of thermodynamics express?",
         "options": ["Entropy always increases", "Conservation of energy", "Absolute zero is unreachable", "PV = nRT"], "answer": "Conservation of energy"},
        {"question": "In the ideal gas law PV = nRT, what does R represent?",
         "options": ["Rate constant", "Universal gas constant", "Resistance", "Reaction quotient"], "answer": "Universal gas constant"},
        {"question": "The second law of thermodynamics deals with which property?",
         "options": ["Enthalpy", "Entropy", "Pressure", "Volume"], "answer": "Entropy"},
        {"question": "An adiabatic process is one in which what is true?",
         "options": ["No heat transfer", "Constant pressure", "Constant temperature", "No work done"], "answer": "No heat transfer"},
        {"question": "Enthalpy H is defined as which expression?",
         "options": ["U + PV", "U - TS", "PV - nRT", "Q - W"], "answer": "U + PV"},
        {"question": "For a spontaneous process at constant T and P, Gibbs free energy change is what?",
         "options": ["Positive", "Negative", "Zero", "Infinite"], "answer": "Negative"},
        {"question": "The efficiency of a Carnot engine depends only on what?",
         "options": ["Working fluid", "The two reservoir temperatures", "Pressure ratio", "Engine size"], "answer": "The two reservoir temperatures"},
        {"question": "Which equation of state corrects the ideal gas law for real gases?",
         "options": ["Bernoulli equation", "Van der Waals equation", "Clausius-Clapeyron", "Antoine equation"], "answer": "Van der Waals equation"},
        {"question": "At a pure substance's critical point, which phases become indistinguishable?",
         "options": ["Solid and liquid", "Liquid and vapor", "Solid and vapor", "All three"], "answer": "Liquid and vapor"},
        {"question": "Fugacity is best described as which of the following?",
         "options": ["An effective partial pressure", "A type of entropy", "Heat capacity ratio", "A rate constant"], "answer": "An effective partial pressure"},
    ],
}

#A dictionary maps each category name to a list of question dictionaries, and each question stores its correct answer as TEXT so the option order can be
# shuffled safely at display time

BASE_POINTS = 10        # points for any correct answer
STARTING_LIVES = 3      # wrong answers allowed before a round ends early
STREAK_FOR_BONUS = 3    # correct answers in a row needed to start earning a bonus
BONUS_POINTS = 5        # extra points added once the streak bonus is active
session_stats = {"total_correct": 0, "total_asked": 0, "total_score": 0}
print("        CHEM-E TRIVIA CHALLENGE")
print("=" * 45)
print("Answer 10 questions per category. They get harder")
print("as you go. Each correct answer is worth", BASE_POINTS, "points.")
print("Get", STREAK_FOR_BONUS, "in a row to earn a +" + str(BONUS_POINTS), "streak bonus!")
print("You have", STARTING_LIVES, "lives per round. Good luck!")
print()

#sets starting values at 0s, sets the constant values for the game and displays intro screen

keep_playing = True
while keep_playing:
 
    print("-" * 45)
    print("Choose a category:")
    category_names = list(quiz.keys())
    #turn the keys into an indexable list so a number can map to a category
    menu_number = 1
    for name in category_names:
        print("   " + str(menu_number) + ") " + name)
        menu_number += 1
    print("   " + str(len(category_names) + 1) + ") Quit")
 
    while True:
        pick = input("Enter your choice: ")
        if pick.isdigit() and 1 <= int(pick) <= len(category_names) + 1:
            pick = int(pick)
            break
        else:
            print("   Please enter a number from the menu.")
    #keep asking until the menu choice is a valid number
 
    if pick == len(category_names) + 1:
        keep_playing = False
        continue
    #the quit option is the last menu number
 
    chosen_category = category_names[pick - 1]
    questions = quiz[chosen_category]
    #set up the chosen round from the picked category
    print()
    print("*** " + chosen_category + " round ***")
    print()
 
    lives = STARTING_LIVES
    streak = 0
    round_score = 0
    round_correct = 0
    question_count = 0
    #per round trackers reset at the start of each category
 
    for question in questions:
        question_count += 1
        session_stats["total_asked"] += 1
        #loop through the 10 questions in order
 
        correct_text = question["answer"]
        shuffled_options = question["options"][:]
        random.shuffle(shuffled_options)
        #copy the options with [:] and shuffle the copy so the bank stays intact
 
        print("Q" + str(question_count) + " | Lives:", lives, "| Streak:", streak)
        print(question["question"])
        number = 1
        for option in shuffled_options:
            print("   " + str(number) + ") " + option)
            number += 1
        #show the question header then number the shuffled options
 
        while True:
            choice = input("Your answer (1-" + str(len(shuffled_options)) + "): ")
            if choice.isdigit() and 1 <= int(choice) <= len(shuffled_options):
                choice = int(choice)
                break
            else:
                print("   Please enter a number between 1 and", len(shuffled_options))
        #keep asking until the answer is a real choice
 
        picked_text = shuffled_options[choice - 1]
        #convert the player's number back into the option text they picked

        if picked_text == correct_text:
            streak += 1
            round_correct += 1
            session_stats["total_correct"] += 1
            #a correct answer grows the streak and the correct counters
 
            earned = BASE_POINTS
            if streak >= STREAK_FOR_BONUS:
                earned += BONUS_POINTS
                print("Correct! +" + str(earned), "(streak bonus!) Streak is now", streak)
            else:
                print("Correct! +" + str(earned) + ". Streak is now", streak)
            #award base points plus a bonus 
 
            round_score += earned
            session_stats["total_score"] += earned
        else:
            lives -= 1
            streak = 0
            print("Wrong. The answer was:", correct_text + ".", "Lives left:", lives)
            #a wrong answer costs a life and resets the streak
 
        print()
 
        if lives == 0:
            print("Out of lives! The", chosen_category, "round is over.")
            print()
            break
        #end the round early if the player is out of lives
 
    print("--- Round Summary (" + chosen_category + ") ---")
    print("Correct this round:", round_correct, "out of", question_count)
    print("Points this round:", round_score)
    print()
    #display how the player did this round
 
    while True:
        again = input("Play another category? (y/n): ").lower()
        if again == "y" or again == "n":
            break
        else:
            print("   Please type y or n.")
    print()
    if again == "n":
        keep_playing = False
    #ask whether to play again accepting only y or n

print("=" * 45)
print("            FINAL SESSION SUMMARY")
print("=" * 45)
print("Total questions answered:", session_stats["total_asked"])
print("Total correct:", session_stats["total_correct"])
print("Total score:", session_stats["total_score"])
 
if session_stats["total_asked"] > 0:
    percent = session_stats["total_correct"] / session_stats["total_asked"] * 100
    print("Accuracy:", round(percent, 1), "percent")
else:
    print("Accuracy: no questions answered.")
#show the percentage 
 
print("Thanks for playing!")