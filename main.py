danh_ba = [
    {"ten": "Nguyễn Văn An", "sdt": "0912345678", "email": "an@gmail.com", "nhom": "Gia đình"},
    {"ten": "Trần Thị Bình", "sdt": "0987654321", "email": "binh@gmail.com", "nhom": "Bạn bè"},
    {"ten": "Lê Minh Châu",  "sdt": "0909090909", "email": "chau@gmail.com", "nhom": "Công việc"},
    {"ten": "Phạm Thị Dung", "sdt": "0911111111", "email": "dung@gmail.com", "nhom": "Bạn bè"},
    {"ten": "Hoàng Văn Em",  "sdt": "0922222222", "email": "em@gmail.com",   "nhom": "Gia đình"},
]

while True:
    print()
    print("""Hãy lựa chọn phương án của bạn
    1. Xem toàn bộ danh bạ
    2. Thêm liên hệ
    3. Tìm kiếm theo tên
    4. Xóa liên hệ
    5. Sửa số điện thoại
    6. Thống kê
    7. Thoát
   """, end = " ")
    nhap = int(input("Nhập lựa chọn của bạn: "))

    if nhap == 7:
        print("Tạm biệt!")
        break

    if nhap == 1:
        for nguoi in danh_ba:
            print(f"Tên: {nguoi['ten']} | SĐT: {nguoi['sdt']} | Email: {nguoi['email']} | Nhóm: {nguoi['nhom']}")

    elif nhap == 2:
        ten = input("Mời nhập tên: ")
        sdt = input("Mời nhập sđt: ")
        email = input("Mời nhập email: ")
        nhom = input("Mời nhập tên nhóm: ")

        lien_he_moi = {
            "ten": ten,
            "sdt": sdt,
            "email": email,
            "nhom": nhom
        }
        danh_ba.append(lien_he_moi)
        print("Đã thêm ✅")

    elif nhap == 3:
        tu_khoa = input("Nhập tên muốn tìm: ").lower()
        tim_thay = False
        for nguoi in danh_ba:
            if tu_khoa in nguoi["ten"].lower():
                print(f"Tên: {nguoi['ten']} | SĐT: {nguoi['sdt']} | Email: {nguoi['email']} | Nhóm: {nguoi['nhom']}")
                tim_thay = True
        if not tim_thay:
            print("Tên chưa có trong danh bạ")

    elif nhap == 4:
        xoa = input("Nhập tên liên hệ bạn muốn xóa: ").lower()
        tim_thay = False
        for nguoi in danh_ba.copy():
            if nguoi["ten"].lower() == xoa:
                danh_ba.remove(nguoi)
                tim_thay = True
        if tim_thay:
            print("Đã xóa ✅")
        else:
            print("Không tìm thấy tên cần xóa")

    elif nhap == 5:
        sua = input("Nhập tên bạn muốn sửa: ").lower()
        sdt_moi = input("Nhập số điện thoại mới: ")
        tim_thay = False
        for nguoi in danh_ba:
            if nguoi["ten"].lower() == sua:
                nguoi["sdt"] = sdt_moi
                tim_thay = True
        if tim_thay:
            print("Đã sửa ✅")
        else:
            print("Không tìm thấy tên cần sửa")

    elif nhap == 6:
        print(f"Tổng số liên hệ là {len(danh_ba)}")

        dem_nhom = {}
        for nguoi in danh_ba:
            nhom = nguoi["nhom"]
            if nhom in dem_nhom:
                dem_nhom[nhom] +=1
            else:
                dem_nhom[nhom] = 1
        print("Thống kê theo nhóm:")
        for nhom, so_luong in dem_nhom.items():
            print(f" {nhom}: {so_luong} liên hệ")
    else:
        print("Lựa chọn không hợp lệ! Vui lòng nhập 1-7")






