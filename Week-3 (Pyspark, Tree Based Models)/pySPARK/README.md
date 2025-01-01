# PySpark Installation Guide for Windows and macOS

This section provides a detailed guide to installing PySpark on **Windows** and **macOS**. Follow the steps carefully to set up a working environment for PySpark.

---

## Windows Installation Guide

1. **Install Java**

   - Download and install the latest version of Java Development Kit (JDK) from [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html) or [OpenJDK](https://openjdk.org/).
   - Set the `JAVA_HOME` environment variable:
     - Right-click on "This PC" or "My Computer" > **Properties** > **Advanced System Settings**.
     - Under **System Variables**, click **New** or **Edit**.
     - Add the path to the `bin` folder of your JDK installation (e.g., `C:\Program Files\Java\jdk-17.0.1\bin`).

2. **Install Hadoop for Spark Compatibility**

   - Download the pre-built Hadoop binaries from [WinUtils](https://github.com/steveloughran/winutils) and extract them.
   - Set the `HADOOP_HOME` environment variable to point to the folder where you extracted Hadoop.

3. **Install PySpark**

   - Open a terminal or command prompt.
   - Install PySpark using pip:
     ```bash
     pip install pyspark
     ```

4. **Verify Installation**

   - Open a Python terminal or an IDE.
   - Run the following:
     ```python
     from pyspark.sql import SparkSession
     spark = SparkSession.builder.appName("TestApp").getOrCreate()
     print(spark.version)
     ```

5. **Optional: Add PySpark to PATH**
   - Add the path to PySpark binaries (e.g., `C:\path\to\pyspark\bin`) in your system environment variables for direct access from the command line.

---

## macOS Installation Guide (Using Homebrew)

1. **Install Java**

   - Install OpenJDK using Homebrew:
     ```bash
     brew install openjdk
     ```
   - Add Java to your environment:
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home)
     echo 'export JAVA_HOME=$(/usr/libexec/java_home)' >> ~/.zshrc
     source ~/.zshrc
     ```

2. **Install Hadoop**

   - Install Hadoop via Homebrew:
     ```bash
     brew install hadoop
     ```
   - Add Hadoop to your environment:
     ```bash
     export HADOOP_HOME=/usr/local/Cellar/hadoop/<version>
     export PATH=$HADOOP_HOME/bin:$PATH
     echo 'export HADOOP_HOME=/usr/local/Cellar/hadoop/<version>' >> ~/.zshrc
     echo 'export PATH=$HADOOP_HOME/bin:$PATH' >> ~/.zshrc
     source ~/.zshrc
     ```

3. **Install PySpark**

   - Use pip to install PySpark:
     ```bash
     pip install pyspark
     ```

4. **Verify Installation**
   - Open a Python terminal and verify using:
     ```python
     from pyspark.sql import SparkSession
     spark = SparkSession.builder.appName("TestApp").getOrCreate()
     print(spark.version)
     ```

---

### Notes

- Ensure `pip` is installed and updated on your system before proceeding.
- If you encounter any issues, confirm that `JAVA_HOME`, `HADOOP_HOME`, and `PATH` variables are correctly set.
- For macOS users, always ensure you are using the latest version of Homebrew with:
  ```bash
  brew update
  ```

## Project Prerequisites

1. Create a new virtual environment; as I have conda installed, I used the specific commands.

   Created a virtual environment here i named it pyspark_env

   ```bash
     conda create --name pyspark_env  python=3.10 -y
   ```

   To see the virual environment list on the system.

   ```bash
      conda env list
   ```

   To run the virtual environment:

   ```bash
     conda activate pyspark_env
   ```

   To deactivate the environment:

   ```bash
   conda deactivate
   ```

2. Get the necessary libraries in the kernel; _do this in cmd prompt or powershell, vs code terminal for conda acts weird_ .

   ```python
     pip install -r requirements.txt
   ```

3. Alternative[Incase issues with Pyspark configuration]
   - Use Google Colab to skip all the steps, and avoid Spark related issues.
   - Need to configure drive and dataset link though.
     -"/content/drive/My Drive/{remaining path to the dataset}"

## Usage

1. Ensure you have PySpark installed and configured.
2. Run the script in a Google Colab environment(<b>preferred to avoid Spark Related issues</b>) or a Jupyter notebook.
3. Make sure the dataset files are accessible in the specified paths.
4. Execute the code cells sequentially to perform the desired operations.
   <br><br>

# PySpark Data Exploration and Transformation

This project demonstrates basic PySpark operations for data exploration, transformation, and analysis using a sample order and customer dataset.

## Description

The script performs the following operations:

- Reading data from CSV files into PySpark DataFrames.
- Exploring the data schema, data types, and descriptive statistics.
- Handling missing values using various techniques like dropping, filling, and imputation.
- Applying filter operations to select specific rows based on conditions.
- Performing group-by aggregations to calculate summary statistics.
- Joining two DataFrames based on a common key (customer_id).
- Manipulating date columns to convert string dates to proper date data types.

## Datasets Used

- **pyspark_order_table_modified.csv:** Contains order data with customer and product information.
- **pyspark_customer_table.csv:** Contains customer information.

## Operations Carried Out

1. **Data Loading:** Reading CSV files into PySpark DataFrames.
2. **Data Exploration:** Examining data schema, data types, and descriptive statistics.
3. **Missing Value Handling:** Dropping, filling, and imputing missing values.
4. **Filter Operations:** Selecting specific rows using where and filter clauses.
5. **Group-by Aggregations:** Calculating summary statistics using groupBy and aggregation functions.
6. **Join Operations:** Joining DataFrames using inner, left, right, and outer joins.
7. **Date Manipulation:** Converting string dates to proper date data types.

## Folder Structure

```
└── root
├── datasets
│ ├── pyspark_order_table_modified.csv
│ ├── pyspark_customer_table.csv
| └── pyspark_order_table.csv
├── Code
|  └── pySpark.ipynb
├── prompts.md
├── README.md
└── requirements.txt
└── PySpark.pdf
└── sqljoins.png
```
