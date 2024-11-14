# HBnB Project

## Project Overview
In this phase of the HBnB Project, we begin the implementation of the core functionality of the application based on the design defined in Part 1. The primary focus is on building the **Presentation** and **Business Logic** layers using Python and Flask, along with the flask-restx extension for creating RESTful APIs.

Our objective is to set up the foundational structure of the project, define the core classes and methods, and implement the API endpoints for managing users, places, reviews, and amenities. While we are not implementing JWT authentication or role-based access control in this phase, we aim to establish a clean, modular architecture that will make it easy to add these features in the next part.

### Set Up the Project Structure
- Organize the project using a modular architecture to follow best practices for Python and Flask applications.
- Create separate packages for the **Presentation** and **Business Logic** layers, ensuring a clear separation of concerns and easy maintainability.

### Implement the Business Logic Layer
- Develop core classes to represent business entities, including `User`, `Place`, `Review`, and `Amenity`.
- Define relationships between entities (e.g., Users owning Places) and implement necessary interactions within the application.
- Use the **Facade Pattern** to simplify the communication between the Presentation and Business Logic layers, enhancing the modularity and extensibility of the codebase.

### Build RESTful API Endpoints
- Implement CRUD endpoints for managing Users, Places, Reviews, and Amenities, ensuring each endpoint is documented and follows RESTful principles.
- Use `flask-restx` to define and document each API endpoint, establishing a consistent and clear structure.
- Enable data serialization to return extended attributes for related objects. For example, retrieving a Place should include details such as the owner's `first_name` and `last_name`, and relevant amenities.

### Test and Validate the API
- Test each endpoint using tools like Postman or cURL to ensure proper functionality and handling of edge cases.
- Validate API responses to confirm accurate data retrieval, especially for nested attributes and relationships.

---

## Project Vision and Scope

The goal of this phase is to establish a functional and scalable foundation for the HBnB application, with a focus on:
1. **Presentation Layer**: Defining the services and API endpoints using Flask and flask-restx. The structure should reflect logical grouping and clear path definitions for each operation.
2. **Business Logic Layer**: Building the core models and relationships, handling data validation, and managing interactions between components.

This phase does not involve implementing user authentication or access control. However, we are structuring the code to make it easy to integrate these features in Part 3.

---
## Learning Objectives

This phase of the project will help you:
- **Design Modular Architecture**: Structure a Python application with a focus on modularity, separation of concerns, and maintainability.
- **Develop APIs with Flask and flask-restx**: Gain hands-on experience in building and documenting RESTful APIs with Flask and flask-restx.
- **Implement Business Logic**: Translate documented designs into working code by developing core business logic and relationships.
- **Handle Data Serialization**: Learn how to handle nested and related data efficiently in API responses.
- **Test and Debug APIs**: Strengthen your testing and validation skills to ensure robust and functional API endpoints.
---

# Project Setup Instructions

### Prerequisites
- Python 3.x
- Flask and flask-restx packages

### Installation

**Clone the repository**:
   ```bash
   git clone <repository_url>
   cd hbnb_project