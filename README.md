# din-action-server-demo

## What is this app?

This is a sample web application for XOXZO DIN (dial in number) action server.
Assume you subscribe DIN and set action url for the DIN phone number and when your number
get a call, XOXZO cloud will call the action url with HTTP GET request.
This GET request has two parameters, recipient and caller. 

In response to this request, the action server must return the action that you want XOXZO cloud to take,
playback, transfer or say. Action is in plain text.

This app will accept DIN action requests and return acton text.

This app has GUI that user can choose the action to take with pull down menu.

## How to install

This app is written in django framework. You must install django to run this app.
Pleas install django if it is not installed yet.

    pip install django

For details about django, please reafer [this site.](https://www.djangoproject.com)

## How to run

In oder to run this app, you use dinago `manage` command.
    
    python manage.py runserver

