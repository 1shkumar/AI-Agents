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

