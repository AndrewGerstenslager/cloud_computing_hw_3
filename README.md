# Cloud Computing HW 3
## Docker

### Objectives
- Create a python file which performs these tasks
    - Opens two files
    - Finds word counts (accounting for contractions)
    - Finds total words in each file and combined
    - Finds top three most frequent words for each file
    - Finds the IP address of the host computer
- Create a dockerfile to add files to /home/data and runs the python file
- Optimize the dockerfile and save it to a .tar file


### Steps Taken
1. I created app.py with the appropriate requirements fulfilled
2. I created a dockerfile using python:3.9-slim as the base image
3. I set the working directory to /home/data
4. I execute the python file, save the file to the output directory, then print the file to the terminal

### How to run
You can build and run this dockerfile with two easy commands. Make sure you have docker enabled in your terminal, navigate to the folder containing the Dockerfile, then run:

```bash
    docker build -t gerstead .
    docker run gerstead
```

