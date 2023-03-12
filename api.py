import os
import random
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# Configure CORS
origins = ["http://localhost", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


IMAGE_FOLDER = "images/"

@app.get("/random_image")
async def get_random_image():
    # Get a list of all the files in the image folder
    files = os.listdir(IMAGE_FOLDER)

    # Randomly select one of the files
    filename = random.choice(files)

    # Return the selected file as a response
    return FileResponse(os.path.join(IMAGE_FOLDER, filename), media_type="image/jpg")



# Same with video

@app.get("/video")
async def get_random_video():
    videos_dir = "videos/"
    video_files = [f for f in os.listdir(videos_dir) if f.endswith(".mp4")]
    random_video = random.choice(video_files)
    return FileResponse(os.path.join(videos_dir, random_video), media_type="video/mp4")
