
/* First created by JCasGen Sat Jun 04 22:42:39 CDT 2016 */
package org.apache.ctakes.typesystem.type.textsem;

import org.apache.uima.jcas.JCas;
import org.apache.uima.jcas.JCasRegistry;
import org.apache.uima.cas.impl.CASImpl;
import org.apache.uima.cas.impl.FSGenerator;
import org.apache.uima.cas.FeatureStructure;
import org.apache.uima.cas.impl.TypeImpl;
import org.apache.uima.cas.Type;
import org.apache.uima.cas.impl.FeatureImpl;
import org.apache.uima.cas.Feature;

/** 
 * Updated by JCasGen Sat Jun 04 22:42:39 CDT 2016
 * @generated */
public class PolarityModifier_Type extends Modifier_Type {
  /** @generated */
  @Override
  protected FSGenerator getFSGenerator() {return fsGenerator;}
  /** @generated */
  private final FSGenerator fsGenerator = 
    new FSGenerator() {
      public FeatureStructure createFS(int addr, CASImpl cas) {
  			 if (PolarityModifier_Type.this.useExistingInstance) {
  			   // Return eq fs instance if already created
  		     FeatureStructure fs = PolarityModifier_Type.this.jcas.getJfsFromCaddr(addr);
  		     if (null == fs) {
  		       fs = new PolarityModifier(addr, PolarityModifier_Type.this);
  			   PolarityModifier_Type.this.jcas.putJfsFromCaddr(addr, fs);
  			   return fs;
  		     }
  		     return fs;
        } else return new PolarityModifier(addr, PolarityModifier_Type.this);
  	  }
    };
  /** @generated */
  @SuppressWarnings ("hiding")
  public final static int typeIndexID = PolarityModifier.typeIndexID;
  /** @generated 
     @modifiable */
  @SuppressWarnings ("hiding")
  public final static boolean featOkTst = JCasRegistry.getFeatOkTst("org.apache.ctakes.typesystem.type.textsem.PolarityModifier");
 
  /** @generated */
  final Feature casFeat_indicated;
  /** @generated */
  final int     casFeatCode_indicated;
  /** @generated */ 
  public boolean getIndicated(int addr) {
        if (featOkTst && casFeat_indicated == null)
      jcas.throwFeatMissing("indicated", "org.apache.ctakes.typesystem.type.textsem.PolarityModifier");
    return ll_cas.ll_getBooleanValue(addr, casFeatCode_indicated);
  }
  /** @generated */    
  public void setIndicated(int addr, boolean v) {
        if (featOkTst && casFeat_indicated == null)
      jcas.throwFeatMissing("indicated", "org.apache.ctakes.typesystem.type.textsem.PolarityModifier");
    ll_cas.ll_setBooleanValue(addr, casFeatCode_indicated, v);}
    
  



  /** initialize variables to correspond with Cas Type and Features
	* @generated */
  public PolarityModifier_Type(JCas jcas, Type casType) {
    super(jcas, casType);
    casImpl.getFSClassRegistry().addGeneratorForType((TypeImpl)this.casType, getFSGenerator());

 
    casFeat_indicated = jcas.getRequiredFeatureDE(casType, "indicated", "uima.cas.Boolean", featOkTst);
    casFeatCode_indicated  = (null == casFeat_indicated) ? JCas.INVALID_FEATURE_CODE : ((FeatureImpl)casFeat_indicated).getCode();

  }
}



    