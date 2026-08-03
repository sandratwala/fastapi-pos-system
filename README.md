Project Description

This project is a CRUD REST API for a Point of Sale (POS) system, built with FastAPI and PostgreSQL.

Manages the full retail workflow: categories, suppliers, products, customers, users, sales, sale items, payments, and receipts.
Supports Create, Read, Update, and Delete operations for every entity.
Uses SQLAlchemy to model relationships between entities, such as products belonging to categories and suppliers, and sales linking to customers, users, and payments.
Validates all incoming data using Pydantic schemas.
Returns proper HTTP status codes, including 404 for records that don't exist and 400 for invalid or duplicate data.
Prevents invalid records, such as a sale item referencing a product or sale that doesn't exist.
Hashes user passwords before storing them, so plain-text passwords are never saved.
