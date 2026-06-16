import streamlit as st
import pandas as pd

@st.dialog("Employee Profile")
def show_profile(employee):
    st.markdown(f"""
    <div style='text-align: center;'>
        <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='120' style='margin-bottom: 10px;'>
        <h3 style='margin: 0px; color: #000000;'>{employee['Name']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"**Name:**<br>{employee['Name']}", unsafe_allow_html=True)
    st.markdown(f"**Email ID:**<br>{employee['Email']}", unsafe_allow_html=True)
    st.markdown(f"**Contact:**<br>{employee['Contact']}", unsafe_allow_html=True)
    st.markdown(f"**Employee ID:**<br>{employee['Employee ID']}", unsafe_allow_html=True)
    st.markdown(f"**Skills:**<br>{employee['Skills']}", unsafe_allow_html=True)
    st.markdown(f"**Certification:**<br>{employee['Certification']}", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Close Profile", use_container_width=True):
        st.query_params.page = "Employees Detail"
        st.rerun()

def show_employee_page():
    st.markdown("<h1 style='color: #000000;'>🧑‍💼 Employees Detail</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("<h3 style='color: #000000;'>Employee Directory</h3>", unsafe_allow_html=True)
    
    data = {
        "Sr.No": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Name": ["Parth Tanve", "Afatab Khan", "Arya sir", "Neha Gupta", "Vikram Verma", "Anjali Desai", "Rohan Mehta", "Sonal Jain", "Karan Patel", "Pooja Reddy"],
        "Email": ["parth.t@pararobo.com", "afatab.k@pararobo.com", "arya.s@pararobo.com", "neha.g@pararobo.com", "vikram.v@pararobo.com", "anjali.d@pararobo.com", "rohan.m@pararobo.com", "sonal.j@pararobo.com", "karan.p@pararobo.com", "pooja.r@pararobo.com"],
        "Contact": ["+91-9876543210", "+91-9876543211", "+91-9876543212", "+91-9876543213", "+91-9876543214", "+91-9876543215", "+91-9876543216", "+91-9876543217", "+91-9876543218", "+91-9876543219"],
        "Employee ID": ["EMP001", "EMP002", "EMP003", "EMP004", "EMP005", "EMP006", "EMP007", "EMP008", "EMP009", "EMP010"],
        "Employee Role": ["AI/ML Developer", "HR Manager", "Flutter Developer", "NLP Engineer", "Data Scientist", "UI/UX Designer", "Database Admin", "Project Manager", "DevOps Engineer", "QA Tester"],
        "Working on Current Project": ["Aquatic Camouflage AI", "Internal Recruitment", "AscendHub", "Bruno Chatbot", "Resume Parser", "CRM Redesign", "Data Migration", "CRM Redesign", "Server Migration", "AscendHub"],
        "Skills": ["Python, YOLOv8, CNNs", "Talent Acquisition, Payroll", "Dart, Flutter, Firebase", "NLP, Google Gemini API", "Python, NLTK, LSTM", "Figma, Adobe XD", "SQL, DB Optimization", "Agile, Scrum", "AWS, Docker, CI/CD", "Manual Testing, Selenium"],
        "Certification": ["NVIDIA Deep Learning Institute", "HR Professional (SHRM)", "Google Flutter Dev", "GenAI Certification", "Coursera Data Science", "Google UX Design", "HackerRank SQL Verified", "PMP Certified", "AWS Solutions Architect", "ISTQB Foundation"]
    }
    
    df = pd.DataFrame(data)

    if "emp_id" in st.query_params:
        emp_id = st.query_params["emp_id"]
        if emp_id in df["Employee ID"].values:
            selected_employee = df[df["Employee ID"] == emp_id].iloc[0]
            show_profile(selected_employee)

    html_table = """
    <style>
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #FFFFFF;
        color: #000000;
    }
    .custom-table th, .custom-table td {
        border: 2px solid #000000;
        padding: 12px;
        text-align: left;
    }
    .custom-table th {
        font-weight: bold;
        font-size: 16px;
    }
    .custom-table a {
        color: #0000EE;
        text-decoration: underline;
        font-weight: bold;
        cursor: pointer;
    }
    .custom-table a:hover {
        color: #FF0000;
    }
    </style>
    <table class="custom-table">
        <thead>
            <tr>
                <th>Sr.No</th>
                <th>Name</th>
                <th>Email</th>
                <th>Contact</th>
                <th>Employee ID</th>
                <th>Employee Role</th>
                <th>Working on Current Project</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in df.iterrows():
        name_link = f"<a href='?page=Employees%20Detail&emp_id={row['Employee ID']}' target='_self'>{row['Name']}</a>"
        
        html_table += f"<tr>"
        html_table += f"<td>{row['Sr.No']}</td>"
        html_table += f"<td>{name_link}</td>"
        html_table += f"<td>{row['Email']}</td>"
        html_table += f"<td>{row['Contact']}</td>"
        html_table += f"<td>{row['Employee ID']}</td>"
        html_table += f"<td>{row['Employee Role']}</td>"
        html_table += f"<td>{row['Working on Current Project']}</td>"
        html_table += f"</tr>"
        
    html_table += "</tbody></table>"
    
    st.markdown(html_table, unsafe_allow_html=True)