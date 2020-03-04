# STA9760-Project-Part_1

## Project Overview
In this part of the project, we are creating a docker container with a python code to extract data of NYC Parking Violations from NYC Opendata.

### Requirements
1. App_Token from NYC Open Data. Link: https://data.cityofnewyork.us/login
2. Dockerhub Account
          or
3. Github Account
4. AWS account (if operating on an EC2 machine)

### Run container from DockerHub
#### Install Docker (If not already installed)

Run following command in Terminal:
```sh
~$ sudo apt install docker.io
```
#### Step 1: Login to dockerhub
```sh
~$ sudo docker login --username={your username}
```
#### Step 2: Pull Docker Container from Dockerhub
```sh
~$ sudo docker pull patelsanket0589/bigdata1:3.0
```
#### Step 3: Run Docker to pull data
```sh
~$ sudo docker run -e APP_KEY={Your App Token} -v $(pwd):/app/outputs -it patelsanket0589/bigdata1:3.0 python main.py --page_size={Enter No. of Records to pull per call} --num_pages={Enter No. of Calls to Database} --output=./outputs/{output filename with format}
```

APP_KEY - (Required Input)It is the App token from NYC OpenData


--page_size - (Required Input) Number of Records to pull per call


--num_pages - (Optional) Number of Calls to make to Database. It will pull complete database of no input provided.


--output - (Optional) Output file for data storage. Program will print data in STDOUT if no input provided.

### Run Container From Github

#### Step 1: Copy all files from github in target folder

#### Step 2: Build Docker Container
```sh
~$ sudo docker build -t {Dockername}:version
```
#### Step 3: Run Docker Container
```sh
~$ sudo docker run -e APP_KEY={Your App Token} -v $(pwd):/app/outputs -it {Dockername}:version python main.py --page_size={Enter No. of Records to pull per call} --num_pages={Enter No. of Calls to Database} --output=./outputs/{output filename with format}
```
### Output

The output of the program is json formatted datastring. Each record is written on a new line in the output file.
