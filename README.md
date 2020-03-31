[![Build Status](https://travis-ci.com/Squelsh84/connemara-sticks-ms4.svg?branch=master)](https://travis-ci.com/Squelsh84/connemara-sticks-ms4)

# [Connemara Sticks]()

- Please find a link to the live website [here](https://connemara-sticks.herokuapp.com/)

![]()

## Table of Contents

1. [UX](#ux)
    - [Owners Stories](#owners-stories)
    - [User Stories](#user-stories)
    - [Design](#design)

2. [Wireframes](#wireframe)

3. [Features](#features)
    - [Current Features](#current-features)
    - [Future Features](#future-features)

4. [Apps](#apps)
    - [Home App](#home-app)
    - [About App](#about-app)
    - [Products App](#products-app)
    - [Blog App](#blog-app)
    - [Cart App](#cart-app)
    - [Accounts App](#accounts-app)
    - [Contact App](#contact-app)

5. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Tools](#tools)

6. [Testing](#testing)
    - [User Testing](#user-testing)
    - [Testing on Browsers](#testing-on-browsers)
    - [Manual Testing](#manual-testing)
    - [Validators](#validators)

7. [Deployment](#deployment)
    - [Clone in Github](#clone-in-github)
    - [MongoDB Atlas Database](#mongodb-atlas-database)
    - [Heroku Deployment](#deploy-to-heroku)

8. [Credits](#credits)
    - [Content](#content)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

# UX

Connemara Sticks is an e-commerces website developed for a small buisness to showcase its work to a bigger audience. Along with showcasing its work it also has a shop to sell its products. Customers can also contact the business with queries. The client wanted something easy to use.

## Owners Stories

Michael Walsh, Owner.

### Owners Story 1

I want to have an online presence for my business.

### Owners Story 2

I want to showcase my sticks for potential customers, with images so they know what we offer.

### Owners Story 3

I want to be able to write about stickmaking and other topics.

### Owners Story 4

I want to be able to recieve payment on sticks sold and to be emailed when one is sold.

## User Stories

Customer.

### User Story 1

I want to be able to see the previous work that has been carried out.

### User Story 2

I want to be able to see the stick and the length of it.

### User Story 3

I want to be able to contact them if I have any questions.

### User Story 4

I want to be able to make a payment by card on the site.

### User Story 5

I want to be know and choose what wood I want it to be.

## Design

### Theme

The original inspiration for the theme design came from [manufactura bold theme](http://manufactura.bold-themes.com/main-demo/home/home-v1/). I really liked the layout of the theme and how it flowed. Also the images of the are strong and work well with the theme. Also I felt that keeping the site simple and not overcrowded let the images of the sticks sell themselves.

### Typography & Fonts

Trying to keep with the theme of nature and wood, my color scheme I hope helps represent this with the use of green, brown and yellow. I choose to use Old Standard TT and Poppins as I believe they look well on the site.

# Wireframe

I decided to use balsamiq to create my mock-ups because it is easy to use and gave me a real visual of what I wanted to implement. The mockups are designed on different sized screens and can be found [here](https://github.com/Squelsh84/connemara-sticks-ms4/blob/master/wireframe/connemara-sticks.pdf) in the wireframe folder.

# Features

## Current Features



## Future Features



# Apps

## Home App

The home app is the landing page of the website. It displays some of the business products as well as displaying blog entries. There is also a jumbotron with a button to hopefully get customers to look around the site.

## About App

The about app introduces the people begnd the business and some of some information about what materials they use. 

## Products App

## Blog App

The blog app displays blogs about different topics such as walking, stick making, woods used and information on making your own stick. Its a great way to rank higher with key words in SEO's.

## Cart App

The cart app holds the items when added to the cart. If the user is in session then it keeps the items in the cart.

## Account App

The account app lets the user login and store his data. It keeps a record of previous purchases.

## Contact App

The contact app allows visitors to the site to contact the businesses with enquires or special request projects.

# Technologies Used

## Languages

- [HTML](https://www.w3.org/)
- [CSS](https://www.w3.org/)
- [JavaScript](http://www.ecma-international.org/)
- [Python](https://www.python.org/)

## Development Tools

- [Visual Studio Code](https://code.visualstudio.com/) IDE used.
- [Git](https://git-scm.com/) Used to track changes during development.
- [GitHub](https://github.com/) Used to host the version control system and website content before deployment to Heroku.

## Hosting Platforms & Database

- [Heroku](https://www.heroku.com/) Cloud based hosting service used.
- [SQLite](https://www.sqlite.org/index.html) Default Django database used.
- [PostgreSQL](https://www.postgresql.org/) Database used for production on deployment to Heroku.
- [AWS S3](https://aws.amazon.com/s3/) Cloud based storage for media files.

## Frontend Resources

- [Google Fonts](https://fonts.google.com/) Used for all fonts.
- [Font Awesome](https://fontawesome.com/) Used for all icons.
- [Bootstrap](https://getbootstrap.com/) Used for responsive layout and styling.
- [Stripe](https://stripe.com/ie)Used to recieve payments.
- [Juicer](https://www.juicer.io/)Used to display social media.

## Backend Resources

- [Django](https://www.djangoproject.com/)Web framework.
- [Pillow](https://pypi.org/project/Pillow/)Used for images.
- [AWS Storages](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)Django's storage.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)Renders Django forms.
- [Heroku](https://heroku.com)Used for deployment.

## Design Tools

- [Balsamiq](https://balsamiq.com/) Used to develop wireframes for the website.

# Testing

## User Testing

.

## Testing on Browsers



## Manual Testing



## Validators

- [W3c validator](https://validator.w3.org/) to validate both HTML and CSS. I copied my code and pasted it into the validator to check for errors and warnings.

- [JSHint](https://jshint.com/) was used to validate JavaScript.

- [PEP8 Online](http://pep8online.com/) was used to check everything was right with code.

- [BrowserStack](https://www.browserstack.com/) was used to test across multiple browsers.

# Deployment

The website was developed in Visual Studio Code using a virtual environment and deployed to Heroku via GitHub.

The following instructions to clone and deploy assume the user has:

- IDE
- Python 3
- Pip
- Virtual Environment
- GitHub Account
- Heroku Account

## Clone in GitHub

The following instructions were taken from [GitHib Help]( https://help.github.com/en/articles/cloning-a-repository).

1. Open the [connemara-sticks-ms4](https://github.com/Squelsh84/connemara-sticks-ms4) repository.
2. Click the --clone or download-- button.
3. In the --clone with HTTPs-- pop-up, click the --copy icon--.
4. Open --git bash--.
5. Change the current working directory to where you want the cloned directory to be made.
6. Type --git clone-- and paste the URL copied earlier.
7. Press --enter--.


## Deploy to Heroku

1. On the [Heroku](https://id.heroku.com/login) website log into your account.
2. Click --new-- and --create new app--.
3. Give your app a --name-- (it must be unique), select a --region-- and click --create app--.
4. Under --deployment method-- click --GitHub--.
5. Under --connect to GitHub-- select your --repository--, enter the --repo-name-- and click --search--.
6. Click the --connect-- button that appears under your repository and repo-name.
7. Under --settings/ config vars-- click --reveal vars--.
8. Enter --IP-- for key, --0.0.0.0-- for value and click --add--.
9. Enter --MONGO_URI-- for key, --your uri-- for value and click --add--.
10. Enter --SECRET_KEY-- for key, --your secret key-- for value and click --add--.
11. Under --deploy/ manual deploy-- click --deploy branch--.
12. Under --resources/ free dynos-- click --edit-- and --confirm--.

# Credits

## Content

- Some information was taken from [Stickmaking Handbook](https://www.ebay.co.uk/itm/174162686143)
- Images were taken from [pixabay](https://pixabay.com/)and [manufactura website](http://manufactura.bold-themes.com/main-demo/home/home-v1/).
  
## Code

- [Django 2.2 Documentation](https://docs.djangoproject.com/en/2.2/).
- [Brad Traversy - YouTube Django Crash Course](https://www.youtube.com/watch?v=e1IyzVyrLSU).
- [Brad Traversy - Udemy Django Dev To Development](https://www.udemy.com/course/python-django-dev-to-deployment/).
- [Corey Schafer - YouTube Django Playlist](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p).
- [Real Python - Build A Portfolio App](https://realpython.com/get-started-with-django-1/).
- [Coding Point - Django Ecommerce Web App](https://www.youtube.com/playlist?list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK).
- [Pretty Printed - YouTube Django Playlist](https://www.youtube.com/watch?v=QVX-etwgvJ8&list=PLXmMXHVSvS-DQfOsQdXkzEZyD0Vei7PKf&index=1).
- [The Zero2Launch Team - Udemy Django](https://www.udemy.com/course/build-ecommerce-website-to-master-django-and-python/).

## Acknowledgements