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


## Architecture (Logical sketch)


## API Structure
basically, domain driven. maybe have a clear deseignation of internal pseudomicro services for change management (ensure we have complete test coverage on external facing services, but can slide a little on internal ones)

Path|Description
------------ | -------------
corpora
  - crud | corpora description here
- terms 
  * extract-terms
- taxonomies
  - crud
  - search
  - subset
- events


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