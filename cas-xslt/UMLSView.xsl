<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xmi="http://www.omg.org/XMI"
    xmlns:refsem="http:///org/apache/ctakes/typesystem/type/refsem.ecore"
    xmlns:textsem="http:///org/apache/ctakes/typesystem/type/textsem.ecore"
    xmlns:types="http:///org/apache/ctakes/assertion/medfacts/types.ecore"
    xmlns:cas="http:///uima/cas.ecore" exclude-result-prefixes="xs" version="2.0">
    <xsl:variable name="doc1" select="//xmi:XMI"/>
    <xsl:template match="/">
        <html>
            <body>
                <h2>UMLS Parsing Output</h2>
                <p>The xslt creating this currently handles the following: <ul>
                        <li>MedicationMention</li>
                        <li>SignSymptomMention</li>
                        <li>DiseaseDisorderMention</li>
                    </ul></p>
                <h3>Medications</h3>
                <p>There are other fields available here, such as frequency and route and so
                    forth</p>

                <table border="1">
                    <tr>
                        <th>Id</th>
                        <th>Score</th>
                        <th>Matched Text</th>
                        <th>Concepts</th>
                    </tr>


                    <xsl:for-each select="//textsem:MedicationMention">

                        <xsl:variable name="conceptseq" as="xs:string*"
                            select="tokenize(@ontologyConceptArr, ' ')"/>
                        <xsl:variable name="polarity">
                            <xsl:choose>
                                <xsl:when test="@polarity">
                                    <xsl:value-of select="@polarity"/>
                                </xsl:when>
                                <xsl:otherwise>1</xsl:otherwise>
                                <!-- default value -->
                            </xsl:choose>
                        </xsl:variable>
                        <tr>
                            <td>
                                <xsl:value-of select="@xmi:id"/>
                            </td>
                            <td>
                                <xsl:value-of
                                    select="format-number(xs:decimal(@confidence) * xs:decimal($polarity), '0.00')"
                                />
                            </td>
                            <td>
                                <xsl:value-of
                                    select="substring(//cas:Sofa/@sofaString, @begin, xs:integer(@end) - xs:integer(@begin) + 1)"
                                />
                            </td>
                            <td>
                                <table>
                                    <!-- concepts -->
                                    <tr>
                                        <th>tui</th>
                                        <th>preferred text</th>
                                        <th>scheme</th>
                                        <th>code</th>
                                    </tr>
                                    <xsl:for-each select="$conceptseq">
                                        <xsl:variable name="conceptid" select="."/>
                                        <tr>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@tui"
                                                />
                                            </td>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@preferredText"
                                                />
                                            </td>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@codingScheme"
                                                />
                                            </td>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@code"
                                                />
                                            </td>
                                        </tr>
                                    </xsl:for-each>
                                </table>
                                <!-- concepts -->
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>

                <h3>Diseases / Disorders</h3>
                <table border="1">
                    <tr>
                        <th>Id</th>
                        <th>Score</th>
                        <th>Matched Text</th>
                        <th>Concepts</th>
                    </tr>
                    <xsl:for-each select="//textsem:DiseaseDisorderMention">
                        <xsl:variable name="conceptseq" as="xs:string*"
                            select="tokenize(@ontologyConceptArr, ' ')"/>
                        <xsl:variable name="polarity">
                            <xsl:choose>
                                <xsl:when test="@polarity">
                                    <xsl:value-of select="@polarity"/>
                                </xsl:when>
                                <xsl:otherwise>1</xsl:otherwise>
                                <!-- default value -->
                            </xsl:choose>
                        </xsl:variable>

                        <xsl:variable name="confidence">
                            <xsl:choose>
                                <xsl:when test="not(xs:decimal(@confidence) eq 0)">
                                    <xsl:value-of select="@confidence"/>
                                </xsl:when>
                                <xsl:otherwise>1</xsl:otherwise>
                                <!-- default value -->
                            </xsl:choose>
                        </xsl:variable>
                        <tr>
                            <td>
                                <xsl:value-of select="@xmi:id"/>
                            </td>
                            <td>
                                <xsl:value-of
                                    select="format-number(xs:decimal($confidence) * xs:decimal($polarity), '0.00')"
                                />
                            </td>
                            <td>
                                <xsl:value-of
                                    select="substring(//cas:Sofa/@sofaString, @begin, xs:integer(@end) - xs:integer(@begin) + 1)"
                                />
                            </td>
                            <td>
                                <table>
                                    <!-- concepts -->
                                    <tr>
                                        <th>tui</th>
                                        <th>preferred text</th>
                                        <th>scheme</th>
                                        <th>code</th>
                                    </tr>
                                    <xsl:for-each select="$conceptseq">
                                        <xsl:variable name="conceptid" select="."/>
                                        <tr>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@tui"
                                                />
                                            </td>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@preferredText"
                                                />
                                            </td>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@codingScheme"
                                                />
                                            </td>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@code"
                                                />
                                            </td>
                                        </tr>
                                    </xsl:for-each>
                                </table>
                                <!-- concepts -->
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>

                <h3>Signs / Symptoms</h3>
                <table border="1">
                    <tr>
                        <th>Id</th>
                        <th>Score</th>
                        <th>Matched Text</th>
                        <th>Concepts</th>
                    </tr>
                    <xsl:for-each select="//textsem:SignSymptomMention">
                        <xsl:variable name="conceptseq" as="xs:string*"
                            select="tokenize(@ontologyConceptArr, ' ')"/>
                        <xsl:variable name="polarity">
                            <xsl:choose>
                                <xsl:when test="@polarity">
                                    <xsl:value-of select="@polarity"/>
                                </xsl:when>
                                <xsl:otherwise>1</xsl:otherwise>
                                <!-- default value -->
                            </xsl:choose>
                        </xsl:variable>

                        <xsl:variable name="confidence">
                            <xsl:choose>
                                <xsl:when test="not(xs:decimal(@confidence) eq 0)">
                                    <xsl:value-of select="@confidence"/>
                                </xsl:when>
                                <xsl:otherwise>1</xsl:otherwise>
                                <!-- default value -->
                            </xsl:choose>
                        </xsl:variable>
                        <tr>
                            <td>
                                <xsl:value-of select="@xmi:id"/>
                            </td>
                            <td>
                                <xsl:value-of
                                    select="format-number(xs:decimal($confidence) * xs:decimal($polarity), '0.00')"
                                />
                            </td>
                            <td>
                                <xsl:value-of
                                    select="substring(//cas:Sofa/@sofaString, @begin, xs:integer(@end) - xs:integer(@begin) + 1)"
                                />
                            </td>
                            <td>
                                <table>
                                    <!-- concepts -->
                                    <tr>
                                        <th>tui</th>
                                        <th>preferred text</th>
                                        <th>scheme</th>
                                        <th>code</th>
                                    </tr>
                                    <xsl:for-each select="$conceptseq">
                                        <xsl:variable name="conceptid" select="."/>
                                        <tr>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@tui"
                                                />
                                            </td>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@preferredText"
                                                />
                                            </td>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@codingScheme"
                                                />
                                            </td>
                                            <td>
                                                <xsl:value-of
                                                  select="$doc1/refsem:UmlsConcept[@xmi:id = $conceptid]/@code"
                                                />
                                            </td>
                                        </tr>
                                    </xsl:for-each>
                                </table>
                                <!-- concepts -->
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>

            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
