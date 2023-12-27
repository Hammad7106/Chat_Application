# REAL TIME CHAT APPLICATION

I have developed a Real Time Chat Application in Django

FUNCTIONALITY

This app has a login/sign up functionality for user authentication.
Then there is a profile section where the data of current user is shown like name profile image and particular groups where this user is added.
When a user open the group for chat then he types a message which is send to the group.So all the users who are in that group will access this message and can reply.
All this process is a Real Time Process.

DEVELOPEMENT

To develop this app I have used Django Web Channels.
For Real Time Data Communication I have used Redis labs 
Database is sqllite for storing message content of users.
I have used AsyncWebConsumers in Web Sockets.So, the flow of messages is asynchronous.

