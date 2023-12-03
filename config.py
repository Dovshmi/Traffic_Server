import streamlit as st
import os
import sys
# Created by Dovshmi V2
# Function to list all files in the given directory

def list_files_in_directory(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Function to create a download button for the specified file
def download_file(file_path, file_name):
    with open(file_path, "rb") as file:
        file_content = file.read()

    # Extract file extension from the file name
    file_extension = os.path.splitext(file_name)[1].lower()

    # Provide file extension when creating the download button
    st.download_button(label=f"Download {file_name}", data=file_content, key=file_name, file_name=f"{file_name}{file_extension}")


# Function to format file size to a human-readable format
def format_file_size(file_size):
    if file_size < 1024:
        return f"{file_size} B"
    elif file_size < 1024 ** 2:
        return f"{file_size / 1024:.2f} KB"
    elif file_size < 1024 ** 3:
        return f"{file_size / (1024 ** 2):.2f} MB"
    else:
        return f"{file_size / (1024 ** 3):.2f} GB"

# Function to authenticate the user with the provided password
def authenticate_user(entered_password, stored_password):
    return entered_password == stored_password

def main(password):
   
    st.title("Local Downloader by Dovshmi")
    st.text('Don\'t be scared... just pick one')
    massage=sys.argv[3]
    if massage =="None" or "":
        st.toast('Safe Downloading 💯')
    else:
        massage= massage.replace("_", " ")
        st.toast(massage)
    # Get the current directory
    current_directory = os.getcwd()
    directory = sys.argv[2]
    # List all files in the current directory
    files = list_files_in_directory(directory)

    # Display the files as download buttons
    for file in files:
        file_path = os.path.join(directory, file)
        file_size = os.path.getsize(file_path) // 1024  # File size in KB

        # Create a download button for each file
        download_file(file_path, file)

        # Display file information
        st.write(f"{file} ({format_file_size(file_size)})")

    # File uploader widget
    uploaded_file = st.file_uploader("Upload a file")
    
    # Display information about the uploaded file
    if uploaded_file is not None:
        st.info(f"Uploaded file: {uploaded_file.name} ({len(uploaded_file.getvalue()) // 1024} KB)")

if __name__ == "__main__":
    site_password = sys.argv[1]
    # Authenticate the user
    entered_password = st.text_input("Enter the site password:", type="password")
    if  entered_password == "":
        sys.exit(1)
    elif not authenticate_user(entered_password, site_password):
        t=st.error("Authentication failed. Exiting...")
        sys.exit(1)
    main(site_password)
    