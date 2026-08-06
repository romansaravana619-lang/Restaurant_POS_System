# Saru POS API Documentation

Version: v1.0

---

# Authentication Module

---

## 1. Login API

### Endpoint

POST /login

### Description

Authenticates a user and returns the logged-in user details.

### Request Body

```json
{
    "username": "admin",
    "password": "admin123"
}
```

### Success Response (200)

```json
{
    "success": true,
    "user": {
        "user_id": "USER001",
        "employee_id": "EMP001",
        "username": "admin",
        "role": "Admin",
        "status": "Active"
    }
}
```

### Error Response (401)

```json
{
    "success": false,
    "message": "Invalid username or password."
}
```

---

# Customer Module

---

## 2. Add Customer

### Endpoint

POST /customers

### Description

Creates a new customer in the Saru POS system.

### Request Body

```json
{
    "customer_id": "CUS001",
    "customer_name": "Saravana Kumar",
    "phone": "9876543210",
    "email": "saravana@gmail.com",
    "status": "Active"
}
```

### Success Response (201)

```json
{
    "success": true,
    "message": "Customer added successfully."
}
```

### Error Response (400)

```json
{
    "success": false,
    "message": "Customer ID already exists."
}
```

---

## 3. Get All Customers

### Endpoint

GET /customers

### Description

Retrieves all customer records from the Saru POS system.

### Request Body

Not Required

### Success Response (200)

```json
{
    "success": true,
    "customers": [
        {
            "customer_id": "CUS001",
            "customer_name": "Saravana Kumar",
            "phone": "9876543210",
            "email": "saravana@gmail.com",
            "status": "Active"
        }
    ]
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "No customers found."
}
```

---

## 4. Get Customer By ID

### Endpoint

GET /customers/{customer_id}

### Description

Retrieves a specific customer using the customer ID.

### Example Endpoint

GET /customers/CUS001

### Request Body

Not Required

### Success Response (200)

```json
{
    "success": true,
    "customer": {
        "customer_id": "CUS001",
        "customer_name": "Saravana Kumar",
        "phone": "9876543210",
        "email": "saravana@gmail.com",
        "status": "Active"
    }
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Customer not found."
}
```

---

## 5. Update Customer

### Endpoint

PUT /customers/{customer_id}

### Description

Updates the details of an existing customer using the customer ID.

### Example Endpoint

PUT /customers/CUS001

### Request Body

```json
{
    "customer_name": "Saravana Kumar Updated",
    "phone": "9999999999",
    "email": "saravana.updated@gmail.com",
    "status": "Active"
}
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Customer updated successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Customer not found."
}
```

---

## 6. Delete Customer

### Endpoint

DELETE /customers/{customer_id}

### Description

Deletes an existing customer from the system using the customer ID.

### Example Endpoint

DELETE /customers/CUS001

### Request Body

Not Required

### Success Response (200)

```json
{
    "success": true,
    "message": "Customer deleted successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Customer not found."
}
```

---

# HTTP Status Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Request completed successfully |
| 201 | Resource created successfully |
| 400 | Invalid request or validation error |
| 401 | Authentication failed |
| 404 | Requested resource not found |

---

# Version History

| Version | Description |
|---------|-------------|
| v1.0 | Authentication Module + Customer CRUD Module Completed |