import streamlit as st
import pandas as pd
import datetime

@st.dialog("Intern Profile")
def show_intern_profile(intern):
    st.markdown(f"""
    <div style='text-align: center;'>
        <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='120' style='margin-bottom: 10px;'>
        <h3 style='margin: 0px; color: #000000;'>{intern['Name']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown(f"**Name:**<br>{intern['Name']}", unsafe_allow_html=True)
    st.markdown(f"**College:**<br>{intern['College']}", unsafe_allow_html=True)
    st.markdown(f"**Branch:**<br>{intern['Branch']}", unsafe_allow_html=True)
    st.markdown(f"**Semester:**<br>{intern['Semester']}", unsafe_allow_html=True)
    st.markdown(f"**Skills:**<br>{intern['Skills']}", unsafe_allow_html=True)
    st.markdown(f"**Intern ID:**<br>{intern['Intern ID']}", unsafe_allow_html=True)
    st.markdown(f"**Role:**<br>{intern['Role']}", unsafe_allow_html=True)
    st.markdown(f"**Assigned Project:**<br>{intern['Assigned Project']}", unsafe_allow_html=True)
    st.markdown(f"**Completed Projects:**<br>{intern['Completed Projects']}", unsafe_allow_html=True)
    st.markdown(f"**Mentor:**<br>{intern['Mentor']}", unsafe_allow_html=True)
    st.markdown(f"**Duration:**<br>{intern['Duration']}", unsafe_allow_html=True)
    status_color = "#00b300" if intern['Status'] == 'Active' else "#ff9900"
    st.markdown(f"**Status:**<br><span style='color: {status_color}; font-weight: bold;'>{intern['Status']}</span>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("Close Profile", use_container_width=True):
        if "intern_id" in st.query_params:
            del st.query_params["intern_id"]
        st.rerun()

def create_intern_table(df):
    html_table = """
    <style>
    .intern-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #FFFFFF;
        color: #000000;
        margin-top: 15px;
        margin-bottom: 25px;
    }
    .intern-table th, .intern-table td {
        border: 2px solid #000000;
        padding: 12px;
        text-align: left;
    }
    .intern-table th {
        font-weight: bold;
        font-size: 16px;
        background-color: #F8F9FA;
    }
    .intern-table a {
        color: #0000EE;
        text-decoration: underline;
        font-weight: bold;
        cursor: pointer;
    }
    .intern-table a:hover {
        color: #FF0000;
    }
    </style>
    <table class="intern-table">
        <thead>
            <tr>
                <th>Intern ID</th>
                <th>Name</th>
                <th>Role</th>
                <th>Assigned Project</th>
                <th>Mentor</th>
                <th>Duration</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
    """
    for _, row in df.iterrows():
        name_link = f"<a href='?page=Intern%20Detail&intern_id={row['Intern ID']}' target='_self'>{row['Name']}</a>"
        
        html_table += "<tr>"
        html_table += f"<td>{row['Intern ID']}</td>"
        html_table += f"<td>{name_link}</td>"
        html_table += f"<td>{row['Role']}</td>"
        html_table += f"<td>{row['Assigned Project']}</td>"
        html_table += f"<td>{row['Mentor']}</td>"
        html_table += f"<td>{row['Duration']}</td>"
        
        status_val = row['Status']
        color = "#00b300" if status_val in ['Active', 'Completed'] else "#ff9900"
        html_table += f"<td style='color: {color}; font-weight: bold;'>{status_val}</td>"
        html_table += "</tr>"
        
    html_table += "</tbody></table>"
    return html_table

def create_task_log_table(df):
    html_table = """
    <table class="intern-table">
        <thead>
            <tr>
                <th>Name</th>
                <th>Date</th>
                <th>Day</th>
                <th>Today's Task</th>
                <th>Outcome</th>
                <th>Extra Curriculum</th>
            </tr>
        </thead>
        <tbody>
    """
    for _, row in df.iterrows():
        html_table += "<tr>"
        html_table += f"<td><strong>{row['Name']}</strong></td>"
        html_table += f"<td>{row['Date']}</td>"
        html_table += f"<td>{row['Day']}</td>"
        html_table += f"<td>{row['Task']}</td>"
        html_table += f"<td>{row['Outcome']}</td>"
        html_table += f"<td>{row['Extra Curriculum']}</td>"
        html_table += "</tr>"
        
    html_table += "</tbody></table>"
    return html_table

def create_attendance_table(df):
    html_table = """
    <table class="intern-table">
        <thead>
            <tr>
                <th>Date</th>
                <th>Intern Name</th>
                <th>Check-In Time</th>
                <th>Check-Out Time</th>
                <th>Attendance Status</th>
            </tr>
        </thead>
        <tbody>
    """
    for _, row in df.iterrows():
        html_table += "<tr>"
        html_table += f"<td>{row['Date']}</td>"
        html_table += f"<td><strong>{row['Intern Name']}</strong></td>"
        html_table += f"<td>{row['Check-In']}</td>"
        html_table += f"<td>{row['Check-Out']}</td>"
        
        status_val = row['Status']
        if status_val == 'Present':
            color = "#00b300"
        elif status_val == 'Absent':
            color = "#ff0000"
        elif status_val == 'Working':
            color = "#3498db"
        else:
            color = "#ff9900"
            
        html_table += f"<td style='color: {color}; font-weight: bold;'>{status_val}</td>"
        html_table += "</tr>"
        
    html_table += "</tbody></table>"
    return html_table

def show_intern_page():
    if 'att_logs' not in st.session_state:
        st.session_state.att_logs = []
    
    if 'task_logs' not in st.session_state:
        st.session_state.task_logs = []
        
    if 'camera_active' not in st.session_state:
        st.session_state.camera_active = False

    st.markdown("""
    <style>
    div[data-testid="stTabs"] button[data-baseweb="tab"] {
        font-size: 20px !important;
        padding: 15px 40px !important;
        background-color: #f1f1f1 !important;
        border: 2px solid #cccccc !important;
        border-bottom: none !important;
        border-radius: 8px 8px 0px 0px !important;
        color: #000000 !important;
        margin-right: 5px !important;
    }
    div[data-testid="stTabs"] button[aria-selected="true"] {
        background-color: #cccccc !important;
        font-weight: bold !important;
        border-color: #000000 !important;
    }
    div[data-testid="stRadio"] > div {
        display: flex;
        gap: 20px;
        background-color: #f8f9fa;
        padding: 10px 20px;
        border-radius: 8px;
        border: 1px solid #ddd;
    }
    button[kind="primary"] {
        padding: 15px !important;
        font-size: 20px !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='color: #000000;'>🎓 Intern Management</h1>", unsafe_allow_html=True)
    st.markdown("---")

    intern_data = {
        "Intern ID": ["INT-001", "INT-002", "INT-003"],
        "Name": ["Rahul Sharma", "Priya Desai", "Aman Singh"],
        "Role": ["AI/ML Intern", "Flutter Dev Intern", "Python Backend Intern"],
        "Assigned Project": ["Aquatic Camouflage AI", "AscendHub App", "Resume Parser Analyzer"],
        "Completed Projects": ["Basic Chatbot Module", "Expense Tracker UI", "-"],
        "Mentor": ["Parth Tanve", "Afatab Khan", "Parth Tanve"],
        "Duration": ["01-May-2026 to 31-Jul-2026", "15-May-2026 to 15-Aug-2026", "01-Jun-2026 to 31-Aug-2026"],
        "Status": ["Active", "Active", "Onboarding"],
        "College": ["VNIT Nagpur", "RCOEM Nagpur", "YCCE Nagpur"],
        "Branch": ["Computer Science", "Information Technology", "AI & Data Science"],
        "Semester": ["6th Semester", "8th Semester", "7th Semester"],
        "Skills": ["Python, YOLOv8, TensorFlow", "Dart, Flutter, Firebase", "Python, Django, SQL"]
    }
    df_interns = pd.DataFrame(intern_data)

    if "intern_id" in st.query_params:
        intern_id = st.query_params["intern_id"]
        if intern_id in df_interns["Intern ID"].values:
            selected_intern = df_interns[df_interns["Intern ID"] == intern_id].iloc[0]
            show_intern_profile(selected_intern)

    tab1, tab2 = st.tabs(["Interns Information", "Intern Log"])

    with tab1:
        st.markdown("<h3 style='color: #333;'>🧑‍🎓 Current Interns Details</h3>", unsafe_allow_html=True)
        st.markdown(create_intern_table(df_interns), unsafe_allow_html=True)

    with tab2:
        st.markdown("<h3 style='color: #333; margin-bottom: 5px;'>📝 Logs Overview</h3>", unsafe_allow_html=True)
        
        log_type = st.radio("Select Log View:", ["📅 Attendance Log", "📋 Daily Task Log"], horizontal=True, label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True)

        if log_type == "📅 Attendance Log":
            st.markdown("<h4 style='color: #444;'> Intern Attendance Verification</h4>", unsafe_allow_html=True)
            
            with st.container(border=True):
                st.markdown("**📸 Capture Photo & Mark Attendance**")
                col_n, col_a = st.columns(2)
                with col_n:
                    sel_intern = st.selectbox("Select Intern Name", ["Rahul Sharma", "Priya Desai", "Aman Singh"])
                with col_a:
                    att_action = st.selectbox("Action", ["Check-In", "Check-Out"])
                
                st.markdown("<br>", unsafe_allow_html=True)
                
            
                if not st.session_state.camera_active:
                    if st.button(" TURN ON CAMERA TO VERIFY", use_container_width=True, type="primary"):
                        st.session_state.camera_active = True
                        st.rerun()
                else:
                    if st.button(" Turn Off Camera", use_container_width=True):
                        st.session_state.camera_active = False
                        st.rerun()
                        
                photo = None
                if st.session_state.camera_active:
                    photo = st.camera_input("Take a picture for verification")
                
                if photo:
                    now = datetime.datetime.now()
                    current_time = now.time()
                    
                    
                    checkin_start = datetime.time(9,50)
                    checkin_end = datetime.time(10, 10)
                    checkout_start = datetime.time(17,50)
                    checkout_end = datetime.time(18,30)   
                    
                    is_disabled = False
                    time_msg = ""
                    
                    
                    if att_action == "Check-In":
                        if not (checkin_start <= current_time <= checkin_end):
                            is_disabled = True
                            time_msg = " Check-In is only allowed between 09:50 AM and 10:10 AM."
                    elif att_action == "Check-Out":
                        if not (checkout_start <= current_time <= checkout_end):
                            is_disabled = True
                            time_msg = " Check-Out is only allowed between 05:50 PM and 06:30 PM."
                    
                    
                    if is_disabled:
                        st.warning(time_msg)
                        
                    if st.button(f" Confirm {att_action}", use_container_width=True, disabled=is_disabled):
                        date_str = now.strftime('%d-%b-%Y')
                        time_str = now.strftime('%I:%M %p')
                        
                        record_found = False
                        
                        for record in st.session_state.att_logs:
                            if record['Date'] == date_str and record['Intern Name'] == sel_intern:
                                record_found = True
                                if att_action == "Check-In":
                                    st.warning("You have already Checked-In today!")
                                elif att_action == "Check-Out":
                                    record['Check-Out'] = time_str
                                    record['Status'] = "Present"
                                    st.success(f"Check-Out successful for {sel_intern} at {time_str}")
                                    st.session_state.camera_active = False 
                                    st.rerun()
                                break
                        
                        if not record_found:
                            if att_action == "Check-In":
                                st.session_state.att_logs.insert(0, {
                                    "Date": date_str,
                                    "Intern Name": sel_intern,
                                    "Check-In": time_str,
                                    "Check-Out": "-",
                                    "Status": "Working"
                                })
                                st.success(f"Check-In successful for {sel_intern} at {time_str}")
                                st.session_state.camera_active = False 
                                st.rerun()
                            else:
                                st.warning("Please Check-In first before Checking-Out!")

            st.markdown("<h4 style='color: #444; margin-top: 20px;'>📋 Today's Attendance Records</h4>", unsafe_allow_html=True)
            
            df_att = pd.DataFrame(st.session_state.att_logs)
            if len(df_att) == 0:
                st.markdown("<p style='color: #888; font-size: 16px; padding: 15px; background: #f9f9f9; border-radius: 8px; border: 1px dashed #ccc; text-align: center;'>No attendance records available today.</p>", unsafe_allow_html=True)
            else:
                st.markdown(create_attendance_table(df_att), unsafe_allow_html=True)

        elif log_type == "📋 Daily Task Log":
            st.markdown("<h4 style='color: #444;'>📋 Intern Daily Task Submission</h4>", unsafe_allow_html=True)
            
            now = datetime.datetime.now()
            today_date = now.strftime('%d-%b-%Y')
            today_day = now.strftime('%A')
            
            with st.container(border=True):
                st.markdown("** Submit Your Today's Progress**")
                
                col_name, col_date, col_day = st.columns(3)
                with col_name:
                    intern_name = st.selectbox("Select Name", ["Rahul Sharma", "Priya Desai", "Aman Singh"], key="task_name")
                with col_date:
                    st.text_input("Date", value=today_date, disabled=True)
                with col_day:
                    st.text_input("Day", value=today_day, disabled=True)
                    
                st.markdown("<span style='font-size:14px; color:red;'>* Mandatory Fields</span>", unsafe_allow_html=True)
                task_input = st.text_area("Today's Tasks *", placeholder="Describe the tasks you worked on today...", height=100)
                outcome_input = st.text_area("Outcome *", placeholder="What was the result or outcome of the tasks?", height=100)
                
                extra_input = st.text_area("Extra Curriculum (Optional)", placeholder="Any additional learning, meeting, or activity...", height=80)
                
                if st.button(" Submit Task Log", use_container_width=True, type="primary"):
                    if not task_input.strip() or not outcome_input.strip():
                        st.error("Please fill the mandatory fields (Today's Tasks and Outcome) before submitting.")
                    else:
                        st.session_state.task_logs.insert(0, {
                            "Name": intern_name,
                            "Date": today_date,
                            "Day": today_day,
                            "Task": task_input,
                            "Outcome": outcome_input,
                            "Extra Curriculum": extra_input if extra_input.strip() else "-"
                        })
                        st.success(f"Task log submitted successfully for {intern_name}!")
                        st.rerun()

            st.markdown("<h4 style='color: #444; margin-top: 20px;'>📋 Recent Task Logs</h4>", unsafe_allow_html=True)
            
            df_logs = pd.DataFrame(st.session_state.task_logs)
            
            if len(df_logs) == 0:
                st.markdown("<p style='color: #888; font-size: 16px; padding: 15px; background: #f9f9f9; border-radius: 8px; border: 1px dashed #ccc; text-align: center;'>No daily task logs submitted yet.</p>", unsafe_allow_html=True)
            else:
                st.markdown(create_task_log_table(df_logs), unsafe_allow_html=True)