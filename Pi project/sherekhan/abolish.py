""" executes the subprocess to remove the video files"""

from subprocess import call

# delete all the files from the given /usr/video, saving the encrypted videos

call(["echo ranJitkiJawani26 | sudo -S rm -f /usr/video"], shell=True)

# removing the  /usr/video and /home/pi/Desktop/paras
# call(["echo ranJitkiJawani26 | sudo -S  rm -f -d -r /usr/video"], shell=True)
#
# call(["echo ranJitkiJawani26 | sudo -S rm -f -d -r /home/pi/Desktop/paras"], shell=True)


