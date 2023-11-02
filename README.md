# New york taxi trip duration
## DatatalksClub ML Zoomcamp Midterm project
## Objectives of Midterm Project:
- Find a dataset
- Explore and prepare the data
- Train the best model
- Export the notebook into a script
- Put model into a web service
- Deploy model locally with Docker

  
### Overview
This project revolves around the analysis of the yellow taxi trip data for the year 2023, obtained from the New York City Taxi and Limousine Commission (TLC). The dataset offers a rich and comprehensive collection of information regarding taxi trips within the bustling metropolis of New York City.

The primary objective of this project is to utilize the temporal aspect of the data by harnessing the difference between the start and end dates and times of each taxi trip. Specifically, we aim to predict the duration of each trip using the temporal data as a key predictor.

The main components of this project include:

### Explore and prepare the data
Exploration of the data was done via *eda.ipynb* jupyter notebook file
- Explore data
  - Checked the Data Structure and columns
  - Checked the numbers of features and observations in the data
- prepare data
  - Checked for missing values 
  - Checked for outliers
  - Checked for Duplicates
- train data
  - Catergorical variables were encoded using the DictVectorizer.
  - trained best model.
    
### Model deployment to web services
- flask was used for web deployment via *web_service.py* script.
- Setup Pipenv Virtual Environment, by opening Cli on your system and run
  
```
pip install pipenv
```

- install the following:
  - flask
  - numpy
  - scikit-learn version 
  - requests
    
```
pipenv install gunicorn flask numpy scikit-learn==1.3.0 requests
```

  
### Deploy model locally with Docker
You can deploy the model on Docker.
To do so, you need to have Docker installed on your machine, then you build the image with the following command:

NOTE: Docker must be running before your run the following commands:

```
pipenv shell
```

Create docker image by running the following:

```
docker build -t midtermproj .
```

followed by this docker command which runs the docker image created

```
docker run -it --rm -p 9690:9690 midtermproj
```

### Expected Outcomes
By the conclusion of this project, we aim to accomplish the following:

Develop a predictive model capable of accurately estimating the duration of yellow taxi trips in New York City.
Gain insights into the factors that influence trip duration, especially the role of temporal variables.
Contribute valuable findings and analysis to the field of transportation data analysis, with implications for optimizing taxi services, traffic management, and passenger experiences.
The utilization of temporal data to predict trip duration holds the potential to enhance the efficiency and reliability of taxi services in New York City, benefiting both passengers and providers. This project demonstrates the power of data analytics and predictive modeling in addressing real-world transportation challenges.