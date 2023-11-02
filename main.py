from fastapi import FastAPI, HTTPException, Query,File
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Chuỗi kết nối MongoDB
uri = "mongodb+srv://admin_course:i7QX0kykBi7XmFeF@cluster0.n6x8tmr.mongodb.net/Admissions"
# Tên cơ sở dữ liệu MongoDB
database_name = "Admissions"

# Hàm để thực hiện chèn dữ liệu vào MongoDB
def insert_admission_data(username, hoTen, heDaoTao, nganhHoc):
    try:
        # Kết nối tới MongoDB
        client = MongoClient(uri)

        # Chọn cơ sở dữ liệu và bảng
        db = client[database_name]
        collection = db["AdmissionsList"]

        # Dữ liệu người dùng
        dataForm = {
            "username": username,
            "hoTen": hoTen,
            "heDaoTao": heDaoTao,
            "nganhHoc": nganhHoc
        }

        # Chèn dữ liệu người dùng vào bảng
        result = collection.insert_one(dataForm)

        # Trả về ID của bản ghi vừa chèn
        return result.inserted_id

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        raise HTTPException(status_code=500, detail="Lỗi trong quá trình chèn dữ liệu")

    finally:
        # Đóng kết nối MongoDB
        client.close()
#Lấy danh sách
def get_all_admission_data(username):
    try:
        # Kết nối tới MongoDB
        client = MongoClient(uri)

        # Chọn cơ sở dữ liệu và bảng
        db = client[database_name]
        collection = db['AdmissionsList']

        projection = {"_id": 0}
        # Tìm tất cả dữ liệu trong bảng
        all_data = list(collection.find({},projection))
        json_data = json.dumps(all_data)
        return json_data

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
        raise HTTPException(status_code=500, detail="Lỗi trong quá trình lấy dữ liệu")

    finally:
        # Đóng kết nối MongoDB
        client.close()


# Định nghĩa endpoint cho API
@app.post("/insert_admission/")
def insert_admission(username: str, hoTen: str, heDaoTao: str, nganhHoc: str):
    inserted_id = insert_admission_data(username, hoTen, heDaoTao, nganhHoc)
    return {"message": "Dữ liệu đã được thêm thành công", "inserted_id": str(inserted_id)}


@app.get("/get_ListAdmission2/")
def get_all_adList1():
    admission_data = get_all_admission_data('admin')
    return {str( admission_data)}
@app.get("/detect_text")
async def detect_text(imageUrl:str ):
   api_url = "http://45.119.82.190:8000/detect_text"
   params = {
        "image_url": imageUrl
    }
   response = requests.get(api_url, params=params)
   if response.status_code == 200:
    # If the response status code is 200 (OK), you can access the API response data
        data = response.json()
        return {"data":data}
   else:
    # Handle error responses, such as 4xx or 5xx status codes
    return {"result":"failed"}
