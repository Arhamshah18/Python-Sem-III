import re

text = """
Contact us at support@example.com or sales.dept@company.co.in.
Invalid emails: john@com, @domain.com, user@.com.
Another valid email: john_doe123@gmail.org.
"""

# Regex pattern for valid email addresses
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(pattern, text)
print("Extracted Email Addresses:")
for email in emails:
    print(f"- {email}")
