[![Build Status](https://travis-ci.com/Squelsh84/connemara-sticks-ms4.svg?branch=master)](https://travis-ci.com/Squelsh84/connemara-sticks-ms4)

# [Connemara Sticks](https://connemara-sticks.herokuapp.com/)

- Please find a link to the live website [here](https://connemara-sticks.herokuapp.com/)

![Responsive Dashboard](https://github.com/Squelsh84/connemara-sticks-ms4/blob/master/static/images/website.jpg)

## Table of Contents

1. [UX](#ux)
    - [Owners Stories](#owners-stories)
    - [User Stories](#user-stories)
    - [Design](#design)

2. [Wireframes](#wireframe)

3. [Features](#features)
    - [Apps](#apps)
    - [Home App](#home-app)
    - [About App](#about-app)
    - [Products App](#products-app)
    - [Blog App](#blog-app)
    - [Cart App](#cart-app)
    - [Checkout](#checkout-app)
    - [Accounts App](#accounts-app)
    - [Contact App](#contact-app)
    - [Future Features](#future-features)
  
4. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Tools](#tools)

5. [Testing](#testing)
    - [User Testing](#user-testing)
    - [Testing on Browsers](#testing-on-browsers)
    - [Manual Testing](#manual-testing)
    - [Validators](#validators)
    - [Bugs](#bugs)

6. [Deployment](#deployment)
    - [Clone in Github](#clone-in-github)
    - [MongoDB Atlas Database](#mongodb-atlas-database)
    - [Heroku Deployment](#deploy-to-heroku)

7. [Credits](#credits)
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

I want to be able to recieve payment on sticks sold and the system to be updated on quantity.

## User Stories

Customer.

### User Story 1

I want to be able to see  work that has been carried out and is available to purchase.

### User Story 2

I want to be able to see the stick and the length of it.

### User Story 3

I want to be able to contact them if I have any questions.

### User Story 4

I want to be able to make a payment by card on the site.

### User Story 5

I want to know about their guarantee and choose what wood I want it to be.

## Design

### Theme

The original inspiration for the theme design came from [manufactura bold theme](http://manufactura.bold-themes.com/main-demo/home/home-v1/). I really liked the layout of the theme and how it flowed. Also the images of the are strong and work well with the theme. Also I felt that keeping the site simple and not overcrowded let the images of the sticks sell themselves.

### Typography & Fonts

Trying to keep with the theme of nature and wood, my color scheme I hope helps represent this with the use of green, brown and yellow. I choose to use Old Standard TT and Poppins as I believe they look well on the site.

# Wireframe

I decided to use balsamiq to create my mock-ups because it is easy to use and gave me a real visual of what I wanted to implement. The mockups are designed on different sized screens and can be found [here](https://github.com/Squelsh84/connemara-sticks-ms4/blob/master/wireframe/connemara-sticks.pdf) in the wireframe folder.

# Features

## Apps

### Home App

The home app is the landing page of the website. It displays some of the business products as well as displaying some key features. There is also a jumbotron with a button to hopefully get customers to look around the site. The products are displayed three at a time with a paginator below the products to click to the next three. Also there is a scroll to top button which is only activated as the user scrolls down the page.
The navbar dropdawn for sticks has been created in a way that if the business creates new categories the dropdown will update automatically.

### About App

The about app introduces the people behind the business and some of some information about what materials they use. It also has links to the contact page so users can contact then=m if they have any questions or maybe want to learn the trade.

### Products App

The product app has two pages, products.html which displays all the products and product.html which displays the product itself. On the all products place I have it set to display six sticks and have a paginator button only displaying when thier are more than six sticks.
Also their is a navbar to the side displaying the categories which when clicked will display only that category.

The product page displays all the information about the stick. It has an add to cart butoon which displays out of stock when the quantity falls to zero.

### Blog App

The blog app displays blogs about different topics such as walking, stick making, woods used and information on making your own stick. Its a great way to rank higher with key words in SEO's. Also I have added the businesses instagram to display all the posts from their page. It refreshes every 24hrs.

### Cart App

The cart app holds the items when added to the cart. If the user is in session then it keeps the items in the cart. The cart can add or remove items and will only increase to the amount in the available. The stripe payment button when clicked activates a modal for payment on larger screens. On smaller screens your are redirected to a new screen.

### Checkout App

The checkout will show the purchase number after a purchase is made. Ths will also confirm the purchase.

### Account App

The account app lets the user login and store his data. It keeps a record of previous purchases.

### Contact App

The contact app allows visitors to the site to contact the business with enquires or special request projects. It also displays the address and phone number.

## Future Features

To send an order confirmation email after purchase has been made.

Add a review and favourite section to the website.

On the product page add a section to give the option of adding a compass, stone or anther trinket.

Area on checout page to estimate shipping costs.

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

The website was constantly tested by [Travis CI](https://travis-ci.com/) each time it was pushed to git.

The website was shared with friends and family to test. When testing there were some issues with design. The checkout was stretching and causing issues on smaller screens. To fix this i decided to great a one column checkout instead of the original two.
Another issue was theat there was alot of over lapping on smaller screens. To fix this issue I added padding to tags for when it was needed. Also I had forgotten to add a back to shopping link after a purchase was made.

## Testing on Browsers

As I don't have every type of screen size and ocomputer on hand I used [browserstack](https://www.browserstack.com/) to help test across multiply browsers. While I have google chrome and internet explorer available to me I used their developmet tools to help with adjusting css and also to see if I had any errors in the console.

## Manual Testing

Chrome Dev tools was used all the way through the build of the site. It was used to test for errors and also the test the responsiveness of the website across all screen sizes.

### Stripe payment testing

The checkout app is using the stripe payment for the payment option. I tested this by using Stripes test card (4242 4242 4242 4242) I tested the forms and ensured all my validation worked as expected and my logic was performing as expected. The checkout app works from the Stripe API.

Card number - 4242424242424242

CVC - Any 3 digit number.

Expiry date - Any date in the future.

## Bugs

During testing I found some bugs in the site.

- Search bar is not working on larger screens but will work on mobile devices. I still have not resolved this issue as I have run out of time.
- The contact page is sending an email but is not sending the information.
- The stripe payment was giving issues depending on the address but this resolved itself after deleting and recreating the code.
- Search bar is not easing in and out as its supposed to.

## Validators

- [W3c validator](https://validator.w3.org/) to validate both HTML and CSS. I copied my code and pasted it into the validator to check for errors and warnings.

- [JSHint](https://jshint.com/) was used to validate JavaScript.

- [PEP8 Online](http://pep8online.com/) was used to check everything was right with code.

- [BrowserStack](https://www.browserstack.com/) was used to test across multiple browsers.

- [Autoprefixer CSS](https://autoprefixer.github.io/) was used to ensure all prefixes were included to CSS.

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

### IDE Development Setup

1. Create a virtual environment for your Python project.
2. Create a env.py file in the iaproject folder.
3. Add the following variables to the env.py file.

```import os
os.environ['EMAIL_HOST_USER']
os.environ['EMAIL_PASSWORD']
os.environ['SECRET_KEY']
os.environ['STRIPE_PUBLISHABLE']
os.environ['STRIPE_SECRET']
os.environ['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']
os.environ['AWS_STORAGE_BUCKET_NAME']
os.environ['DATABASE_URL']
os.environ['ALLOWED_HOSTS']
```

4. Use `pip install -r requirements.txt` to install Python required modules.

### Deploy to Heroku

1. On the [Heroku](https://id.heroku.com/login) website log into your account.
2. Click **new** and **create new app**.
3. Give your app a **name** (it must be unique), select a **region** and click **create app**.
4. Under **resources** choose add on postgres hobby free.
5. Click **reveal id**.
6. Return to your IDE and fill the values for your environment variables in the env.py file.
7. Return to the Heroku dashboard and under **settings/ config vars** click **reveal vars**. Add the key values for all your environment variables.
8. In your console type ```heroku login```, and when prompted click any key to open the browser and log into your heroku account.
9. Type ```heroku git:remote -a appname```.
10. Type ```git subtree push --prefix iaproject heroku master``` to push the code to Heroku.
11. Cd into iaproject and type ```python manage.py makemigrations``` and ```python manage.py migrate``` to create and run migrations.
12. Type ```python manage.py createsuperuser``` to create a super user.
13. Open the Heroku app address adding ```/admin``` to the end of the URL and login with the super user credentials.
14. Use this Django admin interface to add data to populate the blog, cv and portfolio apps.

# Credits

## Content

- Some information was taken from [Stickmaking Handbook](https://www.ebay.co.uk/itm/174162686143)
- Images were taken from [pixabay](https://pixabay.com/) and [manufactura website](http://manufactura.bold-themes.com/main-demo/home/home-v1/).
  
## Code

- [Django 2.2 Documentation](https://docs.djangoproject.com/en/2.2/).
- [Brad Traversy - YouTube Django Crash Course](https://www.youtube.com/watch?v=e1IyzVyrLSU).
- [Brad Traversy - Udemy Django Dev To Development](https://www.udemy.com/course/python-django-dev-to-deployment/).
- [Corey Schafer - YouTube Django Playlist](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p).
- [Real Python - Build A Portfolio App](https://realpython.com/get-started-with-django-1/).
- [Coding Point - Django Ecommerce Web App](https://www.youtube.com/playlist?list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK).
- [Pretty Printed - YouTube Django Playlist](https://www.youtube.com/watch?v=QVX-etwgvJ8&list=PLXmMXHVSvS-DQfOsQdXkzEZyD0Vei7PKf&index=1).
- [The Zero2Launch Team - Udemy Django](https://www.udemy.com/course/build-ecommerce-website-to-master-django-and-python/).
- [Boostrap Blog Starter Page](https://github.com/BlackrockDigital/startbootstrap-blog-home).
  
## Acknowledgements

A massive thank you to my mentor Seun Owonikoko who guided me through my project especially during these strange times. To all the great people on Slack who give their time to answer peoples questions. So many problems I have encountered have already been answered by the wonderful people there.
