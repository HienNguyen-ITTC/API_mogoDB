from fastapi import FastAPI, HTTPException, Query,File
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient

app = FastAPI()
# Chuỗi kết nối MongoDB
uri = "mongodb+srv://admin_course:i7QX0kykBi7XmFeF@cluster0.n6x8tmr.mongodb.net/Admissions"
# Tên cơ sở dữ liệu MongoDB
database_name = "Admissions"

# Hàm để thực hiện chèn dữ liệu vào MongoDB
def insert_admission_data(username, hoTen, heDaoTao, nganhHoc):
    try:
        # Kết nối tới MongoDB
        client = MongoClient(mongo_uri)

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
def get_all_adList(table_name):
    try:
        # Kết nối tới MongoDB (cập nhật chuỗi kết nối với thông tin máy chủ MongoDB của bạn)


        # Chọn cơ sở dữ liệu và bảng
        client = MongoClient(mongo_uri) # Thay "mydatabase" bằng tên cơ sở dữ liệu của bạn
        db = client[database_name]
        collection = db[table_name]  # Thay "user" bằng tên bảng của bạn

        # Tìm tất cả các người dùng
        all_users = list(collection.find())
        # In danh sách người dùng
        return all_users

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

    finally:
        # Đóng kết nối MongoDB
        client.close()   


# Định nghĩa endpoint cho API
@app.post("/insert_admission/")
def insert_admission(username: str, hoTen: str, heDaoTao: str, nganhHoc: str):
    inserted_id = insert_admission_data(username, hoTen, heDaoTao, nganhHoc)
    return {"message": "Dữ liệu đã được thêm thành công", "inserted_id": str(inserted_id)}


@app.get("/get_ListAdmission/")
def get_all_adList():
    listAd = get_all_adList('AdmissionsList')
    return {"data": str( listAd)}

