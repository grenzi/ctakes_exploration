

/* First created by JCasGen Sat Jun 04 22:42:38 CDT 2016 */
package org.apache.ctakes.typesystem.type.refsem;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.uima.jcas.cas.TOP;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:38 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class OntologyConcept extends TOP {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(OntologyConcept.class);
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
  protected OntologyConcept() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public OntologyConcept(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public OntologyConcept(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** <!-- begin-user-doc -->
    * Write your own initialization here
    * <!-- end-user-doc -->
  @generated modifiable */
  private void readObject() {/*default - does nothing empty block */}
     
 
    
  //*--------------*
  //* Feature: codingScheme

  /** getter for codingScheme - gets 
   * @generated */
  public String getCodingScheme() {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_codingScheme == null)
      jcasType.jcas.throwFeatMissing("codingScheme", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    return jcasType.ll_cas.ll_getStringValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_codingScheme);}
    
  /** setter for codingScheme - sets  
   * @generated */
  public void setCodingScheme(String v) {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_codingScheme == null)
      jcasType.jcas.throwFeatMissing("codingScheme", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    jcasType.ll_cas.ll_setStringValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_codingScheme, v);}    
   
    
  //*--------------*
  //* Feature: code

  /** getter for code - gets 
   * @generated */
  public String getCode() {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_code == null)
      jcasType.jcas.throwFeatMissing("code", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    return jcasType.ll_cas.ll_getStringValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_code);}
    
  /** setter for code - sets  
   * @generated */
  public void setCode(String v) {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_code == null)
      jcasType.jcas.throwFeatMissing("code", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    jcasType.ll_cas.ll_setStringValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_code, v);}    
   
    
  //*--------------*
  //* Feature: oid

  /** getter for oid - gets 
   * @generated */
  public String getOid() {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_oid == null)
      jcasType.jcas.throwFeatMissing("oid", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    return jcasType.ll_cas.ll_getStringValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_oid);}
    
  /** setter for oid - sets  
   * @generated */
  public void setOid(String v) {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_oid == null)
      jcasType.jcas.throwFeatMissing("oid", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    jcasType.ll_cas.ll_setStringValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_oid, v);}    
   
    
  //*--------------*
  //* Feature: oui

  /** getter for oui - gets 
   * @generated */
  public String getOui() {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_oui == null)
      jcasType.jcas.throwFeatMissing("oui", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    return jcasType.ll_cas.ll_getStringValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_oui);}
    
  /** setter for oui - sets  
   * @generated */
  public void setOui(String v) {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_oui == null)
      jcasType.jcas.throwFeatMissing("oui", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    jcasType.ll_cas.ll_setStringValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_oui, v);}    
   
    
  //*--------------*
  //* Feature: score

  /** getter for score - gets 
   * @generated */
  public double getScore() {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_score == null)
      jcasType.jcas.throwFeatMissing("score", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    return jcasType.ll_cas.ll_getDoubleValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_score);}
    
  /** setter for score - sets  
   * @generated */
  public void setScore(double v) {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_score == null)
      jcasType.jcas.throwFeatMissing("score", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    jcasType.ll_cas.ll_setDoubleValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_score, v);}    
   
    
  //*--------------*
  //* Feature: disambiguated

  /** getter for disambiguated - gets 
   * @generated */
  public boolean getDisambiguated() {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_disambiguated == null)
      jcasType.jcas.throwFeatMissing("disambiguated", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    return jcasType.ll_cas.ll_getBooleanValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_disambiguated);}
    
  /** setter for disambiguated - sets  
   * @generated */
  public void setDisambiguated(boolean v) {
    if (OntologyConcept_Type.featOkTst && ((OntologyConcept_Type)jcasType).casFeat_disambiguated == null)
      jcasType.jcas.throwFeatMissing("disambiguated", "org.apache.ctakes.typesystem.type.refsem.OntologyConcept");
    jcasType.ll_cas.ll_setBooleanValue(addr, ((OntologyConcept_Type)jcasType).casFeatCode_disambiguated, v);}    
  }

    