# Project Setup Guide

Follow these steps to set up and run the application.

## Backend Setup

1. Navigate to the backend directory:
   ```sh
   cd backend
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Create a `.env` file in the backend directory and add the following:
   ```sh
   SECRET_KEY=your_secret_key_here
   ```
6. Set up Redis in Docker:
   ```sh
   docker run -d --name redis-container -p 6379:6379 redis
   ```

## Frontend Setup

1. Navigate to the frontend directory:
   ```sh
   cd ../frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```

## Running the Application

1. Start the backend:
   ```sh
   cd backend
   python manage.py runserver
   ```
2. Start the frontend:
   ```sh
   cd ../frontend
   npm run dev
   ```

## Using the Application

1. Register as a new user.
2. Sign in with your credentials.
3. Start chatting with other users.

Enjoy your application!
