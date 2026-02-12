VECTORS: List[ValuationVector] = [

# -------------------------------------------------
# REVENUE QUALITY (RQ-01 → RQ-10)
# -------------------------------------------------
ValuationVector("RQ-01", "Revenue Concentration Risk", "Revenue Quality", "Dependency on top customers."),
ValuationVector("RQ-02", "Recurring Revenue Stability", "Revenue Quality", "Durability of contracted revenue."),
ValuationVector("RQ-03", "Customer Churn Velocity", "Revenue Quality", "Rate of customer attrition."),
ValuationVector("RQ-04", "Revenue Growth Sustainability", "Revenue Quality", "Consistency of growth drivers."),
ValuationVector("RQ-05", "Pricing Power Durability", "Revenue Quality", "Ability to maintain pricing."),
ValuationVector("RQ-06", "Contractual Revenue Visibility", "Revenue Quality", "Forward revenue coverage."),
ValuationVector("RQ-07", "Revenue Recognition Integrity", "Revenue Quality", "Aggressiveness of revenue booking."),
ValuationVector("RQ-08", "Channel Dependency Exposure", "Revenue Quality", "Reliance on single distribution channels."),
ValuationVector("RQ-09", "Geographic Revenue Concentration", "Revenue Quality", "Regional revenue dependency."),
ValuationVector("RQ-10", "Customer Credit Quality Exposure", "Revenue Quality", "Financial stability of customers."),

# -------------------------------------------------
# MARGIN INTEGRITY (MI-01 → MI-10)
# -------------------------------------------------
ValuationVector("MI-01", "Gross Margin Volatility", "Margin Integrity", "Fluctuation in gross margins."),
ValuationVector("MI-02", "Operating Leverage Sensitivity", "Margin Integrity", "Sensitivity to volume changes."),
ValuationVector("MI-03", "Cost Structure Rigidity", "Margin Integrity", "Fixed vs variable cost inflexibility."),
ValuationVector("MI-04", "Input Cost Inflation Exposure", "Margin Integrity", "Commodity or supplier inflation risk."),
ValuationVector("MI-05", "Labor Cost Dependency", "Margin Integrity", "Dependence on labor-intensive model."),
ValuationVector("MI-06", "Contribution Margin Compression Risk", "Margin Integrity", "Decline in incremental margins."),
ValuationVector("MI-07", "EBITDA Adjustment Aggressiveness", "Margin Integrity", "Extent of add-back adjustments."),
ValuationVector("MI-08", "Working Capital Drag", "Margin Integrity", "Cash absorption from operations."),
ValuationVector("MI-09", "Economies of Scale Realization Risk", "Margin Integrity", "Failure to achieve scale efficiencies."),
ValuationVector("MI-10", "Margin Forecast Reliability", "Margin Integrity", "Accuracy of projected margins."),

# -------------------------------------------------
# CAPITAL STRUCTURE (CS-01 → CS-10)
# -------------------------------------------------
ValuationVector("CS-01", "Debt Maturity Compression", "Capital Structure", "Near-term refinancing pressure."),
ValuationVector("CS-02", "Covenant Breach Sensitivity", "Capital Structure", "Risk of covenant violations."),
ValuationVector("CS-03", "Interest Coverage Fragility", "Capital Structure", "Ability to service debt."),
ValuationVector("CS-04", "Refinancing Dependency", "Capital Structure", "Need for capital market access."),
ValuationVector("CS-05", "Leverage Escalation Risk", "Capital Structure", "Trend of rising leverage."),
ValuationVector("CS-06", "Off-Balance Sheet Exposure", "Capital Structure", "Hidden leverage risk."),
ValuationVector("CS-07", "Equity Dilution Probability", "Capital Structure", "Likelihood of shareholder dilution."),
ValuationVector("CS-08", "Preferred Stack Complexity", "Capital Structure", "Liquidation preference layering."),
ValuationVector("CS-09", "Capital Structure Subordination Risk", "Capital Structure", "Structural seniority misalignment."),
ValuationVector("CS-10", "Sponsor Exit Overhang Risk", "Capital Structure", "Large shareholder liquidity pressure."),

# -------------------------------------------------
# LIQUIDITY RISK (LR-01 → LR-10)
# -------------------------------------------------
ValuationVector("LR-01", "Runway Coverage Ratio", "Liquidity Risk", "Months of cash coverage."),
ValuationVector("LR-02", "Short-Term Liquidity Mismatch", "Liquidity Risk", "Mismatch of assets and liabilities."),
ValuationVector("LR-03", "Burn Rate Acceleration", "Liquidity Risk", "Increasing operating cash burn."),
ValuationVector("LR-04", "Contingent Liability Shock Risk", "Liquidity Risk", "Potential unexpected obligations."),
ValuationVector("LR-05", "Inventory Illiquidity Exposure", "Liquidity Risk", "Slow-moving inventory burden."),
ValuationVector("LR-06", "Receivables Collection Risk", "Liquidity Risk", "Delayed customer payments."),
ValuationVector("LR-07", "Liquidity Facility Dependence", "Liquidity Risk", "Reliance on revolving credit."),
ValuationVector("LR-08", "Cash Trap Restrictions", "Liquidity Risk", "Restricted cash limitations."),
ValuationVector("LR-09", "Liquidity Stress Scenario Resilience", "Liquidity Risk", "Performance under stress."),
ValuationVector("LR-10", "Dividend Recapitalization Risk", "Liquidity Risk", "Cash extraction vulnerability."),

# -------------------------------------------------
# GOVERNANCE (GV-01 → GV-10)
# -------------------------------------------------
ValuationVector("GV-01", "Board Independence Integrity", "Governance", "Degree of independent oversight."),
ValuationVector("GV-02", "Founder Control Concentration", "Governance", "Voting power imbalance."),
ValuationVector("GV-03", "Related Party Transaction Exposure", "Governance", "Conflicted transactions."),
ValuationVector("GV-04", "Executive Compensation Alignment", "Governance", "Incentive misalignment."),
ValuationVector("GV-05", "Succession Planning Fragility", "Governance", "Leadership continuity risk."),
ValuationVector("GV-06", "Audit Committee Robustness", "Governance", "Financial oversight strength."),
ValuationVector("GV-07", "Governance Disclosure Transparency", "Governance", "Clarity of governance reporting."),
ValuationVector("GV-08", "Shareholder Rights Imbalance", "Governance", "Minority protection weakness."),
ValuationVector("GV-09", "Insider Liquidity Behavior Risk", "Governance", "Suspicious insider selling."),
ValuationVector("GV-10", "Ethics and Compliance Infrastructure", "Governance", "Internal compliance systems."),

# -------------------------------------------------
# REGULATORY EXPOSURE (RE-01 → RE-08)
# -------------------------------------------------
ValuationVector("RE-01", "Jurisdictional Regulatory Sensitivity", "Regulatory Exposure", "Exposure to volatile regimes."),
ValuationVector("RE-02", "Licensing Dependency Risk", "Regulatory Exposure", "Dependence on regulatory licenses."),
ValuationVector("RE-03", "Pending Litigation Materiality", "Regulatory Exposure", "Financial impact of litigation."),
ValuationVector("RE-04", "Antitrust Vulnerability", "Regulatory Exposure", "Market dominance scrutiny risk."),
ValuationVector("RE-05", "Data Privacy Compliance Risk", "Regulatory Exposure", "Exposure to data regulation."),
ValuationVector("RE-06", "Environmental Compliance Exposure", "Regulatory Exposure", "Environmental penalty risk."),
ValuationVector("RE-07", "Sanctions Exposure Risk", "Regulatory Exposure", "Exposure to sanctioned regions."),
ValuationVector("RE-08", "Policy Change Dependency", "Regulatory Exposure", "Reliance on favorable policy."),

# -------------------------------------------------
# OPERATIONAL RESILIENCE (OR-01 → OR-10)
# -------------------------------------------------
ValuationVector("OR-01", "Single-Point Operational Failure Risk", "Operational Resilience", "Lack of redundancy."),
ValuationVector("OR-02", "Supply Chain Concentration Risk", "Operational Resilience", "Supplier dependency."),
ValuationVector("OR-03", "Technology Infrastructure Fragility", "Operational Resilience", "System downtime risk."),
ValuationVector("OR-04", "Cybersecurity Exposure", "Operational Resilience", "Vulnerability to cyber threats."),
ValuationVector("OR-05", "Operational Scalability Constraints", "Operational Resilience", "Growth bottlenecks."),
ValuationVector("OR-06", "Key Personnel Dependency", "Operational Resilience", "Reliance on critical individuals."),
ValuationVector("OR-07", "Business Continuity Preparedness", "Operational Resilience", "Disaster readiness."),
ValuationVector("OR-08", "Outsourcing Dependency Risk", "Operational Resilience", "Third-party reliance."),
ValuationVector("OR-09", "Operational Cost Volatility", "Operational Resilience", "Unpredictable cost swings."),
ValuationVector("OR-10", "Integration Execution Risk", "Operational Resilience", "M&A integration failure."),

# -------------------------------------------------
# COUNTERPARTY RISK (CR-01 → CR-08)
# -------------------------------------------------
ValuationVector("CR-01", "Counterparty Default Exposure", "Counterparty Risk", "Risk of partner insolvency."),
ValuationVector("CR-02", "Vendor Financial Fragility", "Counterparty Risk", "Supplier bankruptcy risk."),
ValuationVector("CR-03", "Banking Relationship Concentration", "Counterparty Risk", "Reliance on single bank."),
ValuationVector("CR-04", "Insurance Coverage Adequacy", "Counterparty Risk", "Coverage insufficiency."),
ValuationVector("CR-05", "Strategic Partner Dependency", "Counterparty Risk", "Dependence on alliances."),
ValuationVector("CR-06", "Distributor Solvency Risk", "Counterparty Risk", "Channel partner risk."),
ValuationVector("CR-07", "Reinsurance Counterparty Risk", "Counterparty Risk", "Exposure in reinsurance chain."),
ValuationVector("CR-08", "Derivative Counterparty Exposure", "Counterparty Risk", "Financial contract risk."),

# -------------------------------------------------
# MACRO SENSITIVITY (MS-01 → MS-08)
# -------------------------------------------------
ValuationVector("MS-01", "Interest Rate Sensitivity", "Macro Sensitivity", "Exposure to rate changes."),
ValuationVector("MS-02", "Currency Volatility Exposure", "Macro Sensitivity", "FX fluctuation risk."),
ValuationVector("MS-03", "Commodity Price Sensitivity", "Macro Sensitivity", "Input commodity exposure."),
ValuationVector("MS-04", "Inflation Pass-Through Capacity", "Macro Sensitivity", "Ability to offset inflation."),
ValuationVector("MS-05", "GDP Correlation Dependency", "Macro Sensitivity", "Dependence on economic cycles."),
ValuationVector("MS-06", "Credit Market Tightening Exposure", "Macro Sensitivity", "Access to capital risk."),
ValuationVector("MS-07", "Geopolitical Instability Exposure", "Macro Sensitivity", "Exposure to instability."),
ValuationVector("MS-08", "Trade Policy Vulnerability", "Macro Sensitivity", "Tariff and trade risk."),

# -------------------------------------------------
# VALUATION INTEGRITY (VI-01 → VI-10)
# -------------------------------------------------
ValuationVector("VI-01", "Multiple Expansion Dependency", "Valuation Integrity", "Reliance on exit multiple growth."),
ValuationVector("VI-02", "Terminal Value Dominance Risk", "Valuation Integrity", "DCF terminal value dependency."),
ValuationVector("VI-03", "Comparable Selection Bias", "Valuation Integrity", "Cherry-picked comps."),
ValuationVector("VI-04", "Aggressive Forecast Horizon", "Valuation Integrity", "Extended projection optimism."),
ValuationVector("VI-05", "Discount Rate Underestimation Risk", "Valuation Integrity", "Underpriced risk premium."),
ValuationVector("VI-06", "Synergy Realization Overstatement", "Valuation Integrity", "Overestimated synergies."),
ValuationVector("VI-07", "Pro Forma Earnings Inflation", "Valuation Integrity", "Adjusted earnings distortion."),
ValuationVector("VI-08", "Asset Impairment Deferral Risk", "Valuation Integrity", "Delayed impairment recognition."),
ValuationVector("VI-09", "Intangible Asset Valuation Risk", "Valuation Integrity", "Subjective asset pricing."),
ValuationVector("VI-10", "Fair Value Estimation Uncertainty", "Valuation Integrity", "Mark-to-model risk."),

# -------------------------------------------------
# DISCLOSURE QUALITY (DQ-01 → DQ-08)
# -------------------------------------------------
ValuationVector("DQ-01", "Financial Reporting Transparency", "Disclosure Quality", "Clarity of disclosures."),
ValuationVector("DQ-02", "Segment Reporting Adequacy", "Disclosure Quality", "Detail of segment breakdown."),
ValuationVector("DQ-03", "Non-GAAP Reconciliation Clarity", "Disclosure Quality", "Transparency of adjustments."),
ValuationVector("DQ-04", "Auditor Qualification Risk", "Disclosure Quality", "Auditor concern signals."),
ValuationVector("DQ-05", "Restatement Frequency Risk", "Disclosure Quality", "History of financial restatements."),
ValuationVector("DQ-06", "Disclosure Lag Timeliness", "Disclosure Quality", "Delay in reporting."),
ValuationVector("DQ-07", "Off-Cycle Disclosure Behavior", "Disclosure Quality", "Selective disclosures."),
ValuationVector("DQ-08", "Risk Factor Disclosure Completeness", "Disclosure Quality", "Completeness of risk section."),

# -------------------------------------------------
# CAPITAL ALLOCATION (CA-01 → CA-10)
# -------------------------------------------------
ValuationVector("CA-01", "Capital Efficiency Discipline", "Capital Allocation", "Return on invested capital discipline."),
ValuationVector("CA-02", "Acquisition Discipline Integrity", "Capital Allocation", "M&A valuation prudence."),
ValuationVector("CA-03", "Share Repurchase Rationality", "Capital Allocation", "Buyback timing quality."),
ValuationVector("CA-04", "Dividend Sustainability Risk", "Capital Allocation", "Dividend coverage reliability."),
ValuationVector("CA-05", "R&D Capital Productivity", "Capital Allocation", "Return on innovation spend."),
ValuationVector("CA-06", "Capex Allocation Efficiency", "Capital Allocation", "Capital expenditure returns."),
ValuationVector("CA-07", "Working Capital Deployment Discipline", "Capital Allocation", "Efficiency of capital cycle."),
ValuationVector("CA-08", "Debt-Funded Expansion Risk", "Capital Allocation", "Leveraged growth strategy risk."),
ValuationVector("CA-09", "Cash Hoarding Inefficiency", "Capital Allocation", "Underutilized balance sheet."),
ValuationVector("CA-10", "Strategic Pivot Capital Risk", "Capital Allocation", "Capital loss from strategic shifts."),
]
