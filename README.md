# Safe&Recycle Backend - AIML (FastAPI)

Backend & AIML service untuk aplikasi **Safe&Recycle** yang dibangun menggunakan **FastAPI**.  
Project ini menyediakan REST API untuk autentikasi, manajemen user, dan fitur backend lainnya beserta AIML inference.

---

## 🚀 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **SQLModel / SQLAlchemy**
- **PostgreSQL / MySQL** (sesuai konfigurasi)
- **JWT Authentication**
- **Uvicorn**

---

## 📁 Struktur Project (Ringkas)
```
backend/
├── app/
│   ├── routers/      # Untuk routing
│   ├── models/       # Untuk struktur table database
|   ├── schemas/      # Untuk request & response format
│   ├── services/     # Untuk Logika dan akses data
│   ├── databases/    # Untuk membuat koneksi dengan database
│   ├── core/         # Untuk fungsi-fungsi umum.
│   └── main.py
├── .env
├── requirements.txt
└── README.md
```
---

## ⚙️ Persiapan Environment

### 1️⃣ Clone repository
```bash
git clone <repository-url>
cd backend
````

---

### 2️⃣ Buat virtual environment

```bash
python -m venv venv
```

Aktifkan virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / MacOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🗄️ Setup Database

Jika project menggunakan auto-create table:

```bash
python -m app.main
```

Atau jika menggunakan migration (Alembic), jalankan sesuai konfigurasi project.

---

## ▶️ Menjalankan Server

Jalankan aplikasi FastAPI dengan **Uvicorn**:

```bash
uvicorn app.main:app --reload
```

Server akan berjalan di:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI menyediakan dokumentasi otomatis:

* **Swagger UI**
  👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

* **ReDoc**
  👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔑 Autentikasi

Project ini menggunakan **JWT Authentication**:

* **Access Token** untuk akses API
* **Refresh Token** untuk memperbarui access token
* Token yang logout akan masuk ke **token blacklist**

Pastikan menambahkan header berikut saat mengakses endpoint terproteksi:

```
Authorization: Bearer <access_token>
```

---

## 🧪 Testing (Opsional)

Gunakan:

* **Postman**
* **Insomnia**
* atau Swagger UI

Pastikan environment variable dan token sudah dikonfigurasi dengan benar.

---

## 🛠️ Development Notes

* Semua timestamp menggunakan **UTC**
* Refresh token dan access token memiliki mekanisme revoke
* Struktur kode dipisahkan berdasarkan **router, service, dan model**

---

## 📌 Catatan

Jika terjadi error terkait database, pastikan:

* Database sudah berjalan
* Kredensial `.env` benar
* Port database sesuai

---
