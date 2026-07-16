from fastapi import FastAPI,Request,Body, Form,UploadFile,File 
from fastapi.staticfiles import StaticFiles
import os 
from pydantic import BaseModel 

app = FastAPI() 
app.mount("/static",StaticFiles(directory="static"),name="static")


# Dummy database
employees = {
    1: {
        "name": "Ranjit Singh",
        "role": "AI Engineer",
        "salary": 80000
    },

    2: {
        "name": "Aman Sharma",
        "role": "Backend Developer",
        "salary": 60000
    },

    3: {
        "name": "Neha Verma",
        "role": "Data Scientist",
        "salary": 90000
    }
}


@app.get("/") 
async def main_page():
    return {"Name":"Ranji Singh",
            "Designation":"Ai Engineer"}






# ------------------------   SEND DATA IN JSON    ------------------
class UserData(BaseModel):
    username: str
    email: str
    contact: int

@app.post("/sendtoserver")
async def main_page(data: UserData):  # send data in json format from postman
    """
    http://127.0.0.1:8000/sendtoserver

    Payload: JSON
    {
            "username": "Radhey",
            "email": "smart@gmail.com",
            "contact": 9759194985
        }
    """


    recieved_data = {
        "username": data.username,
        "email": data.email,
        "contact": data.contact
    }
    print(recieved_data)
    return recieved_data

# ------------------------------------------------------




# ---------------  GET API  ----------------------


@app.get("/employee_id/{emp_id}")
async def employee_id(emp_id:int,show_salary:bool=False):
    """
    http://127.0.0.1:8000/employee_id/1
    http://127.0.0.1:8000/employee_id/1?show_salary=true
    """

    if emp_id not in employees:
        return {"status":"failed",
                "message":"employee record is not found"}

    employee_data = employees[emp_id]
    if not show_salary:
        return {"name":employee_data["name"],
                "role":employee_data["role"]} 
    else:
        return {"name":employee_data["name"],
                "role":employee_data["role"],
                "salary":employee_data["salary"]}
# ------------------------------------------------




# ------------------- RECIVE VALUE BY FORM   --------------------

@app.post("/testbodyinput")
async def login_user(
    username: str = Form(...),
    password: str = Form(...)
):
    """
    http://127.0.0.1:8000/testbodyinput

    Payload:
    key             value 
    username ===>   Radha
    password ===>   kanha
    """

    return {
        "username": username,
        "password": password
    }

# --------------------------------------------------------------





# --------------------------------- UPLOAD FILE ----------------------------
UPLOAD_FOLDER = "uploaded_folder"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):

    """
    Upload any file:
    - image
    - pdf
    - csv
    - txt
    - video
    - docx


    http://127.0.0.1:8000/uploadfile

    PayLoad:
    key =============== Type  ===================== AnyFile 
    file                 file                        .pdf,.jpeg,jpg

    
    """

    # File path
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)  # here file is key of file in form data 

    # Read uploaded file
    content = await file.read()

    # Save file
    with open(file_path, "wb") as f:
        f.write(content)

    return {
        "status": "success",
        "filename": file.filename,
        "content_type": file.content_type,
        "saved_path": file_path
    }

# --------------------------------------------------------------------------------------------------------------