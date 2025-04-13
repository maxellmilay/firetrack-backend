# Incident API Documentation

## Incident Management

### List All Incidents
- **URL**: `/api/incident/`
- **Method**: `GET`
- **Authentication**: Required
- **Response**:
  ```json
  [
    {
      "id": "integer",
      "name": "string",
      "creator": "integer",
      "response_time": "time",
      "status": "string",
      "remarks": "string",
      "location_name": "string",
      "latitude": "float",
      "longitude": "float",
      "date_created": "datetime",
      "date_ended": "datetime",
      "date_updated": "datetime"
    }
  ]
  ```

### Create Incident
- **URL**: `/api/incident/`
- **Method**: `POST`
- **Authentication**: Required
- **Request Body**:
  ```json
  {
    "name": "string",
    "creator": "integer",
    "response_time": "time",
    "status": "string",
    "remarks": "string",
    "location_name": "string",
    "latitude": "float",
    "longitude": "float",
    "date_ended": "datetime"
  }
  ```
- **Response**: Created incident object

### Get Incident Details
- **URL**: `/api/incident/{id}/`
- **Method**: `GET`
- **Authentication**: Required
- **Response**: Incident object

### Update Incident
- **URL**: `/api/incident/{id}/`
- **Method**: `PUT`
- **Authentication**: Required
- **Request Body**: Incident object fields to update
- **Response**: Updated incident object

### Delete Incident
- **URL**: `/api/incident/{id}/`
- **Method**: `DELETE`
- **Authentication**: Required
- **Response**: No content

## Incident Report Management

### List All Incident Reports
- **URL**: `/api/incident/reports/`
- **Method**: `GET`
- **Authentication**: Required
- **Response**:
  ```json
  [
    {
      "id": "integer",
      "incident": "integer",
      "reporter": "integer",
      "title": "string",
      "content": "string",
      "file": "string",
      "date_created": "datetime",
      "date_updated": "datetime"
    }
  ]
  ```

### Create Incident Report
- **URL**: `/api/incident/reports/`
- **Method**: `POST`
- **Authentication**: Required
- **Request Body**:
  ```json
  {
    "incident": "integer",
    "reporter": "integer",
    "title": "string",
    "content": "string",
    "file": "string"
  }
  ```
- **Response**: Created incident report object

### Get Incident Report Details
- **URL**: `/api/incident/reports/{id}/`
- **Method**: `GET`
- **Authentication**: Required
- **Response**: Incident report object

### Update Incident Report
- **URL**: `/api/incident/reports/{id}/`
- **Method**: `PUT`
- **Authentication**: Required
- **Request Body**: Incident report object fields to update
- **Response**: Updated incident report object

### Delete Incident Report
- **URL**: `/api/incident/reports/{id}/`
- **Method**: `DELETE`
- **Authentication**: Required
- **Response**: No content 