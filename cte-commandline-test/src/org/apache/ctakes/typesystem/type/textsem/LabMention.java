

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.textsem;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.ctakes.typesystem.type.relation.ResultOfTextRelation;
import org.apache.ctakes.typesystem.type.relation.DegreeOfTextRelation;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class LabMention extends EventMention {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(LabMention.class);
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
  protected LabMention() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public LabMention(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public LabMention(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** @generated */  
  public LabMention(JCas jcas, int begin, int end) {
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
  //* Feature: abnormalInterpretation

  /** getter for abnormalInterpretation - gets 
   * @generated */
  public DegreeOfTextRelation getAbnormalInterpretation() {
    if (LabMention_Type.featOkTst && ((LabMention_Type)jcasType).casFeat_abnormalInterpretation == null)
      jcasType.jcas.throwFeatMissing("abnormalInterpretation", "org.apache.ctakes.typesystem.type.textsem.LabMention");
    return (DegreeOfTextRelation)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((LabMention_Type)jcasType).casFeatCode_abnormalInterpretation)));}
    
  /** setter for abnormalInterpretation - sets  
   * @generated */
  public void setAbnormalInterpretation(DegreeOfTextRelation v) {
    if (LabMention_Type.featOkTst && ((LabMention_Type)jcasType).casFeat_abnormalInterpretation == null)
      jcasType.jcas.throwFeatMissing("abnormalInterpretation", "org.apache.ctakes.typesystem.type.textsem.LabMention");
    jcasType.ll_cas.ll_setRefValue(addr, ((LabMention_Type)jcasType).casFeatCode_abnormalInterpretation, jcasType.ll_cas.ll_getFSRef(v));}    
   
    
  //*--------------*
  //* Feature: deltaFlag

  /** getter for deltaFlag - gets 
   * @generated */
  public LabDeltaFlagModifier getDeltaFlag() {
    if (LabMention_Type.featOkTst && ((LabMention_Type)jcasType).casFeat_deltaFlag == null)
      jcasType.jcas.throwFeatMissing("deltaFlag", "org.apache.ctakes.typesystem.type.textsem.LabMention");
    return (LabDeltaFlagModifier)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((LabMention_Type)jcasType).casFeatCode_deltaFlag)));}
    
  /** setter for deltaFlag - sets  
   * @generated */
  public void setDeltaFlag(LabDeltaFlagModifier v) {
    if (LabMention_Type.featOkTst && ((LabMention_Type)jcasType).casFeat_deltaFlag == null)
      jcasType.jcas.throwFeatMissing("deltaFlag", "org.apache.ctakes.typesystem.type.textsem.LabMention");
    jcasType.ll_cas.ll_setRefValue(addr, ((LabMention_Type)jcasType).casFeatCode_deltaFlag, jcasType.ll_cas.ll_getFSRef(v));}    
   
    
  //*--------------*
  //* Feature: labValue

  /** getter for labValue - gets 
   * @generated */
  public ResultOfTextRelation getLabValue() {
    if (LabMention_Type.featOkTst && ((LabMention_Type)jcasType).casFeat_labValue == null)
      jcasType.jcas.throwFeatMissing("labValue", "org.apache.ctakes.typesystem.type.textsem.LabMention");
    return (ResultOfTextRelation)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((LabMention_Type)jcasType).casFeatCode_labValue)));}
    
  /** setter for labValue - sets  
   * @generated */
  public void setLabValue(ResultOfTextRelation v) {
    if (LabMention_Type.featOkTst && ((LabMention_Type)jcasType).casFeat_labValue == null)
      jcasType.jcas.throwFeatMissing("labValue", "org.apache.ctakes.typesystem.type.textsem.LabMention");
    jcasType.ll_cas.ll_setRefValue(addr, ((LabMention_Type)jcasType).casFeatCode_labValue, jcasType.ll_cas.ll_getFSRef(v));}    
   
    
  //*--------------*
  //* Feature: ordinalInterpretation

  /** getter for ordinalInterpretation - gets 
   * @generated */
  public DegreeOfTextRelation getOrdinalInterpretation() {
    if (LabMention_Type.featOkTst && ((LabMention_Type)jcasType).casFeat_ordinalInterpretation == null)
      jcasType.jcas.throwFeatMissing("ordinalInterpretation", "org.apache.ctakes.typesystem.type.textsem.LabMention");
    return (DegreeOfTextRelation)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((LabMention_Type)jcasType).casFeatCode_ordinalInterpretation)));}
    
  /** setter for ordinalInterpretation - sets  
   * @generated */
  public void setOrdinalInterpretation(DegreeOfTextRelation v) {
    if (LabMention_Type.featOkTst && ((LabMention_Type)jcasType).casFeat_ordinalInterpretation == null)
      jcasType.jcas.throwFeatMissing("ordinalInterpretation", "org.apache.ctakes.typesystem.type.textsem.LabMention");
    jcasType.ll_cas.ll_setRefValue(addr, ((LabMention_Type)jcasType).casFeatCode_ordinalInterpretation, jcasType.ll_cas.ll_getFSRef(v));}    
   
    
  //*--------------*
  //* Feature: referenceRangeNarrative

  /** getter for referenceRangeNarrative - gets 
   * @generated */
  public LabReferenceRangeModifier getReferenceRangeNarrative() {
    if (LabMention_Type.featOkTst && ((LabMention_Type)jcasType).casFeat_referenceRangeNarrative == null)
      jcasType.jcas.throwFeatMissing("referenceRangeNarrative", "org.apache.ctakes.typesystem.type.textsem.LabMention");
    return (LabReferenceRangeModifier)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((LabMention_Type)jcasType).casFeatCode_referenceRangeNarrative)));}
    
  /** setter for referenceRangeNarrative - sets  
   * @generated */
  public void setReferenceRangeNarrative(LabReferenceRangeModifier v) {
    if (LabMention_Type.featOkTst && ((LabMention_Type)jcasType).casFeat_referenceRangeNarrative == null)
      jcasType.jcas.throwFeatMissing("referenceRangeNarrative", "org.apache.ctakes.typesystem.type.textsem.LabMention");
    jcasType.ll_cas.ll_setRefValue(addr, ((LabMention_Type)jcasType).casFeatCode_referenceRangeNarrative, jcasType.ll_cas.ll_getFSRef(v));}    
  }

    