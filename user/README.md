# User API Documentation

This document describes the API endpoints available under the `/api/user/` path for managing users, teams, firemen, and incident commanders.

**Authentication:** All endpoints listed below, except for registration and standard login/logout/token endpoints, require authentication. Requests must include a valid authentication token (e.g., in the `Authorization: Token <your_token>` or `Authorization: Bearer <your_access_token>` header, depending on your setup).

## Authentication & Registration

These endpoints are provided by `dj-rest-auth`.

*   **Registration:**
    *   `POST /api/user/registration/`
    *   Creates a new user account.
    *   **Request Body:**
        ```json
        {
          "email": "user@example.com",
          "password": "yourpassword",
          "password2": "yourpassword",
          "username": "optional_username"
        }
        ```
        *Note: `username` is optional. `email` must be unique.*
    *   **Response:** User details upon successful registration.

*   **Login:**
    *   `POST /api/user/login/` (or potentially `/api/user/token/`)
    *   Authenticates a user and returns auth tokens (access and refresh, depending on configuration).
    *   **Request Body:**
        ```json
        {
          "email": "user@example.com",
          "password": "yourpassword"
        }
        ```
    *   **Response (Example using Simple JWT):**
        ```json
        {
          "refresh": "refresh_token_string",
          "access": "access_token_string"
        }
        ```
    *   **Response (Example using Knox):**
        ```json
        {
          "expiry": "...",
          "token": "authentication_token_string"
        }
        ```

*   **Logout:**
    *   `POST /api/user/logout/`
    *   Invalidates the user's auth token/session.
    *   Requires Authentication header.

*   **Verify Token:**
    *   `POST /api/user/token/verify/`
    *   Verifies if an access token is still valid.
    *   **Request Body:**
        ```json
        {
          "token": "access_token_string_to_verify"
        }
        ```
    *   **Response:**
        *   `200 OK` (Empty body): Token is valid.
        *   `401 Unauthorized` or `400 Bad Request`: Token is invalid or expired.

*   **Refresh Token:**
    *   `POST /api/user/token/refresh/`
    *   Obtains a new access token using a valid refresh token.
    *   **Request Body:**
        ```json
        {
          "refresh": "refresh_token_string"
        }
        ```
    *   **Response:**
        ```json
        {
          "access": "new_access_token_string"
          // Optionally, may include a new refresh token if rotation is enabled
          // "refresh": "new_refresh_token_string"
        }
        ```

*   **(Other `dj-rest-auth` endpoints):** Password reset, password change, etc., are available under `/api/user/`. Refer to the `dj-rest-auth` documentation for details.

## Teams

Base Path: `/api/user/teams/`

*   **List Teams:**
    *   `GET /api/user/teams/`
    *   Requires Authentication.
    *   Returns a list of all teams.
    *   **Response Body (Example):**
        ```json
        [
          {
            "id": 1,
            "name": "Alpha Team",
            "description": "Primary response team",
            "created_at": "...",
            "updated_at": "..."
          },
          {
            "id": 2,
            "name": "Bravo Team",
            "description": null,
            "created_at": "...",
            "updated_at": "..."
          }
        ]
        ```

*   **Create Team:**
    *   `POST /api/user/teams/`
    *   Requires Authentication.
    *   Creates a new team.
    *   **Request Body:**
        ```json
        {
          "name": "Charlie Team",
          "description": "Support team"
        }
        ```
    *   **Response Body:** The newly created team object.

*   **Retrieve Team:**
    *   `GET /api/user/teams/<int:pk>/`
    *   Requires Authentication.
    *   Returns details for a specific team.
    *   **Response Body:** A single team object (like in the List example).

*   **Update Team:**
    *   `PUT /api/user/teams/<int:pk>/`
    *   Requires Authentication.
    *   Updates details for a specific team.
    *   **Request Body:** Fields to update (e.g., `name`, `description`).
    *   **Response Body:** The updated team object.

*   **Delete Team:**
    *   `DELETE /api/user/teams/<int:pk>/`
    *   Requires Authentication.
    *   Deletes a specific team.
    *   **Response:** `204 No Content` on success.

## Firemen

Base Path: `/api/user/firemen/`

*   **List Firemen:**
    *   `GET /api/user/firemen/`
    *   Requires Authentication.
    *   Returns a list of all firemen profiles.
    *   **Response Body (Example):**
        ```json
        [
          {
            "id": 1,
            "user": {
                "id": 2,
                "username": "firefighter_john",
                "email": "john.doe@example.com",
                "image_url": null,
                "bio": null,
                "phone_number": null,
                "date_of_birth": null
                // ... other user fields not including password
            },
            "team": [
                {"id": 1, "name": "Alpha Team", "description": "...", ...}
            ],
            "created_at": "...",
            "updated_at": "..."
          }
          // ... other firemen
        ]
        ```

*   **Create Fireman:**
    *   `POST /api/user/firemen/`
    *   Requires Authentication.
    *   Creates a new fireman profile. *Note: This likely assumes a `User` object already exists. The exact creation logic depends on how the `FiremanSerializer` handles nested creation or if it expects a user ID.* You might need to provide the `user` ID or nested user data depending on the serializer setup. Check `FiremanSerializer` details and potentially adjust it for creation.
    *   **Request Body (Example - needs verification based on serializer):**
        ```json
        {
          "user": 3, // Assuming User ID 3 exists and is not yet a Fireman/IC
          "team": [1, 2] // Assigning to Team IDs 1 and 2
        }
        ```
        OR potentially (if serializer supports nested creation):
        ```json
         {
           "user": {
               "email": "new.fireman@example.com",
               "password": "...", // Potentially needed if creating user simultaneously
               // ... other required user fields
           },
           "team": [1]
         }
        ```
    *   **Response Body:** The newly created fireman object.

*   **Retrieve Fireman:**
    *   `GET /api/user/firemen/<int:pk>/`
    *   Requires Authentication.
    *   Returns details for a specific fireman.
    *   **Response Body:** A single fireman object (like in the List example).

*   **Update Fireman:**
    *   `PUT /api/user/firemen/<int:pk>/`
    *   Requires Authentication.
    *   Updates details for a specific fireman. *Note: Updating nested `user` data might require specific serializer configuration.* You likely cannot update the `user` field directly; update user details via separate user profile endpoints if needed. You can update the `team` membership.
    *   **Request Body (Example):**
        ```json
        {
            "team": [2] // Change team membership to only Team ID 2
        }
        ```
    *   **Response Body:** The updated fireman object.

*   **Delete Fireman:**
    *   `DELETE /api/user/firemen/<int:pk>/`
    *   Requires Authentication.
    *   Deletes a specific fireman profile (the associated `User` object remains unless `on_delete=models.CASCADE` was specifically set differently on the `OneToOneField`).
    *   **Response:** `204 No Content` on success.

## Incident Commanders

Base Path: `/api/user/incident-commanders/`

These endpoints follow the same structure and principles as the Firemen endpoints, but operate on `IncidentCommander` objects.

*   **List Incident Commanders:** `GET /api/user/incident-commanders/`
*   **Create Incident Commander:** `POST /api/user/incident-commanders/` (See notes on Fireman creation regarding user data)
*   **Retrieve Incident Commander:** `GET /api/user/incident-commanders/<int:pk>/`
*   **Update Incident Commander:** `PUT /api/user/incident-commanders/<int:pk>/` (See notes on Fireman update)
*   **Delete Incident Commander:** `DELETE /api/user/incident-commanders/<int:pk>/`

All Incident Commander endpoints require Authentication and have similar request/response structures to their Fireman counterparts, substituting `IncidentCommander` details. 