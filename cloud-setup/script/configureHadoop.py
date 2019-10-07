import sys
import subprocess

workerNodes = ['satyaki-1', 'satyaki-2', 'satyaki-3']

allNodes = ['satyaki-master', 'satyaki-1', 'satyaki-2', 'satyaki-3']

masterIP = '10.1.1.225'

masterNode = 'satyaki-master'

WorkersString = 'satyaki-1,satyaki-2,satyaki-3'

nameofPemKEy = "seng550" # Change to your own key.

def configureCluster():
    """
    Configures the cluster.

    :return:
    """

    for node in workerNodes:

        print ("Configuring {}".format(node))

        subprocess.call(["scp WorkerScript.py {}:~".format(node)],shell=True)
        subprocess.call(["ssh {} 'python ~/WorkerScript.py {}'".format(node, masterIP)],shell=True)

    subprocess.call(["python ~/MasterScript.py {} {} {}".format(WorkersString, masterIP, masterNode)],shell=True)

print("Configuring Hadoop")
configureCluster()
