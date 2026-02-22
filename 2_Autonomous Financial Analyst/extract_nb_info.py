import json
import re

nb_path = r'c:\Users\Venugopal.malireddy\AIAgents_JHU\JHU_AgenticAI_Project-1_Learners_Notebook.ipynb'

try:
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Extract first markdown cell
    description = ""
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            description = "".join(cell['source'])
            break
            
    # Extract imports
    imports = set()
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = "".join(cell['source'])
            # Simple regex for imports
            matches = re.findall(r'^\s*(?:import|from)\s+(\w+)', source, re.MULTILINE)
            imports.update(matches)

    print("---DESCRIPTION---")
    print(description[:500]) # First 500 chars
    print("\n---IMPORTS---")
    print("\n".join(sorted(imports)))

except Exception as e:
    print(e)
