## Maze Solver

Maze solver development.


## Scripts available

Different scripts are available in the repository. We can see:

 - Docker file
 - Python scripts

The first generates the `docker image` (`Dockerfile`) to be able to launch the containers.

The commands to use to raise the containers are:

generate the image

```docker
docker build -t <<image_name>> -f <<dockerfile_name>> .
```

docker run 

```docker
docker run -ti <<image_name>>
```

It is necessary indicate -ti options due to the input data tha it is asked to the user.

--


## License

Apache License v2.0