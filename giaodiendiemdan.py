from facenet_pytorch import MTCNN
from collections import Counter
import torch
from torchvision import transforms
from facenet_pytorch import InceptionResnetV1, fixed_image_standardization
from PIL import Image
import joblib
from unidecode import unidecode
import streamlit as st
import main

import pandas  as pd

def trans(img):
    transform = transforms.Compose([
            transforms.ToTensor(),
            fixed_image_standardization
        ])
    return transform(img)

def fixed_image_standardization(image_tensor):
    processed_tensor = (image_tensor - 127.5) / 128.0
    return processed_tensor

def load_features(file_path):
    print('loading file')
    print('loaded')
    return joblib.load(file_path)
data_file_path = r'D:\WorkSpace\KhaiPhaDuLieu\classifier\face_recognition\app\app_page\data.csv'

def ReadCSV():
    import csv
    data_dict = {}
    # Đọc file CSV
    with open(data_file_path, 'r', encoding='utf-8') as file:
        # Đọc dữ liệu từ file CSV
        reader = csv.DictReader(file)
        
      
        # Lặp qua từng dòng trong file CSV
        for row in reader:
            # Lấy giá trị của cột "tên"
            ten_value = row['tên']
            # print(ten_value)
            # Tạo mảng giá trị còn lại cho từng dòng
            other_values = [row[key] for key in row if key != 'tên']

            # Thêm vào từ điển với key là "tên" và value là mảng giá trị còn lại
            data_dict[ten_value] = other_values
    return data_dict

def NameSVDiemDanh():
    data_dict = ReadCSV()
    # print(data_dict.keys())
    found_items = {key: value for key, value in data_dict.items() if unidecode(key) in st.session_state.NameSV}
    Ten=list(found_items.keys())
    found_items=list(found_items.values())
    return found_items,Ten[0]

def cap_nhat_tt_diemdanh(masv):
    masv_to_replace = masv

    # Mã SV mới
    new_masv_value = 1

    # Đọc dữ liệu từ file CSV vào DataFrame
    df = pd.read_csv(data_file_path, encoding='utf-8')

    # Thực hiện thay thế giá trị trong cột cuối cùng với điều kiện Mã SV
    df.loc[df['Mã SV'] == masv_to_replace, df.columns[-1]] = new_masv_value

    # Lưu lại DataFrame vào file CSV
    df.to_csv(data_file_path, index=False, encoding='utf-8')


def load_thongke():
    st.session_state.refresh_flag = True
    st.markdown("<script>location.reload();</script>", unsafe_allow_html=True)
    # st.experimental_rerun()

    
knn_model_path = r'D:\WorkSpace\KhaiPhaDuLieu\classifier\dataset\knn_model\knn_model.pkl'
def giaodien(ModelPath=knn_model_path):
    if 'ArraySV' not in st.session_state:
        st.session_state.ArraySV = []
    if 'NameSV' not in st.session_state:
        st.session_state.NameSV = "Unknow"
    if 'Image' not in st.session_state:
        st.session_state.Image = []
    if 'refresh_flag' not in st.session_state:
        st.session_state.refresh_flag = False
    mtcnn = MTCNN(margin=20, keep_all=True, post_process=False, device='cpu')

    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    model = InceptionResnetV1(
        classify=False,
        pretrained="casia-webface"
    ).to(device)

    model.eval()

    knn_model = load_features(ModelPath)

    st.title('Fingermath App')
    mtcnn = MTCNN(margin=20, keep_all=True, post_process=False, device='cpu')

    import cv2
    video_url = r'D:\WorkSpace\KhaiPhaDuLieu\classifier\dataset\test_video\DatVan_v2.mp4'
    v_cap = cv2.VideoCapture(0)

    v_cap .set(3, 1080)
    v_cap .set(4, 720)
    col1, col2 = st.columns([3, 3])
    with st.container():
        
        #Đây là màn hình camera
        with col1:
            frame_placeholder = st.empty()
        
        stop_button_pressed = st.button('Stop')

        fps = v_cap.get(cv2.CAP_PROP_FPS)
        index = 0
        with col2:
            st.header('Thông tin người dùng')
            with st.empty():
                while v_cap .isOpened():
                    try:
                        success, frame = v_cap.read()

                        if not success:
                            st.write("The video capture has ended.")
                            break

                        frame_copy = frame.copy()
                        index +=1
                        if not success:
                            break
                        file_name = r'test.jpg'
                        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        frame = Image.fromarray(frame)
                        mtcnn(frame, file_name)
                        image = Image.open(file_name)
                        embed = model(trans(image).unsqueeze(0).to(device))
                        embed_numpy = embed.detach().cpu().numpy()
                        label = knn_model.predict(embed_numpy)
                        boxes, _ = mtcnn.detect(frame)
                        st.session_state.ArraySV.append(label[0])              
                        # print(label)
                        if index == 20:
                            break
                        label = str(label)
                        for box in boxes:
                            bbox = list(map(int,box.tolist()))
                            # print(bbox)
                            frame_copy = cv2.rectangle(frame_copy, (bbox[0],bbox[1]), (bbox[2],bbox[3]), (0,0,255), 6)
                            frame_copy = cv2.putText(frame_copy, label , (bbox[0],bbox[1]), cv2.FONT_HERSHEY_DUPLEX, 2, (0,255,0), 2, cv2.LINE_8)
                        frame_copy  = cv2.cvtColor(frame_copy, cv2.COLOR_BGR2RGB)
                        st.session_state.Image=frame_copy
                        frame_placeholder.image(frame_copy, channels='RGB')
                        
                        # delay = int(1000 / fps) if fps > 0 else 1
                        if cv2.waitKey(1) & 0xFF == ord('q') or stop_button_pressed:
                            # st.write(st.session_state.ArraySVst.session_state.ArraySV)
                            name_counts = Counter(st.session_state.ArraySV)
                            # Lấy tên xuất hiện nhiều nhất
                            st.session_state.NameSV = name_counts.most_common(1)[0][0]
                            break
                    except Exception as e:
                        frame_copy  = cv2.cvtColor(frame_copy, cv2.COLOR_BGR2RGB)
                        frame_placeholder.image(frame_copy, channels='RGB')
                        if cv2.waitKey(1) & 0xFF == ord('q') or stop_button_pressed:
                            break
                frame_placeholder.image(st.session_state.Image,channels='RGB')
                name_counts = Counter(st.session_state.ArraySV)
                # Lấy tên xuất hiện nhiều nhất
                st.session_state.NameSV  = name_counts.most_common(1)[0][0]
                v_cap.release()
                cv2.destroyAllWindows()
            info,name=NameSVDiemDanh()

            st.write('**Họ và tên:**:',info[0][2],name)
            st.write('**Mã sinh viên:**',info[0][1])
            st.write('**Ngày sinh:**',info[0][4])
            st.write('**Khóa:**',info[0][5])
            st.write('**Ngành:**', " CNTT")
            st.button("Xac Nhan", on_click= load_thongke)
            # st.write('**Nhóm:**',info[0][7])
            cap_nhat_tt_diemdanh(info[0][1])
            st.session_state.ArraySV = []
            
            