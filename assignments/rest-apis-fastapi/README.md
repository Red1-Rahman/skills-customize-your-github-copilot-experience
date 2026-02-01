# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a functional REST API using the FastAPI framework that handles HTTP requests and responses. You'll learn to create endpoints, handle different HTTP methods, validate request data, and structure a web service following REST conventions.

## 📝 Tasks

### 🛠️ Create a Basic Todo API

#### Description
Build a RESTful API with FastAPI that manages a collection of todo items. The API should support creating, retrieving, updating, and deleting todos, with proper validation and HTTP status codes.

#### Requirements
Completed program should:

- Define a data model for todo items with properties like id, title, description, and completed status
- Implement GET endpoint to retrieve all todos and individual todos by id
- Implement POST endpoint to create new todos with request body validation
- Implement PUT endpoint to update existing todos with proper error handling
- Implement DELETE endpoint to remove todos by id
- Return appropriate HTTP status codes (200, 201, 404, etc.)


### 🛠️ Add Query Parameters and Filtering

#### Description
Extend the API with advanced features to filter and paginate todo results based on query parameters.

#### Requirements
Completed program should:

- Add query parameters to filter todos by status (completed/incomplete)
- Implement pagination using skip and limit parameters
- Add query parameter validation with default values
- Return filtered and paginated results with correct data
