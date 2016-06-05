

/* First created by JCasGen Sat Jun 04 22:42:38 CDT 2016 */
package org.apache.ctakes.assertion.medfacts.types;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.uima.jcas.tcas.Annotation;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:38 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class Concept extends Annotation {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(Concept.class);
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
  protected Concept() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public Concept(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public Concept(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** @generated */  
  public Concept(JCas jcas, int begin, int end) {
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
  //* Feature: conceptType

  /** getter for conceptType - gets 
   * @generated */
  public String getConceptType() {
    if (Concept_Type.featOkTst && ((Concept_Type)jcasType).casFeat_conceptType == null)
      jcasType.jcas.throwFeatMissing("conceptType", "org.apache.ctakes.assertion.medfacts.types.Concept");
    return jcasType.ll_cas.ll_getStringValue(addr, ((Concept_Type)jcasType).casFeatCode_conceptType);}
    
  /** setter for conceptType - sets  
   * @generated */
  public void setConceptType(String v) {
    if (Concept_Type.featOkTst && ((Concept_Type)jcasType).casFeat_conceptType == null)
      jcasType.jcas.throwFeatMissing("conceptType", "org.apache.ctakes.assertion.medfacts.types.Concept");
    jcasType.ll_cas.ll_setStringValue(addr, ((Concept_Type)jcasType).casFeatCode_conceptType, v);}    
   
    
  //*--------------*
  //* Feature: conceptText

  /** getter for conceptText - gets 
   * @generated */
  public String getConceptText() {
    if (Concept_Type.featOkTst && ((Concept_Type)jcasType).casFeat_conceptText == null)
      jcasType.jcas.throwFeatMissing("conceptText", "org.apache.ctakes.assertion.medfacts.types.Concept");
    return jcasType.ll_cas.ll_getStringValue(addr, ((Concept_Type)jcasType).casFeatCode_conceptText);}
    
  /** setter for conceptText - sets  
   * @generated */
  public void setConceptText(String v) {
    if (Concept_Type.featOkTst && ((Concept_Type)jcasType).casFeat_conceptText == null)
      jcasType.jcas.throwFeatMissing("conceptText", "org.apache.ctakes.assertion.medfacts.types.Concept");
    jcasType.ll_cas.ll_setStringValue(addr, ((Concept_Type)jcasType).casFeatCode_conceptText, v);}    
   
    
  //*--------------*
  //* Feature: externalId

  /** getter for externalId - gets 
   * @generated */
  public int getExternalId() {
    if (Concept_Type.featOkTst && ((Concept_Type)jcasType).casFeat_externalId == null)
      jcasType.jcas.throwFeatMissing("externalId", "org.apache.ctakes.assertion.medfacts.types.Concept");
    return jcasType.ll_cas.ll_getIntValue(addr, ((Concept_Type)jcasType).casFeatCode_externalId);}
    
  /** setter for externalId - sets  
   * @generated */
  public void setExternalId(int v) {
    if (Concept_Type.featOkTst && ((Concept_Type)jcasType).casFeat_externalId == null)
      jcasType.jcas.throwFeatMissing("externalId", "org.apache.ctakes.assertion.medfacts.types.Concept");
    jcasType.ll_cas.ll_setIntValue(addr, ((Concept_Type)jcasType).casFeatCode_externalId, v);}    
   
    
  //*--------------*
  //* Feature: originalEntityExternalId

  /** getter for originalEntityExternalId - gets 
   * @generated */
  public int getOriginalEntityExternalId() {
    if (Concept_Type.featOkTst && ((Concept_Type)jcasType).casFeat_originalEntityExternalId == null)
      jcasType.jcas.throwFeatMissing("originalEntityExternalId", "org.apache.ctakes.assertion.medfacts.types.Concept");
    return jcasType.ll_cas.ll_getIntValue(addr, ((Concept_Type)jcasType).casFeatCode_originalEntityExternalId);}
    
  /** setter for originalEntityExternalId - sets  
   * @generated */
  public void setOriginalEntityExternalId(int v) {
    if (Concept_Type.featOkTst && ((Concept_Type)jcasType).casFeat_originalEntityExternalId == null)
      jcasType.jcas.throwFeatMissing("originalEntityExternalId", "org.apache.ctakes.assertion.medfacts.types.Concept");
    jcasType.ll_cas.ll_setIntValue(addr, ((Concept_Type)jcasType).casFeatCode_originalEntityExternalId, v);}    
  }

    