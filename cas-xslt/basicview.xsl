<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:xmi="http://www.omg.org/XMI" 
    xmlns:refsem="http:///org/apache/ctakes/typesystem/type/refsem.ecore"
    xmlns:textsem="http:///org/apache/ctakes/typesystem/type/textsem.ecore"
    xmlns:types="http:///org/apache/ctakes/assertion/medfacts/types.ecore"
    xmlns:cas="http:///uima/cas.ecore"
    exclude-result-prefixes="xs"
    version="2.0">
    
    <xsl:template match="/">
        <html>
            <body>
                <h2>YTEX Parsing Output</h2>
                <table border="1">
                    <tr bgcolor="#111111">
                        <th>Id</th>
                        <th>Concept</th>
                        <th>Code</th>
                        <th>Scheme</th>
                        <th>Score</th>
                        <th>Disambiguated</th>
                        <th>subject</th>
                        <th>text matched</th>
                    </tr>
                    <xsl:for-each select="/xmi:XMI/refsem:OntologyConcept" >
                        <xsl:variable name="ontologyId" select="@xmi:id"/>
                        <xsl:variable name="mention_elem" select="//textsem:EntityMention[contains(@ontologyConceptArr, $ontologyId)]"/>
                        <xsl:variable name="concept_elem" select="//types:Concept[@originalEntityExternalId=$mention_elem/@xmi:id]"/>
                       
                        <xsl:variable name="polarity">
                            <xsl:choose>
                                <xsl:when test="$mention_elem/@polarity"><xsl:value-of select="$mention_elem/@polarity"/></xsl:when>
                                <xsl:otherwise>1</xsl:otherwise> <!-- default value -->
                            </xsl:choose>
                        </xsl:variable>
                 
                        <xsl:variable name="score">
                            <xsl:choose>
                                <xsl:when test="xs:decimal(@score) gt 0"><xsl:value-of select="@score"/></xsl:when>
                                <xsl:otherwise>1</xsl:otherwise> <!-- default value -->
                            </xsl:choose>
                        </xsl:variable>

                        <tr>
                            <td><xsl:value-of select="$ontologyId"/></td>
                            <td><xsl:value-of select="$concept_elem/@conceptText"/></td>
                            <td><xsl:value-of select="@code"/></td>
                            <td><xsl:value-of select="@codingScheme"/></td>
                            <td><xsl:value-of select="format-number(xs:decimal($score) * xs:decimal($polarity), '0.0')"/></td>
                            
                            <td><xsl:value-of select="@disambiguated"/></td>
                            <td><xsl:value-of select="$mention_elem/@subject"/></td>
                            <td>
                                <xsl:value-of select="substring(//cas:Sofa/@sofaString, 
                                    $mention_elem/@begin, 
                                    xs:integer($mention_elem/@end)-xs:integer($mention_elem/@begin)+1)"/></td>
                        </tr>
                    </xsl:for-each>                                       
                </table>
                <p></p>
                <h2>Original Text</h2>
                <br></br>
                <PRE>
                 <xsl:value-of select="//cas:Sofa/@sofaString"/> 
                </PRE>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>