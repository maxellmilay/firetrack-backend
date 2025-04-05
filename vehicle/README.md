# Vehicle App API Documentation

This document details the API endpoints provided by the `vehicle` app. All endpoints require authentication.

## Firetrucks

Base URL: `/vehicle/firetrucks/`

### List Firetrucks

*   **Method:** `GET`
*   **URL:** `/vehicle/firetrucks/`
*   **Request Body:** None
*   **Response Body (200 OK):**
    ```json
    [
      {
        "id": <integer>,
        "name": "<string>",
        "description": "<string>" or null,
        "created_at": "<datetime_string>",
        "updated_at": "<datetime_string>"
      }
      // ... more objects
    ]
    ```

### Create Firetruck

*   **Method:** `POST`
*   **URL:** `/vehicle/firetrucks/`
*   **Request Body:**
    ```json
    {
      "name": "<string>",
      "description": "<string>" // Optional
    }
    ```
*   **Response Body (201 Created):** A single Firetruck object (see format in List response).

### Retrieve Firetruck

*   **Method:** `GET`
*   **URL:** `/vehicle/firetrucks/<int:pk>/`
*   **Request Body:** None
*   **Response Body (200 OK):** A single Firetruck object (see format in List response).

### Update Firetruck

*   **Method:** `PUT`
*   **URL:** `/vehicle/firetrucks/<int:pk>/`
*   **Request Body:**
    ```json
    {
      "name": "<string>",
      "description": "<string>" // Optional
    }
    ```
*   **Response Body (200 OK):** The updated Firetruck object (see format in List response).

### Delete Firetruck

*   **Method:** `DELETE`
*   **URL:** `/vehicle/firetrucks/<int:pk>/`
*   **Request Body:** None
*   **Response Body (204 No Content):** Empty. 