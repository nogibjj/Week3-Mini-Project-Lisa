[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)
## Week 3: Polars Descriptive Statistics Script

### Goal of the project:
Write a Python script that practices Exploratory Data Analysis on a dataset using Polars Library

### Report
* Please check more information about the dataset at [READ.md for mini-project-2](https://github.com/nogibjj/Week2-Mini-Project)
* Please check the summary table and scatter plot at the [analyze.pdf](https://github.com/nogibjj/Week3-Mini-Project-Lisa/blob/main/analyze.pdf)

### Takeaways
* I used AI to translate my code from Pandas directly to Polars. However, I found since the ChatGPT was only trained on data till 2021 when the latest Polars at that time was 0.9, but I wanted to use the current latest version of Polars, which is 0.19, I got an error when adding new columns to my data, and I have to manually change the syntax. When we use AI on fast-growing coding languages or libraries, there is this shortcoming in that the AI might not be trained for the latest data.
* But I was still able to use AI to do some manual work of translating my code. For example, I did change to one of my scatter plot, and let AI to apply the similar change to other plots.
* For my project written in Pandas, I used the pandas scatter plot function `df.plot.scatter`. But Polars does not have built-in data visualization feature, so I have to install another library Seaborn to do the plotting. Although Polars is faster than Pandas when processing the data, it is less mature than Pandas in some ways.
