import streamlit as st
import pandas as pd
import base64
import os

def get_image_html(image_name, platform_name):
    if os.path.exists(image_name):
        with open(image_name, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read()).decode()
        return f'<img src="data:image/png;base64,{encoded_string}" width="20" style="vertical-align: middle; margin-right: 8px;"> {platform_name}'
    else:
        return f'{platform_name}'

def create_lead_table(df):
    html_table = """
    <style>
    .lead-table {
        width: 100%;
        border-collapse: collapse;
        background-color: #FFFFFF;
        color: #000000;
        margin-top: 15px;
    }
    .lead-table th, .lead-table td {
        border: 2px solid #000000;
        padding: 12px;
        text-align: left;
    }
    .lead-table th {
        font-weight: bold;
        font-size: 16px;
        background-color: #F8F9FA;
    }
    </style>
    <table class="lead-table">
        <thead>
            <tr>
                <th>Lead Name</th>
                <th>Platform</th>
                <th>Purpose</th>
                <th>Lead Type</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for _, row in df.iterrows():
        lead_color = "#000000"
        if row['Lead Type'] == 'Hot':
            lead_color = "#ff0000"
        elif row['Lead Type'] == 'Warm':
            lead_color = "#ff9900"
        elif row['Lead Type'] == 'Cold':
            lead_color = "#0000EE"
        elif row['Lead Type'] == 'Not Connected':
            lead_color = "#888888"

        html_table += "<tr>"
        html_table += f"<td><strong>{row['Lead Name']}</strong></td>"
        html_table += f"<td>{row['Platform']}</td>"
        html_table += f"<td>{row['Purpose']}</td>"
        html_table += f"<td style='color: {lead_color}; font-weight: bold;'>{row['Lead Type']}</td>"
        html_table += "</tr>"
        
    html_table += "</tbody></table>"
    return html_table

def show_lead_page():
    st.markdown("<h1 style='color: #000000;'>🎯 Leads Detail</h1>", unsafe_allow_html=True)
    st.markdown("---")

    data = {
        "Lead Name": [
            "Rahul Sharma", 
            "Priya Singh", 
            "Amit Kumar", 
            "Sneha Gupta", 
            "Vikram Desai",
            "Kavita Reddy",
            "Nitin Bajaj"
        ],
        "Platform": [
            get_image_html("linkedin.png", "LinkedIn"), 
            get_image_html("whatsapp.png", "WhatsApp"),
            get_image_html("facebook.png", "Facebook"),
            get_image_html("social.png", "Instagram"),
            get_image_html("email.png", "Email"),
            get_image_html("linkedin.png", "LinkedIn"), 
            get_image_html("coldcall.png", "cold call")
        ],
        "Purpose": [
            "Inquiry for Flutter Mobile App Development", 
            "Needs YOLOv8 AI Model for Object Detection", 
            "Wants Gemini AI Chatbot Integration for Website", 
            "Looking for a Resume Parser API for their HR Portal",
            "CRM Dashboard Customization Requirement",
            "General AI/ML Consulting for Startup",
            "Maintenance contract for legacy Python app"
        ],
        "Lead Type": ["Hot", "Warm", "Cold", "Not Connected", "Hot", "Warm", "Not Connected"]
    }
    
    df = pd.DataFrame(data)
    
    st.markdown(create_lead_table(df), unsafe_allow_html=True)