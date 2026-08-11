from fastapi import FastAPI

app = FastAPI 

@app.get("/posts/{post_id}"):
def get_post(post_id: int):
    return( " Retreived {post_id} " )

@app.get("/posts"):
def get_post(limit: int =10):
    # The DB Code Here ( This Will Do Query )
    return ( "Retreived {limit}" )

