# Customer_churn_Prediction
Project Overview
The focuses is on analysing customer churn using the Telco Customer Churn dataset. From this EDA we understand customer behaviour patterns and identify factors that influence churn using Matplotlib visualizations.
Dataset Source: https://www.kaggle.com/datasets/blastchar/telco-customer-churn


Tools & Libraries Used
•	Python
•	Pandas
•	Matplotlib
•	Logging (for tracking execution)


 Dataset Description
Each row represents a customer and includes:
•	Demographic information (Gender, Senior Citizen)
•	Account details (Tenure, Contract type, Payment method)
•	Service usage (Internet service, Monthly charges)
•	Target variable: Churn (Yes / No)

 Visualizations & Insights

1. Customer Churn Distribution
Visualization: Bar Chart

Insight:

•	Majority of customers did not churn

•	A significant portion did churn, indicating a retention problem

Business Meaning:

Customer retention strategies are required to reduce churn rate.

<img width="750" height="540" alt="image" src="https://github.com/user-attachments/assets/b91849fe-d7bd-4fc5-88fa-23057d4fc363" />



 2.Contract Type vs Churn
Visualization: Bar Chart (Crosstab)

Insight:

•	Month-to-month contracts have the highest churn

•	One-year and Two-year contracts show much lower churn

Business Meaning:

Long-term contracts help improve customer retention.

<img width="640" height="480" alt="contract vs churn" src="https://github.com/user-attachments/assets/db2bc9c7-9b34-42d5-bb4a-f4ea39ccb452" />



3. Gender vs Churn
Visualization: Bar Chart

Insight:

•	Churn behaviour is almost equal for both genders

•	Gender is not a strong churn indicator

Business Meaning:

Churn prevention strategies should focus on service factors rather than gender.
<img width="640" height="480" alt="gender_vs_churn" src="https://github.com/user-attachments/assets/dd004052-1153-4d7b-97de-db7b57289238" />



4.Internet Service vs Gender
Visualization: Bar Chart (Crosstab)

Insight:

•	Fiber optic service has the highest number of customers

•	Internet service usage is balanced across genders

Business Meaning:

Internet service adoption is not gender-biased.

<img width="640" height="480" alt="internet services vs gender" src="https://github.com/user-attachments/assets/6f38b184-d1fa-4965-aaa8-89d158e5b5c9" />



5. Monthly Charges vs Churn
Visualization: Histogram

Insight:

•	Customers with higher monthly charges tend to churn more

•	Lower charges show better retention

Business Meaning:

High pricing may be a major reason for customer churn.

<img width="640" height="480" alt="monthly_charges vs churn" src="https://github.com/user-attachments/assets/119839d5-3921-4c65-bc55-94310f4fa8d8" />


6.Churn Among Senior Citizens by Gender
Visualization: Bar Chart

Insight:

•	Senior citizens show a higher churn tendency

•	Gender difference among seniors is minimal

Business Meaning:

Special retention offers may be needed for senior customers.

<img width="640" height="480" alt="senior gender vs churn" src="https://github.com/user-attachments/assets/9dc4de91-71b0-4239-b7a9-80fc2d782a9a" />


7. Tenure vs Churn
Visualization: Histogram

Insight:

•	Customers with low tenure (new customers) churn more

•	Long-tenure customers are more loyal

Business Meaning:

The first few months are critical for customer retention.

<img width="640" height="480" alt="Tenure vs churn" src="https://github.com/user-attachments/assets/d381ce5c-c15b-4b71-a6a3-c49d665770c7" />





8.TelecomPartner vs Churn Visualization: Grouped Bar Chart

Insight:

• Jio shows the highest churn rate (~27.3%) — proportionally more customers are leaving.

• BSNL has the lowest churn rate (~25.2%) — relatively more stable customers.

• Vodafone has the largest absolute number of churned customers (490) due to its bigger customer base.

• Differences are modest (~2 percentage points) — verify statistical significance before strong conclusions.


Business Meaning:


The provider a customer uses is associated with small but actionable differences in churn. Prioritize root-cause analysis for Jio to reduce its churn rate, and target Vodafone for volume-based interventions (even modest rate improvements there yield larger customer retention gains).



<img width="640" height="480" alt="telecom_partner_vs_churn" src="https://github.com/user-attachments/assets/f4d7a58a-de39-4b2d-9669-62b232382fde" />



9.Payment Method vs Churn Visualization: Stacked Bar Chart

Insight:

• Electronic check customers show the highest churn rate (~45%) — a large proportion of customers using this method leave the service.

• Mailed check users have a moderate churn rate (~19%) — lower than electronic check but higher than automatic methods.

• Bank transfer (automatic) and credit card (automatic) users exhibit the lowest churn rates (~15–16%) — indicating stronger customer retention.

• Although total customer counts are similar across payment methods, churn likelihood varies significantly by payment type.

Business Meaning:

Payment method is a strong behavioral indicator of churn. Customers using manual payment methods, especially electronic checks, are more likely to churn. Encouraging migration to automatic payment methods (bank transfer or credit card) can materially reduce churn. Retention campaigns should prioritize electronic check users, as even small improvements in this group can yield meaningful reductions in overall churn.


<img width="600" height="400" alt="paymentmethod vs churn" src="https://github.com/user-attachments/assets/8762488d-4f89-4f3c-830a-80dbb8cce9f2" />






