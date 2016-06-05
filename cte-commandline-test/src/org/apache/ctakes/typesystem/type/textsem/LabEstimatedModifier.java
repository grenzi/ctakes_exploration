

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.textsem;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;



/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class LabEstimatedModifier extends Modifier {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(LabEstimatedModifier.class);
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
  protected LabEstimatedModifier() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public LabEstimatedModifier(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public LabEstimatedModifier(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** @generated */  
  public LabEstimatedModifier(JCas jcas, int begin, int end) {
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
  //* Feature: indicated

  /** getter for indicated - gets 
   * @generated */
  public boolean getIndicated() {
    if (LabEstimatedModifier_Type.featOkTst && ((LabEstimatedModifier_Type)jcasType).casFeat_indicated == null)
      jcasType.jcas.throwFeatMissing("indicated", "org.apache.ctakes.typesystem.type.textsem.LabEstimatedModifier");
    return jcasType.ll_cas.ll_getBooleanValue(addr, ((LabEstimatedModifier_Type)jcasType).casFeatCode_indicated);}
    
  /** setter for indicated - sets  
   * @generated */
  public void setIndicated(boolean v) {
    if (LabEstimatedModifier_Type.featOkTst && ((LabEstimatedModifier_Type)jcasType).casFeat_indicated == null)
      jcasType.jcas.throwFeatMissing("indicated", "org.apache.ctakes.typesystem.type.textsem.LabEstimatedModifier");
    jcasType.ll_cas.ll_setBooleanValue(addr, ((LabEstimatedModifier_Type)jcasType).casFeatCode_indicated, v);}    
  }

    