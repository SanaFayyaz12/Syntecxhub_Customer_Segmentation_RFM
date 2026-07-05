# 🕵️‍♂️ The Case of the Missing Customers (a.k.a. RFM Analysis)

**Syntecxhub Data Analysis Internship – Project 1**

---

## 📖 The Story

Imagine you run an online store. Every day, thousands of customers walk
in, some buy a lot, some buy once and vanish, and some... you haven't
seen in months. 👻

The big question every business owner loses sleep over is:

> *"Who are my best customers? Who's about to leave me? And who do I
> need to win back before it's too late?"*

That's exactly the mystery this project solves — using a detective
technique from the marketing world called **RFM Analysis**
(**R**ecency, **F**requency, **M**onetary). Think of it as a
credit score, but for customer loyalty. 🕵️‍♀️📊

---

## 🎯 The Mission

- 🧹 Clean up messy transactional data (because real data is never neat)
- 🧮 Calculate 3 key clues: **Recency**, **Frequency**, **Monetary**
- 🏷️ Sort every customer into a "personality type"
- 🔍 Study each group's behavior
- 💡 Turn insights into real marketing action
- 📊 Make it all pretty with charts (because nobody reads spreadsheets for fun)

---

## 🧩 Meet the Clues

| Clue | What it really means | How we get it |
|---|---|---|
| ⏰ **Recency** | "How long has it been since you last shopped with us?" | Days since last order |
| 🔁 **Frequency** | "How much of a regular are you?" | Total number of orders |
| 💰 **Monetary** | "How much love (money) have you given us?" | Total amount spent |

Each customer gets scored 1–5 on each clue (5 = superstar, 1 = ghost),
and those three numbers combine into their final **RFM profile**.

---

## 🎭 The Cast of Characters (Customer Segments)

| Segment | Who they really are |
|---|---|
| 👑 **Champions / Loyal** | Your VIPs. Recent, frequent, big spenders. Treat them like royalty. |
| 🌱 **Potential Loyalist** | Showing promise — a little nudge and they could become Champions. |
| 🆕 **New Customers** | Just walked in the door. First impressions matter! |
| ⚠️ **Needs Attention** | Used to be great, now going quiet. Send a "we miss you" text. |
| 🚨 **At Risk** | Big spenders who haven't shown up in a while. Red alert! |
| 💔 **Cannot Lose Them** | High-value customers going cold. Drop everything and win them back. |
| 🥀 **Churned** | Haven't seen them in ages. Might need a big reason to return. |
| 🤷 **Others** | The wildcards who don't fit a neat box. |

---

## 🗂️ What's Inside This Repo
Syntecxhub_Customer_Segmentation_RFM/
│
├── 📁 data/
│   ├── transactions.csv              # The raw evidence (transactional data)
│   ├── rfm_segmented_customers.csv   # Every customer, profiled
│   └── segment_summary.csv           # The group stats
│
├── 📁 images/
│   ├── segment_counts.png            # Who's in which gang?
│   ├── segment_revenue.png           # Who's actually paying the bills?
│   ├── recency_vs_frequency.png      # The full plot twist, visualized
│   ├── rfm_heatmap.png               # Scores at a glance
│   └── monetary_boxplot.png          # Show me the money 💵
│
├── generate_data.py     # Creates a realistic (synthetic) shopping dataset
├── rfm_analysis.py      # The detective script: clean → score → segment → chart
└── README.md            # You are here 📍

---

## ⚙️ How the Investigation Works

1. **Clean the evidence** — remove duplicates, nulls, and junk (negative/zero amounts)
2. **Calculate the clues** — Recency, Frequency, Monetary for every customer
3. **Score them 1–5** using quantiles (fair, data-driven grading)
4. **Assign a segment** based on their R-F-M combo
5. **Study the group behavior** — averages, totals, patterns
6. **Visualize everything** — because a good chart tells a story instantly

---

## 🔍 Plot Twist: What the Data Revealed

- 👑 **Champions/Loyal** are only ~29% of customers but bring in the
  **lion's share of revenue** — classic 80/20 rule in action.
- 🥀 A surprisingly large chunk (~28%) has gone quiet (**Churned**) —
  a huge win-back opportunity hiding in plain sight.
- 💔 Some big spenders are drifting away (**At Risk** / **Cannot Lose
  Them**) — these are the fires worth putting out first.
- 🆕 **New Customers** are showing up but not coming back often yet —
  the classic "first date, no second date" problem.

---

## 💡 The Action Plan (Marketing Recommendations)

| Segment | What To Do |
|---|---|
| 👑 Champions / Loyal | Loyalty perks, early access, referral rewards |
| 🌱 Potential Loyalist | Personalized upsell/cross-sell offers |
| 🆕 New Customers | Warm onboarding + discount on their 2nd order |
| ⚠️ Needs Attention | Friendly "we miss you" re-engagement emails |
| 🚨 At Risk / 💔 Cannot Lose Them | Personalized win-back campaigns, surveys |
| 🥀 Churned | Low-cost reactivation attempt, or stop ad spend on them |

---

## 🛠️ Tools of the Trade

- 🐍 Python 3
- 🐼 pandas, numpy — for wrangling the data
- 📊 matplotlib, seaborn — for making it all look good

---

## ▶️ Run the Investigation Yourself

```bash
pip install pandas numpy matplotlib seaborn

python generate_data.py     # Step 1: create the dataset
python rfm_analysis.py      # Step 2: solve the mystery
```

Charts will land in `/images`, and the full customer case files will be
in `/data`. ☕

---

## 🎬 The End (or Just the Beginning?)

RFM is just the first chapter — the same customer data could power
churn prediction, lifetime value models, or personalized recommendation
engines. But for now, mystery solved. 🕵️‍♂️✅

---

**Internship:** Syntecxhub Data Analysis Internship Program
**Project:** Customer Segmentation using RFM Analysis
