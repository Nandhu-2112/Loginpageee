# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# import mysql.connector
# from fastapi.middleware.cors import CORSMiddleware
#
#
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# class Registeruser(BaseModel):
#     # id: str
#     name: str
#     phno: str
#     email: str
#     password: str
# @app.post("/register")
# def regi(i:Registeruser):
#
#
#
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="office",
#         port="3309"
#     )
#     mypost=mydb.cursor()
#     mypost.execute("insert into logindb (name,phno,email,password)values ('"+i.name+"','"+i.phno+"','"+i.email+"','"+i.password+"')")
#     # result = mypost.fetchall()
#
#     mydb.commit()
#     mydb.close()
#     return {"message":"register successfully"}
#
#
# class Loginuser(BaseModel):
#     email: str
#     password: str
#
# @app.post("/login")
# def login(i:Loginuser):
#
#
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="office",
#         port="3309"
#     )
#     mypost = mydb.cursor()
#     mypost.execute("select * from logindb where email='"+i.email+"' and password='"+i.password+"'")
#     # result = mypost.fetchall()
#
#     mydb.commit()
#
#     if result:
#         return {"message": "Login successful"}
#     else:
#         return {"message": "Invalid email or password"}
#
#
#
#
# @app.get("/table")
# def view():
#
#
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="office",
#         port="3309"
#     )
#     mypost = mydb.cursor()
#     mypost.execute("select * from user")
#     result = mypost.fetchall()
#     mydb.commit()
#     return result



from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RegisterItem(BaseModel):
    name: str
    phno: str
    email: str
    password: str

@app.post("/register")
def register(i: RegisterItem):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="office",
        port=3309
    )
    mypost = mydb.cursor()
    mypost.execute("insert into  usersdb (name, phno, email, password) values ('"
        + i.name + "', '" + i.phno + "', '" + i.email + "', '" + i.password + "')"
    )
    mydb.commit()
    mydb.close()
    return {"message": "registered successfully"}


class LoginItem(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(i: LoginItem):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="office",
        port=3309
    )
    mypost = mydb.cursor()
    mypost.execute(
        "select * from usersdb where email='" + i.email + "' AND password='" + i.password + "'"
    )
    result = mypost.fetchone()
    mydb.close()
    if result:
        return {"message": "Successfully"}
    else:
        return {"message": "not-Invalid"}


@app.get("/table")
def view():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="office",
        port=3309
    )
    mypost= mydb.cursor(dictionary=True)
    mypost.execute("SELECT * FROM usersdb")
    result =  mypost.fetchall()
    mydb.close()
    return result

class UpdateItem(BaseModel):
    name: str

@app.put("/update/{user_id}")
def update(i: UpdateItem, user_id: int):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="office",
        port=3309
    )
    mypost = mydb.cursor()
    mypost.execute("update usersdb set name='" + i.name + "' where id=" + str(user_id))
    mydb.commit()
    mydb.close()
    return {"message": "Updated"}
#
@app.delete("/del/{user_id}")
def delete(user_id: int):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="office",
        port=3309
    )
    mypost = mydb.cursor()
    mypost.execute("delete from usersdb where id=" + str(user_id))
    mydb.commit()
    mydb.close()
    return {"message": "Deleted"}