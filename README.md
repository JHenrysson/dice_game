## Dice_Game



A two player game designed to be played with a friend or against the computer. 
In this game there is a six faced die that is used. 
The players will take turns rolling a six face die until 
someone reaches one-hundred and wins the game. This game was developed 
by students at HKR. 


### Prerequisites

Python 3.7 -- [instructions here](https://www.python.org/downloads/)

Download this repository 


### Getting Started ###

In the console type in the following 
commands one at a time to run this program 


This command changes the directory to dice 

``cd dice ``

Creates the make file 

 ``make ``

This command starts the game 

``python main.py``


### Rules of the Game 

In this game each player takes turns rolling the six face die. In this game the player can 
decide to play with a friend or against the computer.

Each player has two options roll or hold
<br>
If a player decides to hold then it is the next players turn  <br>
If the player rolls and gets a number 2-6 it is added to their total score 
<br>
If the player rolls and gets a 1 their score is 0 
<br>
<br>
The first one to reach 100 wins the game 

**Playing against the computer**

If the player plays against the computer the same rules apply. 
But the player can choose difficulty level EASY or HARD. This is decided 
at the beginning of the game. 

The first one to reach 100 wins the game 

### Guide to play game using commands

Before starting a game, player has to create a name with this command:

``create_player <player1_name>``

The next step is to register the name in to the game by command:

``add_player <player1_name>``

After that the player can choose one of the option below:

The player want to play against the computer, there are 2 difficulty:

``difficulty easy`` or ``difficulty hard``

Or, the player want to play against another player:

``create_player <player2_name>``
then
``add_player <player2_name>``

The player after doing those steps above, now can start a game by writing command:

``start``

The player1 shall play first, either roll or hold:

``roll`` or ``hold``

The next turn is belonged to player2, the same command above roll or hold
If the player1 plays against the machine, the machine shall automatically decide to
roll or hold based the difficulty setting in the beginning.
The game stop when either one player or machine reachs 100 score or the player decides to
stop the game.

To stop the game, player can use this command and no score shall be recorded because the game 
has not finished yet:

``exit``

If player makes wrong moves and want to restart the game:

``restart``

If player forgets the rule, type this command:

``show rule``

To see the command list type:

``help``

If the player want to cheat, and get 100 procents chance to get 99 point, type this command:

``cheat``

To delete player who is not in the game

``delete_player <player_name>``

To remove player who is already registered in the game

``remove_player <player_name>``

To change name of player, type this command:

``change_name <player_old_name> <player_new_name>``



### Running the Tests 

To check test coverage follow these steps 

``make install test coverage``

### UML & Package Diagrams 

Instructions for generating diagrams 
<br> 
To view the diagrams use this link 

[UML & Package Diagrams](https://jhenrysson.github.io/dice_game/)


**To Generate the UML & Package Diagrams**

Run these commands in terminal 

To ensure on correct directory 
<br>

``cd dice``

Next 

``make pyreverse``
<br>

This command creates two .dot files, one for classes and one for packages. 
These are converted into two png files located in doc/pyreverse.


### Generating Documentation 
For this project **make doc** is used
In the console type in the following commands 
<br>

To make sure you are on the correct directory
<br>

``cd dice ``
<br>

Next <br>

``make doc``

This should generate html files in the projects folder. 
You can view these files in your IDE or opening them
in the browser

### Technologies Used 
Python <br>


### Authors
   Paul John Miller,  Xuan Tran, Joselyn Godoy <br>

### Releases 

Will add when tags are uploaded 
<br>

<br> 
 

### License 

This project is licensed under the MIT License - see the [MIT](https://github.com/JHenrysson/dice_game/blob/joselyn_turn/LICENSE) file for details



