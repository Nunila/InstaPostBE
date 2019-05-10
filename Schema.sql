create table Users(
	userId serial primary key,
	username varchar(20),
	password varchar(200));

create table Person(
	personId serial primary key,
	firstName varchar(200),
	lastName varchar(200),
	phoneNumber varchar(200),
	email varchar(200),
	birthday date,
	userId integer references Users(userId));

create table Contacts(
	ownerId integer references Person(personId),
	contactId integer references Person(personId),
	primary key (ownerId, contactId));

create table Chat(
	chatId serial primary key,
	chatName varchar(200),
	creationDate date);

create table Post(
	postId serial primary key,
	chatId integer references Chat(chatId) NOT NULL,
	userId integer references Users(userId) NOT NULL,
	messageId integer references Message(messageId) NOT NULL,
	photourl varchar(200),
	postDate timestamp);

create table Hashtag(
	hashtagId serial primary key,
	hashName varchar(200),
	datetime timestamp);

create table Message(
	messageId serial primary key,
	userId integer references Users(userId) NOT NULL,
	content varchar(500),
	messageDate timestamp);

create table Reaction(
	reactionId serial primary key,
	userId integer references Users(userId) NOT NULL,
	postId integer references Post(postId) NOT NULL,
	messageId integer references Message(messageId),
	type  varchar(20),
	reactionDate timestamp);

create table Participates(
	userId integer references Users(userId),
	chatId integer references Chat(chatId),
	primary key (userId, chatId),
	role varchar(20));

create table Mentioned(
	hashtagId integer references Hashtag(hashtagId),
	messageId integer references Message(messageId),
	primary key (hashtagId, messageId));

CREATE TABLE Reply(
	postId integer references Post(postId) NOT NULL,
	messageId integer references Message(messageId) NOT NULL,
	primary key (postId, messageId));
