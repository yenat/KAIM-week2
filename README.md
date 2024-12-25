# User Engagement and Satisfaction Analysis

This repository contains code and documentation for analyzing user engagement and satisfaction based on network performance metrics. The analysis includes the following key steps:

## Data Aggregation and Preprocessing
- Load and clean the dataset from a PostgreSQL database.
- Aggregate data per customer.

## Engagement and Experience Analysis
- Identify extreme values.
- Visualize distributions of key metrics.
- Segment users into clusters based on their network experience using k-means clustering.

## Satisfaction Analysis
- Assign engagement and experience scores to users.
- Compute a satisfaction score by averaging engagement and experience scores.
- Predict satisfaction scores using a regression model.
- Segment users into clusters based on their satisfaction scores.
- Export the final results to a PostgreSQL database.

## Requirements
To install the required packages, use the following command:

```sh
pip install -r requirements.txt

git clone https://github.com/yourusername/user-engagement-analysis.git
```

### Run the Jupyter Notebook:
Open the Jupyter Notebook containing the analysis.

Execute the cells step-by-step to perform data preprocessing, analysis, and export operations.