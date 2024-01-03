# import streamlit as st
# import pandas as pd
# from datetime import datetime



# def save_to_csv(df):
#     # Chọn vị trí lưu file CSV
#     file_path = st.file_uploader("Chọn nơi lưu file CSV", type=["csv"])

#     # Lưu DataFrame vào file CSV nếu người dùng đã chọn vị trí lưu
#     if file_path:
#         df.to_csv(file_path, index=False)
#         st.success("DataFrame đã được lưu vào file CSV thành công!")

# def view_dataframe(df, state, title):
#     # Tạo một nút để xem hoặc ẩn DataFrame
#     if st.button(title):
#         state.show_df = not state.show_df

#     # Hiển thị DataFrame nếu biến trạng thái là True
#     if state.show_df:
#         st.dataframe(df)

# # def view_dataframe(df, state, df_name, title):
# #     # Tạo một nút để xem hoặc ẩn DataFrame
# #     if st.button(f"Xem/Ẩn {df_name} DataFrame"):
# #         state[df_name] = not state[df_name]

# #     # Hiển thị DataFrame nếu biến trạng thái là True
# #     if state[df_name]:
# #         st.dataframe(df)


# def ThongKe(filePath, lopHocPhan,maLopHocPhan, giangVien):
#     # Đọc dữ liệu từ file CSV
#     print("hello")
#     file_path = filePath
#     data = pd.read_csv(file_path)

#     # Thông tin về lớp học phần
#     lop_hoc_phan = lopHocPhan
#     ma_lop_hoc_phan = maLopHocPhan
#     giang_vien = giangVien

#     # Layout của ứng dụng
#     header_col, info_col = st.columns([1, 2])

#     # Hiển thị nút "Home"
#     # home_button = st.button("Home")

#     # Xử lý sự kiện khi nút "Home" được nhấn
#     # if home_button:
#     #     display_home()
#     # else:
#     # Hiển thị tiêu đề
#     with header_col:
#         st.title("Thông Tin Lớp Học Phần")

#     # Hiển thị thông tin
#     with info_col:
#         st.subheader("Tên Lớp Học Phần:")
#         st.write(lop_hoc_phan)

#         st.subheader("Mã Lớp Học Phần:")
#         st.write(ma_lop_hoc_phan)

#         st.subheader("Giảng Viên:")
#         st.write(giang_vien)
    


#     # Hiển thị dữ liệu bảng
#     if 'show_df' not in st.session_state:
#         st.session_state.show_df = False
#     view_dataframe(data.iloc[:, :7], st.session_state, "Danh sách sinh viên của lớp học phần")
#     # view_dataframe(data, show_df,"Danh sách sinh viên của lớp học phần" )


#     # Chuyển đổi cột 'Ngày sinh' sang định dạng datetime
#     data['Ngày sinh'] = pd.to_datetime(data['Ngày sinh'], format='%d/%m/%Y')

#     # Thống kê số lượng sinh viên nghỉ và đi học trong ngày
#     ngay_hien_tai = datetime.now().date()
    


#     sinh_vien_nghi_hoc = data[data['Ngày sinh'].dt.date == ngay_hien_tai]
#     sinh_vien_di_hoc = data[data['Ngày sinh'].dt.date != ngay_hien_tai]

#     # Hiển thị thống kê
#     st.subheader(f"Thống Kê Sinh Viên Ngày {ngay_hien_tai.strftime('%d/%m/%Y')}")
#     st.write(f"Số lượng sinh viên nghỉ học: {len(sinh_vien_nghi_hoc)}")
#     st.write(f"Số lượng sinh viên đi học: {len(sinh_vien_di_hoc)}")

#     if str(ngay_hien_tai) != data.iloc[0, -1]:
#         data[ngay_hien_tai] = 999
#         data.to_csv('data.csv', index=False)
#     st.dataframe(data)

    


#     # Hiển thị danh sách sinh viên nghỉ học
#     if st.button("Danh Sách Sinh Viên Nghỉ Học"):
#         st.dataframe(sinh_vien_nghi_hoc)
#     # if 'show_df1' not in st.session_state:
#     #     st.session_state.show_df1 = False
#     # view_dataframe(sinh_vien_nghi_hoc, st.session_state, "Danh Sách Sinh Viên Nghỉ Học")


#     # Hiển thị danh sách sinh viên đi học
#     if st.button("Danh Sách Sinh Viên Đi Học"):
#         st.dataframe(sinh_vien_di_hoc)

# # def display_home():
# #     st.title("Trang Chính")
# #     # Hiển thị nội dung trang chính nếu cần

# # Gọi hàm main khi chạy ứng dụng
# file_path = r'D:\WorkSpace\KhaiPhaDuLieu\classifier\face_recognition\app\danhsachsinhvien\danhsachsinhvien.csv'
# lop_hoc_phan = "Khai phá dữ liệu - Nhóm 1"
# ma_lop_hoc_phan = "2023-2024.1.TIN4103.001"
# giang_vien = "Nguyễn Ngọc Thủy (1990)"
# def app():
#     ThongKe(file_path, lop_hoc_phan, ma_lop_hoc_phan, giang_vien)



import streamlit as st
import pandas as pd
from datetime import datetime
import time


def onclick_btn1():
    print('btn1')
def onclick_btn2():
    print('btn2')



def view_dataframe(df, state, title):
    # Tạo một nút để xem hoặc ẩn DataFrame
    if st.button(title):
        state.show_df = not state.show_df

    # Hiển thị DataFrame nếu biến trạng thái là True
    if state.show_df:
        st.dataframe(df)

# def view_dataframe(df, state, df_name, title):
#     # Tạo một nút để xem hoặc ẩn DataFrame
#     if st.button(f"Xem/Ẩn {df_name} DataFrame"):
#         state[df_name] = not state[df_name]

#     # Hiển thị DataFrame nếu biến trạng thái là True
#     if state[df_name]:
#         st.dataframe(df)


def ThongKe(filePath, lopHocPhan,maLopHocPhan, giangVien):
    # Đọc dữ liệu từ file CSV
    file_path = filePath
    file_path = "data.csv"
    data = pd.read_csv(file_path)

    # Thông tin về lớp học phần
    lop_hoc_phan = lopHocPhan
    ma_lop_hoc_phan = maLopHocPhan
    giang_vien = giangVien

    # Layout của ứng dụng
    header_col, info_col = st.columns([1, 2])

    # Hiển thị nút "Home"
    home_button = st.button("Home")

    # Xử lý sự kiện khi nút "Home" được nhấn
    # if home_button:
    #     display_home()
    
    # Hiển thị tiêu đề
    with header_col:
        st.title("Thông Tin Lớp Học Phần")

    # Hiển thị thông tin
    with info_col:
        st.subheader("Tên Lớp Học Phần:")
        st.write(lop_hoc_phan)

        st.subheader("Mã Lớp Học Phần:")
        st.write(ma_lop_hoc_phan)

        st.subheader("Giảng Viên:")
        st.write(giang_vien)
    


    # Hiển thị dữ liệu bảng
    if 'show_df' not in st.session_state:
        st.session_state.show_df = False
    view_dataframe(data.iloc[:, :7], st.session_state, "Danh sách sinh viên của lớp học phần")
    # view_dataframe(data, show_df,"Danh sách sinh viên của lớp học phần" )


    # # Chuyển đổi cột 'Ngày sinh' sang định dạng datetime
    # data['Ngày sinh'] = pd.to_datetime(data['Ngày sinh'], format='%d/%m/%Y')
    # # Lấy ngày tháng năm (không bao gồm giờ và phút)
    # data['Ngày sinh'] = data['Ngày sinh'].dt.date

    # Thống kê số lượng sinh viên nghỉ và đi học trong ngày
    ngay_hien_tai = datetime.now().date()
    
    # Danh sách các mã sinh viên cần xóa
    selected_msv = data.loc[data.iloc[:, -1] == 1, 'Mã SV'].tolist()

    # Xóa các dòng có mã sinh viên trong danh sách
    sinh_vien_nghi_hoc = data[~data['Mã SV'].isin(selected_msv)]
    sinh_vien_di_hoc = data[data['Mã SV'].isin(selected_msv)]
    


    # Hiển thị thống kê
    st.subheader(f"Thống Kê Sinh Viên Ngày {ngay_hien_tai.strftime('%d/%m/%Y')}")
    st.write(f"Số lượng sinh viên nghỉ học: {len(sinh_vien_nghi_hoc)}")
    st.write(f"Số lượng sinh viên đi học: {len(sinh_vien_di_hoc)}")

    if str(ngay_hien_tai) != str(data.columns[-1]):
        data[ngay_hien_tai] = 0
    st.dataframe(data)

    data.to_csv('data.csv', index=False)
    


    # Hiển thị danh sách sinh viên nghỉ học
    if st.button("Danh Sách Sinh Viên Nghỉ Học"):
        st.dataframe(sinh_vien_nghi_hoc.iloc[:, :7])



    # Hiển thị danh sách sinh viên đi học
    if st.button("Danh Sách Sinh Viên Đi Học"):
        st.dataframe(sinh_vien_di_hoc.iloc[:, :7])

# def display_home():
#     st.title("Trang Chính")
#     # Hiển thị nội dung trang chính nếu cần

# Gọi hàm main khi chạy ứng dụng
file_path = r'D:\WorkSpace\KhaiPhaDuLieu\classifier\face_recognition\app\danhsachsinhvien\danhsachsinhvien.csv'
lop_hoc_phan = "Khai phá dữ liệu - Nhóm 1"
ma_lop_hoc_phan = "2023-2024.1.TIN4103.001"
giang_vien = "Nguyễn Ngọc Thủy (1990)"
def app():
    ThongKe(file_path, lop_hoc_phan, ma_lop_hoc_phan, giang_vien)