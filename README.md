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
### Running the Tests 

To check test coverage follow these steps 

``make install test coverage``

### UML & Package Diagrams 

Instructions for generating diagrams 
<br> 
To view the diagrams use this link 

[Diagrams](link goes here)


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



