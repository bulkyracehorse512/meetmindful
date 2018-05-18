To execute the python code: 

i. $ docker build -t code-test .

ii. $ docker run -it --volume "$(pwd)":/code/ code-test