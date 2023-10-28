### Overview

This Python implementation of the game known as UNCLE BERNIE'S CODEBREAKER GAME
was written to emulate the original game as closely as possible.

The algorithms that I have created were inspired by Bernie and his explanation
of how the original game was coded, for which Bernie has my deepest thanks.

Visit https://www.applefritter.com/content/uncle-bernies-codebreaker-game-apple-1
to read a very detailed account of the original game, by the game author, as well
as hints and tips about how to play the game and some screen shots of the game in
progress. 

There, you will also be able to d/load the Codebreaker game manual (PDF format) as
well as source code files that should run on the the Apple-1 and Apple II computers,
should you wish to do so.

I have written this Python implementation for those that simply want to play the
game without having to run the original binary. 

Python dependencies have been kept to a minimum, but in order to have more of an
authentic experience, I have use the Terminal class object from the `blessed` library.

For more information on that, please use these links:
https://pypi.org/project/blessed/
https://blessed.readthedocs.io/en/latest/terminal.html


### Running the game

In order to run this game, you will need to either grant the `codebrk.py` file
executable permission or load the script through your Python3 interpreter.

The game should be run from a terminal window set to apx 50x25. Although the window
size is not important to the game operation, if you resize the terminal window after
the game has been started, you may experience some issues with display until a few
lines have been written. This because the framework that I have used, needs to figure
out where the insertion point is, in relation to the terminal window size. 

You **should not use the enter or return keys**: once you have typed four letters or 
four feedback symbols, the app will recognize that and move on, without any further
keyboard action. If you make a mistake, you can clear your input by pressing the `Esc`
key, before you type the forth letter/symbol, after which, you are committed to your
input, so you'll need to be mindful of that.

This is what the entry screen should look like, once you have the game up and running.

```
*** UNCLE BERNIE'S CODEBREAKER GAME ***

     0 ROOKIE
     1 MASTER
     2 GENIUS
     H HELP

    ENTER YOUR CHOICE: 
```

To exit the game, press the `Esc` at this point. At no other point in the game can a graceful
exit be called.

As of this date (Oct 28 2023) the only level to have been implemented is the ROOKIE level.
My intention is to implement both the MASTER and the GENIUS levels at some point in the
future, so please watch this space for updates.

The code has been thoroughly tested (10,000+ simulated games) and contains no known bugs.
As such, if you are accused of "cheating", I am 100% sure that you will have made some error
in your feedback to the AI guess of your secret code.

So far (as of the date of this document) this game has only been run on a Linux based OS and
as such, I can't say for sure if it will work correctly on a MS Windows system.

Please enjoy. If you have any comments or feedback, please use this channel.
