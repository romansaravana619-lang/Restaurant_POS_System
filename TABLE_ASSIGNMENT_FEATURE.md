# SaruPOS Table Assignment Flow

## Customer creation
- The Customers form now includes an available-table selector.
- Only tables whose current status is `Available` are selectable.
- Customer creation with a selected table is atomic: customer + active dining session + table status update are committed together.
- The selected table becomes `Occupied` immediately.

## Customer list
- Active table number is shown for customers who currently have an active dining session.

## POS
- Selecting a customer with an active dining session automatically selects that customer's occupied table.
- The assigned occupied table is locked to prevent changing it to another table during that order.
- Customers without an active session can use available tables.

## Checkout
- Checkout permits an occupied table only when it is the active dining table for the selected customer.
- Successful checkout closes that dining session and returns the table to `Available` atomically with the bill/payment transaction.
