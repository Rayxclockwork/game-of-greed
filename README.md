# game-of-greed

**Author**: Raven Delaney
**Version**: 1.0.0

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->
Python command line version of the game of greed(farkle, 10,000, etc)

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
After having python 3 and opening the file, respond to the given prompt.
Other features coming soon

Once completed, this will be a command line version of the game farkle.

This is a dice rolling game that consists of 6 dice. You roll all six and then, depending on what you roll,you get points or a re-roll and can bank points then your opponent goes. First to 10,000 points wins.

The scoring system is as follows:

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. This is also an area which you can include any visuals; flow charts, example usage gifs, screen captures, etc.-->
Uses Python 3, random, pytest, command line, github, pipenv shell

## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->

Game class has:
Init - creates new instance of the game
Begin - greets user and begins game
Dice_roll - rolls 6 dice and stores results in tuple for later use
Calculate_score - Scoring rules for game
Each_turn - tracks score and dice according to how user takes turn
Validate_roll - tracks dice kept and dice returned to roll again
Validate - Counts roll of dice versus count of kept dice
Play - Adds to score per turn


## Change Log

<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:
01-01-2001 4:59pm - Added functionality to add and delete some things.
-->
12/09/2019 5:30pm - added basic repo/code structure
12/09/2019 10:15pm - added some code and testing structure
12/09/2019 10:30pm - updated README
12/11/2019 4:30pm - scoring code work, tests pass
12/11/2019 8:19pm - added class demo tests and some turn code
12/12/2019 2:30pm - adding code to each round of play

