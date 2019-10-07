import sys
import subprocess

workerNodes = ['satyaki-1', 'satyaki-2', 'satyaki-3']

allNodes = ['satyaki-master', 'satyaki-1', 'satyaki-2', 'satyaki-3']

masterIP = '10.1.1.225'

masterNode = 'satyaki-master'

WorkersString = 'satyaki-1,satyaki-2,satyaki-3'

nameofPemKEy = "seng550" # Change to your own key.

def installHadoop():
    """
    Installs hadoop on all nodes.
    :return:
    """
    for node in allNodes:
        print ("Working on Node: {}".format(node))
        subprocess.call(["ssh {} 'sudo apt-get update -y'".format(node)],shell=True)

        subprocess.call(["ssh {} 'sudo apt-get install -y openjdk-7-jdk '".format(node)], shell=True)
        subprocess.call(["ssh {} 'wget https://archive.apache.org/dist/hadoop/core/hadoop-2.7.6/hadoop-2.7.6.tar.gz -P ~/Downloads'".format(node)],shell=True)
        subprocess.call(["ssh {} 'sudo tar zxvf ~/Downloads/hadoop-* -C /usr/local'".format(node)], shell=True)
        subprocess.call(["ssh {} 'sudo mv /usr/local/hadoop-* /usr/local/hadoop'".format(node)], shell=True)


print("Installing Hadoop")
installHadoop()
