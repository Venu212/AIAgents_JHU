import json
import ast
from pathlib import Path

path = Path(r"c:\Users\Venugopal.malireddy\AIAgents_JHU\2_Autonomous Financial Analyst\Autonomous_financial_analyst_Learners_Notebook.ipynb")
data = json.loads(path.read_text(encoding="utf-8"))

for idx, cell in enumerate(data.get("cells", [])):
    if cell.get("cell_type") != "code":
        continue
    source = "".join(cell.get("source", []))
    try:
        ast.parse(source)
    except SyntaxError as exc:
        print(f"Cell #{idx} id={cell.get('id')} SyntaxError: {exc}")
