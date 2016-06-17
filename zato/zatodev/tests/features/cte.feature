Feature: zato-apitest cte

  Scenario: *** Get corpus list - empty ***
    Given address "http://localhost:11223"
    Given URL path "/corpus"
    Given HTTP method "GET"
    Given format "JSON"
    Given request is "{}"
    When  the URL is invoked
    Then  status is "200"
    And   JSON Pointer "/response/data" is ""
