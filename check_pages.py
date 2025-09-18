import yaml
from pathlib import Path

# Adjust path if needed
pages_file = Path("docs/Volume1_Foundations/.pages")

if not pages_file.exists():
    print(f"❌ File not found: {pages_file.resolve()}")
else:
    try:
        with open(pages_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        print("✅ YAML parsed successfully!\n")
        print("Contents:")
        print(data)
    except Exception as e:
        print("❌ Error parsing YAML:")
        print(str(e))
