## Documentation
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
