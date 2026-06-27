# 🚦 Traffic_Server — Local Streamlit File Server

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-File_Server-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/Tkinter-Folder_Picker-2563EB?style=for-the-badge" alt="Tkinter" />
  <img src="https://img.shields.io/badge/PyInstaller-EXE_Build-0F172A?style=for-the-badge" alt="PyInstaller" />
  <img src="https://img.shields.io/badge/Local_Network-File_Sharing-16A34A?style=for-the-badge" alt="Local Network" />
  <img src="https://img.shields.io/badge/License-Not_Specified-6B7280?style=for-the-badge" alt="License Not Specified" />
</div>

<div align="center">
  <p><strong>A small Python + Streamlit utility for quickly exposing a selected local folder through a browser-based file download interface.</strong></p>
</div>

---

## Overview

**Traffic_Server** is a lightweight local file server starter. It asks for a server password, optional upload-size limit, port number, a user-facing message, and a folder to serve. It then launches a Streamlit app that lists files from the selected folder and provides download buttons in the browser.

The project is useful when you want a quick temporary file-sharing page on a trusted local network without setting up a full web server such as Apache, Nginx, or a custom Flask/FastAPI application.

> **Important:** This project is best treated as a local/trusted-network tool. Do not expose it directly to the public internet without adding stronger authentication, transport security, upload handling, and access controls.

---

## Core Features

- **Folder picker:** uses Tkinter to let you choose the directory that will be served.
- **Streamlit interface:** opens a simple browser UI for listing and downloading files.
- **Password gate:** asks visitors for the password before showing the file list.
- **Custom port selection:** includes common port presets and a custom-port fallback.
- **Upload-size configuration:** passes a max upload size to Streamlit when launching the app.
- **Optional server message:** lets you display a short message/toast to visitors.
- **Executable-friendly workflow:** can be packaged with PyInstaller for easier use on a desktop machine.

---

## Current Project Behavior

This repository contains two main Python files:

| File | Purpose |
| :--- | :--- |
| `Server_starter.py` | CLI/Tkinter launcher that collects settings and starts Streamlit. |
| `config.py` | Streamlit app that authenticates the user and displays files from the selected directory. |

Current implementation details:

- Downloads are supported through Streamlit download buttons.
- Password protection is a simple plaintext comparison passed from the starter script.
- The upload widget is present in the UI, but uploaded files are not currently saved back into the selected folder.
- The selected folder path, password, and message are passed to `config.py` as command-line arguments.

---

## Tech Stack

| Area | Technology |
| :--- | :--- |
| Language | Python 3.x |
| Web UI | Streamlit |
| Folder Selection | Tkinter |
| File Operations | Python `os` module |
| Packaging | PyInstaller |
| Main Entry Point | `Server_starter.py` |
| Streamlit App | `config.py` |

---

## Repository Structure

```text
Traffic_Server/
├── Server_starter.py       # Starts the local file server setup flow
├── config.py               # Streamlit file-browser app
└── README.md               # Project documentation
```

---

## Requirements

Install Python 3 first, then install the required packages:

```bash
pip install streamlit pyinstaller
```

Tkinter is usually included with standard Python installations on Windows. On some Linux systems, it may need to be installed separately through the system package manager.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Dovshmi/Traffic_Server.git
cd Traffic_Server
```

### 2. Install dependencies

```bash
pip install streamlit pyinstaller
```

### 3. Start the server launcher

```bash
python Server_starter.py
```

The launcher will ask you to:

1. set a server password;
2. choose whether to enable upload-size configuration;
3. choose or enter a max upload size;
4. add an optional message for visitors;
5. choose a port;
6. select the local folder to serve.

After that, it starts Streamlit with your selected settings.

---

## Manual Streamlit Usage

You can also start the Streamlit app directly if you pass the required arguments manually:

```bash
streamlit run --server.maxUploadSize 1024 --server.port 8051 config.py YOUR_PASSWORD "C:\\Path\\To\\Folder" "Safe_Downloading"
```

Argument order:

```text
config.py <password> <directory> <message>
```

Use underscores in the message if you want to avoid shell quoting issues.

---

## Build a Standalone Executable

You can package the launcher with PyInstaller:

```bash
pyinstaller --onefile Server_starter.py
```

After the build finishes, the executable will be created inside:

```text
dist/
```

The Streamlit app file is still required at runtime. Keep `config.py` available next to the executable or in the working directory used to launch it.

---

## Usage Flow

```text
Run Server_starter.py
        ↓
Set password and server options
        ↓
Select the folder to expose
        ↓
Streamlit starts on the selected port
        ↓
Visitor opens the local server URL
        ↓
Visitor enters the password
        ↓
Files are listed with download buttons
```

---

## Security Notes

This tool is intentionally simple. Before using it outside a trusted local network, consider these upgrades:

- replace plaintext password comparison with a stronger authentication flow;
- do not pass sensitive passwords through command-line arguments;
- add HTTPS or place the app behind a trusted reverse proxy;
- save uploaded files only after validating filename, size, and type;
- restrict access by IP or network where possible;
- avoid serving folders that contain private or system files;
- add logging and safer error handling.

---

## Known Limitations

- Uploads are not currently persisted to disk.
- Authentication is basic and intended only for casual/local use.
- There is no built-in HTTPS support.
- There is no formal configuration file yet.
- File-size display may need review for exact byte/KB formatting.
- The app is not designed as a production-grade file-sharing platform.

---

## Roadmap Ideas

- Add a `requirements.txt` file.
- Add a real upload-save workflow with filename sanitization.
- Add hashed password support.
- Add a clean config file instead of command-line argument passing.
- Add clearer browser startup instructions after launch.
- Add tests for path handling and authentication behavior.
- Add an optional Docker setup.
- Add a formal open-source license file.

---

## License

No formal `LICENSE` file is currently included in this repository. Add a license file before encouraging reuse, modification, or redistribution by others.

---

## Author

Created by **Dovshmi**.

GitHub: [@Dovshmi](https://github.com/Dovshmi)
