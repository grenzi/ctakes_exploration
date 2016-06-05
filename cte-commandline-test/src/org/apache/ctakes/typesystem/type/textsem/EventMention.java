

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.textsem;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.ctakes.typesystem.type.refsem.Event;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class EventMention extends IdentifiedAnnotation {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(EventMention.class);
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
  protected EventMention() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public EventMention(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public EventMention(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** @generated */  
  public EventMention(JCas jcas, int begin, int end) {
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
  //* Feature: event

  /** getter for event - gets 
   * @generated */
  public Event getEvent() {
    if (EventMention_Type.featOkTst && ((EventMention_Type)jcasType).casFeat_event == null)
      jcasType.jcas.throwFeatMissing("event", "org.apache.ctakes.typesystem.type.textsem.EventMention");
    return (Event)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((EventMention_Type)jcasType).casFeatCode_event)));}
    
  /** setter for event - sets  
   * @generated */
  public void setEvent(Event v) {
    if (EventMention_Type.featOkTst && ((EventMention_Type)jcasType).casFeat_event == null)
      jcasType.jcas.throwFeatMissing("event", "org.apache.ctakes.typesystem.type.textsem.EventMention");
    jcasType.ll_cas.ll_setRefValue(addr, ((EventMention_Type)jcasType).casFeatCode_event, jcasType.ll_cas.ll_getFSRef(v));}    
  }

    