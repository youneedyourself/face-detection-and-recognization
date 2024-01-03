import streamlit as st
import cv2

from datetime import datetime
import time



import streamlit as st
import pandas as pd
from datetime import datetime


file_path = r'D:\WorkSpace\KhaiPhaDuLieu\classifier\face_recognition\app\danhsachsinhvien\danhsachsinhvien.csv'
lop_hoc_phan = "Khai phá dữ liệu - Nhóm 1"
ma_lop_hoc_phan = "2023-2024.1.TIN4103.001"
giang_vien = "Nguyễn Ngọc Thủy (1990)"

def onclick_btn1():
    print('btn1')
def onclick_btn2():
    print('btn2')

def home_screen(title, monhoc, giangvien, thoigianbatdau, thoigianketthuc):
    
    st.session_state.loaded = True
    st.title(title)
    col1, col2  = st.columns(2)

    _, current_time_col = st.columns(2)

  
    label1 = col1.empty()
    label2 = col2.empty()

    time_label = current_time_col.empty()

   

    # label3 = col3.empty()
    # label4 = col4.empty()

    st.text("Thời gian bắt đầu: " + thoigianbatdau)
    st.text('Thời gian kết thúc: ' + thoigianketthuc)

    # colbtn1, colbtn2  = st.columns(2)
    # labelbtn1 = colbtn1.empty()
    # labelbtn2 = colbtn2.empty()
    # btn1 = st.button('Điểm danh vào lớp', key='diemdanh',on_click=onclick_btn1)
    # btn2 = st.button('Kết quả điểm danh', key='thongke', on_click= onclick_btn2)

    while True:
        # btn1 = False
        # btn2 = False
        # Lấy thời gian hiện tại
        current_time = datetime.now()

        # Định dạng thời gian theo yêu cầu: HH:mm:ss
        formatted_time = current_time.strftime("%H:%M:%S")

        # Cập nhật nội dung của các phần tử
        label1.text('Môn học: ' + monhoc)
        label2.text('Giảng viên: ' + giangvien)

        # Xóa toàn bộ nội dung của cửa sổ trước khi in thời gian mới
        time_label.text('Thời gian hiện tại: ' + formatted_time)

        # Tạm dừng 1 giây trước khi cập nhật lại thời gian
        time.sleep(1)

def app():
    home_screen(title='Thông tin lớp học phần', monhoc='Khai Phá Dữ Liệu', giangvien='Nguyễn Ngọc Thủy (1990)', thoigianbatdau= '13:00:00', thoigianketthuc= '16:00:00')


# home_screen(title='Thông tin lớp học phần', monhoc='Khai Phá Dữ Liệu', giangvien='Nguyễn Ngọc Thủy (1990)', thoigianbatdau= '13:00:00', thoigianketthuc= '16:00:00')



# ThongKe(file_path, lop_hoc_phan, ma_lop_hoc_phan, giang_vien)
# Kết thúc khi nhấn nút dừng
# cap.release()