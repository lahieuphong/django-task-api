# Django Task API

Dự án học Django Backend + Django REST Framework, có frontend đơn giản để thao tác với API quản lý task.

## Tính năng

- CRUD task: thêm, xem, sửa, xoá, đánh dấu hoàn thành.
- CRUD project và tag.
- Minh hoạ quan hệ database:
  - `1-1`: `Task` có một `TaskDetail`.
  - `1-nhiều`: `Project` có nhiều `Task`.
  - `nhiều-nhiều`: `Task` có nhiều `Tag`, một `Tag` dùng cho nhiều `Task`.

## Yêu cầu

- Python 3.12 trở lên
- Git

Kiểm tra Python:

```powershell
python --version
```

## Cách chạy sau khi clone kèm dữ liệu

```powershell
git clone https://github.com/lahieuphong/django-task-api.git
cd django-task-api

python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

# Kiểm tra file dữ liệu đã được clone về
Test-Path .\db.sqlite3

# Cập nhật cấu trúc database nếu code có migration mới
python manage.py migrate

python manage.py runserver
```

Nếu lệnh `Test-Path .\db.sqlite3` trả về `True` thì dữ liệu trong `db.sqlite3` đã có sẵn trên máy mới. Dự án này đã commit file `db.sqlite3`, nên sau khi `git clone` sẽ không cần import dữ liệu bằng `loaddata`.

Không xoá file `db.sqlite3` trước khi chạy server, vì đây là nơi đang lưu dữ liệu SQLite của project. Nếu lỡ xoá hoặc muốn lấy lại bản database đang có trên GitHub, chạy:

```powershell
git restore --source=origin/main -- db.sqlite3
```

Tài khoản admin/superuser cũng đã được lưu trong `db.sqlite3`, nên khi clone sang máy mới có thể đăng nhập lại bằng tài khoản hiện có:

```txt
Username: admin
Password: 123456
```

Trang admin:

```txt
http://127.0.0.1:8000/admin/
```

Không cần chạy lại `createsuperuser` nếu file `db.sqlite3` vẫn còn nguyên. Chỉ cần tạo thêm tài khoản admin mới nếu xoá mất database, database không được clone về, hoặc muốn có thêm tài khoản khác:

```powershell
python manage.py createsuperuser
```

Nếu PowerShell không cho activate môi trường ảo, chạy:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Sau đó chạy lại:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Đường dẫn sử dụng

Frontend:

```txt
http://127.0.0.1:8000/
```

Admin:

```txt
http://127.0.0.1:8000/admin/
```

API:

```txt
http://127.0.0.1:8000/api/tasks/
http://127.0.0.1:8000/api/projects/
http://127.0.0.1:8000/api/tags/
```

## Cách thử nhanh

1. Vào `http://127.0.0.1:8000/`.
2. Tạo một project.
3. Tạo vài tag.
4. Tạo task và chọn project, tag, priority, deadline.
5. Bấm `Sửa`, `Xong`, `Xoá` để thử các thao tác CRUD.

## Luồng hoạt động

```txt
Frontend
-> gọi API bằng fetch()
-> Django URL
-> ViewSet
-> Serializer
-> Model
-> SQLite database
```

Ví dụ khi tạo task:

```txt
POST /api/tasks/
-> tạo Task
-> tạo/cập nhật TaskDetail
-> gắn Project
-> gắn nhiều Tag
-> lưu vào db.sqlite3
```

## File quan trọng

```txt
config/urls.py                  route chính của project
tasks/models.py                 định nghĩa database và quan hệ
tasks/serializers.py            chuyển dữ liệu model <-> JSON
tasks/views.py                  API CRUD bằng ViewSet
tasks/urls.py                   route API
tasks/templates/tasks/index.html frontend gọi API
```

## Lệnh hay dùng

```powershell
python manage.py runserver        # chạy server
python manage.py makemigrations   # tạo migration sau khi sửa model
python manage.py migrate          # cập nhật database
python manage.py createsuperuser  # tạo tài khoản admin
python manage.py check            # kiểm tra cấu hình Django
```

## Lỗi thường gặp

Thiếu Django:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Chưa migrate database:

```powershell
python manage.py migrate
```

Port `8000` bị chiếm:

```powershell
python manage.py runserver 8001
```
