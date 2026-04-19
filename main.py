from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import replicate
import os

app = FastAPI()

# Blogger থেকে কানেক্ট করার পারমিশন
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# আপনার Replicate টোকেন (নিচে Render এ সেট করা শিখিয়ে দেব)
os.environ["REPLICATE_API_TOKEN"] = "আপনার_টোকেন_এখানে"

@app.get("/")
def home():
    return {"status": "AI Video Server is Running"}

@app.post("/generate-video/")
async def generate_video(prompt: str):
    output = replicate.run(
        "anotherjesse/zeroscope-v2-xl:9f7434164220de0bc401242d0f85a201c107e0568c4d7ec666a7b375d6542790",
        input={"prompt": prompt}
    )
    return {"video_url": output[0]}
