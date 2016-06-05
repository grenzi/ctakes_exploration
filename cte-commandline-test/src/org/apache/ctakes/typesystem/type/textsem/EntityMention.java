

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.textsem;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.ctakes.typesystem.type.refsem.Entity;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class EntityMention extends IdentifiedAnnotation {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(EntityMention.class);
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
  protected EntityMention() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public EntityMention(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public EntityMention(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** @generated */  
  public EntityMention(JCas jcas, int begin, int end) {
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
  //* Feature: entity

  /** getter for entity - gets 
   * @generated */
  public Entity getEntity() {
    if (EntityMention_Type.featOkTst && ((EntityMention_Type)jcasType).casFeat_entity == null)
      jcasType.jcas.throwFeatMissing("entity", "org.apache.ctakes.typesystem.type.textsem.EntityMention");
    return (Entity)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((EntityMention_Type)jcasType).casFeatCode_entity)));}
    
  /** setter for entity - sets  
   * @generated */
  public void setEntity(Entity v) {
    if (EntityMention_Type.featOkTst && ((EntityMention_Type)jcasType).casFeat_entity == null)
      jcasType.jcas.throwFeatMissing("entity", "org.apache.ctakes.typesystem.type.textsem.EntityMention");
    jcasType.ll_cas.ll_setRefValue(addr, ((EntityMention_Type)jcasType).casFeatCode_entity, jcasType.ll_cas.ll_getFSRef(v));}    
  }

    