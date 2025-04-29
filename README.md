# ![Digital Futures Academy](https://github.com/digital-futures-academy/DataScienceMasterResources/blob/main/Resources/datascience-notebook-header.png?raw=true)

## Streamlit Workshop

This hands-on workshop is to guide new data engineers through building their first interactive dashboard using Streamlit. The goal is for data engineers to understand the basics of Streamlit, load and explore a demo dataset, create key metrics and visualisations, and build an interactive dashboard from scratch.

---
---

## Learner Stories

```txt
As a Data Engineer,  
I want to understand what Streamlit is and why it’s used for dashboards,  
so that I can choose the right tools for building data-driven applications.

As a Data Engineer,  
I want to set up a Streamlit environment on my machine,  
so that I am ready to develop and run Streamlit applications.

As a Data Engineer,  
I want to load, explore, and clean a demo dataset,  
so that I can prepare high-quality data for analysis and visualisation.

As a Data Engineer,  
I want to create basic metrics and visualisations from my dataset,  
so that I can extract and communicate key insights effectively.

As a Data Engineer,  
I want to add interactivity (such as filters and selectors) to my dashboard,  
so that users can explore the data dynamically and gain deeper insights.

As a Data Engineer,  
I want to build and run an interactive dashboard using Streamlit,  
so that I can present data insights in a user-friendly way.


As a Data Engineer,  
I want to discuss best practices and identify next steps for developing dashboards,  
so that I can continue to improve my skills and deliver robust solutions.
```

---
---

## Workshop Breakdown

- **1. Introduction to Dashboards & Streamlit**
- **2. Environment Setup & Streamlit Basics**
- **3. Loading and Exploring the Demo Dataset**
- **4. Creating Key Metrics & Visualisations**
- **5. Building Interactivity**
- **6. Hands-on Mini Project (40 min)**
- **7. Review, Best Practices & Q&A**

---
---

## 1. Introduction to Dashboards & Streamlit

```txt
As a Data Engineer,  
I want to understand what Streamlit is and why it’s used for dashboards,  
so that I can choose the right tools for building data-driven applications.
```

### 1.1 What is a dashboard?

A dashboard is a visual display of key information, typically presented on a single screen, that helps users quickly understand and monitor important data. Dashboards combine charts, metrics, tables, and other visual elements to turn raw data into actionable insights.

***Purpose of a Dashboard***

- **Summarise complex data** in an easy-to-understand format
- **Monitor key metrics** and trends in real time
- **Support decision-making** by highlighting important patterns, anomalies, or changes
- **Communicate insights** effectively to technical and non-technical audiences

***Examples of Dashboards***

- **Sales Dashboard**: Tracks revenue, sales targets, top-performing products, and sales by region.
- **Website Analytics Dashboard**: Shows website traffic, user engagement, and conversion rates.
- **Operations Dashboard**: Monitors system health, error rates, and service uptime for IT teams.
- **HR Dashboard**: Visualises employee headcount, turnover rates, and diversity metrics.

***Business Value of Dashboards***

- **Faster Decision-Making**: Dashboards provide real-time data, enabling quick responses to changes or issues.
- **Improved Transparency**: Teams and stakeholders can see up-to-date information, reducing misunderstandings.
- **Goal Tracking**: Dashboards make it easy to track progress against targets and KPIs.
- **Data-Driven Culture**: By making data accessible and understandable, dashboards encourage everyone to use data in their daily work.

---

### 1.2 Why use Streamlit?

Streamlit is a powerful, open-source Python library that enables you to quickly build interactive, data-rich web applications—without needing any web development experience. Here’s why Streamlit is especially valuable for data engineers and data scientists:

***Simplicity***

- **Python-First**: Streamlit lets you create web apps using only Python, so there’s no need to learn HTML, CSS, or JavaScript.
- **Minimal Code**: You can display charts, tables, and metrics with just a few lines of code, making it easy to turn scripts into shareable apps.
- **Beginner-Friendly**: Even those new to web development can build functional prototypes in hours, not weeks.

***Interactivity***

- **Built-in Widgets**: Streamlit offers a range of interactive widgets like sliders, dropdowns, and buttons, allowing users to explore data and adjust parameters in real time.
- **Real-Time Updates**: Apps automatically update as users interact with widgets or as data changes, providing a responsive experience.

***Rapid Prototyping***

- **Fast Iteration**: Streamlit’s hot-reloading feature means you see changes instantly as you modify your script, speeding up development and experimentation.
- **Seamless Integration**: It works well with popular Python data science libraries (like Pandas, NumPy, Matplotlib, and Plotly), so you can visualize and manipulate data directly in your app.
- **Easy Sharing**: Apps can be shared with stakeholders quickly, making it simple to gather feedback and iterate on your ideas.

> Streamlit bridges the gap between data analysis and user interaction, allowing you to build and share interactive dashboards and data applications with ease, speed, and minimal code

---
---

## 2. Environment Setup & Streamlit Basics

```txt
As a Data Engineer,  
I want to set up a Streamlit environment on my machine,  
so that I am ready to develop and run Streamlit applications.
```

### 2.1 Create a Virtual Environment

```bash
# Create a new virtual environment
python -m venv streamlit-env
# Activate the virtual environment
# On Windows
streamlit-env\Scripts\activate
# On macOS/Linux
source streamlit-env/bin/activate
```

---

### 2.2 Install Streamlit and Dependencies

```bash
# Install Streamlit and other necessary libraries
pip install streamlit pandas plotly
# Create a requirements.txt file
pip freeze > requirements.txt
# To install the same dependencies in another environment
pip install -r requirements.txt
# To check if Streamlit is installed correctly
streamlit --version
```

---

### 2.3 First Streamlit App

#### 2.3.1 Create a new Python Script

- Add a file called `demo1.py` to your project directory

#### 2.3.2 Add Basic Streamlit Code

- In `demo1.py`, add the following code:

```python
import streamlit as st

# Set the title of the app
st.title("My First Streamlit App")
# Display a simple message
st.write("Hello, Streamlit!")
```

#### 2.3.3 Save Your Script

- Save the `demo1.py` file

#### 2.3.4 Run Your Streamlit App

- Open a terminal and navigate to your project directory
- Run the following command:

```bash
streamlit run demo1.py
```

- This will start a local server and open your default web browser to display the app.
- You can stop the server by pressing `Ctrl+C` in the terminal.

#### 2.3.5 Add Data and Visualisations

- To make a more interesting app, create a `demo2.py` file with the following sample code (using a CSV file named `demo.csv`):

```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Demo Data Dashboard")

# Load data
df = pd.read_csv("demo.csv")

# Show data
st.write("Here is a preview of the data:")
st.dataframe(df)

# Simple visualisation
fig = px.histogram(df, x=df.columns[0])  # Replace with a relevant column name
st.plotly_chart(fig)
```

> ***Examining the Dashboard Code***
>
> - **Title**: The title of the app is set using `st.title()`.
> - **Data Loading**: The app loads a CSV file using `pd.read_csv()`.
> - **Data Display**: The app displays a preview of the data using `st.dataframe()`.
> - **Visualisation**:
>   - The app creates a histogram using Plotly Express (`px.histogram`) passing in the dataframe and the column to visualise.
>   - It displays the chart by calling `st.plotly_chart()`

#### 2.3.6 Run Your Second App

- Save the `demo2.py` file
- Run the following command in the terminal:

```bash
streamlit run demo2.py
```

- This will start a new local server and open your default web browser to display the app.
- You can stop the server by pressing `Ctrl+C` in the terminal.

#### 2.3.7 Explore the Streamlit Interface

The DataFrame and Plotly chart will be displayed in the Streamlit app. You can interact with the app by resizing the window, scrolling, and hovering over the chart to see details.

***DataFrame Interactivity***

1. **Sorting**: Click on the column headers to sort the data.
2. **Kebab Menu**: Use the kebab menu to access additional options for data manipulation and visualisation.
   1. Sort Ascending
   2. Sort Descending
   3. Format
   4. Autosize
   5. Pin Column
   6. Hide Column
3. **Hover Menu**: Hover over the table to see further options:
   1. Download as CSV
   2. Search dataframe
   3. Open/Close Fullscreen view

***Chart Interactivity***

1. **Hover**: Hover over the bars to see details about the data points.
2. **Hover Modebar**:
   1. **Download**: Use the download button to save the chart as a PNG file.
   2. **Zoom**: Zoom in on a specific area of the chart by clicking and dragging.
   3. **Pan**: Click and drag to pan around the chart.
   4. **Zoom In**: Zoom in on the chart.
   5. **Zoom Out**: Zoom out on the chart.
   6. **Autoscale**: Reset the zoom level to fit the entire chart.
   7. **Reset axes**: Reset the axes to their original state.
   8. **Fullscreen**: Open/close the chart in fullscreen mode.

---

### Activity 2 - Explore Other Basic Features (10 mins)

> Can you add a bar chart to the dashboard that groups Sales by Category?
>
> Include some colour on your chart to make it visually appealing.
>
> [Streamlit Documentation](https://docs.streamlit.io/library/api-reference)
> [Plotly Express Documentation](https://plotly.com/python/plotly-express/)

<details>

***SOLUTION***

```python
# Bar chart: Sales by Category
fig = px.bar(df, x="Category", y="Sales", color="Subcategory", barmode="group", title="Sales by Category and Subcategory")
st.plotly_chart(fig)
```

- **Bar Chart**: The code creates a bar chart using Plotly Express, grouping sales by category and subcategory.
- **Colour**: The `color` parameter is used to differentiate between subcategories, making the chart visually appealing.
- **Title**: The `title` parameter is used to set the title of the chart.
- **Display**: The chart is displayed in the Streamlit app using `st.plotly_chart()`.

</details>

#### Bonus Activity

> Try changing the chart to show Sales over Date

<details>

***SOLUTION***

```python
fig = px.bar(df, x="Date", y="Sales", color="Category", barmode="group", title="Sales Over Time by Category")
st.plotly_chart(fig)
```

</details>

---
---

## 3. Loading and Exploring the Demo Dataset

```txt
As a Data Engineer,
I want to load, explore, and clean a demo dataset,
so that I can prepare high-quality data for analysis and visualisation.
```

In this part of the workshop we're going to use the ***Titanic*** dataset to demonstrate some of the other features of Streamlit. The Synthetic Titanic dataset is a well-known dataset that contains information about the passengers on the Titanic, including whether they survived or not.

### 3.1 Create a New Streamlit App

- Create a new file called `demo3.py` in your project directory
- Add the following code to load and display the Titanic dataset:

```python
import streamlit as st
import pandas as pd

# Set the title of the app
st.title("Titanic Dataset Explorer")
# Load the Titanic dataset
df = pd.read_csv("./synthetic_titanic.csv")
# Display the data in Streamlit
st.dataframe(df)
# Show summary statistics
st.write("Summary Statistics:")
st.write(df.describe())
```

- Run the app using the command:

```bash
streamlit run titanic_app.py
```

- This will start a new local server and open your default web browser to display the app.
- You can stop the server by pressing `Ctrl+C` in the terminal.
- The app will display the Titanic dataset in a table format and show summary statistics for each column.

> ***Examining the App Code***
>
> - **Title**: The title of the app is set using `st.title()`.
> - **Data Loading**: The app loads the Titanic dataset using `pd.read_csv()`.
> - **Data Display**: The app displays the dataset in a table format using `st.dataframe()`.
> - **Summary Statistics**: The app shows summary statistics for each column using `st.write(df.describe())`.

### 3.2 Explore the Dataset

- The Titanic dataset contains the following columns:
  - **PassengerId**: Unique identifier for each passenger
  - **Survived**: Survival status (`0` = No, `1` = Yes)
  - **Pclass**: Passenger class (1st (`1`), 2nd (`2`), or 3rd (`3`))
  - **Name**: Name of the passenger
  - **Sex**: Gender of the passenger
  - **Age**: Age of the passenger
  - **SibSp**: Number of siblings/spouses aboard
  - **Parch**: Number of parents/children aboard
  - **Ticket**: Ticket number
  - **Fare**: Ticket fare
  - **Cabin**: Cabin number
  - **Embarked**: Port of embarkation (`C` = Cherbourg, `Q` = Queenstown, `S` = Southampton)

- The dataset contains a mix of numerical and categorical data, which can be used for analysis and visualisation.
- The `describe()` method provides summary statistics for numerical columns, including count, mean, standard deviation, minimum, maximum, and quartiles.
- The `st.dataframe()` method allows you to interact with the data, sort columns, and filter rows.
- You can also use the `st.write()` method to display additional information about the dataset, such as the number of missing values or unique values in each column.

#### 3.2.1 Data Types

- The Titanic dataset contains a mix of numerical and categorical data types:
  - **Numerical**: `PassengerId`, `Pclass`, `Age`, `SibSp`, `Parch`, `Fare`
  - **Categorical**: `Survived`, `Name`, `Sex`, `Ticket`, `Cabin`, `Embarked`
- You can check the data types of each column using the `dtypes` attribute:
  - Add the following code to your `titanic_app.py` file:

    ```python
    st.write("Data Types:")
    st.write(df.dtypes)
    ```

- This will display the data types of each column in the Streamlit app.

#### 3.2.2 Missing Values

- The Titanic dataset may contain missing values, which can affect analysis and visualisation.
- You can check for missing values using the `isnull()` method:
  - Add the following code to your `titanic_app.py` file:

    ```python
    st.write("Missing Values:")
    st.write(df.isnull().sum())
    ```

- This will display the number of missing values in each column in the Streamlit app.
- You can use the `st.write()` method to display the percentage of missing values in each column:
  - Add the following code to your `titanic_app.py` file:

    ```python
    st.write("Percentage of Missing Values:")
    st.write(df.isnull().mean() * 100)
    ```

- This will display the percentage of missing values in each column in the eamlit app.

#### 3.2.3 Data Cleaning

- You can clean the dataset using any of the data cleaning techniques available in Pandas.

- For this dataset, the following cleaning methods are commonly implemented:

***1. Numerical Columns*** (`Age` and `Fare`):

- Fill missing values with the mean or median of the column

    ```python
    df["Age"] = df["Age"].fillna(df["Age"].mean().round())
    df["Fare"] = df["Fare"].fillna(df["Fare"].mean())
    ```

***2. Categorical Columns*** (`Embarked` and `Cabin`):

- For `Embarked`, fill missing values with the mode of the column

    ```python
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    ```

- For `Cabin`, create a new column indicating whether the passenger had a cabin or not:

    ```python
    df['HasCabin'] = df['Cabin'].notnull().astype(int)
    ```

- Drop the `Cabin` column as it is not needed for THIS analysis:

    ```python
    df.drop(columns=['Cabin'], inplace=True)
    ```

***3. Convert Data Types***

- Convert `string` columns to `category` type for better memory efficiency:

    ```python
    df['Sex'] = df['Sex'].astype('category')
    df['Embarked'] = df['Embarked'].astype('category')
    df['Pclass'] = df['Pclass'].astype('category')
    ```

- Convert `Survived` to `boolean` type:

    ```python
    df['Survived'] = df['Survived'].astype('bool')
    ```

- Numeric conversion, making sure numeric columns are in the correct format:

    ```python
    df['Age'] = pd.to_numeric(df['Age'].round().astype(int), errors='coerce')
    df['Fare'] = pd.to_numeric(df['Fare'], errors='coerce')
    ```

***4. Drop Unnecessary Columns***

- Drop columns that are not needed for analysis:

    ```python
    df.drop(columns=['Ticket'], inplace=True)
    ```

***5. Remove Duplicates***

- Check for duplicates and remove them if necessary:

    ```python
    df.drop_duplicates(inplace=True)
    ```

### 3.2.4 Enrich the Dataset with Feature Engineering

- You can create new features from existing columns to enhance the dataset for analysis and visualisation.

***Family Size***

- Create a new column called `FamilySize` that combines the number of siblings/spouses and parents/children aboard:

```python
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
```

- This new feature can provide insights into the survival rates of passengers based on their family size.

***Binned Ages***

- Create a new column called `AgeGroup` that categorises passengers into age groups:

```python
bins = [0, 12, 20, 40, 60, 80]
labels = ['Child', 'Teen', 'Young Adult', 'Adult', 'Senior']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)
```

- This new feature can help analyse survival rates based on age groups.

### 3.2.5 Display the Cleaned Dataset

- After cleaning and enriching the dataset, display the cleaned dataset in the Streamlit app:

```python
st.write("Cleaned DataFrame:")
st.dataframe(df)
st.write("Summary Statistics:")
st.write(df.describe())
st.write("Missing Values:")
st.write(df.isnull().sum())
```

> ***Note:***
>
> **Streamlit** does not update already written dataframes if you modify them later in the script.  
> The `.write` function runs at the time of calling with the data available at the time of calling.  
> If you want to see the updated dataframe, you need to call the `.write` function again after modifying the dataframe.
>
> A version of the app showing just the cleaned and enriched dataset is available in the `titanic_cleaned.py` file.

---
---

## 4. Creating Key Metrics & Visualisations

```txt
As a Data Engineer,
I want to create basic metrics and visualisations from my dataset,
so that I can extract and communicate key insights effectively.
```

### 4.1 Defining KPIs and Metrics

**K**ey **P**erformance **I**ndicators (KPIs) are measurable values that demonstrate how effectively a company is achieving key business objectives. KPIs are used to evaluate success at reaching targets.

Other metrics can also be defined to provide additional insights into the dataset.

These are usually defined, by the project stakeholders, to provide clarity on the goals and expectations.  In the case of the Titanic dataset, the following KPIs and metrics can be defined:

| **KPI/Metric** | **Description** |
|----------------|-----------------|
| Total Passengers | The total number of passengers in the dataset |
| Overall Survival Rate | The proportion of passengers who survived the disaster |
| Average Age | The average age of passengers |
| Survival Rate by Gender | The proportion of passengers who survived based on gender |

### 4.2 Creating Metrics in Streamlit

- You can create metrics in Streamlit using the `st.metric()` function. This function displays a metric with a label, value, and optional delta (change) value.

```python
# Total Passengers
total_passengers = df['PassengerId'].nunique()
st.metric(label="Total Passengers", value=total_passengers)
# Overall Survival Rate
overall_survival_rate = df['Survived'].mean()
st.metric(label="Overall Survival Rate", value=f"{overall_survival_rate:.2%}")
# Average Age
average_age = df['Age'].mean()
st.metric(label="Average Age", value=f"{average_age:.2f}")
# Survival Rate by Gender
survival_rate_by_gender = df.groupby("Sex", observed=False)["Survived"].mean()
# Display each gender's survival rate separately
for gender, rate in survival_rate_by_gender.items():
    st.metric(label=f"Survival Rate ({gender})", value=f"{rate:.2%}")
```

- This code calculates the total number of passengers, overall survival rate, average age, and survival rate
- You can further enhance the dashboard by adding more metrics and visualisations based on the dataset.

### 4.3 Creating Visualisations in Streamlit

- You can create visualisations in Streamlit using libraries like Plotly, Matplotlib, or Seaborn.
- Visualisations can be split into different types, like "Breakdown" and "Distribution"
  - **Breakdown**: Show the breakdown of a metric by a categorical variable
  - **Distribution**: Show the distribution of a metric across a continuous variable

#### 4.3.1 Breakdown Visualisations

- You can create breakdown visualisations using bar charts or pie charts.
- Here we are going to show the *Survival Rate by Gender*
  - Add the following code to your `demo4.py` file:

    ```python
    # Add this to the import section
    import plotly.express as px

    # Add this under the metrics section
    # Convert survival_rate_by_gender to a DataFrame
    survival_rate_by_gender = survival_rate_by_gender.reset_index()
    # Rename columns for clarity
    survival_rate_by_gender.columns = ['Sex', 'Survived']
    
    # Create a bar chart
    fig1 = px.bar(
        survival_rate_by_gender,
        x="Sex",
        y="Survived",
        labels={"Sex": "Gender", "Survived": "Survival Rate"},
        title="Survival Rate by Gender",
        text="Survived",
        color="Sex",
    )

    # Show the bar chart in Streamlit
    st.plotly_chart(fig1)
    ```

- This code creates a bar chart showing the survival rate by gender.
  - The `px.bar()` function is used to create the bar chart, with:
    - `survival_rate_by_gender` set to the DataFrame containing the survival rates.
    - `x` set to the `Sex` column and `y` set to the `Survived` column.
    - The `labels` parameter is used to set the axis labels.
    - The `title` parameter is used to set the title of the chart.
    - The `text` parameter is used to display the survival rate on top of each bar.
    - The `color` parameter is set to `Sex` to differentiate the bars by gender.

---

#### 4.3.2 Distribution Visualisations

- You can create distribution visualisations using histograms or box plots.
- Here we are going to show the *Age Distribution of Passengers*
  - Add the following code to your `demo4.py` file:

    ```python
    # Create a histogram of Age
    fig2 = px.histogram(
        df,
        x="Age",
        nbins=30,
        title="Age Distribution of Passengers",
        labels={"Age": "Age"},
        color_discrete_sequence=["#636EFA"],
    )

    # Show the histogram in Streamlit
    st.plotly_chart(fig2)
    ```

- This code creates a histogram showing the age distribution of passengers.
  - The `px.histogram()` function is used to create the histogram, with:
    - `df` set to the DataFrame containing the Titanic dataset.
    - `x` set to the `Age` column.
    - The `nbins` parameter is used to set the number of bins in the histogram.
    - The `title` parameter is used to set the title of the chart.
    - The `labels` parameter is used to set the axis labels.
    - The `color_discrete_sequence` parameter is used to set the colour of the bars.

---
---

## 5. Building Interactivity

```txt
As a Data Engineer,
I want to add interactivity (such as filters and selectors) to my dashboard,
so that users can explore the data dynamically and gain deeper insights.
```

### 5.1 Adding Sidebar Filters

- You can add filters to your Streamlit app using the sidebar. This allows users to filter the data based on specific criteria.
- Here we are going to add a filter for the `Passenger Class` and `Embarked Port`.

- Add the following code to your `demo5.py` file:

```python
# Add a sidebar for filters
st.sidebar.header("Filters")
# Passenger Class filter
pclass_filter = st.sidebar.multiselect(
    "Select Passenger Class",
    options=sorted(df["Pclass"].unique()),  # Sort the options
    default=sorted(df["Pclass"].unique()),  # Sort the default options
)
# Embarked Port filter
embarked_filter = st.sidebar.multiselect(
    "Select Embarked Port",
    options=sorted(df["Embarked"].unique()),  # Sort the options
    default=sorted(df["Embarked"].unique()),  # Sort the default options
)
# Filter the DataFrame based on the selected filters
filtered_df = df[
    (df["Pclass"].isin(pclass_filter)) & (df["Embarked"].isin(embarked_filter))
]
# Show the filtered DataFrame
st.write("Filtered DataFrame:")
st.dataframe(filtered_df)
```

### 5.2 Updating Metrics and Visualisations Based on Filters

- The filters are a nice addition, but they do not actually change anything!
- You can update the metrics and visualisations based on the selected filters.
- This allows users to see how the metrics and visualisations change based on their selections.

- Modify the section of code in your `demo5.py` file that defines the metrics, replacing `df` with `filtered_df`:

```python
# Total Passengers
# total_passengers = df["PassengerId"].nunique()
total_passengers = filtered_df["PassengerId"].nunique()
# Overall Survival Rate
# overall_survival_rate = df["Survived"].mean()
overall_survival_rate = filtered_df["Survived"].mean()
# Average Age
# average_age = df["Age"].mean()
average_age = filtered_df["Age"].mean()
# Survival Rate by Gender
# survival_rate_by_gender = df.groupby("Sex", observed=False)["Survived"].mean()
survival_rate_by_gender = filtered_df.groupby("Sex", observed=False)[
    "Survived"
].mean()
```

- Modify the section of code in your `demo5.py` file that defines the visualisations, replacing `df` with `filtered_df`:

```python
# Create a histogram of Age
fig2 = px.histogram(
    # df,
    filtered_df,
    x="Age",
    nbins=30,
    title="Age Distribution of Passengers",
    labels={"Age": "Age"},
    color_discrete_sequence=["#636EFA"],
)
```

- Save your changes and return to the Streamlit app in your browser.
- You should see the metrics and visualisations update based on the selected filters in the sidebar.
- You can also add more filters to the sidebar to allow users to filter the data based on other criteria, such as `Gender`, `Age Group`, or `Family Size`.
- You can use the:
  - `st.sidebar.selectbox()` to give a drop down list for filters.
  - `st.sidebar.slider()` to allow users to select a range of values.
  - `st.sidebar.checkbox()` function to add checkboxes for binary filters, such as `Survived` or `HasCabin`.
  - `st.sidebar.radio()` function to add radio buttons for single-select filters, such as `Sex`.

---
---

## 6. Hands-on Mini Project (40 min)

```txt
As a Data Engineer,
I want to build and run an interactive dashboard using Streamlit,
so that I can present data insights in a user-friendly way.
```

### 6.1 Mini Project Instructions

1. **Load and Inspect the Data**
   - Load the provided `synthetic_titanic.csv` dataset into your app.
   - Preview the data using `st.dataframe()` or `st.write()`.

2. **Clean and Prepare the Data**
   - Check for missing values and handle them appropriately.
   - Convert data types if needed (e.g., categorical columns).
   - (Optional) Create new features, such as family size or age groups.

3. **Choose Your Insights**
   - Decide on 2–3 questions you want to answer. Example questions:
     - How does survival rate vary by passenger class, gender, or age group?
     - What is the distribution of fares or ages?
     - Did having family on board affect survival?
     - Are there differences in survival by port of embarkation?

4. **Calculate Key Metrics**
   - Compute and display at least two summary statistics (e.g., total passengers, survival rate, average fare, etc.) using `st.metric()` or `st.write()`.

5. **Create Visualizations**
   - Build at least two charts (e.g., bar chart, pie chart, histogram, boxplot) to illustrate your findings.
   - Use Plotly for interactive charts.

6. **Add Interactivity**
   - Include at least one interactive widget (e.g., sidebar selectbox, slider, multiselect) to let users filter or explore the data dynamically.

7. **Display and Explain**
   - Show your metrics and charts in the app.
   - Add short captions or markdown text to explain what each visualization shows.

### Tips

- Keep your code organized and comment your steps.
- Try to make your dashboard clear and easy to use.
- Don’t be afraid to experiment—there are many ways to answer each question!

---

### Stretch Goals (Optional)

- Add more advanced filters (e.g., filter by multiple columns).
- Try combining two features in a single chart (e.g., survival by class and gender).
- Create a table that updates based on user selections.

---

***Possible Metrics and Visualisations:***

<details>

- Survival by class, by age group, by port, by family size, by cabin assignment, etc.
- Fare distribution by class
- Survival by family size
- Survival by embarkation port
- More complex filtering and combinations (e.g., survival by class and gender, or by age group and class)
- Custom feature engineering (e.g., “child” vs “adult”, “large family” vs “small family”)
- Any advanced visualizations (boxplots, multi-variable plots, etc.)

</details>

---
---

## 7. Review, Best Practices & Q&A

```txt
As a Data Engineer,
I want to discuss best practices and identify next steps for developing dashboards,
so that I can continue to improve my skills and deliver robust solutions.
```

### 7.1 Code Organisation

- Review the code in the `app` folder to see how the app is structured and how the different components work together.
- The `app` folder contains the following files:
  - `main.py`: The main Streamlit app file - use `streamlit run app/main.py` to run the app from the root folder in the terminal
    - The associated `test_` file contains integration tests for the whole application
  - `data_processing.py`: The data processing file - contains functions to load, clean, and prepare the data
    - The associated `test_` file contains unit tests for the data processing functions
  - `filters.py`: The filters file - contains functions to create and apply filters to the data
    - The associated `test_` file contains unit tests for the filter functions
  - `metrics_visuals.py`: The metrics and visualisations file - contains functions to calculate and display metrics and visualisations
    - The associated `test_` file contains unit tests for the metrics and visualisation functions

> ***Why is this best practice?***
>
> - **Modularity**: The code is organized into separate files based on functionality, making it easier to maintain and understand.
> - **Reusability**: Functions can be reused across different parts of the app, reducing code duplication.
> - **Testing**: Each file has an associated test file, allowing for unit and integration testing of the code.
> - **Collaboration**: Multiple developers can work on different parts of the app simultaneously without conflicts.
> - **Scalability**: The app can be easily extended by adding new files or functions without affecting existing code.
> - **Readability**: The code is easier to read and understand, as each file has a specific purpose and follows a consistent structure.
> - **Maintainability**: Bugs can be fixed and features can be added more easily, as the code is organized into logical sections.
> - **Version Control**: The modular structure makes it easier to track changes and manage versions of the codebase.
> - **Documentation**: Each file can have its own documentation, making it easier to understand the purpose and usage of each component.

---

### 7.2 Run Tests with Coverage

To run the tests with a coverage report, use the following command:

```bash
pytest --cov=app --cov-report=term-missing
```

- This will run all the tests in the `app` folder and display a coverage report in the terminal.
- The coverage report will show which lines of code were executed during the tests and which lines were not.
- You can also generate an HTML report by using the following command:

```bash
pytest --cov=app --cov-report=html
```

- This will create a `htmlcov` folder in the root directory containing the HTML report.
- Open the `index.html` file in your web browser to view the coverage report.

***You will notice only 1 line of code is not covered - is this an issue?***

> ***Why is this best practice?***
>
> - **Quality Assurance**: Running tests ensures that the code works as expected and catches any bugs or issues early in the development process.
> - **Code Coverage**: The coverage report helps identify untested code, allowing developers to improve test coverage and ensure all parts of the code are tested.
> - **Regression Testing**: Tests can be run after changes to the code to ensure that new changes do not break existing functionality.
> - **Documentation**: Tests serve as documentation for the code, showing how the functions are expected to behave and what inputs/outputs are expected.

---

### 7.3 Caching

- Streamlit provides a caching mechanism to speed up the app by storing the results of expensive computations.
- You can use the `@st.cache_data` decorator to cache the results of a function.
- This is especially useful for loading and processing large datasets, as it avoids reloading the data every time the app is run.
- The `@st.cache_data` decorator to the data loading function in `data_processing.py`:

```python
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df
```

> ***Why is this best practice?***
>
> - **Performance**: Caching improves the performance of the app by reducing the time taken to load and process data.
> - **Efficiency**: Caching avoids redundant computations, making the app more efficient and responsive.
> - **User Experience**: Caching improves the user experience by reducing loading times and making the app feel more responsive.
> - **Resource Management**: Caching helps manage resources by reducing the load on the server and database, especially for large datasets.
> - **Scalability**: Caching allows the app to scale better, as it can handle more users and larger datasets without slowing down.

---

### 7.4 Page Layout and Design

- Streamlit can automatically adjust the layout of the app based on the screen size and resolution.
- You can use the `st.set_page_config()` function to set the layout of the app.
- This function allows you to set the page title, icon, layout, and initial sidebar state.
- Add the following code to your `main.py` file:

```python
st.set_page_config(
    page_title="Titanic Dashboard",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="auto",
)
```

- Other options for the `layout` parameter are:
  - `centered`: The default layout, which centers the app in the middle of the screen.
  - `fixed`: A fixed layout that does not change based on the screen size.
- Other options for the `initial_sidebar_state` parameter are:
  - `auto`: The default state, which automatically shows or hides the sidebar based on the screen size.
  - `expanded`: The sidebar is always shown.
  - `collapsed`: The sidebar is always hidden.
- You can also use the `st.sidebar.set_expander()` function to create expandable sections in the sidebar.
  - This allows you to group related filters and options together, making the sidebar more organized and user-friendly.
  
  ```python
  # Add an expander for filters
  with st.sidebar.expander("Filters", expanded=True):
      # Add your filters here
      pclass_filter = st.multiselect(
          "Select Passenger Class",
          options=sorted(df["Pclass"].unique()),
          default=sorted(df["Pclass"].unique()),
      )
  ```

  - This will create an expandable section in the sidebar with the title "Filters" and the filters inside it.

> ***Why is this best practice?***
>
> - **User Experience**: A well-designed layout improves the user experience by making the app more visually appealing and easier to navigate.
> - **Responsiveness**: A responsive layout ensures that the app looks good on different screen sizes and resolutions.
> - **Organization**: A structured layout helps organize the content and makes it easier for users to find what they are looking for.
> - **Accessibility**: A well-designed layout improves accessibility for users with disabilities, making it easier for them to navigate and interact with the app.

---

### 7.5 Documentation and Version Control

- Use comments and docstrings to document your code and explain the purpose of each function and class.
- Use version control (e.g., Git) to track changes to the code and collaborate with other developers.
- Use a README file to provide an overview of the project, installation instructions, and usage examples.
- Use a requirements file to specify the dependencies needed to run the app.
- Use a `.gitignore` file to exclude unnecessary files and folders from version control (e.g., virtual environment, cache files, etc.).
- Use a `LICENSE` file to specify the license under which the code is distributed.
- Use a `CHANGELOG` file to track changes and updates to the codebase.

> ***Why is this best practice?***
>
> - **Clarity**: Documentation helps clarify the purpose and functionality of the code, making it easier for others (and yourself) to understand.
> - **Collaboration**: Good documentation and version control facilitate collaboration among team members, allowing them to work together more effectively.
> - **Maintenance**: Well-documented code is easier to maintain and update, reducing the risk of introducing bugs or breaking existing functionality.
> - **Reproducibility**: Documentation and version control help ensure that the code can be reproduced and run in different environments.
> - **Knowledge Transfer**: Documentation helps transfer knowledge between team members, making it easier for new developers to understand the codebase.
> - **Project Management**: Version control helps manage the project and track changes over time, making it easier to roll back changes if needed.
> - **Quality Assurance**: Documentation and version control help ensure the quality of the code and reduce the risk of errors or bugs.
> - **Compliance**: Documentation and version control help ensure compliance with industry standards and best practices.
> - **Security**: Documentation and version control help ensure the security of the code and reduce the risk of vulnerabilities.
> - **Licensing**: Documentation and version control help ensure compliance with licensing requirements and protect intellectual property.

---

### 7.6 Deployment

- Streamlit apps can be deployed to various platforms, including:
  - **Streamlit Sharing**: A free hosting service provided by Streamlit for deploying apps.
  - **Heroku**: A cloud platform that allows you to deploy web applications.
  - **AWS**: Amazon Web Services provides various services for deploying and hosting applications.
  - **Google Cloud Platform**: Google Cloud offers services for deploying and hosting applications.
  - **Azure**: Microsoft Azure provides services for deploying and hosting applications.
- You can also deploy Streamlit apps on your own server or use Docker to containerize the app for deployment.

> For more information on deploying Streamlit apps, refer to the [Streamlit Deployment Documentation](https://docs.streamlit.io/library/deploy_streamlit_app).
