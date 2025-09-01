# --------------------------------------
# Self-Contained Investment Appraisal Script
# --------------------------------------

import pandas as pd
import numpy_financial as nf
import matplotlib.pyplot as plt

# ------------------------------
# Cashflow Data (included in the script)
# ------------------------------
# Year 0 = initial investment, Years 1-5 = inflows
cashflow_data = {
    "Year": [0, 1, 2, 3, 4, 5],
    "CashFlow": [-500000, 120000, 150000, 180000, 200000, 220000]
}

cash_flows = pd.DataFrame(cashflow_data)

# Display cashflow table
print("=== Cashflow Table ===")
print(cash_flows)

# ------------------------------
# Parameters
# ------------------------------
discount_rate = 0.10  # 10%

# ------------------------------
# Investment Appraisal Calculations
# ------------------------------
npv = nf.npv(discount_rate, cash_flows["CashFlow"])
irr = nf.irr(cash_flows["CashFlow"])
cumulative_cashflow = cash_flows["CashFlow"].cumsum()
payback_index = (cumulative_cashflow >= 0).idxmax() if any(cumulative_cashflow >= 0) else None
payback_year = cash_flows.loc[payback_index, "Year"] if payback_index is not None else None

# ------------------------------
# Print Appraisal Results
# ------------------------------
print("\n=== Investment Appraisal Results ===")
print(f"Net Present Value (NPV): {round(npv, 2)}")
print(f"Internal Rate of Return (IRR): {round(irr*100, 2)}%")
print(f"Payback Year: {payback_year if payback_year is not None else 'Not achieved'}")

# Custom decision message
if npv > 0 and irr > discount_rate:
    decision = " The investment is financially viable and recommended."
elif npv <= 0 and irr <= discount_rate:
    decision = " The investment is not viable and should be rejected."
else:
    decision = " The investment has mixed indicators. Consider risk assessment."
print("Decision:", decision)

# ------------------------------
# Visualizations
# ------------------------------
plt.figure(figsize=(10,6))
plt.bar(cash_flows["Year"], cash_flows["CashFlow"], alpha=0.7, label="Annual Cash Flow")
plt.plot(cash_flows["Year"], cumulative_cashflow, marker="o", color="red", label="Cumulative Cash Flow")
if payback_year is not None:
    plt.axvline(x=payback_year, color="green", linestyle="--", label=f"Payback Year {payback_year}")
plt.axhline(y=0, color="black", linestyle="-")
plt.title("Cash Flow & Payback Analysis")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()