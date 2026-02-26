# tools.py

import os
from crewai.tools import tool
from langchain_community.document_loaders import PyPDFLoader
from crewai_tools import SerperDevTool


# ==============================
# 🔍 Internet Search Tool
# ==============================

search_tool = SerperDevTool()


# ==============================
# 📄 Financial Document Reader Tool
# ==============================

@tool("financial_document_reader")
def read_data_tool(path: str) -> str:
    """
    Reads a financial PDF document from the given file path
    and returns cleaned text content.
    """

    if not os.path.exists(path):
        return f"File not found at path: {path}"

    loader = PyPDFLoader(path)
    documents = loader.load()

    full_report = ""

    for page in documents:
        content = page.page_content

        # Clean formatting
        while "\n\n" in content:
            content = content.replace("\n\n", "\n")

        full_report += content + "\n"

    return full_report


# ==============================
# 📊 Investment Analysis Tool
# ==============================

@tool("investment_analysis_tool")
def analyze_investment_tool(financial_document_data: str) -> str:
    """
    Basic investment analysis placeholder.
    """

    if not financial_document_data:
        return "No financial data provided for investment analysis."

    # Basic cleanup
    processed_data = financial_document_data.replace("  ", " ")

    # Placeholder logic
    return (
        "Investment analysis completed.\n\n"
        "Key Observations:\n"
        "- Revenue trends identified\n"
        "- Potential growth indicators found\n"
        "- Further ratio analysis recommended\n\n"
        "NOTE: Detailed investment logic not yet implemented."
    )


# ==============================
# ⚠️ Risk Assessment Tool
# ==============================

@tool("risk_assessment_tool")
def create_risk_assessment_tool(financial_document_data: str) -> str:
    """
    Basic risk assessment placeholder.
    """

    if not financial_document_data:
        return "No financial data provided for risk assessment."

    return (
        "Risk assessment completed.\n\n"
        "Preliminary Risk Indicators:\n"
        "- Market volatility exposure\n"
        "- Liquidity considerations\n"
        "- Regulatory compliance factors\n\n"
        "NOTE: Detailed risk modeling not yet implemented."
    )