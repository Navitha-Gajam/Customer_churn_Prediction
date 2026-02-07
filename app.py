from flask import Flask, render_template, request
import pandas as pd
import pickle
import random

app = Flask(__name__)

# Load artifacts
with open("churn_artifacts.pkl", "rb") as f:
    artifacts = pickle.load(f)

model = artifacts["model"]
pipeline = artifacts["pipeline"]
final_features = artifacts["features"]

with open("num_cat_columns.pkl", "rb") as f:
    cols = pickle.load(f)

NUM_COLS = cols["numerical"]
CAT_COLS = cols["categorical"]

# Load dataset for dropdowns
raw_df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
random.seed(42)
partners = ['Jio', 'Airtel', 'BSNL', 'Vodafone']
raw_df.insert(
    0,
    'telecom_partner',
    [random.choice(partners) for _ in range(len(raw_df))]
)
raw_df = raw_df.drop("customerID", axis=1)

CATEGORY_VALUES = {
    col: sorted(raw_df[col].dropna().unique().tolist())
    for col in CAT_COLS
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            user_input = {}

            for col in NUM_COLS:
                user_input[col] = float(request.form.get(col))

            for col in CAT_COLS:
                value = request.form.get(col)
                if isinstance(value, list):
                    value = value[0]
                user_input[col] = str(value)

            input_df = pd.DataFrame([user_input])
            input_encoded = pd.get_dummies(input_df)
            input_encoded = input_encoded.reindex(
                columns=final_features,
                fill_value=0
            )

            input_scaled = pd.DataFrame(
                pipeline.transform(input_encoded),
                columns=final_features
            )

            prediction = model.predict(input_scaled)[0]

            if prediction == 1:
                decision = "WILL churn"
            else:
                decision = "WILL NOT churn"

            result = {"decision": decision}

        except Exception:
            error = "Invalid input. Please check values and try again."

    return render_template(
        "index.html",
        num_cols=NUM_COLS,
        cat_cols=CAT_COLS,
        category_values=CATEGORY_VALUES,
        result=result,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)