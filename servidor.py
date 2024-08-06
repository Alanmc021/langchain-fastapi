#!/usr/bin/env python
from fastapi import FastAPI  
from langserve import add_routes
from peticaoInicial import chain  

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

add_routes(
    app,
    chain,
    path="/peticao-inicial",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)