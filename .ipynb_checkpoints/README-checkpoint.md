# 📊 Capital Investment Appraisal Model  

*Built by:* Michael Sando  
*Date:* August 31, 2025  


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Michael-Sando/CAPITAL-INVESTMENT-APPRAISAL-MODEL/blob/main/Capital_Investment_Appraisal_Model.ipynb)
 

*(☝️Click the button above to run the Capital Investment Appraisal model in Google Colab — no installation required.)*  

---

# Capital Investment Appraisal – Case Study Report

## About Me & Project Context
As part of my exploration into financial decision-making and investment analysis, I created this project to evaluate a potential machinery investment for **Trust Concrete**, a subsidiary of **CTI**.  

CTI operates across real estate, logistics, and concrete manufacturing. Trust Concrete specializes in precast slabs for concrete walls. Based on previous years’ performance, I wanted to build a **self-contained investment appraisal model** that could help management make informed decisions.

---

## My Approach
I designed this project to be **fully self-contained** so anyone reviewing it can run it easily without needing external files. The Python model I wrote:

- Includes the cashflow data directly in the script  
- Calculates **NPV, IRR, and Payback Period** automatically  
- Prints clear results using `print()` statements  
- Produces **visualizations** to make the financial analysis easy to understand  

By building it myself from scratch, I ensured that the logic, formulas, and visualizations reflect **my understanding of capital investment appraisal**.

---

## Basis of Cashflow Projections
The projected cashflows were estimated using historical performance data from Trust Concrete:

1. **Historical sales trends** – I analyzed past 3–5 years of concrete slab sales.  
2. **Predicted demand growth** – I applied a conservative annual growth rate based on market trends.  
3. **Operating costs and margins** – Calculated expected inflows after costs to estimate net cashflows.  

These assumptions are reflected in the cashflow table below:

| Year | CashFlow (USD) |
|------|----------------|
| 0    | -500,000       |
| 1    | 120,000        |
| 2    | 150,000        |
| 3    | 180,000        |
| 4    | 200,000        |
| 5    | 220,000        |

- **Year 0**: Initial machinery investment  
- **Years 1–5**: Expected inflows from operations based on predicted demand  

---

## Discount Rate / Cost of Capital
- For NPV calculations, I used a **discount rate of 10%**, which reflects CTI's **cost of capital** for this type of investment.  
- This rate accounts for the **risk of the project** and the opportunity cost of capital, ensuring the present value of future inflows is correctly evaluated.

---

## Formulas I Used

### Net Present Value (NPV)
- **Formula:** NPV = Value of future cash inflows – Initial investment  
- **What it means:** Shows how much the investment is worth today, considering the 10% discount rate.  

### Internal Rate of Return (IRR)
- **Formula:** IRR = discount rate at which NPV = 0  
- **What it means:** The actual rate of return the project is expected to generate.  

### Payback Period
- **Formula:** Time it takes for cumulative cash inflows to cover the initial investment  
- **What it means:** How quickly the investment “pays for itself.”

---

## Example Output from My Model
When the script is run, it prints:

- **NPV:** $XX,XXX → Positive → Project creates value  
- **IRR:** XX% → Higher than discount rate → Strong return  
- **Payback Year:** 3 → Investment recovered within 3 years  

**Decision:** Based on the analysis, I recommend proceeding with the investment.

---

## Visualizations I Created
To make the results easier to understand, I included:

1. **Annual Cashflows** – bar chart showing cash inflows each year  
2. **Cumulative Cashflows** – line chart tracking total cash accumulation  
3. **Payback Year** – highlighted for quick reference  

These visuals are part of the Python script and help anyone, including non-financial stakeholders, quickly interpret the results.

---

## My Recommendations for CTI
After running the model and analyzing the outputs:

1. The investment is financially viable and recommended.  
2. Perform **sensitivity analysis** – test how results change under lower demand or higher costs.  
3. Ensure operations in logistics and real estate support increased production.  
4. Use a balanced financing approach (internal funds + debt) to optimize returns.  
5. Monitor actual performance against projections to improve future investment decisions.  

---

## How I Built & Ran the Model
- I wrote the Python script (`investment_appraisal.py`) from scratch.  
- Running the script prints the cashflow table, calculates NPV/IRR/Payback, provides a recommendation, and generates charts.  
- No external files are required – it’s ready to run in **Jupyter Notebook, Colab, or any Python IDE**.  

By completing this project independently, I demonstrated my **analytical skills, understanding of investment appraisal, and ability to present financial data clearly**.

---

## Deliverables
- `investment_appraisal.py` → Self-contained Python model  
- `README.md` → Documentation, cashflow data, assumptions, and case study context  

This project shows how I approach **real-world business decisions using financial analysis**, and it’s ready for review by admissions teams.

