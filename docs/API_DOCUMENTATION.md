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

# Supplier APIs

---

## POST /suppliers

### Description

Creates a new supplier record in the system.

### Request Body

```json
{
    "supplier_id": "SUP001",
    "supplier_name": "ABC Foods",
    "contact_person": "Rajesh",
    "phone": "9876543210",
    "email": "abcfoods@gmail.com",
    "address": "Coimbatore",
    "status": "Active"
}
```

### Success Response

```json
{
    "success": true,
    "message": "Supplier added successfully."
}
```

**Status Code:** `201 Created`

---

## GET /suppliers

### Description

Retrieves all suppliers available in the system.

### Success Response

```json
{
    "success": true,
    "suppliers": [
        {
            "supplier_id": "SUP001",
            "supplier_name": "ABC Foods",
            "contact_person": "Rajesh",
            "phone": "9876543210",
            "email": "abcfoods@gmail.com",
            "address": "Coimbatore",
            "status": "Active"
        }
    ]
}
```

**Status Code:** `200 OK`

---

## GET /suppliers/{supplier_id}

### Description

Retrieves a supplier using the unique supplier ID.

### Example

```http
GET /suppliers/SUP001
```

### Success Response

```json
{
    "success": true,
    "supplier": {
        "supplier_id": "SUP001",
        "supplier_name": "ABC Foods",
        "contact_person": "Rajesh",
        "phone": "9876543210",
        "email": "abcfoods@gmail.com",
        "address": "Coimbatore",
        "status": "Active"
    }
}
```

**Status Code:** `200 OK`

---

## PUT /suppliers/{supplier_id}

### Description

Updates an existing supplier.

### Example

```http
PUT /suppliers/SUP001
```

### Request Body

```json
{
    "supplier_name": "ABC Foods Pvt Ltd",
    "contact_person": "Rajesh Kumar",
    "phone": "9876543210",
    "email": "abcfoods@gmail.com",
    "address": "Coimbatore, Tamil Nadu",
    "status": "Active"
}
```

### Success Response

```json
{
    "success": true,
    "message": "Supplier updated successfully."
}
```

**Status Code:** `200 OK`

---

## DELETE /suppliers/{supplier_id}

### Description

Deletes an existing supplier from the system.

### Example

```http
DELETE /suppliers/SUP001
```

### Success Response

```json
{
    "success": true,
    "message": "Supplier deleted successfully."
}
```

**Status Code:** `200 OK`

---

## Error Response Format

```json
{
    "success": false,
    "message": "Supplier not found."
}
```

**Common Status Codes**

| Status Code | Description |
|-------------|-------------|
| 200 | Request completed successfully |
| 201 | Supplier created successfully |
| 400 | Invalid request body or validation failed |
| 404 | Supplier not found |
| 500 | Internal server error |

---