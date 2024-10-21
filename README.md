# 🌍 Semantic Drone Image Segmentation Using UNet

Welcome to the **Semantic Drone Image Segmentation** project! This repository implements **semantic segmentation** on aerial drone images using the **UNet** architecture. The model is trained on the [Aerial Semantic Segmentation Drone Dataset](https://www.kaggle.com/datasets/bulentsiyah/semantic-drone-dataset) from Kaggle, aiming to accurately segment various objects like **buildings**, **vegetation**, **roads**, and more.

---

## 📄 Overview

This project focuses on the application of **UNet**, a deep learning architecture widely used for **image segmentation**. The model was trained on drone images to predict pixel-wise segmentation masks. Here's a summary of the training:

- **Model:** UNet
- **Dataset Split:** 80% Training | 20% Testing
- **Training Epochs:** 100 (with early stopping)
- **Best Epoch:** 27
- **Final Epoch:** 37 (early stopping applied with patience = 10)
- **Test Accuracy:** 81%

---

## 📊 Dataset

The dataset used for this project is the **Aerial Semantic Segmentation Drone Dataset** from Kaggle, containing high-resolution images annotated with pixel-level segmentation masks. The dataset is split into:

- **80% for Training**
- **20% for Testing**

You can download the dataset from [here](https://www.kaggle.com/datasets/bulentsiyah/semantic-drone-dataset).

---

## 🧠 Model Architecture

We implemented the **UNet** model, which features an **encoder-decoder** structure with **skip connections**. The architecture is particularly well-suited for segmentation tasks, allowing the network to capture both **high-level features** and **fine details**.

![image](https://github.com/user-attachments/assets/6c3ce518-4e77-489f-a553-cb6c4a05bc50)

- **Encoder:** Downsampling the image while learning spatial features
- **Decoder:** Upsampling and reconstructing the image segmentation map
- **Skip Connections:** Retain context from encoder layers to enhance segmentation details

---

## 🚀 Training Details

- **Epochs:** 100
- **Early Stopping:** Enabled with patience of 10 epochs
- **Model Checkpoints:** Best model saved based on validation loss
- **Training Stopped:** After epoch 37 due to early stopping
- **Best Epoch:** 27
- **Testing Accuracy:** 81%

---

## 🔥 Results

The model achieved a **testing accuracy of 81%**. The following images showcase some of the model’s predictions from the test set:

| Original Image | Ground Truth | Predicted Mask |
|:--------------:|:------------:|:--------------:|
| ![image](https://github.com/user-attachments/assets/185ac5c5-2285-442e-978e-979aa66b76ae) | ![image](https://github.com/user-attachments/assets/d22bb0fc-89a9-435a-892e-ed6c61858d7c) | ![image](https://github.com/user-attachments/assets/8ab7b199-47e2-4a38-a3c3-61e7d4f18068) |
| ![image](https://github.com/user-attachments/assets/e758ba68-4d0e-4271-92e1-42254a955a80) | ![image](https://github.com/user-attachments/assets/7b95cda6-b2d4-4b5f-8346-1c21cf080f10) | ![image](https://github.com/user-attachments/assets/cab70608-5b4b-406d-a5b6-0d0984bcca5b) |
| ![image](https://github.com/user-attachments/assets/3e940840-7504-402d-ac78-ca84bf2123a6) | ![image](https://github.com/user-attachments/assets/7d7601b9-abca-46ad-8a42-dcbc18da821d) | ![image](https://github.com/user-attachments/assets/880462a4-c1de-4810-9614-c8f837ba4927) |
| ![image](https://github.com/user-attachments/assets/3835f933-35f9-4ebb-9836-f677fa506284) | ![image](https://github.com/user-attachments/assets/40417604-b7af-4348-9c2b-edb1cbf8d96e) | ![image](https://github.com/user-attachments/assets/8fd40b7e-e430-4c9f-8805-651a74d19c45) |


---

## 🛠️ How to Use

### 1. Clone the Repository:

```bash
git clone https://github.com/yourusername/semantic-drone-segmentation-unet.git
```
### 2. Upload the Notebook on Kaggle
### 3. Run the Notebook Using GPU

---

## 🤝 Contributing
Contributions are welcome! If you want to contribute to this project, feel free to submit a pull request or open an issue.

---

## 🙌 Acknowledgements
- **Dataset** provided by [Kaggle](https://www.kaggle.com/datasets/bulentsiyah/semantic-drone-dataset).
- **The UNet** architecture is inspired by the paper [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597).

---

## 📬 Contact
If you have any questions, feel free to reach out via GitHub or email.
