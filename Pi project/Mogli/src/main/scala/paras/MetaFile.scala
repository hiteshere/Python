package paras

import java.io.File
import java.nio.file.{Files, Paths}
import javax.crypto.{Cipher, CipherOutputStream}

import org.json.JSONObject


/**
  * checks all the functions related to the file metadata
  * provides the properties about the encrypted file
  *
  * auto creates the directory
  *  */
class MetaFile (val fileName:String){

  val toEncrypt_file = new File(fileName)

  //checking if the file exists
  if(!(toEncrypt_file.isFile&&toEncrypt_file.exists())){
    System.err.println("invalid operation ..quiting ")
    sys.exit(-1)
  }

  val dirName = Files.createTempDirectory("").getFileName
  Files.createDirectory(dirName)
  val fileSize = toEncrypt_file.length()
  val encFileName = Files.createTempFile(dirName,"",".pm")

  setMetaFile()

  def setMetaFile()={
    val metaJson = new JSONObject()
    metaJson.put ("name",toEncrypt_file.getName)
    metaJson.put ("size",fileSize.toString)
    metaJson.put ("enc_file_name",encFileName.getFileName.toString)

    // setting up the cipher
    val cipher = Cipher.getInstance("AES/CBC/NoPadding")
    cipher.init(Cipher.ENCRYPT_MODE,Credentials.getSeCretKey_aes,Credentials.getIvParameterSpec)
    //setting up the cipher output stream
    val cof = new CipherOutputStream(Files.newOutputStream(Paths.get(dirName+"/META")),cipher)

    // pad the information with json friendly " "
    val deficit  = metaJson.toString().length % 16
    var paddedMetaJson =  metaJson.toString

    for (a <- 1 to deficit){
      paddedMetaJson +=" "
    }
    /*println(paddedMetaJson)
    println(paddedMetaJson.length,deficit,metaJson.toString.getBytes.length)*/

    cof.write(paddedMetaJson.getBytes(), 0,paddedMetaJson.getBytes.length)

    cof.flush()
    cof.close()
  }

}
