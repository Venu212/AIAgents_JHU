import json
from pathlib import Path

notebook_path = Path("Autonomous_financial_analyst_Learners_Notebook.ipynb")
data = json.loads(notebook_path.read_text(encoding="utf-8"))

print("=" * 80)
print("NOTEBOOK ANALYSIS REPORT")
print("=" * 80)
print(f"\nTotal cells: {len(data['cells'])}")
print(f"Code cells: {sum(1 for c in data['cells'] if c.get('cell_type') == 'code')}")
print(f"Markdown cells: {sum(1 for c in data['cells'] if c.get('cell_type') == 'markdown')}")

print("\n" + "=" * 80)
print("CODE CELLS ANALYSIS")
print("=" * 80)

code_cells = [c for c in data['cells'] if c.get('cell_type') == 'code']

for idx, cell in enumerate(code_cells):
    cell_id = cell.get('id', 'N/A')
    source = ''.join(cell.get('source', []))
    line_count = len(cell.get('source', []))
    
    print(f"\n[Cell #{idx}] ID: {cell_id}")
    print(f"  Lines: {line_count}")
    
    # Check for common issues
    issues = []
    
    if 'Your Code Goes Here' in source or '🧩' in source:
        issues.append("Contains placeholder - needs implementation")
    
    if 'import' in source and line_count < 5:
        issues.append("Import cell")
    
    if 'def ' in source:
        func_names = [line.split('def ')[1].split('(')[0] for line in source.split('\n') if 'def ' in line]
        issues.append(f"Defines functions: {', '.join(func_names)}")
    
    if 'create_financial_agent' in source:
        issues.append("Agent creation code")
    
    if 'StateGraph' in source or 'MessagesState' in source:
        issues.append("LangGraph workflow code")
    
    if 'try:' in source and 'except' in source:
        issues.append("Contains error handling")
    
    if line_count == 0:
        issues.append("EMPTY CELL")
    
    if issues:
        for issue in issues:
            print(f"    - {issue}")
    
    # Show first 3 lines for context
    if line_count > 0:
        preview = source.split('\n')[:3]
        print(f"  Preview: {preview[0][:60]}...")

print("\n" + "=" * 80)
print("SEARCHING FOR SPECIFIC PATTERNS")
print("=" * 80)

full_notebook = json.dumps(data)

patterns = {
    'API Key usage': 'OPENAI_API_KEY',
    'Tavily usage': 'tavily',
    'yfinance usage': 'yfinance',
    'LangChain imports': 'from langchain',
    'Tool decorators': '@tool',
    'Agent types': 'agent_type',
    'Error handling': 'try:',
}

for pattern_name, pattern in patterns.items():
    count = full_notebook.count(pattern)
    print(f"{pattern_name}: {count} occurrences")

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
