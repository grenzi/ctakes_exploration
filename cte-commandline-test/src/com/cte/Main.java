package com.cte;

import org.apache.ctakes.typesystem.type.textsem.EntityMention;
import org.apache.uima.UIMAFramework;
import org.apache.uima.analysis_engine.AnalysisEngine;
import org.apache.uima.cas.CAS;
import org.apache.uima.fit.util.JCasUtil;
import org.apache.uima.jcas.JCas;
import org.apache.uima.jcas.cas.FSArray;
import org.apache.uima.resource.ResourceManager;
import org.apache.uima.resource.ResourceSpecifier;
import org.apache.uima.util.XMLInputSource;
import java.io.File;

public class Main {

    public static void main(String[] args) {
        try {
            String s = "aspirin taken daily for pain";

            File f = new File(
                    "/opt/ctakes/desc/ctakes-ytex-uima/desc/analysis_engine/AggregatePlaintextUMLSProcessor.xml");

            XMLInputSource in = new XMLInputSource(f);
            ResourceSpecifier specifier = UIMAFramework.getXMLParser().parseResourceSpecifier(in);
            ResourceManager manager = UIMAFramework.newDefaultResourceManager();

            AnalysisEngine ae = UIMAFramework.produceAnalysisEngine(specifier, manager, null);
            CAS cas = ae.newCAS();
            cas.setDocumentText(s);
            cas.setDocumentLanguage("en");
            ae.process(cas);
            System.out.println("ran engine, got cas");
            JCas jcas = cas.getJCas();

            for (EntityMention em : JCasUtil.select(jcas, EntityMention.class)) {
                // todo - get output defined, iterate over right types. append
                // to JSON.
                // then move this whole shebang to a servlet
                // statically load the analysis engine, reload on catching
                // execption (db timeout?)
                System.out.println(em.getCoveredText());

                // one or more concepts per mention. each has score, etc.
                FSArray arr = em.getOntologyConceptArr();
            }

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
