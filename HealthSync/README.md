#
## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [API Endpoints](#api-endpoints)
4. [Authentication](#authentication)
5. [Default Admin User](#default-admin-user)
## Installation

To set up the Patient Appointment System locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Start the server by running the command `uvicorn main:app --reload`.

## Usage

Once the server is up and running, you can interact with the API endpoints to perform various tasks such as creating appointments, managing patients and services, and retrieving appointment details.

## API Endpoints

### Admin

- `POST /adminToken`: Login to get access token for admin.
- `PUT /admin/{adminId}`: Update an admin by ID. (Not implemented)

### Appointment

- `POST /appointment`: Create a new appointment.
- `GET /appointment/{patientId}`: Retrieve appointments for a patient.
- `GET /todaysAppointments`: Retrieve all appointments for today.
- `GET /appointment`: Retrieve all appointments.
- `POST /prescription/{appointmentId}`: Create a prescription for an appointment.
- `GET /totalPendingAppointment`: Get total pending appointments.
- `POST /createPaymentLink`: Create a payment link for an appointment.

### Patient

- `POST /patient`: Create a new patient.
- `GET /patient/{patientId}`: Retrieve a patient by ID.
- `GET /patient`: Retrieve all patients.
- `PUT /patient/{patientId}`: Update a patient by ID.
- `DELETE /patient/{patientId}`: Delete a patient by ID.
- `GET /totalPatients`: Get total number of patients.

### Service

- `POST /service`: Create a new service.
- `GET /service`: Retrieve all services.
- `GET /service/{serviceId}`: Retrieve a service by ID.
- `PUT /service/{serviceId}`: Update a service by ID.
- `DELETE /service/{serviceId}`: Delete a service by ID.

### Slot

- `POST /slot`: Create a new slot.
- `GET /slot`: Retrieve all slots.
- `GET /slot/{slotId}`: Retrieve a slot by ID.
- `PUT /slot/{slotId}`: Update a slot by ID.
- `DELETE /slot/{slotId}`: Delete a slot by ID.

## Authentication

- CORS Origin: Describe CORS origin setup here.
- JWT Token Security: Explain how JWT token security is implemented.
- Stripe Integration: Add your Stripe API key to the `controllers/appointmentController.py` file for payment integration.

## Default Admin User

- Username: admin
- Password: admin

