# 🔐 SecurePass Vault

**SecurePass Vault** is a Python-based cybersecurity application that combines **password security analysis**, **breach detection**, and a **fully encrypted password vault** with a modern **GUI interface**.

The project demonstrates practical understanding of:
- Cybersecurity fundamentals  
- Encryption & authentication  
- Secure storage practices  
- Modular Python application design  
- GUI-based application development  

---

## 🚀 Features

### 🔑 Password Security Tools
- **Password Strength Checker**
  - Scores passwords using length, character diversity, and entropy
  - Provides actionable feedback
- **Secure Password Generator**
  - Customizable length and character sets
- **Password Breach Checker**
  - Checks passwords against known breach datasets (K-Anonymity based logic)

### 🛡️ Encrypted Password Vault
- **Master Password Protection**
  - Master password securely hashed using **bcrypt**
- **AES / Fernet Encryption**
  - All stored credentials are encrypted at rest
- **Vault Operations**
  - Add new credentials
  - View stored credentials (decrypted only after authentication)
- **Secure by Design**
  - Vault data files are excluded from version control using `.gitignore`

### 🖥️ GUI Application
- Built using **Flet**
- Multi-screen navigation
- Single-window integrated workflow
- Clean, modern UI suitable for demonstrations

---

## 🧱 Project Architecture
SecurePass-Vault/
│
├── data/ # Encrypted vault data (ignored by git)
├── src/
│ ├── api/ # Breach checking logic
│ ├── crypto_engine/ # Encryption, vault, auth logic
│ ├── gui/ # GUI application (Flet)
│ │ ├── screens/ # Individual GUI screens
│ │ └── app.py # GUI entry point
│ ├── utils/ # Entropy & validation helpers
│ ├── password_checker.py
│ └── password_generator.py
│
├── tests/ # Basic test cases
├── requirements.txt
└── README.md


This follows a **real-world `src/` based Python package structure**, commonly used in production applications.

---

## ⚙️ Technologies Used

- **Python 3.12**
- **Flet** – GUI framework
- **bcrypt** – Secure password hashing
- **cryptography (Fernet/AES)** – Encryption
- **Git & GitHub** – Version control
- **Virtual Environment (venv)**

---

## ▶️ How to Run the Project

1️⃣ Clone the repository 
git clone https://github.com/shadowcoder441/SecurePass-Vault.git
cd SecurePass-Vault

2️⃣ Create & activate virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the GUI application
python -m src.gui.app

** Important **:
This project uses a package-based structure.
Always run using python -m src.gui.app from the project root.

`**Project Versions:**```

`**Version 1**`
Password strength checker
Password generator
CLI-based functionality
`
**Version 2 (Current)**`
Encrypted password vault
Master password authentication
Breach detection
Full GUI integration
Modular architecture

**Security Considerations**
Master passwords are never stored in plaintext
All credentials are encrypted before storage
Vault data files are excluded from version control
Encryption keys are derived securely at runtime

**Learning Outcomes**

`This project helped reinforce:.`

Secure password handling
Encryption & hashing concepts
Real-world Python project structuring
GUI-based application development
Debugging complex import & packaging issues
Version-controlled incremental development
