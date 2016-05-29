# Overview of where I think we can take this

## Architecture (Physical, so far)
- Client via HTTP/FTP/Whatever ([Zato's connectors](https://zato.io/docs/progguide/examples/index.html))
- Zato.io server 
- cTakes server **with YTEX installed** 
  * running YTEX web $CTAKES_HOME/bin/ytexweb.sh
  * running ctakes-server-master (variant - modify code)
- mysql server
  * UMLS db
  * ytex db
  * zato operational db (ODB)
- big storage db
  * probably running cassandra, mongo, or similar
- if we get into workflow /rules, let's look at [Camunda](https://camunda.org/)
- maybe a [ZeroMQ](http://zeromq.org/) box if we get into volume (will need to scale out ctakes servers) 


## Architecture (Logical sketch)
so essentially what we're doing is an integration and bundling play that creates a lot of value. this means we'll have a hodge-podge infrastructure by necessity (scala, java, python, various dbs, etc).

picture coming, but this is a key part of the architecture: basically if we build pseudomicro services, we can compose those internally to pretty quickly adapt to customer needs. could longer term allow a "run your own code" template or similar to allow technical users to build on top. [Here's a link](https://zato.io/docs/progguide/invoking-services.html) to Zato's page on calling services from services.

See [this file here](https://github.com/grenzi/ctakes_exploration/blob/master/zato/zatodev/services/Text-IdentifyTerms.py) for an example of what it takes for Zato to consume the ctakes api. This is functional.


## API Structure
basically, domain driven. maybe have a clear deseignation of internal pseudomicro services for change management (ensure we have complete test coverage on external facing services, but can slide a little on internal ones)


**really still need to think through how to organize this. Relevant questions:** 
- how restful do we want to get? 
- how to balance service as a service against nice restful APIs (i.e., as an api user, I'd like to be able to get terms without having to create a corpora, etc)
- should terms/extract-terms go into an /analyses path? if so, maybe the right strucure is something like /taxonomies/umls/C0018787 for getting a term's info. _as i'm writing this, i think this might be best_.
- asynch

Path|Description
------------------------- | --------------------------
corpora                   | corpora description here
corpora/crud		      |
corpora/text/crud         | text CRUD
terms                     | term 
terms/extract-terms       | pulls terms from a given text (_need to think about if we should have multiple entry points here, e.g., corpora/1/extract-terms, corpora/1/text/2/extract-terms, etc)
terms/similarity		  | endpoint for YTEX similarity score API for UMLS terms
taxonomies				  | not sure if we should use taxonomy or thesauri here. essentially, the goal is to allow clients to create their own term sets and provide here, or to subset existing ones. also need some degree of specificity in terms of standards (umls, snomed, rxnorm, icd10) 
taxonomies/crud			  | user defined taxonomies
taxonomies/search		  | find your terms by...
taxonomies/subset		  | the idea here is that i might want to take UMLS and eliminate junk terms ('disease') that don't add a lot of value 
events                    | this is definitely blue sky here, but i wonder about the utility of being able to subscribe to particular events (e.g., FHIR clinical note contains mention of ebola)


## RESTy notes
let's try and keep a 'that makes sense' design to the URIs. See Zato's notes on [Clean URLs with path patterns](https://zato.io/docs/progguide/rest/channels.html) and [this page](http://www.restapitutorial.com/lessons/restfulresourcenaming.html) on RESTful resource naming


## Misc References

### ctakes / ytex
- for ctakes, need to use ytex to get scoring, disambiguation, and the better negation detection. 
- `$CTAKES_HOME/desc/ctakes-ytex-uima/desc/analysis_engine/AggregatePlaintextUMLSProcessor.xml` is the AE to use
- [Sense Disambiguation Annotator](https://cwiki.apache.org/confluence/display/CTAKES/cTAKES+3.1.2+-+SenseDisambiguatorAnnotator)
- for ytex config, see [this page](https://cwiki.apache.org/confluence/display/CTAKES/User%27s+Guide)
- ytex web provides term similarity for UMLS terms. 
  * sample URL: `http://localhost:8080/services/rest/similarity?conceptGraph=sct-rxnorm&concept1=C0018787&concept2=C0024109&metrics=LCH,INTRINSIC_LCH`

### getting logging on mysql for all queries being run through
file must exist and be writable by mysqld account (e.g., `touch ~/mysql_general.log && chmod a+w ~/mysql_general.log`)

    SET global log_output = 'FILE';
    SET global general_log_file='~/mysql_general.log';
    SET global general_log = 1;`