##about this

This is a sample command line program to validate the approach for the servlet

###sample input
(see note.txt file)

###sample output
(see note.json file)
```
{
    "text-length": 2090,
    "analysis-engine": "/opt/ctakes/desc/ctakes-ytex-uima/desc/analysis_engine/AggregatePlaintextUMLSProcessor.xml",
    "entity-count": 91,
    "concept-count": 113,
    "entities": [
        {
            "generic": false,
            "text": "HISTORY OF",
            "scheme": "UMLS",
            "concepttext": "preferred text will go here",
            "polarity": 1,
            "score": 0,
            "disambiguated": true,
            "code": "C0262926"
        },
        {
            "generic": false,
            "text": "HISTORY",
            "scheme": "UMLS",
            "concepttext": "preferred text will go here",
            "polarity": 1,
            "score": 0,
            "disambiguated": true,
            "code": "C0262926"
        },
        et cetera...
    }
```

##todos
- can we get this sort of thing to show up as the broadest concept,
 i.e., "back pain", instead of all three:
 ```
<types:Concept xmi:id="20757" sofa="6" begin="2046" end="2055" conceptText="back pain" externalId="0" originalEntityExternalId="11709"/>
<types:Concept xmi:id="20765" sofa="6" begin="2046" end="2050" conceptText="back" externalId="0" originalEntityExternalId="11662"/>
<types:Concept xmi:id="20773" sofa="6" begin="2051" end="2055" conceptText="pain" externalId="0" originalEntityExternalId="11607"/>
 ```
 - get preferred term text in the output