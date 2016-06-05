

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.syntax;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.uima.jcas.cas.FSList;
import org.apache.uima.jcas.tcas.Annotation;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class BaseToken extends Annotation {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(BaseToken.class);
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
  protected BaseToken() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public BaseToken(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public BaseToken(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** @generated */  
  public BaseToken(JCas jcas, int begin, int end) {
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
  //* Feature: tokenNumber

  /** getter for tokenNumber - gets 
   * @generated */
  public int getTokenNumber() {
    if (BaseToken_Type.featOkTst && ((BaseToken_Type)jcasType).casFeat_tokenNumber == null)
      jcasType.jcas.throwFeatMissing("tokenNumber", "org.apache.ctakes.typesystem.type.syntax.BaseToken");
    return jcasType.ll_cas.ll_getIntValue(addr, ((BaseToken_Type)jcasType).casFeatCode_tokenNumber);}
    
  /** setter for tokenNumber - sets  
   * @generated */
  public void setTokenNumber(int v) {
    if (BaseToken_Type.featOkTst && ((BaseToken_Type)jcasType).casFeat_tokenNumber == null)
      jcasType.jcas.throwFeatMissing("tokenNumber", "org.apache.ctakes.typesystem.type.syntax.BaseToken");
    jcasType.ll_cas.ll_setIntValue(addr, ((BaseToken_Type)jcasType).casFeatCode_tokenNumber, v);}    
   
    
  //*--------------*
  //* Feature: normalizedForm

  /** getter for normalizedForm - gets 
   * @generated */
  public String getNormalizedForm() {
    if (BaseToken_Type.featOkTst && ((BaseToken_Type)jcasType).casFeat_normalizedForm == null)
      jcasType.jcas.throwFeatMissing("normalizedForm", "org.apache.ctakes.typesystem.type.syntax.BaseToken");
    return jcasType.ll_cas.ll_getStringValue(addr, ((BaseToken_Type)jcasType).casFeatCode_normalizedForm);}
    
  /** setter for normalizedForm - sets  
   * @generated */
  public void setNormalizedForm(String v) {
    if (BaseToken_Type.featOkTst && ((BaseToken_Type)jcasType).casFeat_normalizedForm == null)
      jcasType.jcas.throwFeatMissing("normalizedForm", "org.apache.ctakes.typesystem.type.syntax.BaseToken");
    jcasType.ll_cas.ll_setStringValue(addr, ((BaseToken_Type)jcasType).casFeatCode_normalizedForm, v);}    
   
    
  //*--------------*
  //* Feature: partOfSpeech

  /** getter for partOfSpeech - gets 
   * @generated */
  public String getPartOfSpeech() {
    if (BaseToken_Type.featOkTst && ((BaseToken_Type)jcasType).casFeat_partOfSpeech == null)
      jcasType.jcas.throwFeatMissing("partOfSpeech", "org.apache.ctakes.typesystem.type.syntax.BaseToken");
    return jcasType.ll_cas.ll_getStringValue(addr, ((BaseToken_Type)jcasType).casFeatCode_partOfSpeech);}
    
  /** setter for partOfSpeech - sets  
   * @generated */
  public void setPartOfSpeech(String v) {
    if (BaseToken_Type.featOkTst && ((BaseToken_Type)jcasType).casFeat_partOfSpeech == null)
      jcasType.jcas.throwFeatMissing("partOfSpeech", "org.apache.ctakes.typesystem.type.syntax.BaseToken");
    jcasType.ll_cas.ll_setStringValue(addr, ((BaseToken_Type)jcasType).casFeatCode_partOfSpeech, v);}    
   
    
  //*--------------*
  //* Feature: lemmaEntries

  /** getter for lemmaEntries - gets 
   * @generated */
  public FSList getLemmaEntries() {
    if (BaseToken_Type.featOkTst && ((BaseToken_Type)jcasType).casFeat_lemmaEntries == null)
      jcasType.jcas.throwFeatMissing("lemmaEntries", "org.apache.ctakes.typesystem.type.syntax.BaseToken");
    return (FSList)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((BaseToken_Type)jcasType).casFeatCode_lemmaEntries)));}
    
  /** setter for lemmaEntries - sets  
   * @generated */
  public void setLemmaEntries(FSList v) {
    if (BaseToken_Type.featOkTst && ((BaseToken_Type)jcasType).casFeat_lemmaEntries == null)
      jcasType.jcas.throwFeatMissing("lemmaEntries", "org.apache.ctakes.typesystem.type.syntax.BaseToken");
    jcasType.ll_cas.ll_setRefValue(addr, ((BaseToken_Type)jcasType).casFeatCode_lemmaEntries, jcasType.ll_cas.ll_getFSRef(v));}    
  }

    