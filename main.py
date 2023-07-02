import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException

app = FastAPI()


# class SPAStaticFiles(StaticFiles):
#     async def get_response(self, path: str, scope):
#         try:
#             return await super().get_response(path, scope)
#         except HTTPException as exception:
#             if exception.status_code == 404:
#                 return await super().get_response("index.html", scope)
#             else:
#                 raise exception


# app.mount("/", SPAStaticFiles(directory="../frontend/dist", html=False), name="app")

app.mount("/", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
