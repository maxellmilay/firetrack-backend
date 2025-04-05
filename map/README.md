# Map App API Documentation

This document details the API endpoints provided by the `map` app. All endpoints require authentication.

## Fireman Coordinates

Base URL: `/map/fireman-coordinates/`

### List Fireman Coordinates

*   **Method:** `GET`
*   **URL:** `/map/fireman-coordinates/`
*   **Request Body:** None
*   **Response Body (200 OK):**
    ```json
    [
      {
        "id": <integer>,
        "fireman": {
          "id": <integer>,
          "user": {
            "id": <integer>,
            "username": "<string>",
            "email": "<string>",
            // ... other User fields
          },
          "team": [
            {
              "id": <integer>,
              // ... other Team fields
            }
          ]
          // ... other Fireman fields
        },
        "latitude": <float>,
        "longitude": <float>,
        "timestamp": "<datetime_string>"
      }
      // ... more objects
    ]
    ```

### Create Fireman Coordinates

*   **Method:** `POST`
*   **URL:** `/map/fireman-coordinates/`
*   **Request Body:**
    ```json
    {
      "fireman": <fireman_id>, // Integer ID
      "latitude": <float>,
      "longitude": <float>
    }
    ```
*   **Response Body (201 Created):** A single Fireman Coordinates object (see format in List response).

### Retrieve Fireman Coordinates

*   **Method:** `GET`
*   **URL:** `/map/fireman-coordinates/<int:pk>/`
*   **Request Body:** None
*   **Response Body (200 OK):** A single Fireman Coordinates object (see format in List response).

### Update Fireman Coordinates

*   **Method:** `PUT`
*   **URL:** `/map/fireman-coordinates/<int:pk>/`
*   **Request Body:**
    ```json
    {
      "fireman": <fireman_id>, // Integer ID
      "latitude": <float>,
      "longitude": <float>
    }
    ```
*   **Response Body (200 OK):** The updated Fireman Coordinates object (see format in List response).

### Delete Fireman Coordinates

*   **Method:** `DELETE`
*   **URL:** `/map/fireman-coordinates/<int:pk>/`
*   **Request Body:** None
*   **Response Body (204 No Content):** Empty.

## Firetruck Coordinates

Base URL: `/map/firetruck-coordinates/`

### List Firetruck Coordinates

*   **Method:** `GET`
*   **URL:** `/map/firetruck-coordinates/`
*   **Request Body:** None
*   **Response Body (200 OK):**
    ```json
    [
      {
        "id": <integer>,
        "truck": {
          "id": <integer>,
          // ... other Firetruck fields
        },
        "latitude": <float>,
        "longitude": <float>,
        "timestamp": "<datetime_string>"
      }
      // ... more objects
    ]
    ```

### Create Firetruck Coordinates

*   **Method:** `POST`
*   **URL:** `/map/firetruck-coordinates/`
*   **Request Body:**
    ```json
    {
      "truck": <firetruck_id>, // Integer ID
      "latitude": <float>,
      "longitude": <float>
    }
    ```
*   **Response Body (201 Created):** A single Firetruck Coordinates object (see format in List response).

### Retrieve Firetruck Coordinates

*   **Method:** `GET`
*   **URL:** `/map/firetruck-coordinates/<int:pk>/`
*   **Request Body:** None
*   **Response Body (200 OK):** A single Firetruck Coordinates object (see format in List response).

### Update Firetruck Coordinates

*   **Method:** `PUT`
*   **URL:** `/map/firetruck-coordinates/<int:pk>/`
*   **Request Body:**
    ```json
    {
      "truck": <firetruck_id>, // Integer ID
      "latitude": <float>,
      "longitude": <float>
    }
    ```
*   **Response Body (200 OK):** The updated Firetruck Coordinates object (see format in List response).

### Delete Firetruck Coordinates

*   **Method:** `DELETE`
*   **URL:** `/map/firetruck-coordinates/<int:pk>/`
*   **Request Body:** None
*   **Response Body (204 No Content):** Empty. 