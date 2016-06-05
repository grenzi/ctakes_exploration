

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.structured;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.uima.jcas.cas.TOP;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class DocumentClassification extends TOP {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(DocumentClassification.class);
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
  protected DocumentClassification() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public DocumentClassification(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public DocumentClassification(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** <!-- begin-user-doc -->
    * Write your own initialization here
    * <!-- end-user-doc -->
  @generated modifiable */
  private void readObject() {/*default - does nothing empty block */}
     
 
    
  //*--------------*
  //* Feature: label

  /** getter for label - gets 
   * @generated */
  public String getLabel() {
    if (DocumentClassification_Type.featOkTst && ((DocumentClassification_Type)jcasType).casFeat_label == null)
      jcasType.jcas.throwFeatMissing("label", "org.apache.ctakes.typesystem.type.structured.DocumentClassification");
    return jcasType.ll_cas.ll_getStringValue(addr, ((DocumentClassification_Type)jcasType).casFeatCode_label);}
    
  /** setter for label - sets  
   * @generated */
  public void setLabel(String v) {
    if (DocumentClassification_Type.featOkTst && ((DocumentClassification_Type)jcasType).casFeat_label == null)
      jcasType.jcas.throwFeatMissing("label", "org.apache.ctakes.typesystem.type.structured.DocumentClassification");
    jcasType.ll_cas.ll_setStringValue(addr, ((DocumentClassification_Type)jcasType).casFeatCode_label, v);}    
  }

    