<h1 style="text-align: center">The Barbell Planner</h1>

![hero image screenshot](static/images/barbell_responsive.JPG)

This is my submission for Milestone project 3. The Barbell Planner is a fitness based application allowing the user
to log either a cardio or weights based workout. The user will be able to authenticate themself, log a workout, and then Read, Update or Delete
that workout from the list they have created. The application will also allow them to navigate to the Barbell gym site
and Social Media channels.

Live project: [https://barbell-planner.herokuapp.com/]

### User Experience (UX) ###

* User Story 1 - As a user, I land on the dashboard and it is clear what the site is and it's purpose.
* User Story 2  - As a user, I can easily navigate through the dashboard.
* User Story 3 - As a user, there is a clear call to action to login.
* User Story 4 - As a user, given I havn't registered, there is a clear option for me to register as a user of the planner.
* User Story 5 - As a user I can access the business social media channels from anywhere on the site.
* User Story 6 - As an admin, I can limit the the navigation options presented to the user if they have not yet logged in.
* User Story 7 - As a new user, I can navigate to the registration page easily
* User Story 8 - As a user, There is a clear call to action on what details I must input into the registration fields
* User Story 9 - As a user, I can see if I have successfully registered
* User Story 10 - As a user, I am informed if I have entered invalid data into a field
* User Story 11 - As an admin, I can see the successfully registered username and encoded password in the database
* User Story 12 - As a user, given I have logged in, I can see a navigation bar giving me clear options that are not present to me when i'm logged out
* User Story 13 - As a user, I can see a clear call to action to log a workout when I have logged in
* User Story 14 - As a user, given I have logged in, I can logout at any point in the site
* User Story 15 - As a user, When I log a workout I have the choice to pick either a 'Cardio' Workout or a 'Weights' based workout
* User Story 16 - As a user when I select 'Weight' workout, I am asked for the name, reps and weight used in my workout and the date
* User Story 17 - As a user, When I select 'Cardio', I am asked for the exercise name, duration and date.
* User Story 18 - As a user when I click on 'Log Workout' the workout then shows on the 'My Workout section of the site.
* User Story 19 - As a user, When I navigate to the My Workouts section, I can see the workouts that I have logged.
* User Story - 20 - As a User, I can Read, Update and Delete the work out I have created. 

### Design ###

* Colour scheme - The colour scheme is black and white matching the brand and ethos of the business.

* Typography - the 'Big Shoulders Stencil Text' font is used as it is bold, easy to read and suits the military old school
feel of the brand.

* Imagery - The Barbell Gym logo is shown throughout the site to draw attention as the business' distinctive feature. Background images include images
from the gym and classes to provide an insight to users of what the gym looks like, can be seen throughout various pages of the site.

* WireFrames:
Desktop and Mobile wireframes - https://marvelapp.com/prototype/5d24b2d

* Features:
Responsive layout on mobile and tablet,
Collapsible Nav bar for mobile view,
Collapsible menu for displaying logged workouts,
Authentication (Login/Register functionality),
Defensive programming

### Technologies: ###

* Languages - 
HTML5
CSS3
JS
Python

* Frameworks/libraries/programs - 
  https://favicon.io/favicon-converter/ - Used to create logo for title.

  https://fonts.google.com/ - used for font design.

  Flask App - https://flask.palletsprojects.com/en/2.0.x/ to run site on and use of Jinja templating and Werkzeug functionality. 

  MongoDB Atlas - https://www.mongodb.com/ for the storage and retrieval of non-relational data. 

  Materialize CSS - https://materializecss.com/ Used for responsiveness and design of site,
  used to implement responsive header, footer and collapsible menu.

  Heroku - https://www.heroku.com/ cloud based platform used to deploy the Barbell planner.

  Free formatter - https://www.freeformatter.com/css-beautifier.html used to beautify CSS3 code.

  W3C markup Validator - https://validator.w3.org/ to check HTML formatting.

  JS Hint - https://jshint.com/ - to test JQuery formatting.

  

<h2 style="text-align: center">Testing</h2>

The W3C Markup Validator, W3C CSS and JSHint Validator Services were used to validate the project pages to ensure
there were no syntax errors.

* [W3C Markup validator](https://validator.w3.org/#validate_by_input)


* [W3C CSS validator](https://jigsaw.w3.org/css-validator/validator)

* [JSHint](https://jshint.com/)


### Testing user stories ###

### Further testing ###
     

* Bugs:
     The navigation links do not render correctly on Iphone 5 screen:
     ![hero image screenshot](assets/images/screenshots/user_story_12.JPG)
     Resolved: No, Iphone 5 is now an old model and the navigation renders correctly on all Iphone models in
     the last 5 years. 
     Future fix may include a collapsable nav bar that lends itself to smaller screens.


* Potential enhancements:


<h2 style="text-align: center">Deployment</h2>

### GitHub Pages ###
The project was deployed to GitHub Pages using the following steps...

#### Log in to GitHub and locate the GitHub Repository ####

* At the top of the repository section, locate the "Settings" Button on the menu.
* Scroll down the settings page until you find the "GitHub Pages" section.
* You will see a message "Pages settings now has its own dedicated tab! Check it out here!" click on the link.
* Under "Source", click the dropdown and select "Master Branch".The page will refresh.
* The now published site link in the "GitHub Pages" section will be found at the top of the page.

### Forking the GitHub Repository ###
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

#### Log in to GitHub and locate the GitHub Repository ####

* At the top of the repository section just above the "Settings" button on the menu, click the "Fork" button.
  The original repository in your GitHub account should now have duplicated.

#### Making a Local Clone ####

* Log in to GitHub and locate the GitHub repository, under the repository name, click "clone or download".
* To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
* Open Git Bash
* Change the current working directory to the location where you want the cloned directory to be made.
* Type git clone, and then paste the URL you copied in Step 2.
   * $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
* Press Enter. Your local clone will be created.
   * $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.

<h2 style="text-align: center">Credits</h2>

### Code ###

w3Schools.com to help with some of the syntax of the Js.

Email.js for the contact us email functionality.

### Content ###

All typed content was written by the developer.

### Media ###

#### Image credits ####

### Acknowledgements ###
Thanks to Aaron my mentor, for advice on my project and the Code Institute Slack community.