from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Hello Haifa! Your Python app is running on EKS via GitOps", "Status": "Success"}
