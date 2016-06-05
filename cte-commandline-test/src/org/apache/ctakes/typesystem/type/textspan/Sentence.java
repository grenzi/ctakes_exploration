

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.textspan;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.uima.jcas.tcas.Annotation;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class Sentence extends Annotation {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(Sentence.class);
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int type = typeIndexID;
  /** @generated  */
  @Override
  public              int getTypeIndexID() {return typeIndexID;}
 
  /** Never called.  Disable default constructor
   * @generated */
  protected Sentence() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public Sentence(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public Sentence(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** @generated */  
  public Sentence(JCas jcas, int begin, int end) {
    super(jcas);
    setBegin(begin);
    setEnd(end);
    readObject();
  }   

  /** <!-- begin-user-doc -->
    * Write your own initialization here
    * <!-- end-user-doc -->
  @generated modifiable */
  private void readObject() {/*default - does nothing empty block */}
     
 
    
  //*--------------*
  //* Feature: sentenceNumber

  /** getter for sentenceNumber - gets 
   * @generated */
  public int getSentenceNumber() {
    if (Sentence_Type.featOkTst && ((Sentence_Type)jcasType).casFeat_sentenceNumber == null)
      jcasType.jcas.throwFeatMissing("sentenceNumber", "org.apache.ctakes.typesystem.type.textspan.Sentence");
    return jcasType.ll_cas.ll_getIntValue(addr, ((Sentence_Type)jcasType).casFeatCode_sentenceNumber);}
    
  /** setter for sentenceNumber - sets  
   * @generated */
  public void setSentenceNumber(int v) {
    if (Sentence_Type.featOkTst && ((Sentence_Type)jcasType).casFeat_sentenceNumber == null)
      jcasType.jcas.throwFeatMissing("sentenceNumber", "org.apache.ctakes.typesystem.type.textspan.Sentence");
    jcasType.ll_cas.ll_setIntValue(addr, ((Sentence_Type)jcasType).casFeatCode_sentenceNumber, v);}    
   
    
  //*--------------*
  //* Feature: segmentId

  /** getter for segmentId - gets 
   * @generated */
  public String getSegmentId() {
    if (Sentence_Type.featOkTst && ((Sentence_Type)jcasType).casFeat_segmentId == null)
      jcasType.jcas.throwFeatMissing("segmentId", "org.apache.ctakes.typesystem.type.textspan.Sentence");
    return jcasType.ll_cas.ll_getStringValue(addr, ((Sentence_Type)jcasType).casFeatCode_segmentId);}
    
  /** setter for segmentId - sets  
   * @generated */
  public void setSegmentId(String v) {
    if (Sentence_Type.featOkTst && ((Sentence_Type)jcasType).casFeat_segmentId == null)
      jcasType.jcas.throwFeatMissing("segmentId", "org.apache.ctakes.typesystem.type.textspan.Sentence");
    jcasType.ll_cas.ll_setStringValue(addr, ((Sentence_Type)jcasType).casFeatCode_segmentId, v);}    
  }

    