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


---

# Inventory Module

Base URL:

```
http://127.0.0.1:5000
```

---

## 1. Create Inventory Item

**Endpoint**

```
POST /inventory-items
```

**Description**

Creates a new inventory item.

### Request Body

```json
{
    "inventory_id": "INV001",
    "supplier_id": "SUP001",
    "item_name": "Basmati Rice",
    "unit": "kg",
    "quantity": 50,
    "unit_cost": 95,
    "reorder_level": 5,
    "status": "Active"
}
```

### Success Response (201)

```json
{
    "success": true,
    "message": "Inventory item added successfully."
}
```

### Error Response (400)

```json
{
    "success": false,
    "message": "Inventory ID already exists."
}
```

---

## 2. Get All Inventory Items

**Endpoint**

```
GET /inventory-items
```

**Description**

Retrieves all inventory items from the database.

### Success Response (200)

```json
{
    "success": true,
    "inventory_items": [
        {
            "inventory_id": "INV001",
            "supplier_id": "SUP001",
            "item_name": "Basmati Rice",
            "unit": "kg",
            "quantity": 50,
            "unit_cost": 95,
            "reorder_level": 5,
            "status": "Active"
        }
    ]
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "No inventory items found."
}
```

---

## 3. Get Inventory Item By ID

**Endpoint**

```
GET /inventory-items/{inventory_id}
```

### Example

```
GET /inventory-items/INV001
```

**Description**

Retrieves a specific inventory item using its inventory ID.

### Success Response (200)

```json
{
    "success": true,
    "inventory_item": {
        "inventory_id": "INV001",
        "supplier_id": "SUP001",
        "item_name": "Basmati Rice",
        "unit": "kg",
        "quantity": 50,
        "unit_cost": 95,
        "reorder_level": 5,
        "status": "Active"
    }
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Inventory item not found."
}
```

---

## 4. Update Inventory Item

**Endpoint**

```
PUT /inventory-items/{inventory_id}
```

### Example

```
PUT /inventory-items/INV001
```

### Request Body

```json
{
    "supplier_id": "SUP001",
    "item_name": "Basmati Rice Premium",
    "unit": "kg",
    "quantity": 75,
    "unit_cost": 100,
    "reorder_level": 10,
    "status": "Active"
}
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Inventory item updated successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Inventory item not found."
}
```

---

## 5. Delete Inventory Item

**Endpoint**

```
DELETE /inventory-items/{inventory_id}
```

### Example

```
DELETE /inventory-items/INV001
```

**Description**

Deletes an inventory item from the database.

### Success Response (200)

```json
{
    "success": true,
    "message": "Inventory item deleted successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Inventory item not found."
}
```

---

## Inventory Item Fields

| Field | Type | Description |
|------|------|-------------|
| inventory_id | String | Unique inventory item ID |
| supplier_id | String | Supplier ID (Foreign Key) |
| item_name | String | Inventory item name |
| unit | String | Unit of measurement (kg, litre, piece, bottle, etc.) |
| quantity | Float | Current available stock quantity |
| unit_cost | Float | Cost per unit |
| reorder_level | Float | Minimum stock level before reordering |
| status | String | Inventory item status (Active / Inactive) |

---

---

# Category Module

Base URL:

```
http://127.0.0.1:5000
```

---

## 1. Create Category

**Endpoint**

```
POST /categories
```

**Description**

Creates a new menu category.

### Request Body

```json
{
    "category_id": "CAT001",
    "category_name": "Main Course",
    "description": "Main food items",
    "status": "Active"
}
```

### Success Response (201)

```json
{
    "success": true,
    "message": "Category added successfully."
}
```

### Error Response (400)

```json
{
    "success": false,
    "message": "Category with this ID or name already exists."
}
```

---

## 2. Get All Categories

**Endpoint**

```
GET /categories
```

**Description**

Retrieves all categories ordered alphabetically.

### Success Response (200)

```json
{
    "success": true,
    "categories": [
        {
            "category_id": "CAT001",
            "category_name": "Main Course",
            "description": "Main food items",
            "status": "Active"
        }
    ]
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "No categories found."
}
```

---

## 3. Get Category By ID

**Endpoint**

```
GET /categories/{category_id}
```

### Example

```
GET /categories/CAT001
```

### Success Response (200)

```json
{
    "success": true,
    "category": {
        "category_id": "CAT001",
        "category_name": "Main Course",
        "description": "Main food items",
        "status": "Active"
    }
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Category not found."
}
```

---

## 4. Update Category

**Endpoint**

```
PUT /categories/{category_id}
```

### Example

```
PUT /categories/CAT001
```

### Request Body

```json
{
    "category_name": "Main Course",
    "description": "Updated category description",
    "status": "Active"
}
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Category updated successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Category not found."
}
```

---

## 5. Delete Category

**Endpoint**

```
DELETE /categories/{category_id}
```

### Example

```
DELETE /categories/CAT001
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Category deleted successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Category not found."
}
```

---

## Category Fields

| Field | Type | Description |
|------|------|-------------|
| category_id | String | Unique category ID |
| category_name | String | Category name |
| description | String | Category description |
| status | String | Category status (Active / Inactive) |

---

---

# Category Module

Base URL:

```
http://127.0.0.1:5000
```

---

## 1. Create Category

**Endpoint**

```
POST /categories
```

**Description**

Creates a new menu category.

### Request Body

```json
{
    "category_id": "CAT001",
    "category_name": "Main Course",
    "description": "Main food items",
    "status": "Active"
}
```

### Success Response (201)

```json
{
    "success": true,
    "message": "Category added successfully."
}
```

### Error Response (400)

```json
{
    "success": false,
    "message": "Category with this ID or name already exists."
}
```

---

## 2. Get All Categories

**Endpoint**

```
GET /categories
```

**Description**

Retrieves all categories ordered alphabetically.

### Success Response (200)

```json
{
    "success": true,
    "categories": [
        {
            "category_id": "CAT001",
            "category_name": "Main Course",
            "description": "Main food items",
            "status": "Active"
        }
    ]
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "No categories found."
}
```

---

## 3. Get Category By ID

**Endpoint**

```
GET /categories/{category_id}
```

### Example

```
GET /categories/CAT001
```

### Success Response (200)

```json
{
    "success": true,
    "category": {
        "category_id": "CAT001",
        "category_name": "Main Course",
        "description": "Main food items",
        "status": "Active"
    }
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Category not found."
}
```

---

## 4. Update Category

**Endpoint**

```
PUT /categories/{category_id}
```

### Example

```
PUT /categories/CAT001
```

### Request Body

```json
{
    "category_name": "Main Course",
    "description": "Updated category description",
    "status": "Active"
}
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Category updated successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Category not found."
}
```

---

## 5. Delete Category

**Endpoint**

```
DELETE /categories/{category_id}
```

### Example

```
DELETE /categories/CAT001
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Category deleted successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Category not found."
}
```

---

## Category Fields

| Field | Type | Description |
|------|------|-------------|
| category_id | String | Unique category ID |
| category_name | String | Category name |
| description | String | Category description |
| status | String | Category status (Active / Inactive) |

---

---

# Menu Item Module

Base URL:

```text
http://127.0.0.1:5000
```

---

## 1. Create Menu Item

**Endpoint**

```text
POST /menu-items
```

**Description**

Creates a new menu item and associates it with an existing menu category.

### Request Body

```json
{
    "menu_item_id": "MENU001",
    "category_id": "CAT100",
    "item_name": "Tomato Soup",
    "price": 120,
    "description": "Fresh tomato soup",
    "availability": "Available"
}
```

### Success Response (201)

```json
{
    "success": true,
    "message": "Menu item added successfully."
}
```

### Error Response (400)

```json
{
    "success": false,
    "message": "Menu item with this ID already exists or category does not exist."
}
```

---

## 2. Get All Menu Items

**Endpoint**

```text
GET /menu-items
```

**Description**

Retrieves all menu items ordered alphabetically by item name.

### Success Response (200)

```json
{
    "success": true,
    "menu_items": [
        {
            "menu_item_id": "MENU001",
            "category_id": "CAT100",
            "item_name": "Tomato Soup",
            "price": 120,
            "description": "Fresh tomato soup",
            "availability": "Available"
        }
    ]
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "No menu items found."
}
```

---

## 3. Get Menu Item By ID

**Endpoint**

```text
GET /menu-items/{menu_item_id}
```

### Example

```text
GET /menu-items/MENU001
```

### Success Response (200)

```json
{
    "success": true,
    "menu_item": {
        "menu_item_id": "MENU001",
        "category_id": "CAT100",
        "item_name": "Tomato Soup",
        "price": 120,
        "description": "Fresh tomato soup",
        "availability": "Available"
    }
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Menu item not found."
}
```

---

## 4. Update Menu Item

**Endpoint**

```text
PUT /menu-items/{menu_item_id}
```

### Example

```text
PUT /menu-items/MENU001
```

### Request Body

```json
{
    "category_id": "CAT100",
    "item_name": "Tomato Soup Special",
    "price": 140,
    "description": "Fresh tomato soup with special seasoning",
    "availability": "Available"
}
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Menu item updated successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Menu item not found."
}
```

---

## 5. Delete Menu Item

**Endpoint**

```text
DELETE /menu-items/{menu_item_id}
```

### Example

```text
DELETE /menu-items/MENU001
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Menu item deleted successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Menu item not found."
}
```

### Referenced Menu Item Error

If the menu item is referenced by an existing billing record:

```json
{
    "success": false,
    "message": "Menu item cannot be deleted because it is referenced by existing records."
}
```

---

## Menu Item Fields

| Field | Type | Description |
|------|------|-------------|
| menu_item_id | String | Unique menu item ID |
| category_id | String | ID of the associated menu category |
| item_name | String | Name of the menu item |
| price | Float | Selling price of the menu item |
| description | String | Description of the menu item |
| availability | String | Availability status of the menu item |

---

## Menu Item Relationship

```text
categories
     │
     │ category_id
     ▼
menu_items
     │
     │ menu_item_id
     ▼
bill_items
```

---

---

# Restaurant Table Module

Base URL:

```text
http://127.0.0.1:5000
```

---

## 1. Create Restaurant Table

**Endpoint**

```text
POST /restaurant-tables
```

### Request Body

```json
{
    "table_id": "TABLE001",
    "table_number": "T01",
    "capacity": 4,
    "status": "Available"
}
```

### Success Response (201)

```json
{
    "success": true,
    "message": "Restaurant table added successfully."
}
```

### Error Response (400)

```json
{
    "success": false,
    "message": "Restaurant table with this ID or table number already exists."
}
```

---

## 2. Get All Restaurant Tables

**Endpoint**

```text
GET /restaurant-tables
```

### Success Response (200)

```json
{
    "success": true,
    "restaurant_tables": [
        {
            "table_id": "TABLE001",
            "table_number": "T01",
            "capacity": 4,
            "status": "Available"
        }
    ]
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "No restaurant tables found."
}
```

---

## 3. Get Restaurant Table By ID

**Endpoint**

```text
GET /restaurant-tables/{table_id}
```

### Example

```text
GET /restaurant-tables/TABLE001
```

### Success Response (200)

```json
{
    "success": true,
    "restaurant_table": {
        "table_id": "TABLE001",
        "table_number": "T01",
        "capacity": 4,
        "status": "Available"
    }
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Restaurant table not found."
}
```

---

## 4. Update Restaurant Table

**Endpoint**

```text
PUT /restaurant-tables/{table_id}
```

### Example

```text
PUT /restaurant-tables/TABLE001
```

### Request Body

```json
{
    "table_number": "T01",
    "capacity": 6,
    "status": "Available"
}
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Restaurant table updated successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Restaurant table not found."
}
```

---

## 5. Delete Restaurant Table

**Endpoint**

```text
DELETE /restaurant-tables/{table_id}
```

### Example

```text
DELETE /restaurant-tables/TABLE001
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Restaurant table deleted successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Restaurant table not found."
}
```

### Referenced Table Error

If the restaurant table is referenced by an existing bill:

```json
{
    "success": false,
    "message": "Restaurant table cannot be deleted because it is referenced by existing records."
}
```

---

## Restaurant Table Fields

| Field | Type | Description |
|------|------|-------------|
| table_id | String | Unique restaurant table ID |
| table_number | String | Unique table number or name |
| capacity | Integer | Maximum seating capacity |
| status | String | Current table status |

---

# Billing Module

Base URL:

```text
http://127.0.0.1:5000
```

---

## 1. Create Bill

**Endpoint**

```text
POST /bills
```

**Description**

Creates a new bill for a customer, employee, and restaurant table.

### Request Body

```json
{
    "bill_id": "BILL001",
    "customer_id": "CUS001",
    "employee_id": "EMP001",
    "table_id": "TABLE001",
    "invoice_number": "INV-2026-0001",
    "bill_date": "2026-08-09",
    "total_amount": 1250.00,
    "status": "Completed"
}
```

### Success Response (201)

```json
{
    "success": true,
    "message": "Bill added successfully."
}
```

### Error Response (400)

```json
{
    "success": false,
    "message": "Request body must be valid JSON."
}
```

### Validation Error (400)

```json
{
    "success": false,
    "message": "All fields (bill_id, customer_id, employee_id, table_id, invoice_number, bill_date, total_amount, status) are required."
}
```

### Service Error (400)

```json
{
    "success": false,
    "message": "Bill with this ID or invoice number already exists, or a referenced record does not exist."
}
```

---

## 2. Get All Bills

**Endpoint**

```text
GET /bills
```

**Description**

Retrieves all bills ordered by bill date in descending order.

### Success Response (200)

```json
{
    "success": true,
    "bills": [
        {
            "bill_id": "BILL001",
            "customer_id": "CUS001",
            "employee_id": "EMP001",
            "table_id": "TABLE001",
            "invoice_number": "INV-2026-0001",
            "bill_date": "2026-08-09",
            "total_amount": 1250.00,
            "status": "Completed"
        }
    ]
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "No bills found."
}
```

---

## 3. Get Bill By ID

**Endpoint**

```text
GET /bills/{bill_id}
```

**Description**

Retrieves a specific bill using its bill ID.

### Example

```text
GET /bills/BILL001
```

### Success Response (200)

```json
{
    "success": true,
    "bill": {
        "bill_id": "BILL001",
        "customer_id": "CUS001",
        "employee_id": "EMP001",
        "table_id": "TABLE001",
        "invoice_number": "INV-2026-0001",
        "bill_date": "2026-08-09",
        "total_amount": 1250.00,
        "status": "Completed"
    }
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Bill not found."
}
```

---

## 4. Update Bill

**Endpoint**

```text
PUT /bills/{bill_id}
```

**Description**

Updates an existing bill using its bill ID.

### Example

```text
PUT /bills/BILL001
```

### Request Body

```json
{
    "customer_id": "CUS001",
    "employee_id": "EMP001",
    "table_id": "TABLE001",
    "invoice_number": "INV-2026-0001",
    "bill_date": "2026-08-09",
    "total_amount": 1350.00,
    "status": "Completed"
}
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Bill updated successfully."
}
```

### Error Response (400)

```json
{
    "success": false,
    "message": "Request body must be valid JSON."
}
```

### Validation Error (400)

```json
{
    "success": false,
    "message": "All fields (customer_id, employee_id, table_id, invoice_number, bill_date, total_amount, status) are required."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Bill not found."
}
```

---

## 5. Delete Bill

**Endpoint**

```text
DELETE /bills/{bill_id}
```

**Description**

Deletes an existing bill using its bill ID.

### Example

```text
DELETE /bills/BILL001
```

### Success Response (200)

```json
{
    "success": true,
    "message": "Bill deleted successfully."
}
```

### Error Response (404)

```json
{
    "success": false,
    "message": "Bill not found."
}
```

### Referenced Bill Error (404)

```json
{
    "success": false,
    "message": "Bill cannot be deleted because it is referenced by existing records."
}
```

---

## Bill Fields

| Field | Type | Description |
|------|------|-------------|
| bill_id | String | Unique bill ID |
| customer_id | String | ID of the associated customer |
| employee_id | String | ID of the employee who created the bill |
| table_id | String | ID of the associated restaurant table |
| invoice_number | String | Unique invoice number |
| bill_date | String | Date the bill was created |
| total_amount | Float | Total amount for the bill |
| status | String | Current bill status |

---
