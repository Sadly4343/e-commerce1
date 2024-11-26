# E-Commerce
# Overview

I chose to work on creating this software because I wanted to learn more about Cloud Database infrastructure and how to apply it with my current knowledge of topics like python backend and the development of producing a product that users can rely on for the needs required within the software. I want to apply this software knowledge of Cloud Databases with implementing and creating dynamic websites that rely on a strong backend and frontend design so I was curious to see how this learning could teach me to do that.

The software that I wrote for this project is using Boto3 which allows for the use of python with AWS DynamoDB and allows the ability to pull the tables from that database and modify and edit them from your own python code. I found this incredibly useful and being able to use this once connected to the AWS cloud allows for immediate updates to products and users that will use this website. The other integration uses Flask that can take the information obtained from Boto3 and use it towards creating templates that can use the existing information from boto3 and DynamoDB to pull and offer the ability to have user signup and Login pages as well as create product cards with the information that is within the python backend and display them with your html frontend design to whatever specifications you require. In order to use the software once you install the required dependenecies or you can simply use the same respository and replace the AWS credentials with your own and modify the tables to fit your content from DynamoDB you can use the menus that are present in the db_products.py and db_users.py programs to CRUD through the data in whatever you require.

The purpose of this software is to be able to select any table available in your dynamoDB and dynamically return it back to the programmer that can be queried, deleted, modified, added to the existing table of information. This allows for the ability to retrieve the data and use it for whatever is required and return what you want back to the table or simply view the table contents for your needs. In this scenario the data retrieved is the products within the E-Commerece site and also the users that are within a table and have the ability to use the site.

[Software Demo Video](https://youtu.be/gZkfTUvOsLo)

# Cloud Database

The Cloud Database that I chose was with DynamoDB that is from AWS and implementing it within my code.

The structure of the database was a NOSQL database that allows for the ability to create and modify items dynamically and allows for
further implementation with things such as Lambda that can streamline and automate updates within the products in the future with the use of
the NoSQL database structure provided by AWS.

# Development Environment

The tools used for this project were
-Flask
-Boto3 Amazons Python Library
-Jinja2 Templates
-S3 Buckets AWS
-DynamoDB AWS
-VSC for Coding

The programming language that I used was Python and the libraries used were Boto3 and Flask.

# Useful Websites


- [DynamoDb Boto3 Amazon Source](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html)
- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)

# Future Work

- Optimize the Menus and Combine them and allow for user to select any table they want to be used instead.
- Complete the implementation of Flask to allow for the site to be complete and develop it with AWSElasticBeanStalk to deploy it as a website
- Complet the html templates and work on the overall web app quality for the user experience.
