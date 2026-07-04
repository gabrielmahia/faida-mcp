"""FaidaMCP — Kenya Investment and Capital Markets Tools (6 tools). All data DEMO."""
from __future__ import annotations
from typing import Optional
from fastmcp import FastMCP
mcp = FastMCP(name="faida-mcp", instructions="Kenya investment and capital markets guidance. DEMO data only.")

@mcp.tool(name="treasury_bond_calculator", description="Kenya Treasury bond yield and return calculator. DEMO.")
def treasury_bond_calculator(principal_kes: float, tenor_years: int = 10,
                              coupon_rate_pct: Optional[float] = None) -> dict:
    DEFAULT_RATES = {2: 13.5, 5: 14.2, 10: 14.8, 15: 15.1, 20: 15.5}
    rate = coupon_rate_pct or DEFAULT_RATES.get(tenor_years, 14.5)
    annual_coupon = principal_kes * rate / 100
    total_coupons = annual_coupon * tenor_years
    total_return = total_coupons + principal_kes
    real_rate = rate - 6.5  # rough inflation adjustment (DEMO)
    return {"source": "DEMO — CBK rates indicative Q2 2026", "principal_kes": principal_kes,
            "tenor_years": tenor_years, "coupon_rate_pct": rate,
            "annual_interest_kes": round(annual_coupon, 2),
            "total_interest_kes": round(total_coupons, 2),
            "total_return_kes": round(total_return, 2),
            "real_return_est_pct": round(real_rate, 1),
            "buy_via": "CBK DhowCSD portal: dhowordcsd.cbk.go.ke OR commercial bank", 
            "minimum": "KES 50,000", "tax": "WHT 15% on interest for residents",
            "disclaimer": "DEMO — verify current yields at cbk.go.ke"}

@mcp.tool(name="nse_equities_guide", description="Nairobi Securities Exchange guide for first-time investors. DEMO.")
def nse_equities_guide(query: Optional[str] = None) -> dict:
    GUIDE = {
        "account_setup":   "Open CDS account at NSE-licensed stockbroker. ID + KES 1,000 minimum.",
        "buy_process":     "Instruct broker (phone/app). Settlement T+3 days. Brokerage: 1.8–2.5% per trade.",
        "key_indices":     "NSE 20 Share Index (top 20), NSE All Share Index (NASI), NSE 25 (broader)",
        "segments":        "Main Investment Market (MIM), Alternative Investment Market (AIM), Growth Enterprise Market (GEMS)",
        "top_sectors":     "Banking (KCB, Equity, Co-op), Telecoms (Safaricom), Energy (KenGen, KPLC), Agri (Kakuzi)",
        "costs":           "Brokerage 1.8%, CDS levy 0.12%, NSE levy 0.12%, withholding tax 5% on dividends",
        "diaspora":        "Diaspora investors welcome. CDSC foreign investor account. Remit via licensed dealer.",
        "platforms":       "Mobile: EazyTrader (Equity), I-Trade (Faida Securities), NSE app (coming)",
    }
    if query:
        q = query.lower()
        matched = {k: v for k, v in GUIDE.items() if k in q or any(w in q for w in k.split("_"))}
        return {"source": "DEMO — nse.co.ke", "query": query, "information": matched or GUIDE}
    return {"source": "DEMO — nse.co.ke", "guide": GUIDE, "portal": "nse.co.ke"}

@mcp.tool(name="unit_trust_comparison", description="Compare Kenya unit trust fund types and typical returns. DEMO.")
def unit_trust_comparison(risk_profile: Optional[str] = "moderate") -> dict:
    FUNDS = {
        "money_market": {"risk": "low", "typical_return_pct": 13.5, "liquidity": "T+1 (next day)",
                         "min_kes": 1000, "examples": ["CIC MMF", "Sanlam MMF", "ICEA Lion MMF"]},
        "bond_fund":    {"risk": "low-moderate", "typical_return_pct": 14.5, "liquidity": "T+3",
                         "min_kes": 5000, "examples": ["Old Mutual Bond Fund", "Britam Bond Plus"]},
        "equity_fund":  {"risk": "high", "typical_return_pct": "8–20% (variable)", "liquidity": "T+5",
                         "min_kes": 5000, "examples": ["GenAfrica Equity Fund", "CIC Equity Fund"]},
        "balanced":     {"risk": "moderate", "typical_return_pct": "11–16% (variable)", "liquidity": "T+3",
                         "min_kes": 5000, "examples": ["ICEA Lion Balanced Fund", "Sanlam Balanced Fund"]},
        "real_estate":  {"risk": "moderate", "typical_return_pct": "9–14%", "liquidity": "Limited",
                         "min_kes": 5000, "examples": ["ILAM Fahari I-REIT (NSE listed)"]},
    }
    if risk_profile:
        risk_map = {"low": ["money_market","bond_fund"], "moderate": ["bond_fund","balanced"],
                    "high": ["equity_fund","balanced"]}
        relevant = {k: FUNDS[k] for k in risk_map.get(risk_profile.lower(), list(FUNDS.keys()))}
        return {"source": "DEMO — RBA Kenya", "risk_profile": risk_profile, "funds": relevant,
                "regulator": "Retirement Benefits Authority (RBA) regulates unit trusts",
                "tax": "Dividends and capital gains generally exempt in regulated schemes"}
    return {"source": "DEMO — RBA Kenya", "all_fund_types": FUNDS}

@mcp.tool(name="diaspora_investment_guide", description="Investment options for Kenya diaspora. DEMO.")
def diaspora_investment_guide(location: Optional[str] = None) -> dict:
    return {"source": "DEMO — CBK, NSE, Treasury", "diaspora_location": location,
            "options": [
                {"name": "M-Akiba Retail Bond", "description": "CBK mobile-first Treasury bond via M-PESA",
                 "min_investment": "KES 3,000", "yield": "~13-14%", "platform": "M-PESA"},
                {"name": "NSE Equities", "description": "Buy Kenya stocks via licensed broker",
                 "min_investment": "KES 1,000+", "platform": "NSE-licensed broker"},
                {"name": "Unit Trusts", "description": "Pooled investment in MMF/bonds/equities",
                 "min_investment": "KES 1,000", "remittance": "Via licensed FX dealer"},
                {"name": "REITs", "description": "Real estate via ILAM Fahari I-REIT on NSE",
                 "min_investment": "One share (~KES 5)", "liquidity": "NSE listed"},
                {"name": "Infrastructure Bonds", "description": "Tax-free govt bonds for infrastructure",
                 "yield": "~14-15%", "tax": "Interest tax-exempt for bonds issued before 2027"},
                {"name": "Direct Property", "description": "Land/property (see ardhi-mcp + nyumba-mcp)",
                 "note": "Non-citizen: leasehold only (max 99 years)"},
            ],
            "remittance_tip": "Use licensed money transfer operators. Report above USD 10,000 to CBK.",
            "cds_account": "Open CDS at cdsc.co.ke for equity purchases"}

@mcp.tool(name="nse_ipo_guide", description="Kenya Initial Public Offering (IPO) participation guide. DEMO.")
def nse_ipo_guide() -> dict:
    return {"source": "DEMO — NSE", "how_to_participate": [
                "1. Monitor NSE announcements at nse.co.ke",
                "2. Get a CDS account if you don't have one",
                "3. Obtain prospectus from lead transaction advisor",
                "4. Complete application form via stockbroker or mobile platform",
                "5. Payment via M-PESA/RTGS by closing date",
                "6. Allocation letter + shares credited to CDS within 10 working days",
            ],
            "recent_history": "Kenya's IPO market has been quiet (2020-2025). Keep watching NSE.",
            "min_allocation": "Usually KES 2,500–5,000 (varies per IPO)",
            "tip": "Safaricom IPO (2008) remains Kenya's largest. Future candidates: NTSA, KPLC privatisation."}

@mcp.tool(name="financial_literacy_kenya", description="Kenya personal finance fundamentals and glossary. DEMO.")
def financial_literacy_kenya(topic: Optional[str] = None) -> dict:
    TOPICS = {
        "emergency_fund":  "3-6 months expenses in money market fund (liquid, earning ~13%). Before any investing.",
        "debt_first":      "Pay high-interest debt (credit cards 36%+, Fuliza 9% pm) before investing.",
        "compound_interest":"At 14% return: KES 10K monthly → KES 2.5M in 10 years. Start early.",
        "diversification": "Spread across: money market (liquid), bonds (stable), equities (growth). 70/20/10 for beginners.",
        "m_pesa_savings":  "M-Shwari (CBA) and KCB M-PESA earn 7-8%. Good for emergency fund tier.",
        "sacco_vs_bank":   "SACCO loans: 12-14% pa. Bank loans: 14-18% pa. SACCO savings: 8-12%. Better rates.",
        "budget_rule":     "50/30/20: 50% needs, 30% wants, 20% savings/investments. Adjust for Kenya realities.",
    }
    if topic:
        t = topic.lower()
        matched = {k: v for k, v in TOPICS.items() if k in t or any(w in t for w in k.split("_"))}
        return {"source": "DEMO", "topic": topic, "guidance": matched or TOPICS}
    return {"source": "DEMO", "financial_literacy_topics": TOPICS}

def main() -> None:
    """Console entry point."""
    mcp.run()
