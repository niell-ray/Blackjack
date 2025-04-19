♠️ Blackjack Game (Python Console App)

This is a fun and interactive Blackjack game built with Python that lets you play against the computer in the console. It simulates the classic card game using Python basics like functions, loops, conditionals, and list manipulation.

🎮 How to Play
	•	You and the computer each get 2 random cards.
	•	You can choose to “hit” (get another card) or “stand” (stop).
	•	The goal is to get a hand value as close to 21 as possible without going over.
	•	A hand with an Ace (11) + 10-point card counts as a Blackjack.
	•	The computer will keep drawing cards until it reaches a score of at least 17.

🃏 Features
	•	Random card dealing with face values (11 for Ace, 10 for Jack/Queen/King)
	•	Handles Blackjack and busts automatically
	•	Compares your final score with the computer’s to determine the winner
	•	Uses a simple loop to replay the game as many times as you’d like
	•	ASCII art logo support via art.py

 Do you want to play a game of blackjack? Type 'y' or 'n': y

Your cards: [10, 6], your score: 16
Computer's 1st card: 8

Type 'y' to hit or 'n' to stand: y

Your final hand is: [10, 6, 5], final score is: 21
Computer's final hand is: [8, 9], computer score is: 17
You win.

🧠 Concepts Used
	•	Randomization (random.choice)
	•	Function definitions & return values
	•	List operations and conditions
	•	Game loops and user input
	•	Score calculation with special rules for Aces and Blackjacks

🛠️ Requirements
	•	Python 3.x
	•	art.py (for ASCII logo display)
