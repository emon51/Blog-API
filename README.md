# Blog-API

A simple blog API built with FastAPI and MongoDB. Users can create, read, update, delete posts and add comments. No authentication is implemented.

## Features
- Create, update, delete posts
- Add comments to posts
- View all posts or a single post
- View all comments for a post

## Setup

1. **Clone the project**
```
git clone https://github.com/your-username/Blog-API.git
```
```
cd Blog-API
```

2. Create & activate virtual environment
```
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```
3. Install dependencies
```
pip install -r requirements.txt
```

4. Create a `.env` file in the root folder with your database info:
   - MONGO_URI = "your_mongodb_uri_here"
   - DATABASE_NAME = "blog_db"
  
5. Run the FastAPI server
   ```
   uvicorn main:app --reload
   ```
6. Open `http://127.0.0.1:8000/docs` in your browser to see API docs.


