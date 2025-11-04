# React + Flask Web App

A simple task management web application with a React frontend and Flask backend.

## Project Structure

```
.
├── backend/           # Flask API
│   ├── app.py        # Main Flask application
│   └── requirements.txt
└── frontend/         # React application
    ├── src/
    │   ├── App.jsx   # Main React component
    │   ├── App.css
    │   ├── main.jsx
    │   └── index.css
    ├── index.html
    ├── package.json
    └── vite.config.js
```

## Features

- Create, read, update, and delete tasks
- Mark tasks as complete/incomplete
- Modern React UI with Vite
- RESTful Flask API
- CORS enabled for cross-origin requests

## Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the Flask server:
   ```bash
   python app.py
   ```

The backend will be available at `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:3000`

## API Endpoints

- `GET /api/health` - Check backend health status
- `GET /api/tasks` - Get all tasks
- `POST /api/tasks` - Create a new task
- `PUT /api/tasks/<id>` - Update a task
- `DELETE /api/tasks/<id>` - Delete a task

## Development

### Backend Development

The Flask app uses Flask-CORS to allow requests from the React frontend. The API endpoints are prefixed with `/api/`.

### Frontend Development

The React app uses Vite for fast development. The proxy configuration in `vite.config.js` forwards API requests to the Flask backend.

## Building for Production

### Frontend Build

```bash
cd frontend
npm run build
```

The production build will be in the `frontend/dist` directory.

## License

See LICENSE file for details.
