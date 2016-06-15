# Service directory



url path | method | service | channel
--- | --- | --- | ---
/corpora | GET | cte-corpora-list | channel-cte-corpora-list
/corpora/\<id\> | POST | cte-corpora-upsert | channel-cte-corpora-upsert


# Info

- these are the name suffixes that zato uses to assign input value types
  for simpleio services

From their website [here](https://zato.io/docs/progguide/sio.html)


### Datatypes
Zato uses a few conventions when deciding when to convert request and response parameters between various datatypes. This can be helpful because otherwise all the request parameters could've been strings - this is true for both JSON and XML but doubly so for the latter.

- If a parameter's name is 'id' it will be converted to an integer
- If a parameter ends with '_id', '_size' or '_timeout' it will be converted to an integer
- If a parameter begins with 'is_', 'needs_', 'should_' it will be converted to a bool

Name	Notes
AsIs	A pass-through marker, no conversions will be performed even though normally one would've been attempted
Boolean	Converted to a bool object
CSV	Converted to/from comma-separated values
Dict	Converted to a dictionary
Integer	Converted to an integer
List	Converted to a list
ListOfDicts	Converted to a list of dictionaries
Opaque	Similar to AsIs but works with arbitrarily nested structures as well
Unicode	Converted to a unicode object



