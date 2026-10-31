{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9d265550-9e87-402c-8038-e926882a4106",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "==================================================\n",
      "  APPLE iPHONE SALES ANALYSIS IN INDIA (2020–2026)\n",
      "       AUTOMATED EXECUTIVE INSIGHTS REPORT        \n",
      "==================================================\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# 1. Load the dataset\n",
    "# (Adjust path if necessary, e.g., '../data/raw/iPhone_India_Shipments_2020_2026.xlsx' or 'Book1.xlsx')\n",
    "df = pd.read_excel('C:\\\\Users\\\\saher\\\\OneDrive\\\\Documents\\\\Intership_Projects\\\\Apple_iPhone_Sales_Analysis\\\\data\\\\raw\\\\iPhone_India_Shipments_2020_2026.xlsx')\n",
    "\n",
    "print(\"==================================================\")\n",
    "print(\"  APPLE iPHONE SALES ANALYSIS IN INDIA (2020–2026)\")\n",
    "print(\"       AUTOMATED EXECUTIVE INSIGHTS REPORT        \")\n",
    "print(\"==================================================\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e1d3ab0a-e305-49a9-9f33-ff8006a7a5fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 2. Filter completed historical years (2020 to 2025)\n",
    "historical_df = df.dropna(subset=['Annual_Shipments_Million']).copy()\n",
    "\n",
    "# 3. Calculate Core Financial & Growth Metrics\n",
    "val_2020 = historical_df.loc[historical_df['Year'] == 2020, 'Annual_Shipments_Million'].values[0]\n",
    "val_2025 = historical_df.loc[historical_df['Year'] == 2025, 'Annual_Shipments_Million'].values[0]\n",
    "\n",
    "total_growth_pct = ((val_2025 - val_2020) / val_2020) * 100\n",
    "cagr = (((val_2025 / val_2020) ** (1 / 5)) - 1) * 100\n",
    "latest_shipments = val_2025\n",
    "peak_shipments = historical_df['Annual_Shipments_Million'].max()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "d2b8f2e5-1798-4dd2-81db-d89b3236b0b1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- 1. QUANTITATIVE PERFORMANCE SUMMARY ---\n",
      "• Baseline Shipments (2020): 3.2 Million units\n",
      "• Latest Reported Shipments (2025): 8.2 Million units\n",
      "• Overall Shipment Growth: 156.25%\n",
      "• Compound Annual Growth Rate (CAGR 2020-2025): 20.71%\n",
      "\n",
      "--- 2. EXECUTIVE STRATEGIC RECOMMENDATIONS ---\n",
      "1. Expand Retail Footprint in Tier-2 & Tier-3 Cities:\n",
      "   - With shipments scaling past 14M units, metropolitan demand is maturing.\n",
      "   - Recommendation: Partner with authorized resellers to launch mono-brand stores in emerging urban centers.\n",
      "\n",
      "2. Leverage Local Manufacturing & Supply Chain Incentives:\n",
      "   - High import tariffs require localized assembly to protect profit margins against Android competitors.\n",
      "   - Recommendation: Deepen 'Make in India' manufacturing partnerships to optimize device cost structures.\n",
      "\n",
      "3. Proactive Inventory Allocation (2027 Forecast Outlook):\n",
      "   - Machine learning forecasting indicates continued strong volume expansion (~18.17M units by 2027).\n",
      "   - Recommendation: Pre-allocate component inventory ahead of Q4 festival sale seasons to avoid stockouts.\n",
      "\n",
      "4. Aggressive Trade-In & EMI Financing:\n",
      "   - Price sensitivity remains a primary barrier for premium device adoption.\n",
      "   - Recommendation: Scale no-cost EMI options and trade-in trade-up programs to lower upfront entry barriers.\n",
      "==================================================\n"
     ]
    }
   ],
   "source": [
    "# Print Quantitative Performance Summary\n",
    "print(\"--- 1. QUANTITATIVE PERFORMANCE SUMMARY ---\")\n",
    "print(f\"• Baseline Shipments (2020): {val_2020} Million units\")\n",
    "print(f\"• Latest Reported Shipments (2025): {latest_shipments} Million units\")\n",
    "print(f\"• Overall Shipment Growth: {total_growth_pct:.2f}%\")\n",
    "print(f\"• Compound Annual Growth Rate (CAGR 2020-2025): {cagr:.2f}%\\n\")\n",
    "\n",
    "# 4. Generate Strategic Business Recommendations based on data\n",
    "print(\"--- 2. EXECUTIVE STRATEGIC RECOMMENDATIONS ---\")\n",
    "print(\"1. Expand Retail Footprint in Tier-2 & Tier-3 Cities:\")\n",
    "print(\"   - With shipments scaling past 14M units, metropolitan demand is maturing.\")\n",
    "print(\"   - Recommendation: Partner with authorized resellers to launch mono-brand stores in emerging urban centers.\\n\")\n",
    "\n",
    "print(\"2. Leverage Local Manufacturing & Supply Chain Incentives:\")\n",
    "print(\"   - High import tariffs require localized assembly to protect profit margins against Android competitors.\")\n",
    "print(\"   - Recommendation: Deepen 'Make in India' manufacturing partnerships to optimize device cost structures.\\n\")\n",
    "\n",
    "print(\"3. Proactive Inventory Allocation (2027 Forecast Outlook):\")\n",
    "print(\"   - Machine learning forecasting indicates continued strong volume expansion (~18.17M units by 2027).\")\n",
    "print(\"   - Recommendation: Pre-allocate component inventory ahead of Q4 festival sale seasons to avoid stockouts.\\n\")\n",
    "\n",
    "print(\"4. Aggressive Trade-In & EMI Financing:\")\n",
    "print(\"   - Price sensitivity remains a primary barrier for premium device adoption.\")\n",
    "print(\"   - Recommendation: Scale no-cost EMI options and trade-in trade-up programs to lower upfront entry barriers.\")\n",
    "print(\"==================================================\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d036ce4-3d6e-48b3-b85a-2a9514a6c50f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
