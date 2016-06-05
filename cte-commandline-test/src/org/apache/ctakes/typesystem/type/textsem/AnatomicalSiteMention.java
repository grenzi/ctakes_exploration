

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.textsem;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;



/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class AnatomicalSiteMention extends EntityMention {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(AnatomicalSiteMention.class);
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
  protected AnatomicalSiteMention() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public AnatomicalSiteMention(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public AnatomicalSiteMention(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** @generated */  
  public AnatomicalSiteMention(JCas jcas, int begin, int end) {
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
  //* Feature: bodyLaterality

  /** getter for bodyLaterality - gets 
   * @generated */
  public BodyLateralityModifier getBodyLaterality() {
    if (AnatomicalSiteMention_Type.featOkTst && ((AnatomicalSiteMention_Type)jcasType).casFeat_bodyLaterality == null)
      jcasType.jcas.throwFeatMissing("bodyLaterality", "org.apache.ctakes.typesystem.type.textsem.AnatomicalSiteMention");
    return (BodyLateralityModifier)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((AnatomicalSiteMention_Type)jcasType).casFeatCode_bodyLaterality)));}
    
  /** setter for bodyLaterality - sets  
   * @generated */
  public void setBodyLaterality(BodyLateralityModifier v) {
    if (AnatomicalSiteMention_Type.featOkTst && ((AnatomicalSiteMention_Type)jcasType).casFeat_bodyLaterality == null)
      jcasType.jcas.throwFeatMissing("bodyLaterality", "org.apache.ctakes.typesystem.type.textsem.AnatomicalSiteMention");
    jcasType.ll_cas.ll_setRefValue(addr, ((AnatomicalSiteMention_Type)jcasType).casFeatCode_bodyLaterality, jcasType.ll_cas.ll_getFSRef(v));}    
   
    
  //*--------------*
  //* Feature: bodySide

  /** getter for bodySide - gets 
   * @generated */
  public BodySideModifier getBodySide() {
    if (AnatomicalSiteMention_Type.featOkTst && ((AnatomicalSiteMention_Type)jcasType).casFeat_bodySide == null)
      jcasType.jcas.throwFeatMissing("bodySide", "org.apache.ctakes.typesystem.type.textsem.AnatomicalSiteMention");
    return (BodySideModifier)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((AnatomicalSiteMention_Type)jcasType).casFeatCode_bodySide)));}
    
  /** setter for bodySide - sets  
   * @generated */
  public void setBodySide(BodySideModifier v) {
    if (AnatomicalSiteMention_Type.featOkTst && ((AnatomicalSiteMention_Type)jcasType).casFeat_bodySide == null)
      jcasType.jcas.throwFeatMissing("bodySide", "org.apache.ctakes.typesystem.type.textsem.AnatomicalSiteMention");
    jcasType.ll_cas.ll_setRefValue(addr, ((AnatomicalSiteMention_Type)jcasType).casFeatCode_bodySide, jcasType.ll_cas.ll_getFSRef(v));}    
  }

    