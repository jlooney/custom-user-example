# custom-user-example
Example for creating a custom user in django. This is an incomplete app that will be completed during a webinar. 

## To run this app

The database will need to be set up. To create the database schema, run
`python manage.py makemigrations`

Then, create the tables by running `python manage.py migrate`

This app assumes you will be using the admin (`/admin`) to manage users. Before running your app for the first time, you will need to create a super user account to access the admin. 
Run `python manage.py createsuperuser` to create a super user.

Then, run `python manage.py runserver` to run the app, and navigate to `/admin` to see the profile model in action. 
