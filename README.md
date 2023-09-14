# Person Rest Api

This project is a simple REST API for managing person resources. It supports CRUD (Create, Read, Update, Delete) operations and interfaces with a chosen database. The API allows you to create, read, update, and delete person records securely.

## Objective

The main objective of this project is to build a simple REST API capable of CRUD operations on a "person" resource. The chosen programming language which is python interfaces with a database to securely manage person records.

## Endpoints

Endpoint: /api
Method: POST
Request Body: JSON data representing the new person.
Response: JSON data of the created person.

## READ: Fetching details of a person by user ID

Endpoint: /api/{user_id}
Method: GET
Response: JSON data of the person with the specified user ID

## UPDATE: Modifying details of an existing person by user ID

Endpoint: /api/{user_id}
Method: PUT
Request Body: JSON data representing the updated person.
Response: JSON data of the updated person.

## DELETE: Removing a person by user ID
Endpoint: /api/{user_id}
Method: DELETE
Response: JSON message confirming the deletion.


## Getting Started

To run this API locally, follow these steps:

Clone the repository:
```
git clone https://github.com/eletrikode/hng2.git
```
## API Usage
You can use the API to perform CRUD operations on person records. Here are some sample requests:

Creating a new person:
```
POST /api
Content-Type: application/json

{
  "name": "John Doe"
}
```
Reading a person by ID:
```
GET /api/123
```
Updating a person by ID:
```
PUT /api/123
Content-Type: application/json

{
  "name": "john"
}
```
Deleting a person by ID:
```
DELETE /api/123
```

>>>>>>> origin/main
