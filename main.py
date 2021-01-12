from app import create_app

service = create_app()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:service', host="127.0.0.1", port=8010, reload=True, debug=True)
