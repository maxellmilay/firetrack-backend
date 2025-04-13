# User API Documentation

## Authentication Endpoints

These endpoints are provided by `dj_rest_auth` for authentication.

### Login
- **URL**: `/api/user/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "key": "string"
  }
  ```

### Registration
- **URL**: `/api/user/registration/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "password1": "string",
    "password2": "string"
  }
  ```
- **Response**:
  ```json
  {
    "key": "string"
  }
  ```

## User Management

### List All Users
- **URL**: `/api/user/manage/`
- **Method**: `GET`
- **Authentication**: Required
- **Response**:
  ```json
  [
    {
      "id": "integer",
      "username": "string",
      "email": "string",
      "avatar_url": "string",
      "role": "string",
      "tracker_id": "string",
      "squad": "integer"
    }
  ]
  ```

### Create User
- **URL**: `/api/user/manage/`
- **Method**: `POST`
- **Authentication**: Required
- **Request Body**:
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string",
    "avatar_url": "string",
    "role": "string",
    "tracker_id": "string",
    "squad": "integer"
  }
  ```
- **Response**: Created user object

### Get User Details
- **URL**: `/api/user/manage/{id}/`
- **Method**: `GET`
- **Authentication**: Required
- **Response**: User object

### Update User
- **URL**: `/api/user/manage/{id}/`
- **Method**: `PUT`
- **Authentication**: Required
- **Request Body**: User object fields to update
- **Response**: Updated user object

### Delete User
- **URL**: `/api/user/manage/{id}/`
- **Method**: `DELETE`
- **Authentication**: Required
- **Response**: No content

## Squad Management

### List All Squads
- **URL**: `/api/user/squads/`
- **Method**: `GET`
- **Authentication**: Required
- **Response**:
  ```json
  [
    {
      "id": "integer",
      "name": "string",
      "leader": "integer",
      "description": "string",
      "firestation": "integer",
      "created_at": "datetime",
      "updated_at": "datetime",
      "members": [
        {
          "id": "integer",
          "username": "string",
          "email": "string",
          "avatar_url": "string",
          "role": "string",
          "tracker_id": "string"
        }
      ]
    }
  ]
  ```

### Create Squad
- **URL**: `/api/user/squads/`
- **Method**: `POST`
- **Authentication**: Required
- **Request Body**:
  ```json
  {
    "name": "string",
    "leader": "integer",
    "description": "string",
    "firestation": "integer"
  }
  ```
- **Response**: Created squad object

### Get Squad Details
- **URL**: `/api/user/squads/{id}/`
- **Method**: `GET`
- **Authentication**: Required
- **Response**: Squad object with members

### Update Squad
- **URL**: `/api/user/squads/{id}/`
- **Method**: `PUT`
- **Authentication**: Required
- **Request Body**: Squad object fields to update
- **Response**: Updated squad object

### Delete Squad
- **URL**: `/api/user/squads/{id}/`
- **Method**: `DELETE`
- **Authentication**: Required
- **Response**: No content

## Firestation Management

### List All Firestations
- **URL**: `/api/user/firestations/`
- **Method**: `GET`
- **Authentication**: Required
- **Response**:
  ```json
  [
    {
      "id": "integer",
      "name": "string",
      "address": "string",
      "latitude": "float",
      "longitude": "float",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
  ```

### Create Firestation
- **URL**: `/api/user/firestations/`
- **Method**: `POST`
- **Authentication**: Required
- **Request Body**:
  ```json
  {
    "name": "string",
    "address": "string",
    "latitude": "float",
    "longitude": "float"
  }
  ```
- **Response**: Created firestation object

### Get Firestation Details
- **URL**: `/api/user/firestations/{id}/`
- **Method**: `GET`
- **Authentication**: Required
- **Response**: Firestation object

### Update Firestation
- **URL**: `/api/user/firestations/{id}/`
- **Method**: `PUT`
- **Authentication**: Required
- **Request Body**: Firestation object fields to update
- **Response**: Updated firestation object

### Delete Firestation
- **URL**: `/api/user/firestations/{id}/`
- **Method**: `DELETE`
- **Authentication**: Required
- **Response**: No content 