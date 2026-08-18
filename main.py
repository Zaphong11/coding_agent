import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

# main.py
from graph import app

result = app.invoke({
    "request": "Xây dựng chức năng đăng nhập user với JWT"
})

print("\n=== BACKEND RESULT ===")
print(result["backend_result"])

print("\n=== FRONTEND RESULT ===")
print(result["frontend_result"])

print("\n=== TEST RESULT ===")
print(result["test_result"])
