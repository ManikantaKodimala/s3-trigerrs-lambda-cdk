import uvicorn

if __name__ == '__main__':
    from fastapitutorial import testapi

    uvicorn.run(testapi.app, host="127.0.0.1", port=8080)
