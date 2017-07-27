""" executes the subprocess to remove the video files"""

from subprocess import call
from os import listdir
from os import path
from multiprocessing import Pool, cpu_count


# opening the stdout for call output
stdout = open("stdout", "w")

# removing the  /usr/video and /home/pi/Desktop/paras
call(["echo ranJitkiJawani26 | sudo -S  rm -f -d -r /usr/video"], shell=True, stdout=stdout)

call(["echo ranJitkiJawani26 | sudo -S rm -f -d -r /home/pi/Desktop/paras"], shell=True, stdout=stdout)

# creating the /usr/video and /home/pi/Desktop/paras
call(["echo ranJitkiJawani26 | sudo -S  mkdir /usr/video"], shell=True, stdout=stdout)

call(["echo ranJitkiJawani26 | sudo -S mkdir /home/pi/Desktop/paras"], shell=True, stdout=stdout)

# giving the read write execute permission to the /home/pi/Desktop/paras folder
call(["echo ranJitkiJawani26 | sudo -S chmod  666  /home/pi/Desktop/paras"], shell=True, stdout=stdout)

# ************************************** copy dir with meta folder ******************************

# checking the directories with meta file
# getting all the media from the meta folder
medias = listdir("/media/pi")
c = lambda command: call(command, shell=True, stdout=stdout)
pool = Pool(cpu_count())

for media in medias:
    # for each media copy the dir in media with meta file to /urs/video
    dirs = listdir("/media/pi/"+media)
    for d in dirs:
        directory = "/media/pi/"+media+"/"+d
        # print directory
        if path.isdir(directory) and path.exists(directory+"/META"):
            # copy the directory to /usr/video
            pool.apply_async(c,["echo ranJitkiJawani26 | sudo -S  cp -r "+directory+" /usr/video/"])

pool.close()
pool.join()

# ************************ creating the play python scripts at /home/pi/Desktop/paras********************
# making everything read and write for everyone in /home/pi/Desktop/paras
call(["echo ranJitkiJawani26 | sudo -S chmod 777 /home/pi/Desktop/paras"], shell=True, stdout=stdout)

# calling the play script creates the dynamic pyhton play files
call(["echo ranJitkiJawani26 | sudo -S python -m play"], shell=True, stdout=stdout)

# compile the python files

call(["echo ranJitkiJawani26 | sudo -S python -m compileall /home/pi/Desktop/paras/."], shell=True)

# removing python source files

call(["echo ranJitkiJawani26 | sudo -S rm -f -r /home/pi/Desktop/paras/*.py"], shell=True)


# ****************** setting the final permissions *********************

# setting  permissions for  /home/pi/Desktop/paras/ and  /usr/video

# rwx-rx-rx
call(["echo ranJitkiJawani26 | sudo -S chmod  755  /home/pi/Desktop/paras"], shell=True)

# rwx-rx-rx
call(["echo ranJitkiJawani26 | sudo -S chmod 755 /home/pi/Desktop/paras/."], shell=True)

# rwx--
call(["echo ranJitkiJawani26 | sudo -S chmod 700 /usr/video"], shell=True)

# rwx--
call(["echo ranJitkiJawani26 | sudo -S chmod 700 /usr/video/."], shell=True)

# opening the file explorer when completed
call(["pcmanfm /home/pi/Desktop/paras"], shell=True)
