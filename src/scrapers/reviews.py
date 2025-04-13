import pandas as pd
import json
import os

def extract_reviews(csv_path, company_name, save_to_dir):
    df = pd.read_csv(csv_path)

    # Filter by firm name (not "Company Name" like before)
    matches = df[df['firm'].str.contains(company_name, case=False, na=False)]

    if matches.empty:
        print("❌ No reviews found for", company_name)
        return

    # Drop rows without 'pros' or 'cons'
    reviews = matches[['job_title', 'pros', 'cons']].dropna()

    # Merge pros + cons into single content
    review_data = [
        {
            "title": row['job_title'] if pd.notna(row['job_title']) else "N/A",
            "content": f"Pros: {row['pros']} | Cons: {row['cons']}"
        }
        for _, row in reviews.iterrows()
    ]

    os.makedirs(save_to_dir, exist_ok=True)
    out_path = os.path.join(save_to_dir, f"{company_name}.json")

    with open(out_path, "w") as f:
        json.dump(review_data, f, indent=2)

    print(f"[✓] Extracted {len(review_data)} reviews for '{company_name}' and saved to {out_path}")
