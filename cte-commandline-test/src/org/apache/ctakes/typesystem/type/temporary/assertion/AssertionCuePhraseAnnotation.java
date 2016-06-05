

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.temporary.assertion;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.uima.jcas.tcas.Annotation;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class AssertionCuePhraseAnnotation extends Annotation {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(AssertionCuePhraseAnnotation.class);
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
  protected AssertionCuePhraseAnnotation() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public AssertionCuePhraseAnnotation(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public AssertionCuePhraseAnnotation(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** @generated */  
  public AssertionCuePhraseAnnotation(JCas jcas, int begin, int end) {
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
  //* Feature: id

  /** getter for id - gets 
   * @generated */
  public int getId() {
    if (AssertionCuePhraseAnnotation_Type.featOkTst && ((AssertionCuePhraseAnnotation_Type)jcasType).casFeat_id == null)
      jcasType.jcas.throwFeatMissing("id", "org.apache.ctakes.typesystem.type.temporary.assertion.AssertionCuePhraseAnnotation");
    return jcasType.ll_cas.ll_getIntValue(addr, ((AssertionCuePhraseAnnotation_Type)jcasType).casFeatCode_id);}
    
  /** setter for id - sets  
   * @generated */
  public void setId(int v) {
    if (AssertionCuePhraseAnnotation_Type.featOkTst && ((AssertionCuePhraseAnnotation_Type)jcasType).casFeat_id == null)
      jcasType.jcas.throwFeatMissing("id", "org.apache.ctakes.typesystem.type.temporary.assertion.AssertionCuePhraseAnnotation");
    jcasType.ll_cas.ll_setIntValue(addr, ((AssertionCuePhraseAnnotation_Type)jcasType).casFeatCode_id, v);}    
   
    
  //*--------------*
  //* Feature: cuePhraseCategory

  /** getter for cuePhraseCategory - gets 
   * @generated */
  public String getCuePhraseCategory() {
    if (AssertionCuePhraseAnnotation_Type.featOkTst && ((AssertionCuePhraseAnnotation_Type)jcasType).casFeat_cuePhraseCategory == null)
      jcasType.jcas.throwFeatMissing("cuePhraseCategory", "org.apache.ctakes.typesystem.type.temporary.assertion.AssertionCuePhraseAnnotation");
    return jcasType.ll_cas.ll_getStringValue(addr, ((AssertionCuePhraseAnnotation_Type)jcasType).casFeatCode_cuePhraseCategory);}
    
  /** setter for cuePhraseCategory - sets  
   * @generated */
  public void setCuePhraseCategory(String v) {
    if (AssertionCuePhraseAnnotation_Type.featOkTst && ((AssertionCuePhraseAnnotation_Type)jcasType).casFeat_cuePhraseCategory == null)
      jcasType.jcas.throwFeatMissing("cuePhraseCategory", "org.apache.ctakes.typesystem.type.temporary.assertion.AssertionCuePhraseAnnotation");
    jcasType.ll_cas.ll_setStringValue(addr, ((AssertionCuePhraseAnnotation_Type)jcasType).casFeatCode_cuePhraseCategory, v);}    
   
    
  //*--------------*
  //* Feature: cuePhraseAssertionFamily

  /** getter for cuePhraseAssertionFamily - gets 
   * @generated */
  public String getCuePhraseAssertionFamily() {
    if (AssertionCuePhraseAnnotation_Type.featOkTst && ((AssertionCuePhraseAnnotation_Type)jcasType).casFeat_cuePhraseAssertionFamily == null)
      jcasType.jcas.throwFeatMissing("cuePhraseAssertionFamily", "org.apache.ctakes.typesystem.type.temporary.assertion.AssertionCuePhraseAnnotation");
    return jcasType.ll_cas.ll_getStringValue(addr, ((AssertionCuePhraseAnnotation_Type)jcasType).casFeatCode_cuePhraseAssertionFamily);}
    
  /** setter for cuePhraseAssertionFamily - sets  
   * @generated */
  public void setCuePhraseAssertionFamily(String v) {
    if (AssertionCuePhraseAnnotation_Type.featOkTst && ((AssertionCuePhraseAnnotation_Type)jcasType).casFeat_cuePhraseAssertionFamily == null)
      jcasType.jcas.throwFeatMissing("cuePhraseAssertionFamily", "org.apache.ctakes.typesystem.type.temporary.assertion.AssertionCuePhraseAnnotation");
    jcasType.ll_cas.ll_setStringValue(addr, ((AssertionCuePhraseAnnotation_Type)jcasType).casFeatCode_cuePhraseAssertionFamily, v);}    
   
    
  //*--------------*
  //* Feature: cuePhraseFirstWord

  /** getter for cuePhraseFirstWord - gets 
   * @generated */
  public String getCuePhraseFirstWord() {
    if (AssertionCuePhraseAnnotation_Type.featOkTst && ((AssertionCuePhraseAnnotation_Type)jcasType).casFeat_cuePhraseFirstWord == null)
      jcasType.jcas.throwFeatMissing("cuePhraseFirstWord", "org.apache.ctakes.typesystem.type.temporary.assertion.AssertionCuePhraseAnnotation");
    return jcasType.ll_cas.ll_getStringValue(addr, ((AssertionCuePhraseAnnotation_Type)jcasType).casFeatCode_cuePhraseFirstWord);}
    
  /** setter for cuePhraseFirstWord - sets  
   * @generated */
  public void setCuePhraseFirstWord(String v) {
    if (AssertionCuePhraseAnnotation_Type.featOkTst && ((AssertionCuePhraseAnnotation_Type)jcasType).casFeat_cuePhraseFirstWord == null)
      jcasType.jcas.throwFeatMissing("cuePhraseFirstWord", "org.apache.ctakes.typesystem.type.temporary.assertion.AssertionCuePhraseAnnotation");
    jcasType.ll_cas.ll_setStringValue(addr, ((AssertionCuePhraseAnnotation_Type)jcasType).casFeatCode_cuePhraseFirstWord, v);}    
   
    
  //*--------------*
  //* Feature: cuePhrase

  /** getter for cuePhrase - gets 
   * @generated */
  public String getCuePhrase() {
    if (AssertionCuePhraseAnnotation_Type.featOkTst && ((AssertionCuePhraseAnnotation_Type)jcasType).casFeat_cuePhrase == null)
      jcasType.jcas.throwFeatMissing("cuePhrase", "org.apache.ctakes.typesystem.type.temporary.assertion.AssertionCuePhraseAnnotation");
    return jcasType.ll_cas.ll_getStringValue(addr, ((AssertionCuePhraseAnnotation_Type)jcasType).casFeatCode_cuePhrase);}
    
  /** setter for cuePhrase - sets  
   * @generated */
  public void setCuePhrase(String v) {
    if (AssertionCuePhraseAnnotation_Type.featOkTst && ((AssertionCuePhraseAnnotation_Type)jcasType).casFeat_cuePhrase == null)
      jcasType.jcas.throwFeatMissing("cuePhrase", "org.apache.ctakes.typesystem.type.temporary.assertion.AssertionCuePhraseAnnotation");
    jcasType.ll_cas.ll_setStringValue(addr, ((AssertionCuePhraseAnnotation_Type)jcasType).casFeatCode_cuePhrase, v);}    
  }

    