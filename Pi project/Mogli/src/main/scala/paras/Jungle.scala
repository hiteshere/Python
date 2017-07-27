package paras

import java.io.File
import java.nio.file.{Files,  Paths}
import javax.crypto._

import scala.collection.parallel.ForkJoinTaskSupport
import scala.concurrent.forkjoin.ForkJoinPool

/**
  * >encrypts the given file name
  *
  */


object Jungle {

  //buffer size to be read and then written to encypted file
  val BUFFER_SIZE = 1024

  def main(args:Array[String]): Unit={

    val t_start = System.nanoTime()

    if(args.length==0)
      sys.exit(-1) // not enough arguments to continue this futile stuff

    val fileName = args{0}

    if(Files.isDirectory(Paths.get(fileName))){
      val files =  new File(fileName)
      val filesPar = files.listFiles().par

      val threadPool = new ForkJoinTaskSupport(new ForkJoinPool())
      filesPar.tasksupport =threadPool

      filesPar.filterNot(_.isDirectory).foreach(f=>{
        println("working :"+f.getName)
        encrypt(new MetaFile(f.toString),f.getAbsolutePath)
      })
    }
    else{
      println( "encrypting single file")
      encrypt(new MetaFile(fileName),fileName)
    }


    val timeTaken =(System.nanoTime()-t_start).toDouble/1000000000
    println ("done, time elapsed :"+timeTaken)
  }


  /**encrypts the given set of bytes
    *
    * @param metaFile get information about file
    * @param toEncrypt name of the file to be encrypted */
  def encrypt(metaFile:MetaFile,toEncrypt:String): Unit ={

    //creating a encrypting mechanism
    val key = Credentials.getSeCretKey_aes
    val encryptCipher = Cipher.getInstance("AES/CBC/PKCS5Padding")
    encryptCipher.init(Cipher.ENCRYPT_MODE,key,Credentials.getIvParameterSpec)

    //creating input stream to read to be encrypted file
    val fis = Files.newInputStream(Paths.get(toEncrypt))

    //binding the file to the output stream
    val fOStream = Files.newOutputStream(metaFile.encFileName)

    //bind the cipher and the file output stream to the CipherInputStream
    val cipherOutputStream = new CipherOutputStream(fOStream,encryptCipher)

    val buffer =new  Array[Byte](1024)
    var flag = 0
    while(flag  != -1 ){
      flag = fis.read(buffer)
      cipherOutputStream.write(buffer)
      //flush the streams
      cipherOutputStream.flush()
    }

    //closing streams
    cipherOutputStream.close()
    fis.close()
  }
}
