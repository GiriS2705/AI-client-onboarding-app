import streamlit as st
import os
from db import insert_client, get_clients, update_status
from email_utils import send_email
from ocr_utils import extract_text
from ai_validation import validate_document

st.set_page_config(page_title="Client Onboarding")

st.title("📋 Client Onboarding System")

menu = ["Add Client", "Upload Documents", "View Clients"]
choice = st.sidebar.selectbox("Menu", menu)

# -------------------------------
# 1. ADD CLIENT
# -------------------------------
if choice == "Add Client":
    st.header("Add New Client")

    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    if st.button("Submit"):
        insert_client(name, email, phone)
        send_email(email)
        st.success("Client added & email sent!")

# -------------------------------
# 2. UPLOAD DOCUMENTS
# -------------------------------
elif choice == "Upload Documents":
    st.header("Upload Documents")

    client_id = st.number_input("Client ID", step=1)

    passport = st.file_uploader("Upload Passport")
    license = st.file_uploader("Upload Driving License")

    if st.button("Process Documents"):
        os.makedirs("uploads", exist_ok=True)

        passport_path = f"uploads/passport_{client_id}.png"
        license_path = f"uploads/license_{client_id}.png"

        with open(passport_path, "wb") as f:
            f.write(passport.getbuffer())

        with open(license_path, "wb") as f:
            f.write(license.getbuffer())

        # OCR
        text1 = extract_text(passport_path)
        text2 = extract_text(license_path)

        st.subheader("Extracted Text")
        st.text(text1[:500])
        st.text(text2[:500])

        # AI Validation
        result = validate_document(text1 + text2)

        st.subheader("Validation Result")
        st.write(result)

        update_status(client_id, "Verified")

# -------------------------------
# 3. VIEW CLIENTS
# -------------------------------
elif choice == "View Clients":
    st.header("All Clients")

    data = get_clients()
    for row in data:
        st.write(row)