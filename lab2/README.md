# SENG 550 - Assignment 2

## Satyaki Ghosh, 10077685

1. The solutions to each problem is in their respective folders e.g. ex1 to ex3.

   - The results for each question is in their respective folder in the `results.txt` file

2. There is a `run.bash` script that can be executed to setup hadoop and the hdfs for this assignment
   and compute the results for **ALL** questions in this assignment.

   - Please copy the whole whole `lab2` folder onto master node and then you can just run the bash script
   - This script assumes a similar setup to what we did in class for it to work
     - It _should_ work out of the box without requiring any changes
   - The final output for each question will be stored in their respective folder
     - E.g Answer to Question 1 will be in a file called `results.txt` in the local folder `ex1`
   - After the script completes, it will clean up the HDFS
   - To use different text files for testing, the `input` directory contents can be updated
     and the bash script can be modified to copy those new files to the HDFS instead
     of the pre-defined ones

4. There is also additional comments in each mapper on how it works and which hadoop
   configurations and options that can be used to run it

#### Question 1 Sample Output

```
5990	499	232340
5991	499	109191
5992	499	145199
5993	499	505620
5994	499	687622
5995	499	135354
5996	499	169801
5997	499	310316
5998	499	815010
5999	499	362023
```

#### Question 2 Sample Output

```
1	2,3|0|black|source
2	1,3,4,5|1|black|1
3	1,4,2|1|black|1
4	2,3|2|black|3
5	2|2|black|2
```

#### Question 3 Sample Output

```
f(8126|9972) = 0.0113636363636	
f(8155|9972) = 0.0113636363636	
f(859|9972) = 0.0113636363636	
f(879|9972) = 0.0113636363636	
f(89|9972) = 0.0113636363636	
f(9708|9972) = 0.0113636363636	
f(9849|9972) = 0.0113636363636	
f(9973|9972) = 0.0113636363636	
f(9974|9972) = 0.0113636363636	
f(32|9990) = 1.0
```
