# Advanced Tic-Tac-Toe

## Video Demo: <URL HERE>

## Description:

The Advanced Tic-Tac-Toe is just like the classic Tic-Tac-Toe game, except it has some additional features like the option to select playing modes(Singleplayer, or Multiplayer), Leaderboards, and viewing the stats of each player after each match.
The Termcolor library has been used to provide color to "X" and "O"'s as well as the winner and the losers. The Art library has been used to write the title of the game in ACSII art. The Tabulate package has been used to tabulate the entire game, as well as the Leaderboard and Stats.

### pip installable libraries used: Art, Tabulate, Termcolor

## How to play?:

The game can be played in total of two modes: Singleplayer and multiplayer.

<ul>
<li> First, clone this project repository into your device. </li>
<li> Install all the required libraries from https://pypi.org/ </li>
<li> Run `python game.py` </li>
<li> Choose whatever mode you'd like to play in by selecting either of options 1 or 2.</li>
<li> To view the leaderboard, choose option 3.</li>
<li> While in a game, type in your name and a "X" or "O" seperated by a whitespace to select your character, then the opponent will be prompted to enter their name and choice in a similar fashion(In case of Singleplayer mode, there won't be a second prompt).</li>
<li> After finishing a game, you can choose to view your and your opponents stats(wins,losses,draws).</li>
<li> If you plan to exit the game at any point, you can `Ctrl+C` to exit. </li>

### NOTE: You dont necessarily need to have a stats.csv file in your directory for the leaderboard. The game will do it for you.
