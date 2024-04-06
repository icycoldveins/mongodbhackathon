# Notes Organizer

## Introduction

This project leverages Nomic Embed and MongoDB to build a state-of-the-art Retrieval Augmented Generation (RAG) system. It's designed to enable powerful, data-driven insights and natural language understanding capabilities. Furthermore, we utilize `watchdog` to monitor and react to changes in our data source files automatically.

## Prerequisites

Before setting up the project, ensure you have the following installed:
- Python 3.6 or later
- MongoDB Atlas account
- Nomic Atlas account

## Setup Instructions

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```
git clone <repository_url>
cd <repository_name>
```

### 2. Create a Virtual Environment

Create a virtual environment named `env` to manage your project's dependencies:

```
python3 -m venv env
```

### 3. Activate the Virtual Environment

Activate the virtual environment:

- On Unix/Linux:
  ```
  source env/bin/activate
  ```

- On Windows:
  ```
  env\Scripts\activate
  ```

### 4. Install Dependencies

Install the project dependencies, including `watchdog`, from the `requirements.txt` file:

```
pip install -r requirements.txt
```

If `requirements.txt` does not exist, install the dependencies manually:

```
pip install nomic pymongo[srv] requests tqdm watchdog
```

### 5. Set Up MongoDB

Ensure your MongoDB Atlas account is set up and note your connection string. This string is crucial for connecting your application to MongoDB.

### 6. Configure Nomic and MongoDB in the Project

- Retrieve your Nomic API key following the instructions on Nomic Atlas.
- Update the project configuration files or environment variables with your MongoDB connection string and Nomic API key.

### 7. Launch the Project

With everything set up, you can now run your project:

```
python <main_project_file>.py
```

## Additional Information

For more details on configuring MongoDB Atlas or Nomic, refer to the respective documentation:

- [MongoDB Atlas Documentation](https://docs.atlas.mongodb.com/)
- [Nomic Documentation](https://nomic.ai/docs)

---

Feel free to customize the README based on the specific requirements and structure of your project.