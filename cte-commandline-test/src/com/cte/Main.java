package com.cte;

import org.apache.ctakes.assertion.medfacts.types.Concept;
import org.apache.ctakes.dictionary.lookup.Dictionary;
import org.apache.ctakes.typesystem.type.refsem.OntologyConcept;
import org.apache.ctakes.typesystem.type.textsem.*;
import org.apache.uima.UIMAFramework;
import org.apache.uima.analysis_engine.AnalysisEngine;
import org.apache.uima.cas.CAS;
import org.apache.uima.fit.util.JCasUtil;
import org.apache.uima.jcas.JCas;
import org.apache.uima.jcas.cas.FSArray;
import org.apache.uima.resource.ResourceManager;
import org.apache.uima.resource.ResourceSpecifier;
import org.apache.uima.util.XMLInputSource;
import org.hibernate.mapping.Collection;
import org.json.JSONArray;
import org.json.JSONObject;
import org.mitre.medfacts.i2b2.annotation.ConceptType;
import scala.collection.mutable.HashTable;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Map;

public class Main {

    public static String ReadResource(String resourcename)
    {
        try {
            InputStream stream = Main.class.getResourceAsStream(resourcename);
            BufferedReader reader = new BufferedReader(new InputStreamReader(stream));
            StringBuilder out = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                out.append(line);
                out.append("\n");
            }
            System.out.println(out.toString());   //Prints the string content read from input stream
            reader.close();
            return out.toString();
        }
        catch (Exception e)
        {
            return "error reading";
        }
    }

    public static void main(String[] args) {
        try {
            String s = ReadResource("/note.txt");
            String enginefile = "/opt/ctakes/desc/ctakes-ytex-uima/desc/analysis_engine/AggregatePlaintextUMLSProcessor.xml";
            File f = new File(enginefile);

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


            //store preferred term text by id 10102 is the id to use below
            // <types:Concept xmi:id="20509" sofa="6" begin="1213" end="1218" conceptText="edema" externalId="0" originalEntityExternalId="10102"/>

            //full type here because it picks up one of the scala libraries
            java.util.Hashtable<Integer, String> clu = new java.util.Hashtable<Integer, String>();

            for (Concept c : JCasUtil.select(jcas, Concept.class))
                clu.put(c.getExternalId(), c.getConceptText());




            //prepare output
            JSONArray entitymentions = new JSONArray();
            int ec = 0;
            for (EntityMention em : JCasUtil.select(jcas, EntityMention.class)) {
                ec++;
                for (int i=0; i< em.getOntologyConceptArr().size(); i++){
                    JSONObject o = new JSONObject("{}");
                    OntologyConcept oc = em.getOntologyConceptArr(i);

                    o.put("text", em.getCoveredText());
                    //the following line is returning null - not sure why. need to debug a little more
                    //o.put("concepttext", clu.get(em.getId()));
                    o.put("concepttext", "preferred text will go here");
                    o.put("code", oc.getCode());
                    o.put("scheme", oc.getCodingScheme());
                    o.put("disambiguated", oc.getDisambiguated());
                    o.put("polarity", em.getPolarity());
                    o.put("score", oc.getScore());
                    o.put("generic", em.getGeneric());

                    entitymentions.put(o);
                }
            }

            //add in some descriptives
            JSONObject output = new JSONObject();
            output.put("entity-count", ec);
            output.put("concept-count", entitymentions.length());
            output.put("analysis-engine", enginefile);
            output.put("text-length", s.length());
            output.put("entities", entitymentions);


            System.out.println(output.toString(4));


        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
