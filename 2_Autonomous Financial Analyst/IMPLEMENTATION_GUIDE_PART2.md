# Implementation Guide Part 2 - RAG Implementation

This guide provides complete code implementations for Part 2 (RAG) placeholder sections.

---

## Part 2: RAG Implementation

### Cell #23: Document Loading Implementation

Replace the placeholder in Cell #23 with:

```python
from langchain_community.document_loaders import PyPDFDirectoryLoader

# Load all PDF documents from the Companies-AI-Initiatives folder
loader = PyPDFDirectoryLoader("Companies-AI-Initiatives")
documents = loader.load()

print(f"✅ Loaded {len(documents)} document pages from PDF files")
print(f"Sample document metadata: {documents[0].metadata if documents else 'No documents loaded'}")
```

---

### Cell #24: Document Chunking Implementation

Replace the placeholder in Cell #24 with:

```python
# Chunking the data
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Create text splitter with appropriate chunk size and overlap
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # Size of each chunk in characters
    chunk_overlap=200,      # Overlap between chunks to maintain context
    length_function=len,
    separators=["\n\n", "\n", " ", ""]  # Split on paragraphs, then lines, then words
)

# Split documents into chunks
chunks = text_splitter.split_documents(documents)

print(f"✅ Split {len(documents)} documents into {len(chunks)} chunks")
print(f"\nSample chunk:")
print("=" * 80)
print(f"Content: {chunks[0].page_content[:300]}...")
print(f"Metadata: {chunks[0].metadata}")
print("=" * 80)
```

---

### Cell #25: Vector Store Creation Implementation

Replace the placeholder in Cell #25 with:

```python
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import json

# Load API configuration
config_path = "config.json"
with open(config_path, 'r') as f:
    config = json.load(f)

api_key = config.get('API_KEY')
api_base = config.get('OPENAI_API_BASE')

# Initialize embeddings model
embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002",
    api_key=api_key,
    base_url=api_base
)

# Create vector store from chunks
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db",  # Persist to disk
    collection_name="company_ai_initiatives"
)

print(f"✅ Created vector store with {len(chunks)} chunks")
print(f"Collection name: company_ai_initiatives")
print(f"Persist directory: ./chroma_db")

# Test retrieval
test_query = "What AI initiatives is Microsoft pursuing?"
test_results = vectorstore.similarity_search(test_query, k=3)

print(f"\n📊 Test Query: '{test_query}'")
print(f"Retrieved {len(test_results)} relevant chunks")
print("\nTop result preview:")
print("=" * 80)
print(test_results[0].page_content[:300] if test_results else "No results")
print("=" * 80)
```

---

### Cell #27: query_private_database Tool Implementation

Replace the placeholder in Cell #27 with:

```python
@tool
def query_private_database(query: str) -> str:
    """
    Query the private company AI initiatives database using RAG.
    
    Args:
        query: Natural language query about company AI initiatives
    
    Returns:
        String containing relevant information from company documents with source citations
    """
    try:
        from langchain_openai import OpenAIEmbeddings
        from langchain_community.vectorstores import Chroma
        from datetime import datetime
        import json
        
        # Load API configuration
        config_path = "config.json"
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        api_key = config.get('API_KEY')
        api_base = config.get('OPENAI_API_BASE')
        
        # Initialize embeddings
        embeddings = OpenAIEmbeddings(
            model="text-embedding-ada-002",
            api_key=api_key,
            base_url=api_base
        )
        
        # Load existing vector store
        vectorstore = Chroma(
            persist_directory="./chroma_db",
            embedding_function=embeddings,
            collection_name="company_ai_initiatives"
        )
        
        # Perform similarity search
        results = vectorstore.similarity_search(query, k=5)
        
        if not results:
            return f"No relevant information found in the database for query: {query}"
        
        # Format results with source citations
        formatted_results = f"Private Database Query Results for: '{query}'\n"
        formatted_results += f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        formatted_results += "=" * 80 + "\n\n"
        
        for idx, doc in enumerate(results, 1):
            source = doc.metadata.get('source', 'Unknown source')
            page = doc.metadata.get('page', 'N/A')
            content = doc.page_content
            
            formatted_results += f"Result {idx}:\n"
            formatted_results += f"Source: {source} (Page {page})\n"
            formatted_results += f"Content: {content[:400]}...\n"
            formatted_results += "-" * 80 + "\n\n"
        
        return formatted_results.strip()
        
    except Exception as e:
        return f"Error querying private database: {str(e)}"
```

---

### Cell #28: RAG Tool Testing

Replace the placeholder in Cell #28 with:

```python
# Test the query_private_database tool
print("Testing query_private_database tool...")
print("=" * 80)

test_query = "What are Amazon's AI initiatives?"
test_result = query_private_database.invoke({"query": test_query})
print(test_result)

print("\n" + "=" * 80)
print("✅ RAG tool test complete!")
```

---

### Cell #30: create_enhanced_financial_agent Implementation

Replace the placeholder in Cell #30 with:

```python
def create_enhanced_financial_agent(with_rag: bool = True, with_memory: bool = True):
    """
    Create an enhanced financial research agent with RAG capabilities.
    
    Args:
        with_rag: Whether to include RAG tool for querying private documents
        with_memory: Whether to enable conversation memory
    
    Returns:
        Compiled LangGraph agent with enhanced capabilities
    """
    from langgraph.graph import StateGraph, MessagesState, START, END
    from langgraph.prebuilt import ToolNode
    from langgraph.checkpoint.memory import MemorySaver
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import SystemMessage
    import json
    
    # Load API configuration
    config_path = "config.json"
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    api_key = config.get('API_KEY')
    api_base = config.get('OPENAI_API_BASE')
    
    # Use the enhanced charter with RAG
    system_prompt = AGENT_CHARTER_WITH_RAG
    
    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=api_key,
        base_url=api_base
    )
    
    # Define available tools
    if with_rag:
        tools = [
            get_stock_price, 
            get_stock_history, 
            search_financial_news, 
            analyze_sentiment,
            query_private_database  # Add RAG tool
        ]
    else:
        tools = [
            get_stock_price, 
            get_stock_history, 
            search_financial_news, 
            analyze_sentiment
        ]
    
    # Bind tools to LLM
    llm_with_tools = llm.bind_tools(tools)
    
    # Define agent node
    def agent_node(state: MessagesState):
        """Agent node that decides which tools to call"""
        messages = state["messages"]
        
        # Add system prompt as first message if not present
        if not messages or messages[0].type != "system":
            messages = [SystemMessage(content=system_prompt)] + messages
        
        response = llm_with_tools.invoke(messages)
        return {"messages": [response]}
    
    # Define conditional routing
    def should_continue(state: MessagesState):
        """Determine if agent should continue using tools or end"""
        messages = state["messages"]
        last_message = messages[-1]
        
        # If there are tool calls, continue to tools
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            return "tools"
        # Otherwise, end
        return END
    
    # Define tool node with logging
    def tool_node_with_logging(state: MessagesState):
        """Execute tools and log results"""
        messages = state["messages"]
        last_message = messages[-1]
        
        # Log tool calls
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            print(f"\n🔧 Executing {len(last_message.tool_calls)} tool(s):")
            for tool_call in last_message.tool_calls:
                print(f"  - {tool_call['name']}")
        
        tool_node = ToolNode(tools)
        result = tool_node.invoke(state)
        return result
    
    # Build the graph
    workflow = StateGraph(MessagesState)
    
    # Add nodes
    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", tool_node_with_logging)
    
    # Add edges
    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges("agent", should_continue, ["tools", END])
    workflow.add_edge("tools", "agent")
    
    # Compile with optional memory
    if with_memory:
        memory = MemorySaver()
        agent = workflow.compile(checkpointer=memory)
    else:
        agent = workflow.compile()
    
    return agent
```

---

### Cell #33: Final Testing with RAG

Replace the placeholder in Cell #33 with:

```python
print("="*80)
print("COMPREHENSIVE TEST: Enhanced Agent with RAG")
print("="*80)

# Create enhanced agent
enhanced_agent = create_enhanced_financial_agent(with_rag=True, with_memory=True)

# Configure memory
config = {"configurable": {"thread_id": "enhanced_test_session"}}

# Test query that requires both market data AND private documents
test_query = """
Provide a comprehensive investment analysis for Microsoft (MSFT) that includes:
1. Current stock performance and 3-year history
2. Recent news sentiment
3. Their AI initiatives from our private database
4. Investment recommendation with confidence level
"""

print(f"\nQuery: {test_query}\n")
print("-"*80 + "\n")

result = enhanced_agent.invoke(
    {"messages": [HumanMessage(content=test_query)]},
    config=config
)

print("\n🤖 ENHANCED AGENT RESPONSE:")
print("="*80)
print(result["messages"][-1].content)
print("\n" + "="*80)

print("\n✅ Enhanced agent test complete!")
print("\n📊 This test demonstrates:")
print("  ✓ Integration of all 5 tools (4 market tools + 1 RAG tool)")
print("  ✓ Autonomous tool selection and orchestration")
print("  ✓ Synthesis of public market data with private company documents")
print("  ✓ Comprehensive investment analysis with multiple data sources")
```

---

## Summary of All Implementations

### Part 1 - Core Agent (Cells to Update):
- ✅ **Cell #5**: `get_stock_price` - Fetch current stock data
- ✅ **Cell #6**: `get_stock_history` - Fetch historical performance
- ✅ **Cell #7**: `search_financial_news` - Search financial news
- ✅ **Cell #8**: `analyze_sentiment` - Analyze text sentiment
- ✅ **Cell #9**: Manual tool testing
- ✅ **Cell #12**: `create_financial_agent` - Build LangGraph agent

### Part 2 - RAG Enhancement (Cells to Update):
- ✅ **Cell #23**: Document loading from PDFs
- ✅ **Cell #24**: Document chunking with text splitter
- ✅ **Cell #25**: Vector store creation with Chroma
- ✅ **Cell #27**: `query_private_database` tool
- ✅ **Cell #28**: RAG tool testing
- ✅ **Cell #30**: `create_enhanced_financial_agent` with RAG
- ✅ **Cell #33**: Comprehensive testing with RAG

---

## Important Notes Before Implementation:

1. **API Keys**: Ensure your `config.json` has valid API keys
2. **File Paths**: Verify the `Companies-AI-Initiatives` folder exists with PDF files
3. **Dependencies**: Run Cell #0 (pip install) before implementing
4. **Sequential Execution**: Implement and test Part 1 before moving to Part 2
5. **Error Handling**: All implementations include try-except blocks
6. **Source Citations**: All tools include timestamps and source information

---

## Testing Workflow:

1. **Test each tool individually** (Cells #9, #28)
2. **Test basic agent** (Cells #13-15)
3. **Test error handling** (Cell #18)
4. **Test RAG components** (Cell #26)
5. **Test enhanced agent** (Cells #31-33)

---

**Ready to implement?** Review each code block, understand the logic, then copy into the appropriate cell.
