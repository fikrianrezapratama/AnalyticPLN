# Optical-Probe Data Analitycs

This is a simple Flask application for authentication and data fetching from an external API.

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add the following variables:

   ```
   API_HOST=sample.com
   EMAIL=sample@gmail.com
   PASSWORD=sample_password
   LOG_LEVEL=DEBUG
   ```

5. Run the application:

   ```sh
   python run.py
   ```

## Directory Structure

```
my_flask_app/
│
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── cache.py
│ ├── auth.py
│ └── utils.py
│
├── config/
│ ├── init.py
│ └── settings.py
│
├── .env
├── run.py
└── requirements.txt
```

## Usage

- `/get_data` - GET request to fetch data from the API.
- **GET /get_data/<data_id>**: Fetch data from the API by ID.

## Logging

Logs are configured based on the `LOG_LEVEL` environment variable and can be found in the console output.
