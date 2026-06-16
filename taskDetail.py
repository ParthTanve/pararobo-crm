import streamlit as st
import pandas as pd

def create_task_table(df):
    html_table = """
    <style>
    .task-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #FFFFFF;
        color: #000000;
        margin-top: 15px;
    }
    .task-table th, .task-table td {
        border: 2px solid #000000;
        padding: 12px;
        text-align: left;
    }
    .task-table th {
        font-weight: bold;
        font-size: 16px;
        background-color: #F8F9FA;
    }
    </style>
    <table class="task-table">
        <thead>
            <tr>
                <th>Employees Names</th>
                <th>Related Project</th>
                <th>Task</th>
                <th>Priority</th>
                <th>Result</th>
                <th>Outcome</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in df.iterrows():
        
        priority_color = "#000000"
        if row['Priority'] == 'High':
            priority_color = "#ff0000"
        elif row['Priority'] == 'Medium':
            priority_color = "#ff9900"
        elif row['Priority'] == 'Low':
            priority_color = "#00b300"
            
        result_color = "#000000"
        if row['Result'] == 'Completed':
            result_color = "#00b300"
        elif row['Result'] == 'Pending':
            result_color = "#ff0000"
        elif row['Result'] == 'In Progress':
            result_color = "#0000EE"

        html_table += "<tr>"
        html_table += f"<td><strong>{row['Employees Names']}</strong></td>"
        html_table += f"<td><strong>{row['Related Project']}</strong></td>"
        html_table += f"<td>{row['Task']}</td>"
        html_table += f"<td style='color: {priority_color}; font-weight: bold;'>{row['Priority']}</td>"
        html_table += f"<td style='color: {result_color}; font-weight: bold;'>{row['Result']}</td>"
        html_table += f"<td>{row['Outcome']}</td>"
        html_table += "</tr>"
        
    html_table += "</tbody></table>"
    return html_table

def show_task_page():
    st.markdown("<h1 style='color: #000000;'>📝 Task Details</h1>", unsafe_allow_html=True)
    st.markdown("---")
    

    data = {
        "Employees Names": [
            "Parth Tanve", 
            "Arya sir", 
            "Vikram Verma", 
            "Neha Gupta", 
            "Karan Patel", 
            "Anjali Desai", 
            "Rohan Mehta", 
            "Sonal Jain", 
            "Pooja Reddy",
            "Afatab Khan"
        ],
        "Related Project": [
            "Resume Parser Analyzer",
            "AscendHub",
            "Resume Parser Analyzer",
            "Resume Parser Analyzer",
            "AscendHub",
            "AscendHub",
            "Resume Parser Analyzer",
            "AscendHub",
            "AscendHub",
            "Resume Parser Analyzer"
        ],
        "Task": [
            "Train CNN on new dataset for layout detection", 
            "Fix Flutter UI rendering issue on Android devices", 
            "Develop LSTM model for skill extraction",
            "Optimize NLTK tokenization speed",
            "Integrate Firebase Authentication",
            "Design modern UI wireframes for User Dashboard",
            "Setup SQL Database for parsed resume storage",
            "Manage Sprint 3 deliverables and client updates",
            "Write automated Selenium tests for login flow",
            "Recruit data annotators for resume dataset"
        ],
        "Priority": ["High", "High", "High", "Medium", "High", "Medium", "High", "Low", "Medium", "Medium"],
        "Result": ["In Progress", "In Progress", "Pending", "Completed", "In Progress", "Completed", "Completed", "Completed", "Pending", "In Progress"],
        "Outcome": [
            "Model accuracy improving, currently at 88%.",
            "Stuttering reduced, testing on low-end devices pending.",
            "Awaiting clean data from HR annotations.",
            "Parsing speed increased by 3x per document.",
            "Auth flow logic written, database connection pending.",
            "Wireframes approved by stakeholders.",
            "Database schemas successfully deployed and tested.",
            "Sprint 3 roadmap clearly defined and aligned.",
            "Test scripts drafted, execution pending.",
            "Sourced 15 potential freelancers for data labeling."
        ]
    }
    
    df = pd.DataFrame(data)
    
    st.markdown(create_task_table(df), unsafe_allow_html=True)