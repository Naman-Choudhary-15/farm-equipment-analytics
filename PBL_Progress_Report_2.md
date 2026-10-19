**Program and Branch Name:** BTech CSE-DS

# PBL Progress Report – II 

**Course Name:** Foundation of Data Science Lab  
**Course Code:** CCSDS0301  
**Faculty Name:** Ms. Garima Dhawan  
**Assignment Type:** Individual Assignment  
**Student(s) Name:** Naman Choudhary  
**ERP ID (I Year) / Roll No. (II Year onwards):** 2501331540177  
**Team/Group No:** N/A (Individual Assignment)  
**Problem Statement / Project Title:** Farm Equipment Utilization Analytics   
**SDG(s):** SDG 2: Zero Hunger  
**Reporting Month:** Month 2  
**Date of Submission:** 17 October 2026  

---

### Review 2: Implementation & Visualization Progress

**1. Work Completed During Month 2**
*   **Data Generation & Pipeline:** Created a robust synthetic dataset (500 records) using Python (`pandas`, `numpy`) to simulate agricultural IoT sensor telemetry (fuel dissipation, idle hours, operating load, and machine failure flags).
*   **Data Cleaning & Preprocessing:** Implemented preprocessing routines to identify and handle missing values (imputing missing sensor readings via group medians).
*   **Exploratory Data Analysis (EDA):** Generated statistical plots (`seaborn`, `matplotlib`) analyzing correlations between idle time, fuel wastage, and seasonal demand.
*   **Baseline SaaS Dashboard Prototype:** Architected an interactive web dashboard using **Streamlit** styled after modern analytics tools (featuring custom metric cards, breadcrumbs, personalized operator authentication badge, and status-pill tagged activity feeds).
*   **Interactive Visualizations:** Implemented multidimensional Plotly components, including a machine condition share donut chart, operating efficiency grouped bar charts, and an interactive 3D Telemetry Spatial Matrix.
*   **Code Versioning on GitHub:** Initialized Git version control, configured `.gitignore`, and published the complete codebase to a public GitHub repository.
*   **Cloud Deployment on Render:** Successfully deployed the baseline application as a live cloud web service on Render with continuous deployment, accessible from any mobile or desktop web browser.

**2. Unit/Module Concepts Identified for Application**
Applied Data Cleaning techniques, Handling Missing Sensor Values, Exploratory Data Analysis (EDA) on time-series telemetry, Interactive Data Visualization, and Cloud Deployment principles from Unit/Module 2 and Unit/Module 3 of the syllabus.

**3. Evidence / Supporting Material**
*   **Live Cloud Web Application:** [https://farm-equipment-analytics.onrender.com](https://farm-equipment-analytics.onrender.com)
*   **GitHub Repository:** [https://github.com/Naman-Choudhary-15/farm-equipment-analytics](https://github.com/Naman-Choudhary-15/farm-equipment-analytics)
*   **Python Codebase:** `dashboard.py`, `generate_mock_data.py`, `eda_analysis.py`, `.streamlit/config.toml`, and `requirements.txt`.
*   **Dataset & Visuals:** `telemetry_data.csv` and static EDA summary `eda_results.png`.

**4. Challenges Faced**
*   **Theme & Contrast Compatibility:** Resolved widget inheritance conflicts where system dark mode caused low contrast and invisible labels against light container backgrounds; resolved using `.streamlit/config.toml` and targeted CSS rules.
*   **Cloud Production Configuration:** Configured Render's dynamic host and port environment variables (`--server.port $PORT --server.address 0.0.0.0`) to ensure 100% cloud uptime without binding errors.
*   **Multi-Sensor 3D Mapping:** Handled multidimensional coordinate mapping in Plotly to visualize interactions between engine load, fuel usage, and idle duration without cluttering the UI.

**5. Individual / Team Contribution**
This is an individual assignment; all work completed during Month 2—including data generation, EDA coding, baseline SaaS UI architecture, contrast tuning, GitHub repository setup, and cloud deployment on Render—has been carried out independently.

**6. Overall Progress (%)**
Approximately 55–60% complete (Data pipeline, EDA, and baseline dashboard prototype completed; ML modeling phase pending).

**7. Plan for Next Review (Month 3 / Review 3)**
*   **Machine Learning Model Development:** Train supervised ML models using `scikit-learn` (e.g., Random Forest / Logistic Regression classifier for predictive maintenance and Linear Regression for fuel consumption forecasting).
*   **Model Evaluation & Metrics:** Evaluate model accuracy, generate confusion matrices, and plot precision-recall / ROC curves.
*   **Dashboard Integration:** Embed real-time ML model inference directly into the Streamlit dashboard to replace static thresholds with predictive probability scores.
*   **Final Deliverables:** Compile the comprehensive final project report and presentation slide deck for the final viva review.

---
**Student Declaration**
I/We certify that this assignment is my/our own work, with all sources appropriately acknowledged. I/We understand that a 0% mark and further academic penalties may apply if the content is found to be plagiarised or inappropriately AI-generated.

**Student Name & Signature(s):** Naman Choudhary  
**Date:** 17 October 2026
