# 💰 Finance Tracker CLI

A lightweight, terminal-based personal finance tracker built with Python. Manage your expenses, incomes, and financial balance directly from your command line with ease and persistence.

---

## ✨ Features

- **Add Transactions:** Log expenses and incomes with description, category, and amounts.
- **Interactive Menu:** Intuitive CLI menu with error handling for smooth navigation.
- **Transaction History:** List all registered transactions in a clean, organized format.
- **Balance & Summary:** Quickly inspect total revenues, expenses, and net balance.
- **Data Persistence:** Automatically saves your transactions locally in `JSON` format so your records are never lost.

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- [Python 3.10+](https://www.python.org/downloads/) installed on your machine.
- [Git](https://git-scm.com/) installed.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TfMarra5/finance-tracker-cli.git
   cd finance-tracker-cli
   ```

2. **Create and activate a virtual environment:**
   - **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   - **Linux / macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python main.py
   ```

---

## 🛠️ Built With

- **Python 3** - Core programming language.
- **JSON** - Lightweight data interchange format used for local storage.
- **Rich** *(optional/planned)* - Terminal formatting and styled tables.

---

## 📌 Project Structure

```text
finance-tracker-cli/
├── .gitignore          # Files and directories ignored by Git
├── README.md           # Project documentation and guide
├── requirements.txt    # Project dependencies
└── main.py             # Main application entry point and logic
```

---

## 🎯 Next Steps / Roadmap

- [ ] Export transactions to CSV format.
- [ ] Add category-based expense filtering.
- [ ] Monthly budgeting limits with warning thresholds.
- [ ] Visual charts in terminal using `rich` or `asciichartpy`.

---

## 👨‍💻 Author

Developed by **[TfMarra5](https://github.com/TfMarra5)**.

Feel free to open an issue or submit a pull request if you want to contribute!
