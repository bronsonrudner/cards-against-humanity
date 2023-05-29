# Cards Against Humanity Cardsheet Generator

## Description

I wanted to generate some custom decks for Cards Against
Humanity in Tabletop Simulator.

I found [Roberto Amabile's Latex Against Humanity](https://github.com/ramabile/latex-against-humanity) and made some tweaks to simplify and tailor it to this purpose.

A python script manages compiling custom lines of card text
into PDF cardsheets, and then converts these sheets to PNG
images for importing into Tabletop Simulator.

Each generated sheet will contain at most 70 cards. The
first number in a sheet name is the number of that sheet for
the set, and the second number is the number of cards on that
sheet, to make it a little easier to import without too much
thought. Images for the backs are in the `img` folder.

## Adding new cardsheets

Under `sets`, create a `<name>_black.csv` and `<name>_white.csv`, and add the text for your cards (one line for each card).

Then follow the steps under "Run" to produce cardsheets in the `output` folder.

## Run
(Tested on Windows)

Ensure your shell has the following commands:
* `pdflatex` - https://miktex.org/
* `convert` - https://imagemagick.org/script/download.php
* `python` - https://www.python.org/ (tested on 3.10)

Then in a shell, run `python src/compile.py`

## Help

If the Latex compilation breaks, it may be a special symbol in
the card text causing the problem (I've accounted for the
common `$`, `?` and `%`).

## Licensing and credits

> Logo and name of Cards Against Humanity and its related concepts are [Creative Commons BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode). That means you can use, remix, and share the game for free, but you can't sell it without their permission. Please do not steal their name or they will smash you.

Tex (modified) and logo.eps taken from https://github.com/ramabile/latex-against-humanity under the [~"Do what you want" license](https://github.com/ramabile/latex-against-humanity/blob/master/LICENSE.txt)

Otherwise, feel free to do what you want.