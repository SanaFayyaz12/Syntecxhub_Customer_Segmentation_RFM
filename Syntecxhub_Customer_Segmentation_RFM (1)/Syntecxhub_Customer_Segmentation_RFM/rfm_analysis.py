"""
rfm_analysis.py
Customer Segmentation using RFM (Recency, Frequency, Monetary) Analysis
Syntecxhub Data Analysis Internship - Project 1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 120

# ---------------------------------------------------------
# 1. LOAD & CLEAN DATA
# ---------------------------------------------------------
df = pd.read_csv("data/transactions.csv", parse_dates=["OrderDate"])

print("Raw shape:", df.shape)

# Clean: drop duplicates, drop nulls, remove negative/zero amounts
df = df.drop_duplicates()
df = df.dropna(subset=["CustomerID", "OrderDate", "Amount"])
df = df[df["Amount"] > 0]

print("Cleaned shape:", df.shape)

# ---------------------------------------------------------
# 2. CALCULATE RFM METRICS
# ---------------------------------------------------------
snapshot_date = df["OrderDate"].max() + pd.Timedelta(days=1)

rfm = df.groupby("CustomerID").agg(
    Recency=("OrderDate", lambda x: (snapshot_date - x.max()).days),
    Frequency=("OrderID", "count"),
    Monetary=("Amount", "sum")
).reset_index()

rfm["Monetary"] = rfm["Monetary"].round(2)

print("\nRFM sample:")
print(rfm.head())

# ---------------------------------------------------------
# 3. RFM SCORING (1 = worst, 5 = best)
# ---------------------------------------------------------
rfm["R_Score"] = pd.qcut(rfm["Recency"], 5, labels=[5, 4, 3, 2, 1]).astype(int)
rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
rfm["M_Score"] = pd.qcut(rfm["Monetary"], 5, labels=[1, 2, 3, 4, 5]).astype(int)

rfm["RFM_Score"] = rfm["R_Score"].astype(str) + rfm["F_Score"].astype(str) + rfm["M_Score"].astype(str)
rfm["RFM_Total"] = rfm[["R_Score", "F_Score", "M_Score"]].sum(axis=1)

# ---------------------------------------------------------
# 4. CUSTOMER SEGMENTATION
# ---------------------------------------------------------
def segment_customer(row):
    r, f, m = row["R_Score"], row["F_Score"], row["M_Score"]
    if r >= 4 and f >= 4 and m >= 4:
        return "Champions / Loyal"
    elif r >= 4 and f >= 3:
        return "Potential Loyalist"
    elif r >= 4 and f <= 2:
        return "New Customers"
    elif r == 3 and f >= 3:
        return "Needs Attention"
    elif r <= 2 and f >= 4:
        return "At Risk"
    elif r <= 2 and f <= 2 and m >= 3:
        return "Cannot Lose Them"
    elif r <= 2 and f <= 2:
        return "Churned"
    else:
        return "Others"

rfm["Segment"] = rfm.apply(segment_customer, axis=1)

# Save final RFM table
rfm.to_csv("data/rfm_segmented_customers.csv", index=False)
print("\nSegment counts:")
print(rfm["Segment"].value_counts())

# ---------------------------------------------------------
# 5. BEHAVIOR ANALYSIS PER SEGMENT
# ---------------------------------------------------------
segment_summary = rfm.groupby("Segment").agg(
    Customers=("CustomerID", "count"),
    Avg_Recency=("Recency", "mean"),
    Avg_Frequency=("Frequency", "mean"),
    Avg_Monetary=("Monetary", "mean"),
    Total_Revenue=("Monetary", "sum")
).round(1).sort_values("Total_Revenue", ascending=False)

segment_summary.to_csv("data/segment_summary.csv")
print("\nSegment summary:")
print(segment_summary)

# ---------------------------------------------------------
# 6. VISUALIZATIONS
# ---------------------------------------------------------

# 6.1 Segment size bar chart
plt.figure(figsize=(9, 5.5))
order = rfm["Segment"].value_counts().index
sns.countplot(data=rfm, y="Segment", order=order, palette="viridis")
plt.title("Customer Count by Segment", fontsize=14, fontweight="bold")
plt.xlabel("Number of Customers")
plt.ylabel("")
plt.tight_layout()
plt.savefig("images/segment_counts.png")
plt.close()

# 6.2 Revenue contribution by segment
plt.figure(figsize=(9, 5.5))
rev = segment_summary["Total_Revenue"].sort_values(ascending=True)
plt.barh(rev.index, rev.values, color=sns.color_palette("viridis", len(rev)))
plt.title("Total Revenue Contribution by Segment", fontsize=14, fontweight="bold")
plt.xlabel("Total Revenue")
plt.tight_layout()
plt.savefig("images/segment_revenue.png")
plt.close()

# 6.3 Recency vs Frequency scatter, colored by segment
plt.figure(figsize=(9, 6.5))
sns.scatterplot(
    data=rfm, x="Recency", y="Frequency", hue="Segment",
    palette="tab10", s=60, alpha=0.75
)
plt.title("Recency vs Frequency by Segment", fontsize=14, fontweight="bold")
plt.xlabel("Recency (days since last purchase)")
plt.ylabel("Frequency (number of orders)")
plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left", fontsize=8)
plt.tight_layout()
plt.savefig("images/recency_vs_frequency.png")
plt.close()

# 6.4 Heatmap of average RFM scores per segment
heatmap_data = rfm.groupby("Segment")[["R_Score", "F_Score", "M_Score"]].mean().round(2)
plt.figure(figsize=(7, 5.5))
sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f", linewidths=0.5)
plt.title("Average RFM Scores by Segment", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("images/rfm_heatmap.png")
plt.close()

# 6.5 Monetary distribution boxplot
plt.figure(figsize=(9, 5.5))
sns.boxplot(data=rfm, x="Monetary", y="Segment", order=order, palette="viridis")
plt.title("Monetary Value Distribution by Segment", fontsize=14, fontweight="bold")
plt.xlabel("Total Spend")
plt.ylabel("")
plt.tight_layout()
plt.savefig("images/monetary_boxplot.png")
plt.close()

print("\nAll charts saved to /images")
print("Analysis complete. Outputs in /data folder.")
