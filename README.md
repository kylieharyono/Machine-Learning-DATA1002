# Predictive Modeling with Global Health Data

## Description:

In this project, we worked with a large, integrated dataset containing global health indicators like life expectancy, mortality rates, and GDP. The goal was to predict life expectancy using various regression models. We divided the dataset into training and test sets and used k-Nearest Neighbors (kNN) regression and logistic regression to make predictions. We assessed the model’s performance using metrics such as R-squared and Root Mean Square Error (RMSE). This project aimed to understand how global health factors could predict outcomes and demonstrated the challenges of working with real-world datasets.

## Techniques & Tools:

- Data Integration: Combining diverse global health data sources

- Modeling: k-Nearest Neighbors (kNN) regression, Logistic regression

- Evaluation: R-squared, RMSE

- Tools: Python, Scikit-learn, Pandas, Microsoft Excel (csv and xlsx)

## Contributions: 

This was a project done for university work. The parts being included here are all the individual contirbutions extracted from the groupwork.
- Data Processing: integrating the 4 different datasets into one, done by me.
- Data Visualisation: creating graphs and charts to represent information from the datasets, part of group contribution.
- Machine Learning & Results Report: using machine learning to predict information, extracting information, and testing the accuracy from results. The report is part of the group work, but the code and cleaned dataset included in this repository are all done by me.

The parts included in this repository are all the contributions I did for the project, so the parts included are mostly my work, along with contributions in the final stage by Andy Chen. 


## Acknowledgements:

This group project was done by Andy Chen and me as part of the DATA1002 Informatics: Data & Computation course by the University of Sydney. 

The integrated data set is combined from 4 different data sets gathers by each member of the group: “annual-number-of-deaths-by-cause.csv”, “health(combined).csv”, “Economic Statues.csv” and “led(1).csv”. “0220327 annual-number-of-deaths-by-cause.csv” is extracted from [Kaggle](https://www.kaggle.com/datasets/ivanchvez/causes-of-death-our-world-in-data/metadata). The author of this data is Ivan Chavez. He created this data set by extracting from parts of the data from the website: “Our World in Data” and downloading the chart under the subcategory: [“Causes of death”](https://ourworldindata.org/causes-of-death) as CSV. The dataset has CC0: Public Domain licensing, which is free for public use and has no copyright restrictions. The file “health(combined).csv” is by Zeus on Kaggle. The data is originally sourced from the World Health Organization (WHO). The dataset has CC0: Public Domain licensing, no copyright, and is free for public use. “Economic Statues.csv” data set is combined data from International Monetary Fund, WHO and World Bank. The data set is under a Creative Commons Attribution 4.0 International License (CC BY 4.0) and is accessible free of charge. [“led(1).csv”](https://www.kaggle.com/datasets/augustus0498/life-expectancy-who?resource=download) was posted by Akhil on Kaggle. The original dataset was collected from WHO and United Nations website with the help of Deeksha Russell and Duan Wang. The data was obtained from KumarRajarshi on Kaggle, before posted by Akhil. The dataset has CC0: Public Domain licensing, which is free for public use and has no copyright restrictions.

Due to limitations, we decided to only keep data from the year 2015 and removed the data from rest of the years when integrating our data. We also removed fields that were repeated more than once across the 4 data sets such as Country and Population. No other changes were made while integrating data.

