from app.services.text_cleaning_service import clean_text


text = """
Patient     Name:     John Doe


Blood Pressure:     150/95 mmHg



The patient was
advised to follow up.

HbA1c     7.2%
"""

cleaned_text = clean_text(text)

print("----- CLEANED TEXT -----")
print(cleaned_text)