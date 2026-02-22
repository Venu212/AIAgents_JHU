import json
from pathlib import Path

NOTEBOOK = Path(r"c:\Users\Venugopal.malireddy\AIAgents_JHU\2_Autonomous Financial Analyst\Autonomous_financial_analyst_Learners_Notebook.ipynb")
TARGET_IDS = {"fjpfklmps2j", "d481535a"}

data = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
for cell in data.get("cells", []):
    cell_id = cell.get("id")
    if cell_id in TARGET_IDS:
        print(f"Cell {cell_id}:")
        print(''.join(cell.get('source', [])))
        print("=" * 40)
