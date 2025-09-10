# Nobel Prize Winners by Country (Animated Timeline)

## 📌 Project Overview
This project visualizes the **historical distribution of Nobel Prize winners** by birth country over time.  
It uses **pandas** for data processing and **matplotlib’s animation** tools to create a dynamic horizontal bar chart race, showing the **top 10 countries** with the most Nobel Prize laureates each year.

The final output is an **animated GIF** (`nobel_timeline.gif`) that demonstrates how different countries have contributed to Nobel Prizes throughout history.

---

## ⚙️ Features
- Loads and cleans Nobel Prize dataset (`nobel.csv`).  
- Aggregates the **cumulative number of Nobel Prizes** per country.  
- Animates the evolution of Nobel winners year by year.  
- Highlights the **top 10 countries** for each year.  
- Saves the visualization as an animated GIF for easy sharing.  

---

## 📂 Dataset
The dataset used: **`nobel.csv`**  
- **year** – Year of the Nobel Prize award.  
- **birth_country** – Country of birth of the laureate.  

⚠️ Ensure that your dataset contains these columns. If not, adjust the column names in the code.

---

## 🚀 Installation & Usage

1. **Clone the repository (or copy the script)**  
   ```bash
   git clone https://github.com/your-username/nobel-prize-visualization.git
   cd nobel-prize-visualization
2. **Install dependencies**
   ```bash
   pip install pandas matplotlib
3. **Place the dataset (**`nobel.csv`**) in the same folder as the script.**
4. **Run the script**
   ```bash
   python nobel_animation.py
5. **The script will generate:**

   **`nobel_timeline.gif`** → Animated bar chart race
