import json
from pathlib import Path

NOTEBOOK_PATH = Path(r"c:\Users\Venugopal.malireddy\AIAgents_JHU\2_Autonomous Financial Analyst\Autonomous_financial_analyst_Learners_Notebook.ipynb")
TARGET_CELL_ID = "f1625d18"
NEW_SOURCE = [
    "# Create your agent (choose type: \"traditional\", \"basic\", or \"full\")\n",
    "my_agent = create_financial_agent(agent_type=\"full\", with_memory=True)\n",
    "\n",
    "# Configure memory\n",
    "config = {\"configurable\": {\"thread_id\": \"my_test_session\"}}\n",
    "\n",
    "# Test with your own query (keep prompts in triple quotes for HTML export)\n",
    "YOUR_QUERY = \"\"\"Tell me about Amazon's financial performance\"\"\"\n",
    "\n",
    "print(\"=\" * 80)\n",
    "print(\"YOUR CUSTOM QUERY TEST\")\n",
    "print(\"=\" * 80 + \"\\n\")\n",
    "print(f\"Query: {YOUR_QUERY}\\n\")\n",
    "print(\"-\" * 80 + \"\\n\")\n",
    "\n",
    "result = my_agent.invoke(\n",
    "    {\"messages\": [HumanMessage(content=YOUR_QUERY)]},\n",
    "    config=config\n",
    ")\n",
    "\n",
    "print(\"\\n🤖 AGENT RESPONSE:\")\n",
    "print(\"=\" * 80)\n",
    "print(result[\"messages\"][ -1].content)\n",
    "print(\"\\n\" + \"=\" * 80)\n",
]

def main():
    data = json.loads(NOTEBOOK_PATH.read_text(encoding="utf-8"))
    for cell in data.get("cells", []):
        if cell.get("id") == TARGET_CELL_ID:
            cell["source"] = NEW_SOURCE
            break
    else:
        raise ValueError(f"Cell id {TARGET_CELL_ID} not found")
    NOTEBOOK_PATH.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

if __name__ == "__main__":
    main()
