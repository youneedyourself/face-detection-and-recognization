# face-detection-and-recognization

![Python version](https://img.shields.io/badge/python-3.8.0-blue)
![License](https://img.shields.io/badge/license-MIT-white)
![Tensorflow version](https://img.shields.io/badge/tensorflow-1.7.0-orange)

 Building face object detection and recognization model based on MTCNN and Facenet model.
 Building an application to recognize face using Streamlit.

## Abstract

This project was carried out by 6 students from Hue University of Sciences: Nguyen Luon Mong Do, Nguyen Tien Nhat, Vo Dat Van, Nguyen Ngoc Quang Huy, Ly Nhat Phuong, and Nguyen Hoai Nam.

The Face Detection and Classification project aims to detect and recognize faces in video/camera to predict the name of the person in each detected face. This repository provides an implementation of the MTCNN and FaceNet model, which is a deep convolutional neural network (CNN) designed for face recognition tasks. Finally, we use Streamlit to build application.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/youneedyourself/face-detection-and-recognization.git
   ```
2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Download the pre-trained detect face models for the FaceNet model and place in the `model/` directory (We use CASIA-WebFace).

    | Model name      | LFW accuracy | Training dataset | Architecture |
    |-----------------|--------------|------------------|-------------|
    | [20180408-102900](https://drive.google.com/open?id=1R77HmFADxe87GmoLwzfgMu_HY0IhcyBz) | 0.9905        | CASIA-WebFace    | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |
    | [20180402-114759](https://drive.google.com/open?id=1EXPBSXwTaqrSC0OhUdXNmKSh9qJUQ55-) | 0.9965        | VGGFace2      | [Inception ResNet v1](https://github.com/davidsandberg/facenet/blob/master/src/models/inception_resnet_v1.py) |

## Dataset

To train the face classification model, you will need a dataset of labeled face images. 

Our dataset includes 15 videos from 15 students in the Data Mining 2023 - Group 1. You need to go to Source folder to learn about MTCNN and use this model to create a dataset.
We did that and created 2 files: face_embeddings.pkl and names.pkl.

Ensure that your dataset is organized in the following structure:

```
data/images/raw
├── person1/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── person2/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── ...
```

Note: Facenet model required at least 2 object detection to train and predict.

# Methods 
- Use MTCNN Model to detect face and create datasets.
- After that, use FaceNet model (Apply CASIA-WebFace pre-trained) to train. 
- Use Streamlit to build application.

## Results

Run the file `mainpy` to test your result trained model online in video (You can test your result in camera by change the line "v_cap = cv2.VideoCapture(0)" to "v_cap = cv2.VideoCapture()" in giaodiendiemdanh.py).

```
python main.py
```

The results achieved by the face detection and classification model trained on your dataset will vary depending on various factors such as the quality of your dataset, the size of the training set, and the chosen hyperparameters. It is recommended to experiment with different configurations to achieve the best results for your specific use case.

<p align="center">
  <img src="data/diemdanh.png"width="541" height="241">
</p>

## References
* Rongrong Jin; Hao Li; Jing Pan; Wenxi Ma; and Jingyu Lin. Face recognition based on mtcnn and facenet. 2020.
* Siyao Qi, Xinyu Zuo, Weijia Feng, and I G Naveen. Face recognition model based on mtcnn and facenet. In 2022 IEEE 2nd International Conference on Mobile Networks and Wireless Communications (ICMNWC), pages 1–5, 2022.
* Florian Schroff, Dmitry Kalenichenko, and James Philbin. Facenet: A unified embedding for face recognition and clustering. In 2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), pages 815–823, 2015.
* F. Schroff; D. Kalenichenko and J. Philbin. Facenet: A unified embedding for face recognition and clustering. 2015.
* Application: Streamlit
* This project is mainly referenced at: https://github.com/pewdspie24/FaceNet-Infer. Thanks a lot!

## Contributing

Contributions to this repository are welcome. If you find any issues or would like to suggest improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/youneedyourself/face-detection-and-recognization/blob/main/LICENSE). Feel free to use and modify the code for your own purposes.