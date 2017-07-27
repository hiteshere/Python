package paras

import javax.crypto.SecretKey
import javax.crypto.spec.{IvParameterSpec, SecretKeySpec}

/**
  * Created by Pluto on 04-07-2016.
  */
object Credentials {

  private val PASS = "changMer9*fa@*/40q345w1<?75|=-23"
  private val IV = "2paras Version 1"

  /**creating the 256 bit key.
    * to be used for encryption and decryption
    * @return SecretKey
    * */
  def getSeCretKey_aes:SecretKey ={
    new SecretKeySpec(Credentials.PASS.getBytes("UTF-8"),"AES")
  }

  /**Creates the Iv Parameter Spec
    * to be used for Cipher init
    * @return IvParameterSpec
    * */
  def getIvParameterSpec:IvParameterSpec=new IvParameterSpec(Credentials.IV.getBytes("UTF-8"))
}
