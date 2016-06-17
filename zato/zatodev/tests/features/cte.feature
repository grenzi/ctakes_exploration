# -*- coding: utf-8 -*-
Feature: zato-apitest cte

  Scenario: *** Get corpus list - empty ***
    Given address "http://localhost:11223"
    Given URL path "/corpus"
    Given HTTP method "GET"
    Given format "JSON"
    Given request is "{}"
    When  the URL is invoked
    Then  status is "200"
    And   JSON Pointer "/response/data" is empty
    And   JSON Pointer "/response/status/msg" is "OK"

  Scenario: *** Create Corpus ***
    Given address "http://localhost:11223"
    Given URL path "/corpus/add"
    Given HTTP method "POST"
    Given format "JSON"
    Given request is "{}"
    Given JSON Pointer "/name" in request is "API Testing Corpus One"
    Given JSON Pointer "/description" in request is "This is an interesting description of the content in the corpus"
    When  the URL is invoked
    Then  status is "200"
    And   JSON Pointer "/response/status/msg" is "OK"
    And   JSON Pointer "/response/data/id" is an integer "1"

  Scenario: *** Get corpus list - one item ***
    Given address "http://localhost:11223"
    Given URL path "/corpus"
    Given HTTP method "GET"
    Given format "JSON"
    Given request is "{}"
    When  the URL is invoked
    Then  status is "200"
    And   JSON Pointer "/response/status/msg" is "OK"
    And   JSON Pointer "/response/data" is equal to "[{"id": 1, "description": "This is an interesting description of the content in the corpus", "name": "API Testing Corpus One"}]"
