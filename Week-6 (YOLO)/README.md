# YOLO Object Detection Project

This project demonstrates object detection using the YOLO (You Only Look Once) framework.

## Project Setup

### 1. Create a Virtual Environment

It's recommended to use a virtual environment to manage project dependencies. You can create one using conda:

```bash
   conda create -n yolo_env python=3.10 -y
```

This command creates a virtual environment named `yolo_env` with Python 3.10. The `-y` flag automatically answers "yes" to any prompts.
Use the `-p` instead of `-n` if env dir needs to be in current working directory.

### 2. Activate the Virtual Environment

Activate the virtual environment:

```bash
conda activate yolo_env
```

### 3. Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

Make sure you have a `requirements.txt` file in your project directory listing the necessary libraries (e.g., `ultralytics`, `torch`, `torchvision`, `torchaudio`).

### 4. GPU Recommendation

**Important:** Training YOLO models is computationally intensive and requires significant processing power. It is **highly recommended** to use a GPU for training, otherwise, the training process will be extremely slow and may take a very long time to complete.

If you are using Google Colab, ensure you have selected a GPU runtime by going to "Runtime" -> "Change runtime type" and selecting "GPU" as the hardware accelerator.
<br><br>

# YOLO Project Folder Structure and Configuration

To work effectively with YOLO, it's crucial to maintain a well-organized folder structure. Below is an example structure for setting up a YOLO project along with the details of a `.yaml` file used for configuration.

---

## Folder Structure

The recommended folder structure for a YOLO project is as follows:

```
yolo_dataset/
|
├── images/
│   ├── train/
│   │   ├── image1.jpg
│   │   ├── image2.jpg
│   │   └── ...
│   ├── val/
│   │   ├── image3.jpg
│   │   ├── image4.jpg
│   │   └── ...
│   └── test/
│       ├── image5.jpg
│       ├── image6.jpg
│       └── ...
└── labels/
    ├── train/
    │   ├── image1.txt
    │   ├── image2.txt
    │   └── ...
    ├── val/
    │   ├── image3.txt
    │   ├── image4.txt
    │   └── ...
    └── test/
        ├── image5.txt
        ├── image6.txt
        └── ...
├── data/
│   └── dataset.yaml
└── results/
    ├── runs
    └── ...  # Training logs, inference outputs, etc.
```

---

## Explanation of Folders

1. **`datasets`**:

   - **`images`**: Contains `train`,`test` and `val` directories with training and validation images.
   - **`labels`**: Contains `train`,`test` and `val` directories with `.txt` files specifying bounding box labels for corresponding images.
   - **`dataset.yaml`**: The dataset configuration file used by YOLO during training.

2. **`data`**:

   - Contains predefined model architecture `.yaml` files (e.g., `yolov5s.yaml`, `yolov5m.yaml`, `yolov5l.yaml`).

3. **`results`**:
   - Stores results such as training logs, inference outputs, and evaluation metrics.

---

## `dataset.yaml` File

The `dataset.yaml` file is a critical configuration file used to define dataset properties for YOLO. Below is an example of its content:

```yaml
train: datasets/images/train # Path to training images
val: datasets/images/val # Path to validation images
test: images/test # Path to testing images

nc: 5 # Number of classes in the dataset
names: # List of class names
  - class1
  - class2
  - class3
  - class4
  - class5
```

## Training

To train the YOLO model, run the following command:

```python
from ultralytics import YOLO

model = YOLO('yolo11n.yaml') # Choose your desired model architecture
results = model.train(data='datasets/dataset.yaml', epochs=250)
```

## Inference

To perform inference on new images, use the trained model:

```python
model = YOLO('path/to/runs/detect/train/weights.pt') # Load your trained model
results = model('path/to/image.jpg') # Run inference on an image
```

## Deactivate the Virtual Environment

When you are finished working on the project, deactivate the virtual environment:

```bash
conda deactivate
```

## Additional Notes

- Ensure you have the necessary CUDA drivers and libraries installed if you are using a GPU.
- Refer to the YOLO documentation for more advanced configuration options and usage details.

## Project Folder Structure

```
└── project_folder_name/
    ├── CODE/
    │   ├── predict_dog_breed.ipynb
    │   └── yolo_dog_breed_detection.ipynb
    ├── data/
    │   └── yolo_dog_breed_detector.yaml
    ├── dataset/
    │   └── yolo_dog_breed_dataset[Unizip before working].zip
    ├── dog_breed_predict_images/
    │   └── ...  # Images for inferencing
    ├── results/
    │   └── runs/
    │       └── ...  # Subfolders
    ├── README.md
    ├── requirements.txt
    └── prompts.md
```
**Important**

*   **Unzip Dataset:** Before using the dataset, you will need to unzip `yolo_dog_breed_dataset[Unizip before working].zip`.
*   **File Paths:** Ensure that file paths in your code and configuration files are correct relative to this folder structure.