from fastapi import FastAPI, HTTPException
from bson import ObjectId

from models import Post, Comment
from database import posts_collection, comments_collection

app = FastAPI(title="Blog-API")


@app.get('/')
async def home():
    return {"message": "Welcome to my world :)"}

# Create a post
@app.post("/create-post")
async def create_post(post: Post):
    post_dict = post.dict()
    result = await posts_collection.insert_one(post_dict)
    post_dict["_id"] = str(result.inserted_id)
    return {"message": "Post created successfully.", "post": post_dict}


# Get all posts.
@app.get("/get-all-posts")
async def get_all_posts():
    posts = []
    async for post in posts_collection.find():
        post["_id"] = str(post["_id"])
        posts.append(post)
    return {"posts": posts}


# Get a single post
@app.get("/get-post/{post_id}")
async def get_post(post_id: str):
    post = await posts_collection.find_one({"_id": ObjectId(post_id)})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post["_id"] = str(post["_id"])
    return {"post": post}


# Update a post.
@app.put("/update-post/{post_id}")
async def update_post(post_id: str, post: Post):
    old_post = await posts_collection.find_one({"_id": ObjectId(post_id)})
    if not old_post:
        raise HTTPException(status_code=404, detail="Post not found")

    update_data = {key: val for key, val in post.dict().items() if val}
    await posts_collection.update_one({"_id": ObjectId(post_id)}, {"$set": update_data})
    new_post = await posts_collection.find_one({"_id": ObjectId(post_id)})
    new_post["_id"] = str(new_post["_id"])

    return {"message": "Post updated successfully.", "post": new_post}


# Delete a post
@app.delete("/delete-post/{post_id}")
async def delete_post(post_id: str):
    post = await posts_collection.find_one({"_id": ObjectId(post_id)})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found to delete.")
    await posts_collection.delete_one({"_id": ObjectId(post_id)})
   
    return {"message": "Post deleted successfully."}


# Add comment to a post
@app.post("/add-comment/{post_id}")
async def add_comment(post_id: str, comment: Comment):
    post = await posts_collection.find_one({"_id": ObjectId(post_id)})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    comment_dict = comment.dict()
    comment_dict["post_id"] = post_id
    result = await comments_collection.insert_one(comment_dict)
    comment_dict["_id"] = str(result.inserted_id) 
    return {"message": "Comment added successfully", "comment": comment_dict}


# Get all comments for a post.
@app.get("/get-comments/{post_id}")
async def get_comments(post_id: str):
    comments = []
    async for comment in comments_collection.find({"post_id": post_id}):
        comment["_id"] = str(comment["_id"])
        comments.append(comment)
    return {"comments": comments}


