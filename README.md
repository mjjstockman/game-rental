# Game Rental



[View the live project here](https://mjjstockman.github.io/hangman/).


---


# Introduction

The following is a stock handling system for a physical game rental service.  It is used by the employee who checks in and out the rentals and adds new games and customers.

[Back to top ⇧](#Hangman)

# UX and Design

## User Demographics

The target market are individuals who want to play a quick game as a short distraction.  It is focused towards younger players, so a lot of guesses are allowed before the game is over.


## User Stories

1. As a gamer, I want to quickly tell what the game is, so I can see if I want to play it.

2. As a gamer, I want to be able to either win or loose, so I am motivated to try my best.

3. As a gamer, I want to be able to enter a guess using either my keyboard or by clicking on a button, so I can play in a way that best suits me.

4. As a gamer, I want visual representation on how well I am doing, so that I am kept engaged and can easily see my progress.

5. As a gamer, I want to be able to restart a game easily, so that I don't have to refresh the browser to start a new game whilst I am already playing.

[Back to top ⇧](#Hangman)

## Wireframes

| Under 500px width | Over 500px width |
| --------------| -------------- | 
| <img  src="additional-files/wireframe-small.png"  alt="Wireframe for under 500px width"> | <img  src="additional-files/wireframe.png"  alt="Wireframe for over 500px width"> |

*Images created and taken from [Balsamiq](https://balsamiq.com/wireframes)*

[Back to top ⇧](#Hangman)

  "Do you want to:\n 1) Make a rental?\n 2) Return a rental?\n "
              "3) Print stock?\n 4) Add a new customer?\n "
              "5) Add a new title?\n 6) Update fines?\n")

# Features

## Add a customer

The user can add new customers to the customers worksheet.  This hold the cutomers first name, last name, date of birth


## Add a game

New games can be added to the games worksheet, holding information on its title, platform, genre, age restriction and stock.


## Print stock

The entirety of the games worksheet can be printed to the screen.


## Make a rental

When a rental is being made, the user is asked to enter the customers first name, last name, the game title and platform.  Once it has checked that all information has been added, the following takes place:

* The title is checked to see if it is in the games worksheet.  This makes sure it is a game that is currently stocked.

* The stock is checked to see if there are any titles currently in stock.

* The platform the game is on is checked to make sure it is the platform the customer wants.

* The customers first name and last name are looked up in the customers worksheet and checked against the inputed data.

* The customers age is worked out using their date of birth and todays date.

* Their age is checked against the minimum age for the game in the games worksheet.

* A due date for the rental to be returned is calculated by adding 3 days to todays date.

* Stock in the games worksheet is reduced by 1.

* The rentals worksheet is updated with the customers first name, last name, game title, platform and due return date.


## Return a rental
A rental can be booked in once returned.  This asks for the customers first name, last name, game and platform.  The rental is then deleted from the rental worksheet.


## Update fines
The fine column in the rentals worksheet can be updated.  This checks an items due return date against todays date and if the due date is in the past the amount of days late is multiplied by the fine_per_day variable and entered into the fines column.



***

# Features to Implement in the future

## Customer ID
A membership ID number will be used when making a rental and return.  This will allow for customers with the same first and last name to use the service.  This was implemented within commit number 93 and 107.  New customers were automatically assigned a unique ID number when being placed in the customers worksheet.  The user was then prompted to input the customers ID number when making a rental and the specific customer data was then displayed.  This could then be confirmed by the user before proceding.  This allowed for a much more realistic and useable app.  However this feature was discarded due to a lack of time.

## Better validation
The error messages displayed to the user will be improved and try / except statements used to catch incorrect details and other issues.

## Fine awareness
Instead of just inputting fines in the rentals worksheet when the user has selected to do so, this would be carried out automatically and the information printed back to the user.


# Technologies Used

## Main Languages Used

- HTML
- Python



# Testing

Details on site testing can be found [here](TESTING.md).

[Back to top ⇧](#Hangman)

# Deployment

## How the site was Deployed

The code was deployed to GitHub Pages in the following way:

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Select the [GitHub Repository](https://github.com/mjjstockman/hull-hangman).
3. Open Settings by clicking on the Settings link (with the cog icon).
4. Scroll down to the GitHub Pages section and click on the link.
5. Click the dropdown box in the Source section (which currently states "none") and select master (this may be named "main" for some users).
6. Click Save.
7. The URL address for the deployed site will be shown.


[Back to top ⇧](#Hangman)

## How to Fork the Repository

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Select the [GitHub Repository](https://github.com/mjjstockman/hangman).
3. Click "Fork" at the top right of the page.
4. The repository will be copied into your GitHub account.

[Back to top ⇧](#Hangman)

## How to create a Clone using SSH

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Select the [GitHub Repository](https://github.com/mjjstockman/hangman).
3. Click on the Code button.
4. Copy the provided SSH link.
5. Open Terminal.
6. Navigate into the directory you want to clone the repository to.
7. Type git clone and paste the copied URL.

```
$ git clone https://github.com/mjjstockman/hangman
```

8. Press **Enter**.

[Back to top ⇧](#Hangman)

# Credits

Many thanks to the following which were used throughout the creation of this site:

- [w3c Markup Validator](https://validator.w3.org)
- [Am I Responsive?](http://ami.responsivedesign.is)
- [Balsamiq](https://balsamiq.com/)
- [Design Course tutorial](https://www.youtube.com/watch?v=z9H7p1_iI14)
- [Free Formatter](https://www.freeformatter.com/)
- [Google Fonts](https://fonts.google.com)
- [Git](https://git-scm.com)
- [GitHub](https://github.com)
- [Responsinator](http://www.responsinator.com)


[Back to top ⇧](#Hangman)

## Images

The Gallows image was taken from [Stick PNG](www.stickpng.com).

The background image was taken from [Unsplash](https://unsplash.com/)


[Back to top ⇧](#Hangman)

## Acknowledgements

- Many thanks to my mentor for guidance.
- Thank you to the Code Institute Slack community for their advice.
- A wonderful [README.md](https://github.com/rebeccatraceyt/KryanLive) by [Rebecca Tracey-Timoney](https://github.com/rebeccatraceyt) was used for inspiration and guidance.

[Back to top ⇧](#Hangman)