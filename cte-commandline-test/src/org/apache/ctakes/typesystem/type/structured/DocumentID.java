

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
public class DocumentID extends TOP {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(DocumentID.class);
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
  protected DocumentID() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public DocumentID(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public DocumentID(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** <!-- begin-user-doc -->
    * Write your own initialization here
    * <!-- end-user-doc -->
  @generated modifiable */
  private void readObject() {/*default - does nothing empty block */}
     
 
    
  //*--------------*
  //* Feature: documentID

  /** getter for documentID - gets 
   * @generated */
  public String getDocumentID() {
    if (DocumentID_Type.featOkTst && ((DocumentID_Type)jcasType).casFeat_documentID == null)
      jcasType.jcas.throwFeatMissing("documentID", "org.apache.ctakes.typesystem.type.structured.DocumentID");
    return jcasType.ll_cas.ll_getStringValue(addr, ((DocumentID_Type)jcasType).casFeatCode_documentID);}
    
  /** setter for documentID - sets  
   * @generated */
  public void setDocumentID(String v) {
    if (DocumentID_Type.featOkTst && ((DocumentID_Type)jcasType).casFeat_documentID == null)
      jcasType.jcas.throwFeatMissing("documentID", "org.apache.ctakes.typesystem.type.structured.DocumentID");
    jcasType.ll_cas.ll_setStringValue(addr, ((DocumentID_Type)jcasType).casFeatCode_documentID, v);}    
  }

    