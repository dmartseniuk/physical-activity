# Physical Activity Classification

## Description

This project focuses on classifying different physical activities using data collected from wearable sensors, such as accelerometers, gyroscopes, and magnetometers. The goal is to create a model that can accurately recognize activities and be applied to fitness tracking devices to improve activity monitoring and calorie estimation.

## Dataset

Due to size limitations, the dataset is **not included** in this repository. Please download it manually from the following link:

[Download Dataset](https://www.kaggle.com/datasets/diegosilvadefrana/fisical-activity-dataset)

After downloading, place the dataset inside a `data/` folder in the project directory:

```
📂 Physical-Activity-Classification/
│── 📂 data/               # Place dataset files here
│── 📂 notebooks/          # Folder containing Jupyter Notebooks
│── 📄 environment.yml     # Conda dependencies
│── 📄 requirements.txt    # Pip dependencies
│── 📄 .gitignore          # Ignore large files
│── 📄 README.md           # Project documentation
```

## Installation

To set up the environment, install the required dependencies using either Conda or Pip:

### Using Conda (Recommended)

```bash
conda env create -f environment.yml
conda activate physical_activity_env
```

### Using Pip

```bash
pip install -r requirements.txt
```

## Usage

Once the dataset is downloaded and placed in the `data/` folder, run the Jupyter Notebook:

```bash
jupyter notebook notebooks/notebook.ipynb
```

## Model

The project explores different machine learning models for activity classification. The best-performing model was **Random Forest**, which achieved **56% accuracy on the test set** and a **weighted F1-score of 56%**. The model performed well on static activities like **lying, sitting, and standing**, but struggled with **dynamic activities** like **running, rope jumping, and stair climbing**.

## Future Improvements

- Improve data balancing techniques to handle class imbalance
- Introduce additional features that capture movement dynamics
- Explore alternative models such as deep neural networks to enhance accuracy

## Contributing

If you want to improve this project, feel free to fork the repository and submit pull requests.
