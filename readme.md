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

### Extras

Because this is a challenging game, at first, you may find it hard to concentrate on both
working out what your next best guess should be, as well as working out what your correct
response should be to the AI best guess. Getting this wrong, will result in you being accused
of cheating, at which point you will forfeit the game. As this can be a source of frustration,
I have provided a small helper script, that will provide the correct response for any given
secret code/guess combination.

My understanding is that with the original game, the order in which the feedback symbols
are entered, is unimportant (so, `++*-` is as good as `*++-`). This has been retained in
my implementation of the game, but a purest will tell you that the order should always be
entered as `*` `+` `-` as the priority order. 


### Game play hints and tips

If you wait for the AI first best guess, before you decide on what your secret code will be,
you can gain a slight advantage by basing your code on the AI first best guess.

As an example, if the AI first best guess happens to be `ECEC`, then make sure that you
choose a secret code that contains one of those letters, in the correct position, because,
if it does not, your response will have to be `----`, in which case the AI can completely
rule out both the `C` and the `E` from its search space and with only six letters
(at the ROOKIE level), this means that the AI will only have to include the remaining four
letters in any subsequent best guess, making it much easier to find your secret code.

Likewise, if you have to respond with `+---` (one correct letter, in the wrong place), then
the AI knows that there can't be a `E` at positions one or three, and there can't be a `C`
at positions two or four, but there is definitely a `C` at either p1 or p3, or there is
definitely a `E` at p2 or p4.

A response of `*---`, on the other hand (one correct letter, in the correct position) would
give away as little information as possible, because all that the AI would know is that
there is one correct letter, but (at this stage) it will have no clear idea about which
letter is correct or at which position said letter will be.

### In closing

So far as I can tell, when the original game was run and a level of play had been chosen,
the player was then committed to that level, until a machine `RESET` signal was sent, at
which point the game could once again be run, at the same level, or a different level.

This is where my implementation diverges, in so much as; once a game has been concluded, you
will see the game menu displayed, rather than simply starting a new game, at the same level. 
From there, you can choose whatever level of play you wish and the game scores will continue
to accumulate.

Please enjoy. If you have any comments or feedback, please use this channel.
