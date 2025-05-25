# 📊 Sales Data Insights

## 🎯 Objective
This project performs basic analysis on a sales dataset using **Pandas** and **NumPy** to derive insights such as regional sales distribution, product performance, and key statistics.

---

## 📁 Dataset
The dataset used contains the following columns (required for the script to run properly):

- `Region` – Sales region (e.g., North, South)
- `Product` – Name of the product
- `TotalSales` – Sales value per entry

Make sure your CSV file is named `datset - Sheet1.csv` and is in the same directory as the script.

---

## ⚙️ Setup Instructions

### ✅ Prerequisites
Ensure you have Python installed along with the following libraries:

- `pandas`
- `numpy`

### 📦 Installation

Install the required packages using:

```bash
pip install pandas numpy
```

---

## 🚀 How to Run

Run the script using:

```bash
python sales_analysis.py
```

Make sure your dataset file (`datset - Sheet1.csv`) is placed in the same folder as the script.

---

## 📊 Functionalities

This script includes the following functionalities:

- ✔️ Load and clean the dataset (drop missing/null values)
- 📍 Sum of sales by **region**
- 📈 Average sales per **product**
- 🥇 Identify the **highest** and **lowest** selling products
- 📐 Use **NumPy** to compute:
  - Mean of total sales
  - Median of total sales
  - Standard deviation of total sales

---

## 📌 Output

The script prints the following to the console:

- Preview of the dataset
- Total sales by region
- Average sales per product
- Highest and lowest selling products
- NumPy-based statistical analysis (mean, median, standard deviation)

---

## 👩‍💻 Author

**Pinky Gupta**  
Created on **May 25, 2025**

---

## 📎 License

This project is for academic purposes only.
