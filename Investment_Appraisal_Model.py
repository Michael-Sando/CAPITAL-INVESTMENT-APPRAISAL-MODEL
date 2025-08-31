!pip install numpy-financial
!pip install reportlab
# --------------------------------------
# Investment Appraisal Report Generator
# --------------------------------------

import pandas as pd
import numpy_financial as nf
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

# ------------------------------
# Load Cashflows from Excel
# ------------------------------
file_path = r"C:\Users\DELL\Capital_Investment_Appraisal_Model\cashflows.xlsx"
cash_flows = pd.read_excel(file_path, sheet_name="Sheet1")

# Parameters
discount_rate = 0.10  # 10%

# ------------------------------
# Investment Appraisal Metrics
# ------------------------------
npv = nf.npv(discount_rate, cash_flows["CashFlow"])
irr = nf.irr(cash_flows["CashFlow"])
cumulative_cashflow = cash_flows["CashFlow"].cumsum()
payback_index = (cumulative_cashflow >= 0).idxmax() if any(cumulative_cashflow >= 0) else None
payback_year = cash_flows.loc[payback_index, "Year"] if payback_index is not None else None

# ------------------------------
# Save Results to Excel
# ------------------------------
output_excel = r"C:\Users\DELL\Capital_Investment_Appraisal_Model\investment_appraisal_report.xlsx"

with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
    cash_flows["CumulativeCashFlow"] = cumulative_cashflow
    cash_flows.to_excel(writer, sheet_name="Cashflows", index=False)

    summary = pd.DataFrame({
        "Metric": ["NPV", "IRR (%)", "Payback Year"],
        "Value": [round(npv, 2), round(irr * 100, 2), payback_year if payback_year else "Not achieved"]
    })
    summary.to_excel(writer, sheet_name="Summary", index=False)

print(f"✅ Excel report saved at: {output_excel}")

# ------------------------------
# Visualization (save as image)
# ------------------------------
plt.figure(figsize=(10, 6))
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

chart_path = r"C:\Users\DELL\Capital_Investment_Appraisal_Model\cashflow_chart.png"
plt.savefig(chart_path)
plt.close()

# ------------------------------
# Generate PDF Report
# ------------------------------
output_pdf = r"C:\Users\DELL\Capital_Investment_Appraisal_Model\investment_appraisal_report.pdf"

doc = SimpleDocTemplate(output_pdf, pagesize=A4)
styles = getSampleStyleSheet()
story = []

story.append(Paragraph("📊 Investment Appraisal Report", styles["Title"]))
story.append(Spacer(1, 20))

story.append(Paragraph(f"<b>Net Present Value (NPV):</b> {round(npv, 2)}", styles["Normal"]))
story.append(Paragraph(f"<b>Internal Rate of Return (IRR):</b> {round(irr * 100, 2)} %", styles["Normal"]))
story.append(Paragraph(f"<b>Payback Period:</b> {payback_year if payback_year else 'Not achieved'}", styles["Normal"]))
story.append(Spacer(1, 20))

story.append(Paragraph("Below is the cash flow & payback analysis chart:", styles["Normal"]))
story.append(Spacer(1, 10))
story.append(Image(chart_path, width=400, height=250))

doc.build(story)

print(f"✅ PDF report generated at: {output_pdf}") 
