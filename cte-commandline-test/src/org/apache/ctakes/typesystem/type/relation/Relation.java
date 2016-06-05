

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.relation;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.uima.jcas.cas.TOP;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class Relation extends TOP {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(Relation.class);
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
  protected Relation() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public Relation(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public Relation(JCas jcas) {
    super(jcas);
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
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_id == null)
      jcasType.jcas.throwFeatMissing("id", "org.apache.ctakes.typesystem.type.relation.Relation");
    return jcasType.ll_cas.ll_getIntValue(addr, ((Relation_Type)jcasType).casFeatCode_id);}
    
  /** setter for id - sets  
   * @generated */
  public void setId(int v) {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_id == null)
      jcasType.jcas.throwFeatMissing("id", "org.apache.ctakes.typesystem.type.relation.Relation");
    jcasType.ll_cas.ll_setIntValue(addr, ((Relation_Type)jcasType).casFeatCode_id, v);}    
   
    
  //*--------------*
  //* Feature: category

  /** getter for category - gets 
   * @generated */
  public String getCategory() {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_category == null)
      jcasType.jcas.throwFeatMissing("category", "org.apache.ctakes.typesystem.type.relation.Relation");
    return jcasType.ll_cas.ll_getStringValue(addr, ((Relation_Type)jcasType).casFeatCode_category);}
    
  /** setter for category - sets  
   * @generated */
  public void setCategory(String v) {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_category == null)
      jcasType.jcas.throwFeatMissing("category", "org.apache.ctakes.typesystem.type.relation.Relation");
    jcasType.ll_cas.ll_setStringValue(addr, ((Relation_Type)jcasType).casFeatCode_category, v);}    
   
    
  //*--------------*
  //* Feature: discoveryTechnique

  /** getter for discoveryTechnique - gets 
   * @generated */
  public int getDiscoveryTechnique() {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_discoveryTechnique == null)
      jcasType.jcas.throwFeatMissing("discoveryTechnique", "org.apache.ctakes.typesystem.type.relation.Relation");
    return jcasType.ll_cas.ll_getIntValue(addr, ((Relation_Type)jcasType).casFeatCode_discoveryTechnique);}
    
  /** setter for discoveryTechnique - sets  
   * @generated */
  public void setDiscoveryTechnique(int v) {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_discoveryTechnique == null)
      jcasType.jcas.throwFeatMissing("discoveryTechnique", "org.apache.ctakes.typesystem.type.relation.Relation");
    jcasType.ll_cas.ll_setIntValue(addr, ((Relation_Type)jcasType).casFeatCode_discoveryTechnique, v);}    
   
    
  //*--------------*
  //* Feature: confidence

  /** getter for confidence - gets 
   * @generated */
  public double getConfidence() {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_confidence == null)
      jcasType.jcas.throwFeatMissing("confidence", "org.apache.ctakes.typesystem.type.relation.Relation");
    return jcasType.ll_cas.ll_getDoubleValue(addr, ((Relation_Type)jcasType).casFeatCode_confidence);}
    
  /** setter for confidence - sets  
   * @generated */
  public void setConfidence(double v) {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_confidence == null)
      jcasType.jcas.throwFeatMissing("confidence", "org.apache.ctakes.typesystem.type.relation.Relation");
    jcasType.ll_cas.ll_setDoubleValue(addr, ((Relation_Type)jcasType).casFeatCode_confidence, v);}    
   
    
  //*--------------*
  //* Feature: polarity

  /** getter for polarity - gets 
   * @generated */
  public int getPolarity() {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_polarity == null)
      jcasType.jcas.throwFeatMissing("polarity", "org.apache.ctakes.typesystem.type.relation.Relation");
    return jcasType.ll_cas.ll_getIntValue(addr, ((Relation_Type)jcasType).casFeatCode_polarity);}
    
  /** setter for polarity - sets  
   * @generated */
  public void setPolarity(int v) {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_polarity == null)
      jcasType.jcas.throwFeatMissing("polarity", "org.apache.ctakes.typesystem.type.relation.Relation");
    jcasType.ll_cas.ll_setIntValue(addr, ((Relation_Type)jcasType).casFeatCode_polarity, v);}    
   
    
  //*--------------*
  //* Feature: uncertainty

  /** getter for uncertainty - gets 
   * @generated */
  public int getUncertainty() {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_uncertainty == null)
      jcasType.jcas.throwFeatMissing("uncertainty", "org.apache.ctakes.typesystem.type.relation.Relation");
    return jcasType.ll_cas.ll_getIntValue(addr, ((Relation_Type)jcasType).casFeatCode_uncertainty);}
    
  /** setter for uncertainty - sets  
   * @generated */
  public void setUncertainty(int v) {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_uncertainty == null)
      jcasType.jcas.throwFeatMissing("uncertainty", "org.apache.ctakes.typesystem.type.relation.Relation");
    jcasType.ll_cas.ll_setIntValue(addr, ((Relation_Type)jcasType).casFeatCode_uncertainty, v);}    
   
    
  //*--------------*
  //* Feature: conditional

  /** getter for conditional - gets 
   * @generated */
  public boolean getConditional() {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_conditional == null)
      jcasType.jcas.throwFeatMissing("conditional", "org.apache.ctakes.typesystem.type.relation.Relation");
    return jcasType.ll_cas.ll_getBooleanValue(addr, ((Relation_Type)jcasType).casFeatCode_conditional);}
    
  /** setter for conditional - sets  
   * @generated */
  public void setConditional(boolean v) {
    if (Relation_Type.featOkTst && ((Relation_Type)jcasType).casFeat_conditional == null)
      jcasType.jcas.throwFeatMissing("conditional", "org.apache.ctakes.typesystem.type.relation.Relation");
    jcasType.ll_cas.ll_setBooleanValue(addr, ((Relation_Type)jcasType).casFeatCode_conditional, v);}    
  }

    