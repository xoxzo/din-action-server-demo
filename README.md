# din-action-server-demo

## What is this app?

This is a sample web application for XOXZO DIN (dial in number) action server.
Assume you subscribe a DIN and set action url for the DIN phone number, when your number
get a call, XOXZO cloud will call the action url with the HTTP GET request.
This GET request has two parameters, `recipient` and `caller`. 
For details about DIN, please refer [this page.](http://docs.xoxzo.com/en/din.html)

In response to this request, the action server must return the action that you want XOXZO cloud to take,
playback, transfer or say. Action is in the plain text.
This app will accept DIN action requests and return the acton text.
This app has GUI that the user can choose the action to take with the pull down menu.

## How to install

This app is written in django framework. You must install django to run this app.
Pleas install django if it is not installed yet.

    pip install django

For details about django, please refer [this site.](https://www.djangoproject.com)

## How to run

Currently, sample actions are stared in the database.
You have to insert the actions into the database in advance.
Run this shell script to insert default actions into the database.

    sh init_database.sh
    
In oder to run this app, you use dinago `manage` command.
    
    python manage.py runserver

## ToDo

+ GUI to edit action
+ Change behaviour according to the GET parameters
+ Show access logs
+ Enhance GUI design, look

We appreciate your contribution.