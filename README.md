# Naukri Resume Automation (Local Script)

This repository provides a **working Python script** to automatically refresh your resume on [Naukri.com](https://www.naukri.com).  
Unlike GitHub Actions (which gets blocked), this script runs perfectly on your **local machine**.

---

## ✨ Features
- Logs into your Naukri account with email + password.
- Navigates to the profile page.
- Uploads the latest resume PDF.
- Captures screenshots (`after_login.png`, `error.png`) for debugging.

---

## 📦 Requirements
- [Python 3.8+](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (must match your Chrome version)
- Install dependencies:
  ```bash
  pip install selenium
  ```

---

## 🚀 Usage
-Edit refresh_resume.py with your details:
```
-NAUKRI_EMAIL = "user@gmail.com"
-NAUKRI_PASSWORD = "password"
-RESUME_PATH = r"C:\path\to\resume.pdf"
```
Run the script:
```
python refresh_resume.py
```

Check screenshots:

after_login.png → confirms login worked

error.png → shows what went wrong (if any)

--

##⏰ Automating Daily Run
On Windows
```
-Open Task Scheduler
-Create a new task
-Trigger: Daily (choose time)
-Action: Run python refresh_resume.py
```
On Linux/macOS

Use cron:
```
0 10 * * * /usr/bin/python3 /path/to/refresh_resume.py
```

This will refresh your resume every day at 10 AM.

---
