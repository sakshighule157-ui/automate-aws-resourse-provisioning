# 🚀 AWS Resource Automation using Python (Boto3)

## 📌 Project Overview

This project demonstrates **Infrastructure Automation on AWS using Python (Boto3)**.
It eliminates manual AWS Console operations and enables provisioning of cloud resources using code.

The project automates core AWS services like:

* EC2 (Virtual Machines)
* S3 (Storage Buckets)
* IAM (Access Management)

---

## 🎯 Key Features

* 🖥️ Launch EC2 instances programmatically
* 🪣 Create and manage S3 buckets
* 📂 Upload files to S3 using Python
* 🔐 Secure authentication using IAM credentials
* ⚙️ Fully automated cloud provisioning (no manual clicks)

---

## 🧰 Tech Stack

* Python 🐍
* Boto3 (AWS SDK for Python)
* AWS EC2
* AWS S3
* AWS IAM
* AWS CLI

---

## 📁 Project Structure

```
aws-automation-boto3-project/
│
├── ec2_script.py          # Launch EC2 instance
├── s3_upload.py           # Create bucket & upload file
├── iam_setup.py           # IAM user/role setup (optional)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Prerequisites

Before running this project, ensure you have:

* AWS account
* IAM user with programmatic access
* AWS CLI installed and configured
* Python 3.x installed

---

## 🔧 Installation Steps

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/aws-automation-boto3-project.git
cd aws-automation-boto3-project
```

### 2️⃣ Install Dependencies

```bash
pip install boto3
```

### 3️⃣ Configure AWS Credentials

```bash
aws configure
```

Enter:

* Access Key ID
* Secret Access Key
* Region (e.g., ap-south-1)
* Output format (json)

---

## 🚀 How to Run

### ▶️ Run EC2 Automation

```bash
python ec2_script.py
```

### ▶️ Run S3 Automation

```bash
python s3_upload.py
```

---

## 📤 Example Output

### EC2 Launch Output:

```
EC2 Instance launched: i-0a1b2c3d4e5f67890
```

### S3 Upload Output:

```
S3 Bucket created: my-automation-bucket
File uploaded successfully!
```

---

## 📊 AWS Architecture Flow

```
Python Script (Boto3)
        ↓
AWS API Calls
        ↓
EC2 Instance / S3 Bucket Created
        ↓
Resources Available in AWS Console
```

---

## 🔐 Security Best Practices

* Use IAM roles instead of hardcoding credentials
* Avoid using root account
* Store secrets securely (env variables / AWS Secrets Manager)
* Follow least privilege access policy

---

## 📈 Future Improvements

* Add Terraform support (Infrastructure as Code)
* Add CI/CD using GitHub Actions
* Add CloudWatch monitoring
* Add auto-scaling EC2 automation
* Deploy Flask dashboard for AWS control panel

---

## 👨‍💻 Author

**sakshi ghule**
Aspiring Data Analyst / Cloud & DevOps Enthusiast

---

## ⭐ If you like this project

Give a ⭐ to the repository and support learning journey 🚀# automate-aws-resourse-provisioning
