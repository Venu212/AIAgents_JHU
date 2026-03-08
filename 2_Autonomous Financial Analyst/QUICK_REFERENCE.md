# Quick Reference - Cell-by-Cell Implementation Map

Use this guide to quickly find which code to copy into each placeholder cell.

---

## 📍 Cell Mapping

| Cell # | Cell ID | What to Implement | Guide File | Section |
|--------|---------|-------------------|------------|---------|
| **5** | `21cf6f8d` | `get_stock_price` function | IMPLEMENTATION_GUIDE.md | Cell #5 |
| **6** | `cb16edb4` | `get_stock_history` function | IMPLEMENTATION_GUIDE.md | Cell #6 |
| **7** | `ded889d7` | `search_financial_news` function | IMPLEMENTATION_GUIDE.md | Cell #7 |
| **8** | `c71c2821` | `analyze_sentiment` function | IMPLEMENTATION_GUIDE.md | Cell #8 |
| **9** | `1c44ae8b` | Tool testing code | IMPLEMENTATION_GUIDE.md | Cell #9 |
| **12** | `b78756d2` | `create_financial_agent` function | IMPLEMENTATION_GUIDE.md | Cell #12 |
| **23** | `vdtrhFRYs_Uz` | Document loading | IMPLEMENTATION_GUIDE_PART2.md | Cell #23 |
| **24** | `fgw8MqC8nTdP` | Document chunking | IMPLEMENTATION_GUIDE_PART2.md | Cell #24 |
| **25** | `ye-w6C3YSlVJ` | Vector store creation | IMPLEMENTATION_GUIDE_PART2.md | Cell #25 |
| **27** | `7e7aab29` | `query_private_database` tool | IMPLEMENTATION_GUIDE_PART2.md | Cell #27 |
| **28** | `fac732f8` | RAG tool testing | IMPLEMENTATION_GUIDE_PART2.md | Cell #28 |
| **30** | `d481535a` | `create_enhanced_financial_agent` | IMPLEMENTATION_GUIDE_PART2.md | Cell #30 |
| **33** | `ad1a098c` | Final comprehensive testing | IMPLEMENTATION_GUIDE_PART2.md | Cell #33 |

---

## 🚀 Implementation Order (Recommended)

### Phase 1: Basic Tools (30 minutes)
1. ✅ Cell #5 - `get_stock_price`
2. ✅ Cell #9 - Test it
3. ✅ Cell #6 - `get_stock_history`
4. ✅ Cell #7 - `search_financial_news`
5. ✅ Cell #8 - `analyze_sentiment`

### Phase 2: Agent Creation (15 minutes)
6. ✅ Cell #12 - `create_financial_agent`
7. ✅ Run Cells #13-15 - Test different agent types
8. ✅ Run Cell #18 - Test error handling

### Phase 3: RAG Setup (20 minutes)
9. ✅ Cell #23 - Load documents
10. ✅ Cell #24 - Chunk documents
11. ✅ Cell #25 - Create vector store
12. ✅ Cell #26 - Test retrieval

### Phase 4: RAG Integration (20 minutes)
13. ✅ Cell #27 - `query_private_database` tool
14. ✅ Cell #28 - Test RAG tool
15. ✅ Cell #30 - `create_enhanced_financial_agent`
16. ✅ Run Cells #31-33 - Test enhanced agent

**Total Time: ~85 minutes**

---

## 🎯 What Each Implementation Does

### Part 1: Core Financial Tools

**`get_stock_price`** (Cell #5)
- Fetches current stock price from Yahoo Finance
- Returns: price, volume, market cap, 52-week high/low
- Error handling for invalid tickers

**`get_stock_history`** (Cell #6)
- Fetches historical performance (default 3 years)
- Calculates: price change, percent change, trend analysis
- Returns: start/end prices, high/low, average volume

**`search_financial_news`** (Cell #7)
- Uses Tavily API to search financial news
- Returns: Top 5 articles with titles, URLs, summaries
- Includes timestamps for source citation

**`analyze_sentiment`** (Cell #8)
- Uses OpenAI GPT-4o-mini for sentiment analysis
- Returns: Sentiment (Positive/Negative/Neutral), confidence score
- Includes investment implications

**`create_financial_agent`** (Cell #12)
- Builds LangGraph workflow with agent and tool nodes
- Supports 3 agent types: traditional, basic, full
- Optional conversation memory
- Autonomous tool selection and routing

---

### Part 2: RAG Enhancement

**Document Loading** (Cell #23)
- Loads all PDFs from `Companies-AI-Initiatives` folder
- Uses PyPDFDirectoryLoader
- Returns list of document objects with metadata

**Document Chunking** (Cell #24)
- Splits documents into 1000-character chunks
- 200-character overlap for context preservation
- Uses RecursiveCharacterTextSplitter

**Vector Store Creation** (Cell #25)
- Creates Chroma vector database
- Uses OpenAI text-embedding-ada-002
- Persists to `./chroma_db` directory
- Enables semantic search over company documents

**`query_private_database`** (Cell #27)
- RAG tool for querying company AI initiatives
- Performs similarity search (top 5 results)
- Returns relevant chunks with source citations
- Includes page numbers and document names

**`create_enhanced_financial_agent`** (Cell #30)
- Extended agent with 5 tools (4 market + 1 RAG)
- Uses enhanced charter with RAG instructions
- Synthesizes public market data with private documents
- Conversation memory enabled by default

---

## ⚠️ Common Issues & Solutions

### Issue: "API_KEY not found"
**Solution:** Check `config.json` exists and has valid keys

### Issue: "No module named 'yfinance'"
**Solution:** Run Cell #0 (pip install) first

### Issue: "Companies-AI-Initiatives folder not found"
**Solution:** Verify folder exists in same directory as notebook

### Issue: "Chroma database not found"
**Solution:** Run Cells #23-25 to create vector store first

### Issue: Tool returns "Error: ..."
**Solution:** Check error message - usually API connectivity or invalid input

---

## 📝 Before You Start Checklist

- [ ] Run Cell #0 to install all packages
- [ ] Verify `config.json` has valid API keys
- [ ] Confirm `Companies-AI-Initiatives` folder exists with PDFs
- [ ] Read through one implementation example to understand structure
- [ ] Have IMPLEMENTATION_GUIDE.md and IMPLEMENTATION_GUIDE_PART2.md open

---

## 🔍 Testing Strategy

**After each implementation:**
1. Run the cell to define the function
2. Run the corresponding test cell
3. Verify output looks correct
4. Fix any errors before moving to next cell

**Key test cells:**
- Cell #9: Test individual tools
- Cells #13-15: Test agent types
- Cell #18: Test error handling
- Cell #26: Test vector store retrieval
- Cell #28: Test RAG tool
- Cells #31-33: Test enhanced agent

---

## 💡 Tips for Success

1. **Copy carefully** - Preserve indentation exactly as shown
2. **Test incrementally** - Don't implement everything at once
3. **Read error messages** - They usually tell you exactly what's wrong
4. **Check API limits** - OpenAI and Tavily have rate limits
5. **Use print statements** - Add debugging output if needed

---

## 📚 Additional Resources

- **LangChain Docs:** https://python.langchain.com/docs/
- **LangGraph Docs:** https://langchain-ai.github.io/langgraph/
- **yfinance Docs:** https://pypi.org/project/yfinance/
- **Chroma Docs:** https://docs.trychroma.com/

---

**Need help?** Check the error message first, then review the implementation guide for that specific cell.
