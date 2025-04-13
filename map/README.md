# Map API Documentation

## Coordinates Management

### List All Coordinates
- **URL**: `/api/map/coordinates/`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "id": "integer",
      "tracker_id": "string",
      "latitude": "float",
      "longitude": "float",
      "timestamp": "datetime"
    }
  ]
  ```

### Create Coordinate Entry
- **URL**: `/api/map/coordinates/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "tracker_id": "string",
    "latitude": "float",
    "longitude": "float"
  }
  ```
- **Response**: Created coordinate object

### Get Coordinate Entry Details
- **URL**: `/api/map/coordinates/{id}/`
- **Method**: `GET`
- **Response**: Coordinate object
  ```json
  {
    "id": "integer",
    "tracker_id": "string",
    "latitude": "float",
    "longitude": "float",
    "timestamp": "datetime"
  }
  ```

### Update Coordinate Entry
- **URL**: `/api/map/coordinates/{id}/`
- **Method**: `PUT`
- **Request Body**: Coordinate object fields to update
  ```json
  {
    "tracker_id": "string",
    "latitude": "float",
    "longitude": "float"
  }
  ```
- **Response**: Updated coordinate object

### Delete Coordinate Entry
- **URL**: `/api/map/coordinates/{id}/`
- **Method**: `DELETE`
- **Response**: No content 