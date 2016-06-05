

/* First created by JCasGen Sat Jun 04 22:42:38 CDT 2016 */
package org.apache.ctakes.typesystem.type.refsem;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;



/** 
 * Updated by JCasGen Sat Jun 04 22:42:38 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class MedicationStatusChange extends Attribute {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(MedicationStatusChange.class);
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
  protected MedicationStatusChange() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public MedicationStatusChange(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public MedicationStatusChange(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** <!-- begin-user-doc -->
    * Write your own initialization here
    * <!-- end-user-doc -->
  @generated modifiable */
  private void readObject() {/*default - does nothing empty block */}
     
 
    
  //*--------------*
  //* Feature: value

  /** getter for value - gets 
   * @generated */
  public String getValue() {
    if (MedicationStatusChange_Type.featOkTst && ((MedicationStatusChange_Type)jcasType).casFeat_value == null)
      jcasType.jcas.throwFeatMissing("value", "org.apache.ctakes.typesystem.type.refsem.MedicationStatusChange");
    return jcasType.ll_cas.ll_getStringValue(addr, ((MedicationStatusChange_Type)jcasType).casFeatCode_value);}
    
  /** setter for value - sets  
   * @generated */
  public void setValue(String v) {
    if (MedicationStatusChange_Type.featOkTst && ((MedicationStatusChange_Type)jcasType).casFeat_value == null)
      jcasType.jcas.throwFeatMissing("value", "org.apache.ctakes.typesystem.type.refsem.MedicationStatusChange");
    jcasType.ll_cas.ll_setStringValue(addr, ((MedicationStatusChange_Type)jcasType).casFeatCode_value, v);}    
  }

    