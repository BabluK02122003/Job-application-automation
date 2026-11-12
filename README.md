# Job Application Automation 

An automated job application project developed using **Python and Selenium WebDriver** to simplify the job application process on Shine.com.

The project automates browser interactions, including website navigation, user login, job searching, job selection, applying for a job, and checking application status.

##  Features

- Automated browser initialization using Selenium WebDriver.
- Automatic navigation to Shine.com.
- Automated login using user credentials.
- Navigation to a specified job search page.
- Automatic extraction and selection of job listings.
- Automated interaction with job application buttons.
- Application status verification.
- Automatic screenshots at different stages of execution.
- Explicit waits for reliable browser interactions.

##  Technologies Used

- Python
- Selenium WebDriver
- Google Chrome
- ChromeDriver
- Web Automation

##  Project Structure

```text
shine-job-application-automation/
│
├── shine_job_apply.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    └── (Optional execution screenshots)
```

##  Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/BabluK02122003/Job-application-automation.git
```

### 2. Navigate to the Project Directory

```bash
cd Job-application-automation
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure ChromeDriver

Install Google Chrome and configure a compatible ChromeDriver, or use Selenium Manager to manage the driver automatically.

### 5. Configure Login Credentials

Store your Shine.com login credentials securely using environment variables. Never hardcode passwords in the source code.

### 6. Run the Automation

```bash
python shine_job_apply.py
```

##  Workflow

1. Launch the Chrome browser.
2. Open Shine.com.
3. Navigate to the login page.
4. Enter login credentials.
5. Open the specified job search page.
6. Identify available job listings.
7. Select a job listing.
8. Navigate to the job details page.
9. Locate and click the Apply button.
10. Check whether the application status is displayed.
11. Capture screenshots for execution tracking.
12. Close the browser.

##  Screenshots

Execution screenshots can be added here to demonstrate the automation workflow.

##  Project Objective

The primary objective of this project is to reduce repetitive manual activities involved in online job applications through browser automation.

It demonstrates practical implementation of Selenium WebDriver, dynamic web element handling, browser interaction, explicit waits, and automation workflows.

##  Future Enhancements

- Automate job filtering based on skills and experience.
- Support multiple job listings.
- Add automated resume selection and uploading.
- Implement error handling and logging.
- Generate application reports.
- Develop a configurable dashboard.
- Extend automation to additional job portals.

##  Disclaimer

This project is developed for educational and automation practice purposes. Use it responsibly and comply with Shine.com's terms of service and applicable website policies. Review job details and application information before submitting applications.

##  Author

**Durga Prasad**

GitHub: https://github.com/BabluK02122003
