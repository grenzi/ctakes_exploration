

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.textsem;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.ctakes.typesystem.type.refsem.Attribute;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class Modifier extends IdentifiedAnnotation {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(Modifier.class);
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
  protected Modifier() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public Modifier(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public Modifier(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** @generated */  
  public Modifier(JCas jcas, int begin, int end) {
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
  //* Feature: normalizedForm

  /** getter for normalizedForm - gets 
   * @generated */
  public Attribute getNormalizedForm() {
    if (Modifier_Type.featOkTst && ((Modifier_Type)jcasType).casFeat_normalizedForm == null)
      jcasType.jcas.throwFeatMissing("normalizedForm", "org.apache.ctakes.typesystem.type.textsem.Modifier");
    return (Attribute)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((Modifier_Type)jcasType).casFeatCode_normalizedForm)));}
    
  /** setter for normalizedForm - sets  
   * @generated */
  public void setNormalizedForm(Attribute v) {
    if (Modifier_Type.featOkTst && ((Modifier_Type)jcasType).casFeat_normalizedForm == null)
      jcasType.jcas.throwFeatMissing("normalizedForm", "org.apache.ctakes.typesystem.type.textsem.Modifier");
    jcasType.ll_cas.ll_setRefValue(addr, ((Modifier_Type)jcasType).casFeatCode_normalizedForm, jcasType.ll_cas.ll_getFSRef(v));}    
   
    
  //*--------------*
  //* Feature: category

  /** getter for category - gets 
   * @generated */
  public String getCategory() {
    if (Modifier_Type.featOkTst && ((Modifier_Type)jcasType).casFeat_category == null)
      jcasType.jcas.throwFeatMissing("category", "org.apache.ctakes.typesystem.type.textsem.Modifier");
    return jcasType.ll_cas.ll_getStringValue(addr, ((Modifier_Type)jcasType).casFeatCode_category);}
    
  /** setter for category - sets  
   * @generated */
  public void setCategory(String v) {
    if (Modifier_Type.featOkTst && ((Modifier_Type)jcasType).casFeat_category == null)
      jcasType.jcas.throwFeatMissing("category", "org.apache.ctakes.typesystem.type.textsem.Modifier");
    jcasType.ll_cas.ll_setStringValue(addr, ((Modifier_Type)jcasType).casFeatCode_category, v);}    
  }

    