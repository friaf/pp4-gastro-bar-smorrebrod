I have submited my project while its not fully finished, I understand this work is not going to be gradet and i will be finishing all the points bellow to re-submiting it.

Coding is the most difficult thing i have ever done but i enjoy every second of it!

Add to site:
- I need to add validation for double booking, as for now tables can be booked for the same time by many users.
- Add responsivness to menu images
- Responsivness to couple of buttons
- error page 505 
- Ability for staff to view and edit menu items and bookings from the website, not admin panel

Add to Readme file:
- tests
- database diagram
- Screenshots for my website with description
- Responsive view (responsive websites didnt connect to my site, i dont know why as deployment was successful)
- Credits to


# Smorrebrod Gastro-Bar (Project 4)

![](docs/readme_images/responsive_color/home_small.png)



This is a fictional Gastro-Bar based in Cork city, Ireland.
Website is a booking management system, where customers can easily make bookings, edit and delete them. Staff has edit, delete and can view customers bookings and prepare tables for specific time and date.

## Using Agile Methods 

This project was developed using agile methodologies by delivering small features in sprints. There were 3 sprints, spaced out evenly over 5 weeks.

The Kanban board was created using github projects and can be located <a href="https://github.com/users/friaf/projects/12" target="_blank">here</a> and can be viewed to see more information on the project cards. 

![](docs/readme_images/agile/1.png)
![](docs/readme_images/agile/3.png)
![](docs/readme_images/agile/2.png)


## Color Scheme

![](docs/readme_images/responsive_color/colors.png)


## Wireframes Plane
### Home page
![](docs/readme_images/wireframes/home.png)
### Menu page
![](docs/readme_images/wireframes/menu.png)
### Register page
![](docs/readme_images/wireframes/register.png)
### Booking page
![](docs/readme_images/wireframes/booking.png)
### Manage booking page
![](docs/readme_images/wireframes/manage_booking.png)
### Delete booking page
![](docs/readme_images/wireframes/delete_booking.png)


## Technolgies

- HTML
- CSS
- avaScript
- Python (Django Framework)
- Gitpod
- Github
- Git
- Fontawesome
- Favicon
- Balsamiq
- Google Fonts

### External Python Modules

- asgiref==3.6.0
- click==6.7
- cloudinary==1.33.0
- cursor==1.1.0
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==3.2.19
- django-admin-rangefilter==0.10.0
- django-allauth==0.54.0
- django-crispy-forms==1.14.0
- gunicorn==20.1.0
- oauthlib==3.2.2
- psycopg2==2.9.6
- pydantic==1.10.7
- PyJWT==2.7.0
- python3-openid==3.2.0
- pytz==2023.3
- requests-oauthlib==1.3.1
- sqlparse==0.4.4
- tempus==1.1.0
- urllib3==1.26.15
- whitenoise==6.4.0


## Deployment

The following git commands were used throughout development to push code to the remote repo:

git add . - This command was used to add the file(s) to the staging area before they are committed.

git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

git push - This command was used to push all committed code to the remote repository on github.

## Heroku Deployment

## The site was deployed to Heroku. The steps to deploy are as follows:

- Navigate to heroku and create an account
- Click the new button in the top right corner
- Select create new app
- Enter app name
- Select region and click create app
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (database url)
  - CLOUNDINARY_URL: (cloudinary api url)
  - PORT: (PORT)
  - HEROKU_POSTGRESQL_PUCE_URL: (postgres api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repositoy you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click deploy
The app should now be deployed.

The live link can be found here: <a href="https://pp4-gastro-bar-smorrebrod.herokuapp.com/" target="_blank">Live Site</a>




