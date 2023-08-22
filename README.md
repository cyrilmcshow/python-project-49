### Hexlet tests and linter status:
[![Actions Status](https://github.com/cyrilmcshow/python-project-49/workflows/hexlet-check/badge.svg)](https://github.com/cyrilmcshow/python-project-49/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/b850f1968c0b2d2bb4ca/maintainability)](https://codeclimate.com/github/cyrilmcshow/python-project-49/maintainability)

## Description
Project containing 5 mini-games, each game is started by commands.

### Required version
python = "^3.10"
prompt = "^0.4.1"


### Makefile
#### Using the Makefile you can generate all the needed packages for you virtual environment
```make install``` to install poetry packages. \
```make build``` to build your packages inside your project. \
```make publish``` It will let us execute the publish command knowing exactly what is going into the build. \
```make package-install``` installs the built package from our OS, so we can start using simple shell commands.

#### test your application by adding ```brain-games``` to the command line


## Game launch examples
### run brain-even
The essence of the game is as follows: the user is shown a random number. And he needs to answer yes, if the number is even, or no, if it is odd.
[![asciicast](https://asciinema.org/a/4Cfyg1cvM4SMV7VlIaJc9l8sF.svg)](https://asciinema.org/a/4Cfyg1cvM4SMV7VlIaJc9l8sF)


### run brain-calc
The essence of the game is as follows: the user is shown a random mathematical expression, for example, 35 + 16, which must be calculated and the correct answer written down.
[![asciicast](https://asciinema.org/a/sHtbHfnect8X1Va8cadVb7KwM.svg)](https://asciinema.org/a/sHtbHfnect8X1Va8cadVb7KwM)

### run brain-gcd
The essence of the game is as follows: the user is shown two random numbers, for example, 25 50. The user must calculate and enter the greatest common divisor of these numbers.
[![asciicast](https://asciinema.org/a/3PmKxht17XzaHeEwkgfaoGU5b.svg)](https://asciinema.org/a/3PmKxht17XzaHeEwkgfaoGU5b)

## run brain-progression
We show the player a series of numbers that forms an arithmetic progression, replacing any numbers with two dots. The player must determine this number.
[![asciicast](https://asciinema.org/a/Nc7RLmkGl8pgqakTXTEuqXVzP.svg)](https://asciinema.org/a/Nc7RLmkGl8pgqakTXTEuqXVzP)

## run brain-prime
We show the player the numbers, he needs to answer whether the number is prime
[![asciicast](https://asciinema.org/a/JU2xHEqzeazEZKaNqWEJFJKQG.svg)](https://asciinema.org/a/JU2xHEqzeazEZKaNqWEJFJKQG)
