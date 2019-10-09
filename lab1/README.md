# SENG 550 - Assignment 1

## Satyaki Ghosh, 10077685

1. The solutions to each problem is in their respective folders e.g. ex1 to ex4.

   - The results for each question is in their respective folder in the `results.txt` file

2. There is a `text` folder that contains all the text files used for this assignment.

3. There is a `run.bash` script that can be executed to setup hadoop and the hdfs for this assignment
   and compute the results for **ALL** questions in this assignment.

   - Please copy the whole whole `lab1` folder onto master node and then you can just run the bash script
   - This script assumes a similar setup to what we did in class for it to work
     - It _should_ work out of the box without requiring any changes
   - The final output for each question will be stored in their respective folder
     - E.g Answer to Question 1 will be in a file called `results.txt` in the local folder `ex1`
   - After the script completes, it will clean up the HDFS
   - To use different text files for testing, the `text` directory contents can be updated
     and the bash script can be modified to copy those new files to the HDFS instead
     of the pre-defined ones

4. There is also additional comments in each mapper on how it works and which hadoop
   configurations and options that can be used to run it

#### Question 1 Sample Output

```
how your efforts and donations can help, see Sections 3 and 4 and the
mailing address: PO Box 750175, Fairbanks, AK 99775, but its volunteers
www.gutenberg.org/contact

For additional contact information:
Archive Foundation
distributed in machine readable form accessible by the widest array of

the U.S. unless a copyright notice is included. Thus, we do not
```

#### Question 2 Sample Output

```
zounds where		Count: 1
zounds who		Count: 1
zounds ye		Count: 1
zounds you		Count: 1
zwaggered out		Count: 1
zwounds an		Count: 1
zwounds how		Count: 1
zwounds i		Count: 3
zwounds will		Count: 1
zwounds ye		Count: 1
```

#### Question 3 Sample Output

```
zodiacs	shakespeare.txt
zogranda	moby.txt
zone	iliad.txt, jane.txt, moby.txt, shakespeare.txt
zoned	moby.txt
zones	iliad.txt, jane.txt, moby.txt
zoology	moby.txt
zoroaster	moby.txt
zounds	shakespeare.txt
zwaggered	shakespeare.txt
zwounds	shakespeare.txt
```

#### Question 4 Sample Output

```
zodiacs	1
zogranda	1
zone	16
zoned	2
zones	5
zoology	2
zoroaster	1
zounds	16
zwaggered	1
zwounds	7
```
