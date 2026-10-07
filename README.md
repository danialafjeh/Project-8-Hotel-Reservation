# 💻 About Project #8

[Complete Guide | Run this project on your computer](https://github.com/danialafjeh/Run-My-Projects-Locally)<br>
Projects are numbered in development order. Higher numbers represent newer projects that introduce new backend tools, concepts, and increasing levels of complexity throughout my learning journey.


# Hotel Reservation Management System (Website)

A full-stack hotel reservation web application developed with **Django (MVT Architecture)**. The project provides a complete hotel management experience, including room management, secure user authentication, reservation processing, reservation validation, and an administration panel.

The frontend template is based on a modern design from **themewagon.com**, which has been extensively customized and extended with additional pages and backend integration.

‼️ Website's language is in English.

---

# Technologies

### Backend

* Python
* Django
* Django MVT Architecture
* Django ORM
* PostgreSQL Database
* Django Authentication System
* Django Messages Framework

### Frontend

* HTML5
* CSS3
* JavaScript

---

# Project Structure

The project consists of three Django applications:

### Main App

Responsible for the core website features, including:

* Home page
* About Us
* Hotel Gallery
* Hotel Rooms
* Hotel Information
* Dynamic room display
* Dynamic gallery management

---

### Account App

Responsible for all user account operations:

* User Registration
* User Login
* User Logout
* User Profile
* Profile Editing
* Password Changing
* User Authentication
* Permission Validation

---

### Reservation App

Responsible for the complete hotel reservation workflow:

* Room Reservation
* Reservation Validation
* concurrency-safe booking.
* Reservation Cancellation
* Reservation History
* Reservation Price Calculation

---

# Features

## User Authentication

The application uses Django's built-in authentication system.

Features include:

* Sign Up
* Sign In
* Sign Out
* Secure Password Management
* Account's info Editing
* Password Editing

---

## Access Level Management

The backend completely separates guest accounts from management accounts.

During login, the backend validates user permissions.

A regular guest **cannot** log into the management section.

Management accounts **cannot** log in through the guest login page.

All invalid login attempts are properly handled and meaningful error messages are displayed.

User roles are displayed inside each user's profile.

Supported user roles:

* Guest
* Staff
* Manager

Only management accounts can access the Django Administration Panel.

---

## Hotel Management

Hotel information is fully dynamic.

Administrators can manage:

* Hotel Information
* Contact Information
* Gallery Images
* Rooms
* Reservations
* Users

using the Django Admin Panel.

---

## Room Info In Database

Each hotel room contains the following information:

* Room Name
* Room Number
* Room Image
* Guest Capacity
* beds info
* Price Per Night
* Is sale Status
* Sale Price Per Night
* Service Availability
* Created Date
* Updated Date

Rooms can be dynamically created, edited, activated, deactivated, or removed by administrators.

## Reservation Info In Database

Each reservation contains the foloowing information:

 * Related User
 * Related Room
 * Arrival Date
 * Departure Date
 * Total Price
 * Status (Pending, Confirm, Cancelled)
 * Created At
 * Updated At

## Hotel Info In Database

* Name
* Description
* Address
* Phone 1
* Phone 2
* Phone 3
* Email 1
* Email 2
* Email 3

## Hotel Gallary In Database

* Section
* Image
* Created At
  
---

## Reservation System

Main goal of this project was implementing a complete backend reservation logic.

The reservation system validates every submitted reservation before saving it.

Implemented validations include:

* Empty arrival date validation
* Empty departure date validation
* Room availability validation
* Room service status validation
* Arrival date cannot be in the past
* Arrival date must be before departure date
* Accurate reservation overlap detection
* Maximum reservation period (30 nights)
* Automatic stay duration calculation
* Automatic reservation price calculation
* Sale price calculation

Only valid reservations are stored in the database.

---

## Reservation Overlap Detection

The backend prevents multiple guests from reserving the same room during overlapping time periods.

The overlap validation has been fully implemented using Django ORM queries and accurately detects conflicts between reservation date ranges.

---

## User Profile

Each authenticated user has access to a personal profile page.

Users can:

* View account information
* Edit account information
* Change password
* View all reservations
* View reservation details
* Cancel any reservation

---

## Administration Panel

Managers can manage the entire website through Django Administration.

The administration panel provides full CRUD functionality for:

* Users
* Hotel Information
* Rooms
* Reservations
* Gallery Images

---

# Frontend

The frontend template was originally obtained from:

https://themewagon.com/

The template has been customized and extended to fit the requirements of this project.

Several new pages and backend integrations were implemented.

---

# Pages

The website contains the following pages:

* Home
* About Us
* Hotel Gallery
* Our Rooms
* Sign Up
* Sign In
* Update account's info
* Update account's password
* User Profile
* Room Reservation

---

# Main Learning Objectives

This project focuses on implementing real-world backend business logic using Django.

Major concepts practiced include:

* Business Logic Implementation (Main Purpose)
* Reservation Conflict Detection (Main Purpose)
* Date Validation (Main Purpose)
* Django MVT Architecture
* User Authentication
* Authorization
* ORM Queries
* CRUD Operations
* PostgreSQL Integration
* Dynamic Template Rendering
* Django Forms
* Django Messages Framework

---

