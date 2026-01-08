# ReAct Agent using Ollama

This project is a simple **ReAct-based AI agent** built using a **local LLM**.  
The agent can **reason about user queries** and **take actions** using tools such as calculation, customer data lookup, and email rewriting.

The entire project runs **locally using Ollama**, without any paid APIs.

---

##  Features

-  Perform mathematical calculations  
-  Fetch customer information  
-  Rewrite emails in different tones (formal, polite, urgent, etc.)  
-  Uses the ReAct (Reason + Act) agent pattern  
-  Runs fully offline using a local LLM  

---

##  Tech Stack

- **Python**
- **Ollama** – Local LLM runtime
- **LangChain** – Tool abstraction
- **LangGraph** – ReAct agent control flow
- **uv** – Dependency management

---

## What is ReAct?

**ReAct** stands for **Reason + Act**.

In this project, the agent:

1. Understands the user query  
2. Decides whether a tool is required  
3. Calls the appropriate tool  
4. Combines the tool outputs  
5. Returns the final response  

The internal reasoning process is handled by the agent and is not exposed to the user.

---

##  Summary

This project demonstrates how an AI agent can go beyond simple chat responses and **interact with tools to perform real tasks**.  
It is designed as a **learning project**, especially suitable for beginners exploring **agentic AI concepts**.

---
