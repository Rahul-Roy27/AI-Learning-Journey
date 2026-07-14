# 1. What is Streamlit?

## Definition

Streamlit is an open-source Python framework used to build interactive web applications for data science, machine learning, and AI using only Python.

It allows developers to convert Python scripts into web applications without requiring HTML, CSS, or JavaScript.

---

## Why was Streamlit created?

Streamlit was created to simplify the process of sharing data science and machine learning applications.

Instead of building a complete frontend, developers can create interactive web applications directly from Python code.

---

## Why is Streamlit popular?

- Pure Python framework
- Fast development
- Ideal for AI and ML projects
- Built-in interactive widgets
- Easy deployment
- Minimal boilerplate code

---

## Advantages

- Easy to learn
- Rapid prototyping
- Interactive UI components
- Suitable for AI dashboards and demos
- No frontend knowledge required for basic apps

---

## Limitations

- Less flexible than full-stack web frameworks
- Not intended for large-scale web applications
- Limited customization compared to frameworks like Flask or Django

---

## Common Use Cases

- RAG chatbots
- LLM applications
- Data dashboards
- Machine learning demos
- Data visualization
- AI prototypes


# 2. Streamlit Execution Model

## Reactive Execution Model

Streamlit follows a reactive execution model.

Whenever the user interacts with the application (such as clicking a button, typing in a text box, or uploading a file), Streamlit reruns the entire Python script from top to bottom.

---

## Why does Streamlit rerun the script?

Instead of updating only a small part of the page, Streamlit rebuilds the interface based on the current application state.

This ensures that the UI always reflects the latest data.

---

## Execution Flow

User Interaction
        │
        ▼
Entire Script Reruns
        │
        ▼
UI Rebuilt
        │
        ▼
Updated Output Displayed

---

## Limitation

Normal Python variables are recreated during every rerun.

As a result, their values are lost unless they are stored using `st.session_state`.

---

## Key Point

Every interaction in Streamlit causes the entire script to execute again from top to bottom.


# Streamlit Widgets

Widgets are the building blocks of a Streamlit application. They allow users to interact with the application by displaying information, accepting input, and providing feedback.

In this section, we'll learn each widget by understanding:
- What problem it solves
- What it is
- Syntax
- Parameters
- Example
- Common mistakes
- Best practices
- How we'll use it in our RAG project


## 1. st.title()

### 🧩 Problem Statement

Users should immediately understand what an application does when they open it. Without a clear title, the purpose of the application may not be obvious.

---

### 📖 Definition

`st.title()` displays the main heading of a Streamlit application.

It is typically used once at the top of the page to represent the application's title.

---

### 💻 Syntax

```python
st.title("Your Title")
```

---

### ⚙️ Parameters

**body (str)**

The text to be displayed as the page title.

Example:

```python
st.title("📄 AI PDF Assistant")
```

---

### 🧪 Example

```python
import streamlit as st

st.title("📄 AI PDF Assistant")
```

---

### 👀 Output

```
📄 AI PDF Assistant
===================
```

---

### ❌ Common Mistakes

**1. Using multiple titles**

```python
st.title("Upload PDF")
st.title("Ask Question")
st.title("Answer")
```

Instead, use one title and organize the page using `st.header()`.

---

**2. Using `print()` instead of `st.title()`**

```python
print("AI PDF Assistant")
```

`print()` displays output in the terminal, whereas `st.title()` displays it on the web page.

---

### ✅ Best Practices

- Use only one `st.title()` per page.
- Keep the title short and descriptive.
- Clearly indicate the purpose of the application.

Examples:

```python
st.title("📄 AI PDF Assistant")
st.title("📈 Stock Market Dashboard")
st.title("🌦️ Weather App")
```

---

### 🤖 Our RAG Project

We'll use `st.title()` at the top of our application to display:

```python
st.title("📄 AI PDF Assistant")
```

This gives users an immediate understanding of the application's purpose.

---

### 🎤 Interview Question

**Q. Why do we use `st.title()` instead of `print()`?**

**Answer:**

`st.title()` renders a large heading on the Streamlit web interface, whereas `print()` only displays output in the terminal. Streamlit widgets are designed to build interactive web applications.

---

### ⭐ Key Takeaway

Use `st.title()` once to define the main heading of the application. It helps establish a clear visual hierarchy and improves the user experience.


## 2. st.header()

### 🧩 Problem Statement

As an application grows, displaying all content without organization makes the interface cluttered and difficult to navigate.

`st.header()` is used to divide the application into logical sections, improving readability and user experience.

---

### 📖 Definition

`st.header()` displays a medium-sized heading in a Streamlit application.

It is used to organize the application into different sections and establish a clear visual hierarchy below the main title.

---

### 💻 Syntax

```python
st.header("Header")
```

---

### ⚙️ Parameters

**body (str)**

The text displayed as the section heading.

Example:

```python
st.header("Upload PDF")
```

---

### 🧪 Example

```python
import streamlit as st

st.title("📄 AI PDF Assistant")

st.header("Upload PDF")

st.header("Ask a Question")

st.header("Answer")
```

---

### 👀 Output

```
📄 AI PDF Assistant

Upload PDF

Ask a Question

Answer
```

The application title appears larger than the headers, creating a clear visual hierarchy.

---

### ❌ Common Mistakes

**1. Using multiple titles instead of headers**

❌ Incorrect

```python
st.title("Upload PDF")
st.title("Ask Question")
st.title("Answer")
```

✅ Correct

```python
st.title("📄 AI PDF Assistant")

st.header("Upload PDF")

st.header("Ask a Question")

st.header("Answer")
```

---

**2. Using headers for paragraphs**

❌ Incorrect

```python
st.header("This application allows users to upload PDFs and ask questions.")
```

Use `st.write()` or `st.markdown()` for descriptive text instead.

---

### ✅ Best Practices

- Use only one `st.title()` for the application.
- Use `st.header()` to organize the page into sections.
- Keep header text short and meaningful.
- Avoid writing long sentences as headers.

---

### 🤖 Our RAG Project

We'll use `st.header()` for sections such as:

```python
st.header("📂 Upload PDF")

st.header("💬 Ask a Question")

st.header("📖 Answer")

st.header("📑 Retrieved Context")
```

This makes the interface clean and easy to navigate.

---

### 🎤 Interview Question

**Q. What is the difference between `st.title()` and `st.header()`?**

**Answer:**

`st.title()` is used for the main title of the application and is generally used only once. `st.header()` is used to create section headings that organize different parts of the application.

---

### ⭐ Key Takeaway

Use `st.title()` for the application's main heading and `st.header()` to divide the application into logical, well-organized sections.


## 3. st.write()

### 🧩 Problem Statement

After creating the title and section headings, we need a way to display information such as instructions, answers, variables, messages, and other data on the webpage.

Using Python's `print()` won't work because it displays output in the terminal, not in the Streamlit web application.

To display information on the webpage, Streamlit provides `st.write()`.

---

### 📖 Definition

`st.write()` is the most versatile display function in Streamlit.

It can display various Python objects such as text, numbers, variables, lists, dictionaries, DataFrames, charts, and more.

Because of its flexibility, it is often referred to as the **Swiss Army Knife** of Streamlit.

---

### 💻 Syntax

```python
st.write(object)
```

---

### ⚙️ Parameters

**object**

The Python object you want to display.

It can be:

- String
- Integer
- Float
- List
- Dictionary
- DataFrame
- Variable
- Chart
- Image
- and many other supported objects.

---

### 🧪 Example

```python
import streamlit as st

name = "Rahul"
age = 20

st.write("Welcome!")
st.write(name)
st.write(age)
```

---

### 👀 Output

```
Welcome!

Rahul

20
```

The output is displayed on the web page instead of the terminal.

---

### ❌ Common Mistakes

**1. Using `print()` instead of `st.write()`**

❌ Incorrect

```python
print("Welcome")
```

This displays the output only in the terminal.

✅ Correct

```python
st.write("Welcome")
```

This displays the output inside the Streamlit application.

---

**2. Using `st.write()` for titles**

❌ Incorrect

```python
st.write("AI PDF Assistant")
```

Use `st.title()` instead for the main application heading.

---

### ✅ Best Practices

- Use `st.write()` for displaying general information.
- Use specialized widgets such as `st.title()`, `st.header()`, `st.success()`, and `st.error()` when appropriate.
- Take advantage of `st.write()`'s ability to display different Python objects without additional formatting.

---

### 🤖 Our RAG Project

We'll use `st.write()` to display:

```python
st.write("Ask questions about your uploaded PDF.")

st.write(answer)

st.write(retrieved_chunks)
```

---

### 🎤 Interview Question

**Q. Why is `st.write()` called the Swiss Army Knife of Streamlit?**

**Answer:**

Because it can automatically display many different types of Python objects, including text, numbers, lists, dictionaries, DataFrames, charts, and more, making it one of the most flexible widgets in Streamlit.

---

### ⭐ Key Takeaway

Use `st.write()` whenever you want to display general information or Python objects on the webpage. It is the most commonly used display widget in Streamlit.


## 4. st.markdown()

### 🧩 Problem Statement

Sometimes plain text isn't enough. We may want to make certain words **bold**, *italic*, create bullet lists, headings, links, code blocks, or even use HTML (when enabled).

While `st.write()` is excellent for displaying general information, it offers limited control over text formatting.

To display richly formatted text, Streamlit provides `st.markdown()`.

---

### 📖 Definition

`st.markdown()` is used to display text formatted using **Markdown**.

Markdown is a lightweight markup language that allows developers to easily style text without writing HTML.

It is commonly used for documentation, GitHub README files, and Streamlit applications.

---

### 💻 Syntax

```python
st.markdown(body, unsafe_allow_html=False)
```

---

### ⚙️ Parameters

#### **body (str)**

The text written in Markdown syntax.

Example:

```python
st.markdown("**Hello World**")
```

---

#### **unsafe_allow_html (bool)**

- Default: `False`
- Allows rendering HTML inside the Markdown.

Example:

```python
st.markdown("<h2>Hello</h2>", unsafe_allow_html=True)
```

⚠️ Use this only when necessary.

---

### 🧪 Example

```python
import streamlit as st

st.markdown("# Main Heading")

st.markdown("## Section Heading")

st.markdown("This is **bold** text.")

st.markdown("This is *italic* text.")

st.markdown("- Upload PDF\n- Ask Question\n- Get Answer")
```

---

### 👀 Output

# Main Heading

## Section Heading

**bold**

*italic*

• Upload PDF

• Ask Question

• Get Answer

---

### ❌ Common Mistakes

#### 1. Using `st.markdown()` for the application title

❌ Incorrect

```python
st.markdown("# AI PDF Assistant")
```

Although it works, `st.title()` is the correct widget for the application's main title.

---

#### 2. Using Markdown when plain text is enough

❌

```python
st.markdown("Hello")
```

✅ Better

```python
st.write("Hello")
```

Choose the simplest widget that satisfies your needs.

---

### ✅ Best Practices

- Use `st.markdown()` when text formatting is required.
- Prefer `st.title()` and `st.header()` for headings.
- Use Markdown for:
  - Bold text
  - Italic text
  - Bullet lists
  - Numbered lists
  - Links
  - Code blocks
- Avoid excessive HTML unless absolutely necessary.

---

### 🤖 Our RAG Project

We'll use `st.markdown()` for things like:

```python
st.markdown("### 💬 Ask your question")

st.markdown("**Instructions:** Upload a PDF before asking questions.")

st.markdown("---")
```

This helps make the interface cleaner and easier to read.

---

### 🎤 Interview Question

**Q. What is the difference between `st.write()` and `st.markdown()`?**

**Answer:**

`st.write()` is a general-purpose display function that can render many Python objects automatically.

`st.markdown()` is specifically used to display text formatted using Markdown syntax, allowing greater control over text styling.

---

### ⭐ Key Takeaway

Use `st.markdown()` whenever you need formatted text. Use `st.write()` for displaying general content and Python objects.


# 5. st.file_uploader()

### 🧩 Problem Statement

Our RAG chatbot is designed to answer questions based on a PDF document.

Currently, the PDF path is hardcoded:

```python
pdf_path = "Artificial Intelligence with Machine Learning.pdf"
```

This means that every time we want to use a different PDF, we have to manually replace the file in our code.

This is not practical for users.

Instead, users should be able to upload any PDF directly from the browser.

To achieve this, Streamlit provides `st.file_uploader()`.

---

### 📖 Definition

`st.file_uploader()` creates a file upload widget that allows users to upload files from their local computer.

It supports various file types such as PDFs, images, videos, CSV files, and more.

Once a file is uploaded, Streamlit returns an **UploadedFile** object, which behaves like a file object in Python.

---

### 💻 Syntax

```python
st.file_uploader(
    label,
    type=None,
    accept_multiple_files=False
)
```

---

### ⚙️ Parameters

#### **label (str)**

The text displayed above the upload box.

Example:

```python
label="Upload a PDF"
```

---

#### **type (str | list)**

Restricts the allowed file types.

Example:

```python
type="pdf"
```

or

```python
type=["pdf", "txt"]
```

---

#### **accept_multiple_files (bool)**

- Default: `False`
- If `True`, users can upload multiple files at once.

Example:

```python
accept_multiple_files=True
```

---

### 🧪 Example

```python
import streamlit as st

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type="pdf"
)
```

---

### 👀 Output

```
Upload a PDF

[ Browse Files ]
```

After selecting a PDF, the uploaded file is stored in the variable:

```python
uploaded_file
```

---

### ⚠️ Important

`st.file_uploader()` **does not automatically save the uploaded file** to your computer.

It only loads the file into memory and returns an `UploadedFile` object.

If you want to keep the file permanently, you must save it yourself.

This is an important concept because many beginners assume the uploaded file is automatically stored on disk.

---

### ❌ Common Mistakes

#### 1. Forgetting to check whether a file was uploaded

❌ Incorrect

```python
uploaded_file.read()
```

If no file has been uploaded, this will cause an error because `uploaded_file` is `None`.

✅ Correct

```python
if uploaded_file is not None:
    ...
```

---

#### 2. Not restricting file types

❌ Incorrect

```python
st.file_uploader("Upload File")
```

Users could upload any file type.

✅ Better

```python
st.file_uploader(
    "Upload PDF",
    type="pdf"
)
```

---

#### 3. Assuming the file is saved automatically

Remember:

```
Upload

↓

Memory

❌ Not Disk
```

You must explicitly save the file if your application needs a physical copy.

---

### ✅ Best Practices

- Restrict uploads to the required file type.
- Always check whether a file has been uploaded.
- Save the file manually if your backend expects a file path.
- Display appropriate success or error messages after upload.

---

### 🤖 Our RAG Project

This widget will replace our hardcoded PDF path.

Instead of:

```python
pdf_path = "Artificial Intelligence with Machine Learning.pdf"
```

We'll allow users to upload any PDF:

```
User uploads PDF
        │
        ▼
Save PDF
        │
        ▼
Create Chroma Collection
        │
        ▼
Index PDF
        │
        ▼
Ready for Questions
```

This makes our chatbot dynamic instead of being limited to a single document.

---

### 🎤 Interview Question

**Q. What does `st.file_uploader()` return?**

**Answer:**

`st.file_uploader()` returns an `UploadedFile` object when a file is uploaded. This object behaves like a Python file object and can be read or saved. If no file is uploaded, it returns `None`.

---

### ⭐ Key Takeaway

`st.file_uploader()` allows users to upload files through the browser. It loads the file into memory as an `UploadedFile` object and does **not** automatically save it to disk.


# 6. st.button()

### 🧩 Problem Statement

Simply displaying information isn't enough. Users need a way to trigger actions.

For example, in our RAG chatbot, we may want users to:

- Index a PDF
- Ask a question
- Clear chat history
- Reset the application

These actions should happen **only when the user requests them**, not automatically every time the page loads.

To perform actions based on user interaction, Streamlit provides `st.button()`.

---

### 📖 Definition

`st.button()` creates a clickable button in a Streamlit application.

When the button is clicked, it returns **`True`** for that rerun of the script. Otherwise, it returns **`False`**.

This allows developers to execute code only when the button is pressed.

---

### 💻 Syntax

```python
st.button(label)
```

---

### ⚙️ Parameters

#### **label (str)**

The text displayed on the button.

Example:

```python
st.button("Ask")
```

---

### 🧪 Example

```python
import streamlit as st

if st.button("Click Me"):
    st.write("Button Pressed!")
```

---

### 👀 Output

Initially:

```
[ Click Me ]
```

After clicking:

```
Button Pressed!
```

---

### ⚠️ Important

When the button is clicked:

1. Streamlit reruns the **entire script**.
2. During that rerun, `st.button()` returns `True`.
3. On subsequent reruns (without another click), it returns `False` again.

This is why button clicks are considered **one-time events**.

---

### ❌ Common Mistakes

#### 1. Forgetting that buttons return a boolean

❌ Incorrect

```python
st.button("Ask")

st.write("Answer Generated")
```

The answer is displayed even if the button is never clicked.

✅ Correct

```python
if st.button("Ask"):
    st.write("Answer Generated")
```

---

#### 2. Expecting the button to stay "pressed"

Many beginners think:

```text
Click

↓

True forever
```

This is incorrect.

A button only returns `True` during the rerun caused by that click.

---

#### 3. Putting important data only inside the button block

Since the script reruns, values created inside the button block may disappear unless stored using `st.session_state`.

---

### ✅ Best Practices

- Use buttons to trigger actions.
- Wrap the action inside an `if st.button():` block.
- Use `st.session_state` if the action updates data that must persist.

---

### 🤖 Our RAG Project

We'll use buttons for actions such as:

```python
if st.button("Index PDF"):
    ...

if st.button("Ask"):
    ...

if st.button("Clear Chat"):
    ...
```

Each button performs a specific task when clicked.

---

### 🎤 Interview Question

**Q. What does `st.button()` return?**

**Answer:**

`st.button()` returns a boolean value.

- `True` only during the rerun triggered by the button click.
- `False` otherwise.

---

### ⭐ Key Takeaway

`st.button()` is used to trigger actions in a Streamlit application. It returns `True` only when the user clicks the button, making it ideal for executing code conditionally.


# 6. st.button()

### 🧩 Problem Statement

Simply displaying information isn't enough. Users need a way to trigger actions.

For example, in our RAG chatbot, we may want users to:

- Index a PDF
- Ask a question
- Clear chat history
- Reset the application

These actions should happen **only when the user requests them**, not automatically every time the page loads.

To perform actions based on user interaction, Streamlit provides `st.button()`.

---

### 📖 Definition

`st.button()` creates a clickable button in a Streamlit application.

When the button is clicked, it returns **`True`** for that rerun of the script. Otherwise, it returns **`False`**.

This allows developers to execute code only when the button is pressed.

---

### 💻 Syntax

```python
st.button(label)
```

---

### ⚙️ Parameters

#### **label (str)**

The text displayed on the button.

Example:

```python
st.button("Ask")
```

---

### 🧪 Example

```python
import streamlit as st

if st.button("Click Me"):
    st.write("Button Pressed!")
```

---

### 👀 Output

Initially:

```
[ Click Me ]
```

After clicking:

```
Button Pressed!
```

---

### ⚠️ Important

When the button is clicked:

1. Streamlit reruns the **entire script**.
2. During that rerun, `st.button()` returns `True`.
3. On subsequent reruns (without another click), it returns `False` again.

This is why button clicks are considered **one-time events**.

---

### ❌ Common Mistakes

#### 1. Forgetting that buttons return a boolean

❌ Incorrect

```python
st.button("Ask")

st.write("Answer Generated")
```

The answer is displayed even if the button is never clicked.

✅ Correct

```python
if st.button("Ask"):
    st.write("Answer Generated")
```

---

#### 2. Expecting the button to stay "pressed"

Many beginners think:

```text
Click

↓

True forever
```

This is incorrect.

A button only returns `True` during the rerun caused by that click.

---

#### 3. Putting important data only inside the button block

Since the script reruns, values created inside the button block may disappear unless stored using `st.session_state`.

---

### ✅ Best Practices

- Use buttons to trigger actions.
- Wrap the action inside an `if st.button():` block.
- Use `st.session_state` if the action updates data that must persist.

---

### 🤖 Our RAG Project

We'll use buttons for actions such as:

```python
if st.button("Index PDF"):
    ...

if st.button("Ask"):
    ...

if st.button("Clear Chat"):
    ...
```

Each button performs a specific task when clicked.

---

### 🎤 Interview Question

**Q. What does `st.button()` return?**

**Answer:**

`st.button()` returns a boolean value.

- `True` only during the rerun triggered by the button click.
- `False` otherwise.

---

### ⭐ Key Takeaway

`st.button()` is used to trigger actions in a Streamlit application. It returns `True` only when the user clicks the button, making it ideal for executing code conditionally.


# 8. st.chat_input()

### 🧩 Problem Statement

While `st.text_input()` works for accepting user input, modern AI applications such as ChatGPT, Gemini, and Claude use a dedicated chat interface.

Instead of typing a question and clicking an **Ask** button, users simply type their message and press **Enter** to send it.

To build chat-style applications, Streamlit provides `st.chat_input()`.

---

### 📖 Definition

`st.chat_input()` creates a chat input box specifically designed for conversational applications.

It provides a modern messaging experience where users type a message and send it by pressing **Enter**.

Unlike `st.text_input()`, it is optimized for chatbot interfaces.

---

### 💻 Syntax

```python
st.chat_input(
    placeholder="Send a message..."
)
```

---

### ⚙️ Parameters

#### **placeholder (str)**

Displays hint text inside the chat box.

Example:

```python
placeholder="Ask anything about the uploaded PDF..."
```

---

### 🧪 Example

```python
import streamlit as st

prompt = st.chat_input(
    "Ask anything..."
)

if prompt:
    st.write(prompt)
```

---

### 👀 Output

```
_____________________________________

Ask anything...
```

User types:

```
What is Artificial Intelligence?
```

Presses **Enter**

↓

```python
prompt
```

contains

```python
"What is Artificial Intelligence?"
```

---

### ⚠️ Important

Like `st.text_input()`, `st.chat_input()` returns a **string**.

If no message has been submitted, it returns `None`.

Unlike `st.text_input()`, it is designed around **sending messages**, making it ideal for chatbot applications.

---

### ❌ Common Mistakes

#### 1. Using `st.chat_input()` without displaying chat history

The input box alone does not create a chatbot.

You must also display previous messages using widgets such as `st.chat_message()`.

---

#### 2. Expecting it to remember conversations

`st.chat_input()` only captures the current message.

Conversation history should be stored separately, typically using `st.session_state`.

---

#### 3. Using it for forms

`st.chat_input()` is intended for conversational interfaces.

For login forms, search bars, API keys, and similar inputs, use `st.text_input()` instead.

---

### ✅ Best Practices

- Use `st.chat_input()` for chatbots and AI assistants.
- Combine it with `st.chat_message()` to display conversations.
- Store chat history using `st.session_state`.
- Keep the placeholder short and helpful.

---

### 🤖 Our RAG Project

Eventually, our chatbot will look like this:

```
👤 What is AI?

🤖 Artificial Intelligence is...

---------------------------------

💬 Ask anything about your uploaded PDF...
```

We'll use:

```python
prompt = st.chat_input(
    "Ask anything about the uploaded PDF..."
)
```

and process the prompt through our RAG pipeline.

---

### 🎤 Interview Question

**Q. When should you use `st.chat_input()` instead of `st.text_input()`?**

**Answer:**

Use `st.chat_input()` when building chatbot or conversational applications. It provides a messaging-style input experience where users send messages by pressing **Enter**, making it more suitable for AI assistants than a regular text input field.

---

### ⭐ Key Takeaway

`st.chat_input()` is specifically designed for chatbot interfaces. It provides a modern messaging experience and works best when combined with `st.chat_message()` and `st.session_state`.


# 9. st.chat_message()

### 🧩 Problem Statement

Suppose we build a chatbot using only `st.write()`.

```python
st.write("You: What is AI?")
st.write("Bot: Artificial Intelligence is...")
```

Output:

```
You: What is AI?

Bot: Artificial Intelligence is...
```

It works...

But it doesn't look like a modern chatbot.

Users expect conversations to appear as separate chat bubbles, just like ChatGPT, Gemini, or Claude.

To create chat-style message bubbles, Streamlit provides `st.chat_message()`.

---

### 📖 Definition

`st.chat_message()` displays a single chat message in a conversational format.

It creates visually separate message containers for the user and the assistant, making chatbot interfaces cleaner and easier to read.

It is usually used together with:

- `st.chat_input()`
- `st.session_state`

to build complete chat applications.

---

### 💻 Syntax

```python
with st.chat_message(name):
    ...
```

---

### ⚙️ Parameters

#### **name (str)**

Specifies who sent the message.

Common values:

```python
"user"
```

Displays a user message.

```python
"assistant"
```

Displays an AI assistant message.

---

### 🧪 Example

```python
import streamlit as st

with st.chat_message("user"):
    st.write("What is AI?")

with st.chat_message("assistant"):
    st.write("Artificial Intelligence is the simulation of human intelligence by machines.")
```

---

### 👀 Output

```
👤 What is AI?

🤖 Artificial Intelligence is the simulation of human intelligence by machines.
```

Each message appears in its own chat container, similar to ChatGPT.

---

### ⚠️ Important

`st.chat_message()` only **displays** a message.

It does **not**:

- accept user input,
- remember previous messages,
- generate responses.

Those responsibilities belong to:

- `st.chat_input()`
- `st.session_state`
- your chatbot backend.

Think of it as the **display component** of a chat interface.

---

### ❌ Common Mistakes

#### 1. Expecting it to create a chatbot

❌ Incorrect assumption:

> "Using `st.chat_message()` automatically creates a chatbot."

It only displays messages.

You still need logic for:

- input,
- AI responses,
- memory.

---

#### 2. Not storing messages

If chat history isn't stored in `st.session_state`, previous messages disappear after every rerun.

---

#### 3. Using `st.write()` instead

While `st.write()` works, `st.chat_message()` provides a much cleaner conversational UI.

---

### ✅ Best Practices

- Use `"user"` for user messages.
- Use `"assistant"` for AI responses.
- Store conversations in `st.session_state`.
- Loop through stored messages and display each one using `st.chat_message()`.

---

### 🤖 Our RAG Project

Our final chatbot will follow this flow:

```
User types a question
        │
        ▼
st.chat_input()
        │
        ▼
Retrieve Context
        │
        ▼
Gemini Response
        │
        ▼
Save both messages in st.session_state
        │
        ▼
Display them using st.chat_message()
```

This gives us a professional ChatGPT-style interface.

---

### 🎤 Interview Question

**Q. What is the purpose of `st.chat_message()`?**

**Answer:**

`st.chat_message()` is used to display messages in a chat-style interface. It creates separate message containers for the user and the assistant but does not handle input, memory, or response generation.

---

### ⭐ Key Takeaway

`st.chat_message()` is a display widget for chatbot conversations. It should be combined with `st.chat_input()` for user input and `st.session_state` for conversation history.


# 10. st.spinner()

### 🧩 Problem Statement

Some operations in an application take time to complete.

Examples:

- Uploading a PDF
- Creating embeddings
- Indexing documents
- Querying Gemini
- Loading a machine learning model

If the application does not provide any feedback during these operations, users may assume that it has stopped working.

To indicate that a task is currently in progress, Streamlit provides `st.spinner()`.

---

### 📖 Definition

`st.spinner()` displays a loading spinner along with a message while a block of code is executing.

Once the operation is complete, the spinner automatically disappears.

It is commonly used for long-running tasks to improve user experience.

---

### 💻 Syntax

```python
with st.spinner("Loading..."):
    # Long-running task
```

---

### ⚙️ Parameters

#### **text (str)**

The message displayed alongside the loading spinner.

Example:

```python
with st.spinner("Processing PDF..."):
```

---

### 🧪 Example

```python
import streamlit as st
import time

with st.spinner("Loading..."):
    time.sleep(3)

st.write("Finished!")
```

---

### 👀 Output

```
⏳ Loading...

(3 seconds)

Finished!
```

The spinner automatically disappears after the task finishes.

---

### ❌ Common Mistakes

#### 1. Forgetting to use `with`

❌ Incorrect

```python
st.spinner("Loading...")
```

This does nothing.

✅ Correct

```python
with st.spinner("Loading..."):
    ...
```

---

#### 2. Using the spinner for very fast operations

If an operation completes almost instantly, a spinner is unnecessary.

Use it only for tasks that take noticeable time.

---

#### 3. Forgetting to display a completion message

After the spinner disappears, it's good practice to inform the user that the task completed successfully.

Example:

```python
st.success("PDF Indexed Successfully!")
```

---

### ✅ Best Practices

- Use meaningful loading messages.
- Show a spinner only for long-running tasks.
- Follow it with a success or error message.
- Avoid unnecessary loading animations for very short tasks.

---

### 🤖 Our RAG Project

We'll use `st.spinner()` during operations such as:

```python
with st.spinner("Indexing PDF..."):
    index_pdf(...)
```

```python
with st.spinner("Generating answer..."):
    answer = ask_gemini(...)
```

This lets users know that the application is still working.

---

### 🎤 Interview Question

**Q. Why should we use `st.spinner()`?**

**Answer:**

`st.spinner()` improves user experience by showing a loading indicator during long-running operations. It assures users that the application is processing their request instead of appearing frozen.

---

### ⭐ Key Takeaway

Use `st.spinner()` whenever an operation takes noticeable time to complete. It provides visual feedback and makes the application feel more responsive.


# 11. st.success()

### 🧩 Problem Statement

After completing an operation successfully, users should receive clear feedback confirming that the task was completed.

Examples:

- PDF uploaded successfully
- PDF indexed successfully
- Answer generated successfully

Instead of displaying plain text, Streamlit provides `st.success()` to show success messages in a visually distinct way.

---

### 📖 Definition

`st.success()` displays a green success message indicating that an operation has completed successfully.

---

### 💻 Syntax

```python
st.success("Success Message")
```

---

### ⚙️ Parameters

**body (str)**

The success message displayed to the user.

---

### 🧪 Example

```python
st.success("PDF Indexed Successfully!")
```

---

### ❌ Common Mistakes

- Using `st.write()` for success messages.
- Displaying success messages before the operation has actually completed.

---

### ✅ Best Practices

- Display success messages only after successful operations.
- Keep the message short and informative.

---

### 🤖 Our RAG Project

```python
st.success("PDF Indexed Successfully!")

st.success("Answer Generated!")
```

---

### 🎤 Interview Question

**Q. Why use `st.success()` instead of `st.write()`?**

**Answer:**

`st.success()` provides a visually distinct success notification, making it easier for users to recognize successful operations.

---

### ⭐ Key Takeaway

Use `st.success()` to provide clear confirmation that an operation completed successfully.


# 12. st.error()

### 🧩 Problem Statement

Applications should inform users when something goes wrong.

Examples:

- No PDF uploaded.
- Unsupported file type.
- Gemini API error.
- Failed to index the document.

To display errors clearly, Streamlit provides `st.error()`.

---

### 📖 Definition

`st.error()` displays a red error message indicating that an operation failed or invalid input was provided.

---

### 💻 Syntax

```python
st.error("Error Message")
```

---

### ⚙️ Parameters

**body (str)**

The error message displayed to the user.

---

### 🧪 Example

```python
st.error("Please upload a PDF first.")
```

---

### ❌ Common Mistakes

- Using generic messages like "Error".
- Not explaining how the user can fix the issue.

---

### ✅ Best Practices

- Write clear, actionable error messages.
- Tell the user what went wrong and what to do next.

---

### 🤖 Our RAG Project

```python
st.error("Please upload a PDF.")

st.error("Question cannot be empty.")

st.error("Failed to connect to Gemini.")
```

---

### 🎤 Interview Question

**Q. Why is `st.error()` important?**

**Answer:**

It clearly communicates problems to users and improves usability by helping them understand what went wrong.

---

### ⭐ Key Takeaway

Use `st.error()` whenever an operation fails or user input is invalid.


# 13. st.sidebar()

### 🧩 Problem Statement

Sometimes additional information or settings should be available without cluttering the main interface.

Examples:

- App information
- Settings
- Collection details
- Clear Chat button

To organize secondary content, Streamlit provides `st.sidebar()`.

---

### 📖 Definition

`st.sidebar()` creates a sidebar displayed on the left side of the application.

It is commonly used for navigation, settings, filters, and application information.

---

### 💻 Syntax

```python
st.sidebar.title("Settings")
```

---

### 🧪 Example

```python
st.sidebar.title("Settings")

st.sidebar.button("Clear Chat")
```

---

### ❌ Common Mistakes

- Placing the main application inside the sidebar.
- Overcrowding the sidebar with unnecessary content.

---

### ✅ Best Practices

- Keep only secondary information in the sidebar.
- Use it for settings, filters, and app information.

---

### 🤖 Our RAG Project

Sidebar contents may include:

- Current Collection
- Indexed PDF
- Chunk Count
- Clear Chat
- About App

---

### 🎤 Interview Question

**Q. What is the purpose of `st.sidebar()`?**

**Answer:**

`st.sidebar()` organizes secondary controls and information separately from the main application interface.

---

### ⭐ Key Takeaway

Use the sidebar for settings and supporting information, not the main workflow.


# 14. st.expander()

### 🧩 Problem Statement

Sometimes information is useful but doesn't need to be visible all the time.

Examples:

- Retrieved Context
- Metadata
- Debug Information
- Logs

Displaying everything can make the interface cluttered.

To hide optional information until needed, Streamlit provides `st.expander()`.

---

### 📖 Definition

`st.expander()` creates a collapsible container that users can expand or collapse.

---

### 💻 Syntax

```python
with st.expander("Title"):
    ...
```

---

### 🧪 Example

```python
with st.expander("Retrieved Context"):
    st.write(context)
```

---

### 👀 Output

```
▶ Retrieved Context

(click)

Artificial Intelligence is...
```

---

### ❌ Common Mistakes

- Hiding important information inside an expander.
- Using expanders for very small amounts of content.

---

### ✅ Best Practices

- Use expanders for optional or advanced information.
- Keep essential information visible.

---

### 🤖 Our RAG Project

We'll use it for:

```python
with st.expander("Retrieved Context"):
    st.write(context)
```

This keeps the interface clean while allowing users to inspect the retrieved chunks if they want.

---

### 🎤 Interview Question

**Q. Why use `st.expander()`?**

**Answer:**

`st.expander()` helps organize optional information by hiding it until the user chooses to expand it, resulting in a cleaner interface.

---

### ⭐ Key Takeaway

Use `st.expander()` to hide secondary or advanced information while keeping the main interface uncluttered.




