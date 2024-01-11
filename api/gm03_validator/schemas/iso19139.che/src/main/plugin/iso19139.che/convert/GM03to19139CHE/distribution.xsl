<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:gmd="http://www.isotc211.org/2005/gmd"
                xmlns:che="http://www.geocat.ch/2008/che"
                xmlns:gco="http://www.isotc211.org/2005/gco"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template mode="Distribution" match="GM03Core.Core.MD_Distribution">
        <gmd:MD_Distribution>
            <xsl:choose>
                <xsl:when test="GM03Core.Core.MD_DistributiondistributionFormat">
                    <xsl:for-each select="GM03Core.Core.MD_DistributiondistributionFormat">
                        <gmd:distributionFormat>
                            <xsl:apply-templates mode="ResourceFormat">
                                <xsl:with-param name="loop">1</xsl:with-param>
                            </xsl:apply-templates>
                        </gmd:distributionFormat>
                    </xsl:for-each>
                </xsl:when>
                <xsl:otherwise>
                <gmd:distributionFormat>
                    <gmd:MD_Format>
                        <gmd:name>
                            <gco:CharacterString>N/A</gco:CharacterString>
                        </gmd:name>
                        <gmd:version>
                            <gco:CharacterString>N/A</gco:CharacterString>
                        </gmd:version>
                    </gmd:MD_Format>
                </gmd:distributionFormat>
                </xsl:otherwise>
            </xsl:choose>
            <xsl:for-each select="GM03Core.Core.MD_Distributiondistributor|GM03Comprehensive.Comprehensive.MD_Distributiondistributor">
                <gmd:distributor>
                    <xsl:apply-templates select="." mode="Distributor"/>
                </gmd:distributor>
            </xsl:for-each>

            <xsl:for-each select="GM03Comprehensive.Comprehensive.MD_DigitalTransferOptions|GM03Core.Core.MD_DigitalTransferOptions">
                <gmd:transferOptions>
                    <xsl:apply-templates mode="Distribution" select="." />
                </gmd:transferOptions>
            </xsl:for-each>
        </gmd:MD_Distribution>
    </xsl:template>

    <xsl:template mode="Distribution" match="GM03Comprehensive.Comprehensive.MD_DigitalTransferOptions|GM03Core.Core.MD_DigitalTransferOptions">
            <gmd:MD_DigitalTransferOptions>
                <xsl:apply-templates mode="text" select="unitsOfDistribution"/>
                <xsl:apply-templates mode="real" select="transferSize"/>
                <xsl:apply-templates mode="Distribution" select="GM03Core.Core.CI_OnlineResource"/>
                <xsl:apply-templates mode="Distribution" select="offLine"/>
            </gmd:MD_DigitalTransferOptions>
    </xsl:template>

    <xsl:template mode="Distribution" match="GM03Core.Core.CI_OnlineResource">
        <gmd:onLine>
            <xsl:apply-templates select="." mode="OnlineResource"/>
        </gmd:onLine>
    </xsl:template>

    <xsl:template mode="Distribution" match="offLine">
        <gmd:offLine>
            <xsl:apply-templates mode="Distribution"/>
        </gmd:offLine>
    </xsl:template>

    <xsl:template mode="Distribution" match="GM03Comprehensive.Comprehensive.MD_Medium">
        <gmd:MD_Medium>
            <gmd:name>
                <gmd:MD_MediumNameCode codeList="./resources/codeList.xml#MD_MediumNameCode" codeListValue="{.}"/>
            </gmd:name>
            <xsl:apply-templates mode="real" select="density"/>
            <xsl:apply-templates mode="text" select="densityUnits"/>
            <xsl:apply-templates mode="integer" select="volumes"/>
            <xsl:apply-templates mode="text" select="mediumFormat"/>
        </gmd:MD_Medium>
    </xsl:template>

    <xsl:template mode="Distribution" match="text()">
        <xsl:call-template name="UnMatchedText">
            <xsl:with-param name="mode">Distribution</xsl:with-param>
        </xsl:call-template>
    </xsl:template>

    <!-- ================================================================================= -->

    <xsl:template mode="OnlineResource" match="GM03Core.Core.CI_OnlineResource">
        <gmd:CI_OnlineResource>
            <xsl:for-each select="linkage">
                <gmd:linkage>
                    <xsl:apply-templates mode="language"/>
                </gmd:linkage>
            </xsl:for-each>

            <xsl:for-each select="name">
                <gmd:name>
                    <xsl:apply-templates mode="language"/>
                </gmd:name>
            </xsl:for-each>

            <xsl:for-each select="description">
                <gmd:description>
                    <xsl:apply-templates mode="language"/>
                </gmd:description>
            </xsl:for-each>

            <xsl:for-each select="function">
                <gmd:function>
                    <gmd:CI_OnLineFunctionCode codeList="./resources/codeList.xml#CI_OnLineFunctionCode" codeListValue="{.}"/>
                </gmd:function>
            </xsl:for-each>
        </gmd:CI_OnlineResource>
    </xsl:template>

    <!-- ================================================================================= -->

    <xsl:template mode="Format" match="GM03Comprehensive.Comprehensive.MD_Format|GM03Core.Core.MD_Format">
            <xsl:apply-templates mode="ResourceFormat" select=".">
            <xsl:with-param name="loop">1</xsl:with-param>
            </xsl:apply-templates>
    </xsl:template>

    <xsl:template mode="Format" match="formatDistributor">
        <gmd:formatDistributor>
            <xsl:apply-templates mode="Distributor"/>
        </gmd:formatDistributor>
    </xsl:template>

    <xsl:template mode="Format" match="text()">
        <xsl:call-template name="UnMatchedText">
            <xsl:with-param name="mode">Distributor</xsl:with-param>
        </xsl:call-template>
    </xsl:template>

    <!-- ================================================================================= -->

    <xsl:template mode="Distributor" match="GM03Comprehensive.Comprehensive.MD_Distributor">
        <gmd:MD_Distributor>
            <xsl:for-each select="distributorContact">
                <gmd:distributorContact>
                    <xsl:apply-templates select="." mode="RespParty"/>
                </gmd:distributorContact>
            </xsl:for-each>

            <xsl:apply-templates mode="Distributor" select="GM03Comprehensive.Comprehensive.distributionOrderProcessMD_Distributor"/>
            <xsl:apply-templates mode="Distributor" select="GM03Comprehensive.Comprehensive.formatDistributordistributorFormat"/>
            <xsl:if test="not(ancestor::GM03Comprehensive.Comprehensive.formatDistributordistributorFormat)">
                <xsl:apply-templates mode="Distributor" select="/GM03Comprehensive.Comprehensive/GM03Comprehensive.Comprehensive.formatDistributordistributorFormat"/>
            </xsl:if>
            <xsl:apply-templates mode="Distributor" select="GM03Comprehensive.Comprehensive.distributorTransferOptionsMD_Distributor"/>
        </gmd:MD_Distributor>
    </xsl:template>

    <xsl:template mode="Distributor" match="GM03Comprehensive.Comprehensive.distributionOrderProcessMD_Distributor">
        <gmd:distributionOrderProcess>
            <xsl:apply-templates mode="Distributor" select="distributionOrderProcess/GM03Comprehensive.Comprehensive.MD_StandardOrderProcess"/>
        </gmd:distributionOrderProcess>
    </xsl:template>
    <xsl:template mode="Distributor" match="GM03Comprehensive.Comprehensive.MD_StandardOrderProcess">
        <gmd:MD_StandardOrderProcess>
            <xsl:apply-templates mode="text" select="fees"/>
            <xsl:for-each select="plannedAvailableDateTime">
                <gmd:plannedAvailableDateTime>
                    <xsl:apply-templates mode="dateTime" select="."/>
                </gmd:plannedAvailableDateTime>
            </xsl:for-each>
            <xsl:apply-templates mode="text" select="orderingInstructions"/>
            <xsl:apply-templates mode="text" select="turnaround"/>
        </gmd:MD_StandardOrderProcess>
    </xsl:template>
    <xsl:template mode="Distributor" match="GM03Comprehensive.Comprehensive.formatDistributordistributorFormat">
        <gmd:distributorFormat>
            <xsl:apply-templates mode="Format" select="distributorFormat/GM03Comprehensive.Comprehensive.MD_Format"/>
        </gmd:distributorFormat>
    </xsl:template>
    <xsl:template mode="Distributor" match="GM03Comprehensive.Comprehensive.distributorTransferOptionsMD_Distributor">
        <gmd:distributorTransferOptions>
            <xsl:apply-templates mode="Distribution" select="distributorTransferOptions/GM03Comprehensive.Comprehensive.MD_DigitalTransferOptions"/>
        </gmd:distributorTransferOptions>
    </xsl:template>

</xsl:stylesheet>
