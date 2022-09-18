# Project1_Kashaf

Hi, this is my first project for my IDS706: Data Engineering course. I will be writing a Big Data Script that uses the Pandas API for Dask and will also use FastApi with Uvicorn to create a microservice. Below is the layout for my project and the main steps I will follow:


<img width="719" alt="image" src="https://user-images.githubusercontent.com/111402572/190930583-6394d54e-79e6-4461-b0b5-d663b3ae2be5.png">


## Data Source:

I will be using a big dataset for Spotify Charts (3.48 GB) from Kaggle (linked [here][1]). This is a complete dataset of all the "Top 200" and "Viral 50" charts published globally by Spotify since January 1, 2017. The main columns in this dataset are as follows: 

Variable | Description
--- | ---
title | song title
--- | ---
rank | the song's rank in the charts
--- | ---
date | the date when the song appeared in the charts
--- | ---
artist | song's artist
--- | ---
url | link to the song
--- | ---
region | region where the song appeared in the charts
--- | ---
chart | the chart name
--- | ---
trend | if the song moved up, down or stayed in the same position on the charts
--- | ---
streams | number of streams for the song.


## Goal of the Project:

1. Build a microservice that talks to a big data system using dask
2. Create a webservice to query the data usign FastApi and Uvicorn

## Components to build a project:

A. Build a repo in Github
B. Configure "scaffold": Makefile, app file (fastapi), requirements file, python code file (to create a Dask dataframe)
C. Building a webservice using FastAPI
D. Testing the webservice in the demo (artist name, region's rate of streams)

## Next Steps:

I plan on using this dataset to drive some interesting insights about Spotify charts and the trending songs as a next step to this project.


[1]:https://www.kaggle.com/datasets/dhruvildave/spotify-charts "Kaggle Dataset"
