
from pymongo.mongo_client import MongoClient

#kết nối database
_databaseName = "Admissions"
def Connection_db():
    uri = "mongodb+srv://admin_course:i7QX0kykBi7XmFeF@cluster0.n6x8tmr.mongodb.net/Admissions"
        # Create a new client and connect to the server
    client = MongoClient(uri)

        # Chọn cơ sở dữ liệu và bảng

    return client
    
def is_username_exists(client,username,password):
    try:
      
        # uri = "mongodb+srv://admin_course:i7QX0kykBi7XmFeF@cluster0.n6x8tmr.mongodb.net/Admissions"
        # # Create a new client and connect to the server
        # client = MongoClient(uri)

        # # Select the database and collection
        # db = client["mydatabase"]  # Replace "mydatabase" with your database name
        db = client[_databaseName]
        collection = db["user"]  # Replace "user" with your collection name
        
        # Query to find a user with the given username
        query = {"username": username}
        user = collection.find_one(query)
        # Check if the user exists
        if user and user['password'] ==password:
            return True
        else:
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    finally:
        # Close the MongoDB connection
        client.close()
        
#Thêm users
def insert_user(client,username, password):
    try:
        # Kết nối tới MongoDB (cập nhật chuỗi kết nối với thông tin máy chủ MongoDB của bạn)
       
        # Chọn cơ sở dữ liệu và bảng
        db = client[_databaseName]  # Thay "mydatabase" bằng tên cơ sở dữ liệu của bạn
        collection = db["user"]  # Thay "user" bằng tên bảng của bạn

        # Dữ liệu người dùng
        user_data = {
            "username": username,
            "password": password
        }

        # Chèn dữ liệu người dùng vào bảng
        result = collection.insert_one(user_data)

        print(f"Đã chèn người dùng mới với ID: {result.inserted_id}")

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

    finally:
        # Đóng kết nối MongoDB
        client.close()
#Thêm vào danh sách tuyển sinh
def insert_admission(client,userName,hoTen,heDaoTao,nganhHoc):
    try:
        # Kết nối tới MongoDB (cập nhật chuỗi kết nối với thông tin máy chủ MongoDB của bạn)
       
        # Chọn cơ sở dữ liệu và bảng
        db = client[_databaseName]  # Thay "mydatabase" bằng tên cơ sở dữ liệu của bạn
        collection = db["AdmissionsList"]  # Thay "user" bằng tên bảng của bạn

        # Dữ liệu người dùng
        dataForm = {
            "username": userName,
            "hoTen": hoTen,
            "heDaoTao":heDaoTao,
            "nganhHoc":nganhHoc
        }

        # Chèn dữ liệu người dùng vào bảng
        result = collection.insert_one(dataForm)

        return result.inserted_id

    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

    finally:
        # Đóng kết nối MongoDB
        client.close()
    
    
def get_all_adList(client,table_name):
    try:
        # Kết nối tới MongoDB (cập nhật chuỗi kết nối với thông tin máy chủ MongoDB của bạn)


        # Chọn cơ sở dữ liệu và bảng
        db = client[_databaseName]  # Thay "mydatabase" bằng tên cơ sở dữ liệu của bạn
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


        
if __name__ =='__main__':
   client=Connection_db()
   print(get_all_adList(client,'AdmissionsList'))
#    print( insert_user(client,'admin','123'))
#    print(is_username_exists(client,'admin','123'))
#    print( insert_admission(client,'admin','Nguyễn Văn Test','9+','CNTT'))

   