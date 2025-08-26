from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "TRACE", "CONNECT"])
async def funya(request: Request, path: str):
    return Response(
        content="ふにゃふにゃ\n",
        media_type="text/plain",
        headers={"Funya-Protocol": "HFTP/1.0"}
    )

