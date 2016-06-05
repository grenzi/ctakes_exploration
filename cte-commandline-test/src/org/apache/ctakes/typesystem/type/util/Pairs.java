

/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.util;

import org.apache.uima.jcas.JCas; 
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.jcas.cas.TOP_Type;

import org.apache.uima.jcas.cas.FSArray;
import org.apache.uima.jcas.cas.TOP;


/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * XML source: /Users/gage/Documents/Code/ctakes_exploration/cte-commandline-test/ytex.typesystem.xml
 * @generated */
public class Pairs extends TOP {
  /** @generated
   * @ordered 
   */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = JCasRegistry.register(Pairs.class);
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
  protected Pairs() {/* intentionally empty block */}
    
  /** Internal - constructor used by generator 
   * @generated */
  public Pairs(int addr, TOP_Type type) {
    super(addr, type);
    readObject();
  }
  
  /** @generated */
  public Pairs(JCas jcas) {
    super(jcas);
    readObject();   
  } 

  /** <!-- begin-user-doc -->
    * Write your own initialization here
    * <!-- end-user-doc -->
  @generated modifiable */
  private void readObject() {/*default - does nothing empty block */}
     
 
    
  //*--------------*
  //* Feature: pairs

  /** getter for pairs - gets 
   * @generated */
  public FSArray getPairs() {
    if (Pairs_Type.featOkTst && ((Pairs_Type)jcasType).casFeat_pairs == null)
      jcasType.jcas.throwFeatMissing("pairs", "org.apache.ctakes.typesystem.type.util.Pairs");
    return (FSArray)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefValue(addr, ((Pairs_Type)jcasType).casFeatCode_pairs)));}
    
  /** setter for pairs - sets  
   * @generated */
  public void setPairs(FSArray v) {
    if (Pairs_Type.featOkTst && ((Pairs_Type)jcasType).casFeat_pairs == null)
      jcasType.jcas.throwFeatMissing("pairs", "org.apache.ctakes.typesystem.type.util.Pairs");
    jcasType.ll_cas.ll_setRefValue(addr, ((Pairs_Type)jcasType).casFeatCode_pairs, jcasType.ll_cas.ll_getFSRef(v));}    
    
  /** indexed getter for pairs - gets an indexed value - 
   * @generated */
  public Pair getPairs(int i) {
    if (Pairs_Type.featOkTst && ((Pairs_Type)jcasType).casFeat_pairs == null)
      jcasType.jcas.throwFeatMissing("pairs", "org.apache.ctakes.typesystem.type.util.Pairs");
    jcasType.jcas.checkArrayBounds(jcasType.ll_cas.ll_getRefValue(addr, ((Pairs_Type)jcasType).casFeatCode_pairs), i);
    return (Pair)(jcasType.ll_cas.ll_getFSForRef(jcasType.ll_cas.ll_getRefArrayValue(jcasType.ll_cas.ll_getRefValue(addr, ((Pairs_Type)jcasType).casFeatCode_pairs), i)));}

  /** indexed setter for pairs - sets an indexed value - 
   * @generated */
  public void setPairs(int i, Pair v) { 
    if (Pairs_Type.featOkTst && ((Pairs_Type)jcasType).casFeat_pairs == null)
      jcasType.jcas.throwFeatMissing("pairs", "org.apache.ctakes.typesystem.type.util.Pairs");
    jcasType.jcas.checkArrayBounds(jcasType.ll_cas.ll_getRefValue(addr, ((Pairs_Type)jcasType).casFeatCode_pairs), i);
    jcasType.ll_cas.ll_setRefArrayValue(jcasType.ll_cas.ll_getRefValue(addr, ((Pairs_Type)jcasType).casFeatCode_pairs), i, jcasType.ll_cas.ll_getFSRef(v));}
  }

    