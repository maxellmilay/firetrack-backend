# Incident App API Documentation

This document details the API endpoints provided by the `incident` app. All endpoints require authentication.

## Incidents

Base URL: `/incident/incidents/`

### List Incidents

*   **Method:** `GET`
*   **URL:** `/incident/incidents/`
*   **Request Body:** None
*   **Response Body (200 OK):**
    ```json
    [
      {
        "id": <integer>,
        "name": "<string>",
        "description": "<string>",
        "category": "<string>",
        "remarks": "<string>",
        "latitude": <float>,
        "longitude": <float>,
        "created_at": "<datetime_string>",
        "updated_at": "<datetime_string>"
      }
      // ... more objects
    ]
    ```

### Create Incident

*   **Method:** `POST`
*   **URL:** `/incident/incidents/`
*   **Request Body:**
    ```json
    {
      "name": "<string>",
      "description": "<string>",
      "category": "<string>",
      "remarks": "<string>",
      "latitude": <float>,
      "longitude": <float>
    }
    ```
*   **Response Body (201 Created):** A single Incident object (see format in List response).

### Retrieve Incident

*   **Method:** `GET`
*   **URL:** `/incident/incidents/<int:pk>/`
*   **Request Body:** None
*   **Response Body (200 OK):** A single Incident object (see format in List response).

### Update Incident

*   **Method:** `PUT`
*   **URL:** `/incident/incidents/<int:pk>/`
*   **Request Body:**
    ```json
    {
      "name": "<string>",
      "description": "<string>",
      "category": "<string>",
      "remarks": "<string>",
      "latitude": <float>,
      "longitude": <float>
    }
    ```
*   **Response Body (200 OK):** The updated Incident object (see format in List response).

### Delete Incident

*   **Method:** `DELETE`
*   **URL:** `/incident/incidents/<int:pk>/`
*   **Request Body:** None
*   **Response Body (204 No Content):** Empty.

## Travel Orders

Base URL: `/incident/travel-orders/`

### List Travel Orders

*   **Method:** `GET`
*   **URL:** `/incident/travel-orders/`
*   **Request Body:** None
*   **Response Body (200 OK):**
    ```json
    [
      {
        "id": <integer>,
        "incident": { /* Incident object, see above */ },
        "firetruck": { /* Firetruck object */ },
        "fireman": [
          { /* Fireman object */ },
          // ... more firemen
        ],
        "created_at": "<datetime_string>",
        "updated_at": "<datetime_string>"
      }
      // ... more objects
    ]
    ```

### Create Travel Order

*   **Method:** `POST`
*   **URL:** `/incident/travel-orders/`
*   **Request Body:**
    ```json
    {
      "incident": <incident_id>, // Integer ID
      "firetruck": <firetruck_id>, // Integer ID
      "fireman": [<fireman_id1>, <fireman_id2>, ...] // List of Integer IDs
    }
    ```
*   **Response Body (201 Created):** A single Travel Order object (see format in List response).

### Retrieve Travel Order

*   **Method:** `GET`
*   **URL:** `/incident/travel-orders/<int:pk>/`
*   **Request Body:** None
*   **Response Body (200 OK):** A single Travel Order object (see format in List response).

### Update Travel Order

*   **Method:** `PUT`
*   **URL:** `/incident/travel-orders/<int:pk>/`
*   **Request Body:**
    ```json
    {
      "incident": <incident_id>, // Integer ID
      "firetruck": <firetruck_id>, // Integer ID
      "fireman": [<fireman_id1>, <fireman_id2>, ...] // List of Integer IDs
    }
    ```
*   **Response Body (200 OK):** The updated Travel Order object (see format in List response).

### Delete Travel Order

*   **Method:** `DELETE`
*   **URL:** `/incident/travel-orders/<int:pk>/`
*   **Request Body:** None
*   **Response Body (204 No Content):** Empty.

## Incident Reports

Base URL: `/incident/incident-reports/`

### List Incident Reports

*   **Method:** `GET`
*   **URL:** `/incident/incident-reports/`
*   **Request Body:** None
*   **Response Body (200 OK):**
    ```json
    [
      {
        "id": <integer>,
        "title": "<string>",
        "incident": { /* Incident object, see above */ },
        "report": "<string>",
        "created_at": "<datetime_string>",
        "updated_at": "<datetime_string>"
      }
      // ... more objects
    ]
    ```

### Create Incident Report

*   **Method:** `POST`
*   **URL:** `/incident/incident-reports/`
*   **Request Body:**
    ```json
    {
      "title": "<string>",
      "incident": <incident_id>, // Integer ID
      "report": "<string>"
    }
    ```
*   **Response Body (201 Created):** A single Incident Report object (see format in List response).

### Retrieve Incident Report

*   **Method:** `GET`
*   **URL:** `/incident/incident-reports/<int:pk>/`
*   **Request Body:** None
*   **Response Body (200 OK):** A single Incident Report object (see format in List response).

### Update Incident Report

*   **Method:** `PUT`
*   **URL:** `/incident/incident-reports/<int:pk>/`
*   **Request Body:**
    ```json
    {
      "title": "<string>",
      "incident": <incident_id>, // Integer ID
      "report": "<string>"
    }
    ```
*   **Response Body (200 OK):** The updated Incident Report object (see format in List response).

### Delete Incident Report

*   **Method:** `DELETE`
*   **URL:** `/incident/incident-reports/<int:pk>/`
*   **Request Body:** None
*   **Response Body (204 No Content):** Empty. 