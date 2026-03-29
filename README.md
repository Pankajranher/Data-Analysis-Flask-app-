# 📊 Sales Data Analysis Dashboard (Flask Project)

## 🚀 About the Project

This is a **Flask-based Sales Data Analysis Dashboard** that allows users to upload a CSV file and visualize insights from the data.

The application performs:
- Data cleaning
- Data analysis using Pandas
- Chart generation using Matplotlib
- Displays insights in a simple and interactive dashboard UI

This project simulates a **real-world data analyst workflow**, where raw data is processed and converted into meaningful insights.

---

## ✨ Features

✅ Upload CSV file  
✅ Data cleaning (remove nulls, duplicates)  
✅ Revenue analysis  
✅ Top product identification  
✅ Chart generation (Product vs Revenue)  
✅ Dashboard UI with insights  

---

## 🛠️ Tools & Technologies Used

- **Backend:** Flask (Python)
- **Data Processing:** Pandas
- **Visualization:** Matplotlib
- **Frontend:** HTML, CSS
- **Other:** Jinja2 Templates

---

## 📂 Project Structure
Data-analysis/
│
├── app/
│ ├── init.py # App factory
│ ├── routes.py # All routes (upload, dashboard)
│ ├── utils.py # Data processing functions
│
├── templates/
│ ├── index.html # Upload page
│ ├── dashboard.html # Dashboard page
│
├── static/ # Stores generated charts
├── uploads/ # Stores uploaded CSV files
│
├── run.py # Entry point
└── README.md


---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone <your-repo-link>
cd Data-analysis
python -m venv venv
venv\Scripts\activate   # Windows
python run.py
http://127.0.0.1:5000/

📊 How It Works
User uploads a CSV file
File is saved in uploads/
Data is cleaned using Pandas
Insights are generated (Revenue, Top Product)
Chart is created using Matplotlib
Dashboard displays results

Example CSV Format are in 'Sample csv files'

Future Improvements
Add multiple charts (Category, Trend)
Add filters (Date, Category)
Use Plotly for interactive charts
Add user authentication
Store data in database

👨‍💻 Author

Pankaj Ranher

🔗 LinkedIn: https://www.linkedin.com/in/pankaj-ranher