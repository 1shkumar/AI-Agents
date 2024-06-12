# AI-Agents
Experimenting with implementing AI agents and exploring their potential applications using Langgraph.

# What are AI agents?
An AI agent is an entity that can act autonomously in an environment. It can take information from its surroundings, make decisions based on that data, and act to transform those circumstances—physical, digital, or mixed. More advanced systems can learn and update their behavior over time, constantly trying out new solutions to a problem until they achieve the goal.
These agents and their behaviour is defined by signal flow graph. To support directly building agents like this, langchain has extended to support langGraph. 

![Screenshot (832)](https://github.com/1shkumar/AI-Agents/assets/97458999/ebef25b3-16df-4fa8-8a25-2e80da118eeb)

![Screenshot (831)](https://github.com/1shkumar/AI-Agents/assets/97458999/db527cb0-8eeb-42ae-9a12-fe219c0b17d3)

# Define the state logic
This is the logic for what state the chatbot is in. If the last message is a tool call, then we are in the state where the "prompt creator" (prompt) should respond. Otherwise, if the last message is not a HumanMessage, then we know the human should respond next and so we are in the END state. If the last message is a HumanMessage, then if there was a tool call previously we are in the prompt state. Otherwise, we are in the "info gathering" (info) state.

# Create the graph

![Screenshot (833)](https://github.com/1shkumar/AI-Agents/assets/97458999/5bf2244e-d1ff-43df-9d59-e71759998f9e)

# LangGraph

Langgraph is a specialized library within the LangChain ecosystem designed to enhance the efficiency of AI applications. It facilitates the creation of stateful, multi-actor applications with large language models (LLMs). The primary advantage of Langgraph is its ability to coordinate and checkpoint various chains or actors using standard Python functions.

Langgraph marks a significant advancement in managing cyclic computational steps, where traditional Directed Acyclic Graphs (DAGs) fall short. Inspired by systems like Pregel and Apache Beam, and utilizing an interface akin to NetworkX, it extends the LangChain Expression Language to handle multiple actors and chains in complex workflows. These capabilities enable developers to orchestrate intricate program structures, which are crucial for applications that require intelligent, agent-like behaviors and iterative decision-making processes.

![langgraph1 (1)](https://github.com/1shkumar/AI-Agents/assets/97458999/c5d980f5-1099-4c9a-aab0-a4f5249075e5)

LangGraph offers several benefits over other AI libraries for developers who want to create stateful, multi-actor applications with Large Language Models (LLMs).

#Flexibility: LangGraph provides a high-level abstraction for defining and managing the actors, the LLMs, and their interactions using a graph-based representation. This approach allows developers to create more complex and sophisticated applications that require a memory of previous conversations or actions.
#Scalability: LangGraph is built on top of LangChain, a decentralized network for language model computation and storage. This architecture enables developers to scale their applications easily by adding more nodes to the network.
#Cyclic data flows: LangGraph supports cyclic data flows, which allow nodes to receive feedback from their previous outputs and inputs. This feature enables applications to maintain a memory of past interactions and use that information to tailor their responses accordingly.
#Ease of use: LangGraph is designed to be easy to use, with a simple and intuitive API that enables developers to create stateful, multi-actor applications with LLMs quickly.

