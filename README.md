To execute the python code:

`$ cd python/`

then to build the docker container and run the script execute the following commands
```
i. $ docker build -t code-test .

ii. $ docker run -it --volume "$(pwd)":/code/ code-test
```
To check out the CSS: 
`$ cd css/`

then open the index.html file that should match the one you sent over.
