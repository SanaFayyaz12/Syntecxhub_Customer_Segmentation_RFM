# Customer Segmentation using RFM Analysis
**Syntecxhub Data Analysis Internship – Project 1**

## 📌 Overview
This project segments customers based on their purchasing behavior using
**RFM (Recency, Frequency, Monetary) Analysis** — a proven technique used
in real-world marketing and CRM systems to identify loyal customers,
customers at risk of churning, and new customers.

## 🎯 Objectives
- Clean and prepare transactional customer data
- Calculate RFM metrics (Recency, Frequency, Monetary)
- Score and segment customers into meaningful groups
- Analyze the behavior pattern of each segment
- Provide targeted marketing recommendations
- Visualize segments using charts

## 🗂️ Project Structure
```
Syntecxhub_Customer_Segmentation_RFM/
│
├── data/
│   ├── transactions.csv              # Raw transactional dataset
│   ├── rfm_segmented_customers.csv   # Final customer-level RFM + segment table
│   └── segment_summary.csv           # Aggregated metrics per segment
│
├── images/
│   ├── segment_counts.png
│   ├── segment_revenue.png
│   ├── recency_vs_frequency.png
│   ├── rfm_heatmap.png
│   └── monetary_boxplot.png
│
├── generate_data.py     # Generates the synthetic transactional dataset
├── rfm_analysis.py      # Main analysis script (cleaning → RFM → segmentation → charts)
└── README.md
```

## ⚙️ How It Works

### 1. Data Cleaning
Removes duplicate transactions, null values, and non-positive order amounts.

### 2. RFM Metric Calculation
| Metric | Meaning | Formula |
|---|---|---|
| Recency | Days since the customer's last order | `snapshot_date - last_order_date` |
| Frequency | Number of orders placed | `count(orders)` |
| Monetary | Total amount spent | `sum(order_amount)` |

### 3. Scoring
Each metric is split into 5 quantile-based bands (1 = lowest, 5 = highest),
producing an `R_Score`, `F_Score`, and `M_Score` for every customer.

### 4. Segmentation Logic
Customers are grouped using their R/F/M scores into:

| Segment | Description |
|---|---|
| Champions / Loyal | Recent, frequent, high spenders |
| Potential Loyalist | Recent buyers, moderate frequency |
| New Customers | Very recent, low order count |
| Needs Attention | Average recency & frequency, may slip away |
| At Risk | Was frequent, but hasn't purchased in a while |
| Cannot Lose Them | High spenders who have gone quiet |
| Churned | Long inactive, low activity |
| Others | Doesn't fit a clear pattern |

## 📊 Key Insights (from this run)
- **Champions/Loyal** customers make up ~29% of the base but generate the
  **majority of total revenue** — the highest-value group to retain.
- **Churned** customers are a large group (~28%) with very low recent
  engagement, representing a significant win-back opportunity.
- **At Risk** and **Cannot Lose Them** customers have high historic spend
  but declining recency — reactivation campaigns should prioritize them.
- **New Customers** show strong recency but low frequency — good onboarding
  nurture campaigns could convert them into loyalists.

## 💡 Marketing Recommendations
- **Champions / Loyal** → Loyalty rewards, early access to new products, referral programs.
- **Potential Loyalist** → Personalized upsell/cross-sell offers to increase frequency.
- **New Customers** → Onboarding email series, first-purchase discount for the 2nd order.
- **Needs Attention** → Re-engagement emails, limited-time offers.
- **At Risk / Cannot Lose Them** → Win-back campaigns, personalized discounts, feedback surveys.
- **Churned** → Low-cost reactivation campaign or exclusion from paid ad spend (low ROI).

## 🛠️ Tech Stack
- Python 3
- pandas, numpy — data processing
- matplotlib, seaborn — visualization

## ▶️ How to Run
```bash
pip install pandas numpy matplotlib seaborn
python generate_data.py     # creates the synthetic dataset
python rfm_analysis.py      # runs full analysis and saves charts
```

## 📈 Sample Visualizations
See the `/images` folder for:
- Customer count per segment
- Revenue contribution per segment
- Recency vs Frequency scatter plot
- RFM score heatmap
- Monetary distribution boxplot

---
**Internship:** Syntecxhub Data Analysis Internship Program
**Project:** Customer Segmentation using RFM Analysis
