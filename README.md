**StackOverflow-lite**

StackOverflow-lite is a platform where people can ask questions and provide answers

**Motivation**

Stackoverflow-lite is a platform that brings great minds together to solve a problem

**Code style**

The API was constracted using python,flask and restplus

**Installation**

Clone the repo to your local machine install a virtual enviroment install the dependacies from terminal run run.py. Test the endpoint using postman.

**Features**

1. Users can create an account and log in. 
2. Users can post questions. 
3. Users can delete the questions they post. 
4. Users can post answers. 
5. Users can view the answers to questions. 
6. Users can accept an answer out of all the answers to his/her question as the preferred answers

**Tests**

The test were carried out from the unittest library. for python version 3.5 and below use py.test to run yur test for python version 3.5 and above use pytest to run your test. To view code coverage use pytest --cov

**EndPoint Functionality**

POST /auth/signup  Register a user   
POST /auth/login  Login a user   
GET /questions   Fetch all questions   
GET /questions/<questionId>   Fetch a specific question
Delete /questions/<questionId>   Delete a question  This endpoint should be available to the question author. 
POST /questions/<questionId>/answers  Post an answer to a question   
PUT /questions/<questionId>/answers/<answerId> Mark an answer as accepted or update an answer

**Authors**

Kwame Asiago

**Badges**

[![Travis Build Status](https://travis-ci.org/SelaDanti/StackOverflow-lite.svg?branch=ft-register-160887043)](https://travis-ci.org/SelaDanti/StackOverflow-lite)  