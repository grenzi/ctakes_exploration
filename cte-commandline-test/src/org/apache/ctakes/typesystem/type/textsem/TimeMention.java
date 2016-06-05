

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.textsem;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.ctakes.typesystem.type.refsem.Time;
import org.apache.ctakes.typesystem.type.refsem.Date;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class TimeMention extends IdentifiedAnnotation {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(TimeMention.class);
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
  protected TimeMention() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public TimeMention(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public TimeMention(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** @generated */  
  public TimeMention(JCas jcas, int begin, int end) {
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
  //* Feature: date

  /** getter for date - gets 
   * @generated */
  public Date getDate() {
    if (TimeMention_Type.featOkTst && ((TimeMention_Type)jcasType).casFeat_date == null)
      jcasType.jcas.throwFeatMissing("date", "org.apache.ctakes.typesystem.type.textsem.TimeMention");
    return (Date)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((TimeMention_Type)jcasType).casFeatCode_date)));}
    
  /** setter for date - sets  
   * @generated */
  public void setDate(Date v) {
    if (TimeMention_Type.featOkTst && ((TimeMention_Type)jcasType).casFeat_date == null)
      jcasType.jcas.throwFeatMissing("date", "org.apache.ctakes.typesystem.type.textsem.TimeMention");
    jcasType.ll_cas.ll_setRefValue(addr, ((TimeMention_Type)jcasType).casFeatCode_date, jcasType.ll_cas.ll_getFSRef(v));}    
   
    
  //*--------------*
  //* Feature: time

  /** getter for time - gets 
   * @generated */
  public Time getTime() {
    if (TimeMention_Type.featOkTst && ((TimeMention_Type)jcasType).casFeat_time == null)
      jcasType.jcas.throwFeatMissing("time", "org.apache.ctakes.typesystem.type.textsem.TimeMention");
    return (Time)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((TimeMention_Type)jcasType).casFeatCode_time)));}
    
  /** setter for time - sets  
   * @generated */
  public void setTime(Time v) {
    if (TimeMention_Type.featOkTst && ((TimeMention_Type)jcasType).casFeat_time == null)
      jcasType.jcas.throwFeatMissing("time", "org.apache.ctakes.typesystem.type.textsem.TimeMention");
    jcasType.ll_cas.ll_setRefValue(addr, ((TimeMention_Type)jcasType).casFeatCode_time, jcasType.ll_cas.ll_getFSRef(v));}    
   
    
  //*--------------*
  //* Feature: timeClass

  /** getter for timeClass - gets 
   * @generated */
  public String getTimeClass() {
    if (TimeMention_Type.featOkTst && ((TimeMention_Type)jcasType).casFeat_timeClass == null)
      jcasType.jcas.throwFeatMissing("timeClass", "org.apache.ctakes.typesystem.type.textsem.TimeMention");
    return jcasType.ll_cas.ll_getStringValue(addr, ((TimeMention_Type)jcasType).casFeatCode_timeClass);}
    
  /** setter for timeClass - sets  
   * @generated */
  public void setTimeClass(String v) {
    if (TimeMention_Type.featOkTst && ((TimeMention_Type)jcasType).casFeat_timeClass == null)
      jcasType.jcas.throwFeatMissing("timeClass", "org.apache.ctakes.typesystem.type.textsem.TimeMention");
    jcasType.ll_cas.ll_setStringValue(addr, ((TimeMention_Type)jcasType).casFeatCode_timeClass, v);}    
  }

    