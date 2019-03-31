# InstaPost
Photo sharing through group chat App for Database access.

This simple app shows the REST API for the backend of a database application using Flask. The application has 7 entities.
1. Users - contains basic log in info of an app user.
2. Persons - contains personal contact info of a user.
3. Chats - place where various users share posts and react to them. Has the name and creation date. 
4. Posts - contain a photo and an optional caption. Made by users in a chat. Can be liked, disliked and replied to.
5. Messages - can be either a reply to a post or a post caption. May contain hashtags.
6. Reactions - done to a post or reply by a user. Can be either a like or dislike. 
7. Hashtags - contained in messages.

The application is organized in three broad layers:
1. Main - the main app module takes care to setup the routes for the REST API and calling the proper handler objects to process the request.
2. Handlers - [Returns hard coded object] the handler modules takes care of implementing the logic of each REST call. In this sense, a handler is a Facade for accessing a given operation on a data collection. Each object handles a particular type of request for a data collection (e.g. Chats). The handlers rely upon the Data Access Objects (DAOs) to extract data from the database. The handlers encode the responses to the client with JSON and provide the appropriate HTTP response code.
3. DAOs - [Returns hard coded object] the Data Access Objects (DAOs) take care of moving data in and out of the database engine by making SQL queries and wrapping the results in the objects and object list of appropriate types.

## Requirements
You need the following software installed to run this application:
1. Flask - web bases framework to implement the REST API.

