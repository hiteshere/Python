"""decrypts the file with given credentials
 command line wrapper around the Decrypt class
 accepts the following arguments

 Directory : can contain meta files, or dirs with meta files

 out directory : directory to which decrypt file to
 """

# coding=UTF-8


import os
import time
from decrypt import Decrypt
import sys
from multiprocessing import Pool, cpu_count


def decrypt(directory, out_directory):
    """decrypts the given directory content using Decrypt"""
    if os.path.isdir(directory) and os.path.exists(directory+"/META"):
        Decrypt(directory, out_directory).decrypt()


if __name__ == "__main__":

    t_start = time.time()

    args = sys.argv
    if len(args) < 3:
        print "no enough argument"
        exit(-1)

    dirname = args[1]
    out_dirname = args[2]

    dirs = os.listdir(dirname)
    if "META" in dirs:
        print "processing single file"
        dec = Decrypt(dirname, out_dirname)
        dec.decrypt()
    else:
        print "looking for files to process"
        process_pool = Pool(cpu_count())
        # [decrypt(dirname+"/"+d, out_dirname) for d in dirs]
        [process_pool.apply_async(decrypt, (dirname+"/"+d, out_dirname)) for d in dirs]
        process_pool.close()
        process_pool.join()

    print "time taken:"+str(time.time()-t_start)
    print "done"

