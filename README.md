# __Blackjack__
#### Video demo: https://youtu.be/2SC16Yl2Wqs
## Description:
### Introduction
For my CS50p final project, I decided to create a simple, text-based version
of the popular card game, blackjack. My inspiration came from a Discord bot that
allowed users in a group chat to gamble points with games like blackjack and I
wanted to create my own version, purely in Python.

### Implementation
At its eccense, the program continually jumps back and forth between the functions
until the user decides to exit the program. The memory that stores the user's
balance is simply a text file that will be read at the beginning of the program,
and written to and the end.

The few data structures defined at the beginning include: a dictionary which includes
cards of a deck and their corresponding values in blackjack; lists for the dealer's
card, values, and suites; lists for the player's cards, values, and suites.

The function, main(), is only run at the start of the program but never called again.
Its only purpose is to obtain the score using another function, begin_game(), and
prompt the user using choice(). The score is continuously passed from function to
function throughout the program.

The function, begin_game(), opens and reads the text file, balance.txt, which only
stores a single-line int that corresponds to the user's current balance. It then
welcomes the user by printing the user's current balance.

The function, choice(), prompts the user for a valid action (play, exit, load) and
calls the appropriate function. To ensure the programs accepts invalid entries, it
will continue to loop until the user gives proper input.

The function, play(), houses the bulk of the code. First, it prompts the user for
their bet, looping until they provide one that is within their balance. Then, four
cards are randomly drawn using the function, draw_card(), and stored in variables
a, b, c, d. Two cards are added for each the dealer and player cards and the variables
are used as keys to access the index of the dictionary, deck, which are then added
to the dealer and player values. Random suites are also generated for each card using
the function, suite(). Next, the value of the player's card are summed up using the
function, value(), and the value of the dealer's card is only the first one since
the other is hidden from the user. The programs outputs the dealer and player hands
before asking the user what to play (stand or hit). The loop will break if the user
stands or keep going if the user hits. If the user hits, they are allowed to draw a
card as many times as they want until they either stand or get a bust. If they stand,
the programs draws the rests of the card for the dealer until the dealer has a value
above 17. Finally, the final hands of the dealer and player are outputed and a win
or lose message follows depending on the values of the dealer and player. The player
gets points added to their score if the win and function closes by reseting the lists
with the function, reset(), and prompts the user for an action again using the
function, choice().

The function, load(), loops and tries to get a valid integer amount from the user
except if a ValueError is encountered. The user's balance is updated and then prompted
for an action using the function, choice().

Th function, exit(), opens the text file, balance.txt, and overwrites anything
previously in the file with the new user balance. The program then exits and thanks
the user for playing.

The function, bust(), is a subset of the function, play(), when the user decides to
hit and gets a value over 21. When this happens, the rest of the dealer's deck is
drawn and both of the final dealer and player hands are displayed. A message states
that the user has lost and the lists are reset using the function, reset(). The user
is then prompted for an action using the function, choice().

### Testing
One of the major challenges was testing. Since many of the functions didn't rely on
returning values but instead operated on just calling another function, I had to
modify certain parts to ensure Pytest could be used.

Three test functions tested the functions: begin_game() for reading the correct score
from the text file; exit() for raising SystemExit when called; and value() to make sure
the summation function was working properly.

### Further improvements
To make this program even better, certain aspects can be improved. For example, this
version of the program doesn't encompass all the rules of the real blackjack game. It
doesn't have the capability of setting ace to the value of either 1 or 11, you can't
split if you have two cards of equal value, etc.