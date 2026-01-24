**💸 Intelligent Expense Analyzer**

An end-to-end expense analysis application that builds **personalized spending profiles** and detects **monthly anomalies** based on a user’s own historical behavior.

This project focuses on **product thinking, system design, and real-world data handling**, rather than simple rule-based expense categorization.



**🚀 Features (v1)**

  **🔐 Soft User Identity**
     - Email-based identity (no dummy user IDs)
     - Persistent user data across sessions

  **📊 Historical Expense Tracking**
     - Stores transaction history incrementally
     - Visualizes long-term spending trends
     - Read-only historical mode (no accidental changes)

 **📈 Monthly Analysis & Anomaly Detection**
     - Upload current month transactions
     - Detects anomalies based on *personal historical patterns*
     - Severity-based insights (percentage deviation, impact level)

  **🧠 Personalized Modeling**
     - Builds a baseline profile per user
     - Learns what is “normal” for each individual
     - Avoids generic thresholds



  **🛠️ Tech Stack**

      - Python
      - Pandas – data processing
      - Streamlit – frontend & app framework
      - Plotly – interactive visualizations
      - Modular backend architecture



  **🧱 System Design (High Level)**

            User Email
                 ↓
       Load Historical Data
                 ↓
      User Uploads Monthly CSV
                 ↓
     Anomaly Detection (Monthly Mode)
                 ↓
        Append to History
                 ↓
        Update User Profile


  Clear separation of: 
     - 📊 Historical View 
     - 📈 Monthly Analysis



 **📂 Project Structure**

Intelligent Expense Analyzer/
├── app.py
├── services/
│ ├── profile.py
│ ├── anomaly.py
│ └── init.py
├── data/
│ ├── history/ (ignored in Git)
│ └── profiles/ (ignored in Git)
├── requirements.txt
└── README.md




 **▶️ How to Run Locally**

```bash
# Create virtual environment
    python -m venv venv

# Activate (Windows)
    venv\Scripts\activate

# Install dependencies
   pip install -r requirements.txt

# Run the app
   streamlit run app.py
