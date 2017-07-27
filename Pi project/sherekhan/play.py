from os import listdir
from multiprocessing import Pool, cpu_count
from decrypt import Decrypt

# enable multi processing in the file
pyhton_script = """

from subprocess import call

call(["echo ranJitkiJawani26 | sudo -S python -m sherekhan {enc_dir} /usr/video"], shell=True)
call(['echo ranJitkiJawani26 | sudo -S xterm -fullscreen -fg black -bg black -e omxplayer -o both {file} '], shell=True)

call(["xrefresh -display :0"], shell=True)
call(["xrefresh -display :0"], shell=True)

call(["echo ranJitkiJawani26 | sudo -S rm -f {file}"], shell=True)


"""


def write_play_files(d):
    try:
        dec = Decrypt(dirname="/usr/video/"+d, out_dirname="/usr/video")
        f = dec.file_name
        with open("/home/pi/Desktop/paras/play-"+f+".py", "wb") as p_file:
            p_file.write(pyhton_script.format(file="/usr/video/"+f.replace(" ", "\\ "), enc_dir="/usr/video/"+d))
    except AttributeError, e:
        print "File :" + d + " not encrypted properly error: " + e.message

if __name__ == "__main__":
    process_pool = Pool(processes=cpu_count())
    dirs = listdir("/usr/video")
    # [process_pool.apply_async(write_play_files, dr) for dr in dirs]
    [write_play_files(dr) for dr in dirs]
    process_pool.close()
    process_pool.join()
