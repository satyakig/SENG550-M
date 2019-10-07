# SENG 550 - Assignment 1
###By: Satyaki Ghosh, 10077685

The solutions to each problem is in their respective folders e.g. ex1 to ex4.

There is a `text` folder that contains all the text files used for this assignment.

There is a `run.bash` script that can be executed to setup hadoop for this assignment
and compute the results for **ALL** questions in this assignment.

* This script assumes a similar setup to what we did in class for it to work
    * It _should_ work out of the box without requiring any changes
* The final output for each question will be stored in their respective folder
    * Answer to Question 1 will be in a file called `results.txt` in the local folder `ex1`
* After the script completes, it will clean up the HDFS
* To use different text files for testing, the `text` directory contents can be updated 
and the bash script can be modified to copy those new files to the HDFS instead 
of the pre-defined ones

There is also additional comments in each mapper on how it works and which hadoop 
configurations and options that can be used to run it
     