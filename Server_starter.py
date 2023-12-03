import os
import tkinter
from tkinter import filedialog
from datetime import datetime
# Created by Dovshmi V2
# Function to display the current date and time with the Welcome screen
def show_current_date_time():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%A, %B %d, %Y %I:%M %p")
    print("\n")
    print("Welcome To The Local Server Starter" + "       " + formatted_datetime)
    print("............................................................................\n")

# Initialize the Tkinter root window and hide it
root = tkinter.Tk()
root.withdraw()

# Function to get the upload size from the user
def get_upload_size():
    print("Choose upload size:\n")
    print("1. 512 MB")
    print("2. 1024 MB")
    print("3. 2048 MB")
    print("4. 4096 MB")
    print("5. 12000 MB")
    print("")
    # Take user input for upload size choice
    choice = input("Enter the number corresponding to your choice (or press Enter for default): ")

    # Dictionary to map user choices to upload sizes
    switch = {
        '1': 512,
        '2': 1024,
        '3': 2048,
        '4': 4096,
        '5': 12000,
    }

    # Return the selected upload size or default if the choice is not in the dictionary
    return switch.get(choice, None)

# Function to get the port number from the user
def get_port_number():
    print("Choose Server Host Port:\n")
    print("1. Port 80")
    print("2. Port 8080")
    print("3. Port 443")
    print("4. port 8051")
    print("")
    # Take user input for port number choice
    choice = input("Enter the number corresponding to your choice (or press Enter for default): ")

    # Dictionary to map user choices to port numbers
    switch = {
        '1': 80,
        '2': 8080,
        '3': 443,
        '4': 8051,
    }

    # Return the selected port number or default if the choice is not in the dictionary
    return switch.get(choice, None)

# Display the current date and time
show_current_date_time()

# Set the server password
passwd = input("Set The Server Password: ")
print("")

# Ask user whether to enable the upload feature
toupload = input("Do you Want Yo Enable The Upload Feature? (Y/N): ")
print("")

# Use a boolean flag to control the loop
answer = True
while answer:
    # Check user input for upload feature
    if toupload.lower() == "y":
        # Call the function to get upload size
        uploadsize = get_upload_size() or input("Enter Your Custom Upload Size: ")
        # Check if the user entered an empty string or space, set default if so
        if uploadsize == "" or uploadsize == " ":
            uploadsize = 1024
        answer = False
    elif toupload.lower() == "n":
        print("The Upload Feature Is Disabled...")
        uploadsize = 0
        answer = False
    else:
        print("Please Type Again Your Answer")
        toupload = input("(Y/N): ")

print("")

# Ask user for a server message
massage = input("Enter a Server Message To The User (Press Enter For None): ")
print("")

# Check if the message is empty, replace spaces with underscores
if massage == "":
    massage = "None"
else:
    massage.replace(" ", "_")

# Call the function to get port number or ask user for a custom port
port = get_port_number() or input("Enter The Custom Port Number: ")
# Check if the port is empty or 0, set default if so
if port == "" or port == " " or port == 0:
    print("Enabling Default Port (8051)")
    port = 8051

# Get the current directory
currdir = os.getcwd()

# Ask user to select the server file folder
directory = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please Select the Server File Folder')

# Specify the script path
script_path = r"config.py"

# Print information about the selected directory
print("\nOpening " + str(directory) + " as the Local Server")
print("")

# Build the command to start the server
command = f"streamlit run --server.maxUploadSize {uploadsize} --server.port {port} {script_path} {passwd} {directory} {massage}"

# Execute the command to start the server
os.system(command)
