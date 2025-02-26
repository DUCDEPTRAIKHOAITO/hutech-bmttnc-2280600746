# Hàm kiểm tra số nguyên tố
def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Kiểm tra số nguyên tố với số nhập từ người dùng
number = int(input("Nhập số cần kiểm tra: "))

if kiem_tra_so_nguyen_to(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải là số nguyên tố.")
