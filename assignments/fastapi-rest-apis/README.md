# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI that can return JSON data and manage a collection of items. This assignment helps students practice web API concepts such as routes, request handling, and basic validation.

## 📝 Tasks

### 🛠️ Set up the FastAPI Application

#### Description
Create a FastAPI app and make sure it starts successfully from a Python file.

#### Requirements
Completed program should:

- Import `FastAPI` from the `fastapi` package
- Create an app instance
- Add a root endpoint at `GET /`
- Return a JSON response such as `{"message": "Welcome to the API"}`
- Be able to run the server with `uvicorn`

### 🛠️ Build CRUD Endpoints for Items

#### Description
Add routes to create, view, and retrieve item records through a simple API.

#### Requirements
Completed program should:

- Define a list or dictionary to store items in memory
- Add `GET /items` to return all items as JSON
- Add `POST /items` to create a new item from request data
- Add `GET /items/{item_id}` to retrieve one item by its ID
- Use a Pydantic model to validate item data before saving it
- Return clear JSON responses for successful requests

### 🛠️ Add Basic Validation and Error Handling

#### Description
Improve the API so invalid requests are handled cleanly and the program is more reliable.

#### Requirements
Completed program should:

- Validate required fields such as `name` and `price`
- Return a useful error when an item is not found
- Prevent invalid input values from crashing the app
- Keep the API response format consistent and easy to read
