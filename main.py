import uvicorn
from routers.main import router


if __name__ == "__main__":
    uvicorn.run(router, host='127.0.0.1', port=4557)