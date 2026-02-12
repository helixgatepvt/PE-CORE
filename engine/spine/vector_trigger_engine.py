"""
HelixGate — Deterministic Vector Trigger Engine
------------------------------------------------

Evaluates structured company data against
canonical valuation vectors.

Outputs:
• triggered_vectors
• neutral_vectors
• suppressed_vectors (future use)
"""

from typing import Dict, List
from .vector_registry import load_all_vectors, ValuationVector


class VectorTriggerEngine:

    def __init__(self):
        self.vectors = load_all_vectors()

    def evaluate(self, company_data: Dict) -> Dict[str, List[str]]:
        """
        Evaluate company data against deterministic vector rules.
        """

        triggered = []
        neutral = []
        suppressed = []

        for vector in self.vectors:

            # --- Revenue Concentration Risk ---
            if vector.code == "RQ-01":
                concentration = company_data.get("top_customer_percentage", 0)
                if concentration > 40:
                    triggered.append(vector.code)
                else:
                    neutral.append(vector.code)

            # --- Gross Margin Volatility ---
            elif vector.code == "MI-01":
                volatility = company_data.get("gross_margin_volatility", 0)
                if volatility > 0.15:
                    triggered.append(vector.code)
                else:
                    neutral.append(vector.code)

            # --- Debt Maturity Compression ---
            elif vector.code == "CS-01":
                near_term_debt = company_data.get("debt_due_12m", 0)
                cash = company_data.get("cash_on_hand", 1)
                if near_term_debt > cash:
                    triggered.append(vector.code)
                else:
                    neutral.append(vector.code)

            # --- Runway Coverage Ratio ---
            elif vector.code == "LR-01":
                burn = company_data.get("monthly_burn", 0)
                cash = company_data.get("cash_on_hand", 0)
                if burn > 0 and (cash / burn) < 12:
                    triggered.append(vector.code)
                else:
                    neutral.append(vector.code)

            # Default: neutral (until rule defined)
            else:
                neutral.append(vector.code)

        return {
            "triggered_vectors": triggered,
            "neutral_vectors": neutral,
            "suppressed_vectors": suppressed,
        }
