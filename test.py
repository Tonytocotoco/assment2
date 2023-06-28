from tabulate import tabulate

def ghi_thong_tin_don_hang(file_name, ma_don_hang, thong_tin_khach_hang, thong_tin_san_pham, ten_nhan_vien, ma_nhan_vien, tinh_trang_don_hang, thoi_gian):
    # Chuẩn bị dữ liệu để trình bày
    data = [
        ["Mã đơn hàng", ma_don_hang],
        ["Mã khách hàng", thong_tin_khach_hang["ma_khach_hang"]],
        ["Tên khách hàng", thong_tin_khach_hang["ten_khach_hang"]],
        ["Số điện thoại", thong_tin_khach_hang["so_dien_thoai"]],
        ["Mã sản phẩm", thong_tin_san_pham["ma_san_pham"]],
        ["Tên sản phẩm", thong_tin_san_pham["ten_san_pham"]],
        ["Số lượng", thong_tin_san_pham["so_luong"]],
        ["Đơn giá", thong_tin_san_pham["don_gia"]],
        ["Tổng tiền", thong_tin_san_pham["tong_tien"]],
        ["Tên nhân viên bán hàng", ten_nhan_vien],
        ["Mã nhân viên bán hàng", ma_nhan_vien],
        ["Tình trạng đơn hàng", tinh_trang_don_hang],
        ["Thời gian thực hiện", thoi_gian]
    ]

    # Ghi thông tin đơn hàng vào file
    with open(file_name, "w") as file:
        file.write(tabulate(data, tablefmt="plain"))

# Thông tin đơn hàng
ma_don_hang = "DH001"
thong_tin_khach_hang = {
    "ma_khach_hang": "KH001",
    "ten_khach_hang": "Nguyen Van A",
    "so_dien_thoai": "0123456789"
}
thong_tin_san_pham = {
    "ma_san_pham": "SP001",
    "ten_san_pham": "Áo thun",
    "so_luong": 2,
    "don_gia": 100000,
    "tong_tien": 200000
}
ten_nhan_vien = "Nguyen Thi B"
ma_nhan_vien = "NV001"
tinh_trang_don_hang = "Đã giao"
thoi_gian = "2023-06-19 10:30:00"

# Ghi thông tin đơn hàng vào file
file_name = "thong_tin_don_hang.txt"
ghi_thong_tin_don_hang(file_name, ma_don_hang, thong_tin_khach_hang, thong_tin_san_pham, ten_nhan_vien, ma_nhan_vien, tinh_trang_don_hang, thoi_gian)
