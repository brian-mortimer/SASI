import React, { useEffect, useRef, useState } from "react";
import { sendQuestion } from "../scripts/chatbot_handler";
import Message from "./Message";
import NavBar from "./NavBar";

function ChatPage() {
  const messageEndRef = useRef(null);
  const [messages, setMessages] = useState([]);
  const [question, setQuestion] = useState("");

  const handleInputChange = (event) => {
    setQuestion(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    // Add the users message to the messages list.
    const newMessage = {
      content: question,
      sender: "user",
      timestamp: new Date().toLocaleTimeString(),
    };
    setMessages((prevMessages) => [...prevMessages, newMessage]);

    try {
      // Send user question to the chatbot API and wait for response.
      const response = await sendQuestion(question);
      const ans = response[0]["text"];
      setQuestion("");

      // Add the bot message to the message list.
      const botMessage = {
        content: ans,
        sender: "bot",
        timestamp: new Date().toLocaleTimeString(),
      };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.log(error); // Add the bot message to the message list.
      const errorMessage = {
        content: "Error: Request failed. SASI is unable to answer this question at the moment. Please try again later!",
        sender: "bot",
        timestamp: new Date().toLocaleTimeString(),
      };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }
  };

  useEffect(() => {
    messageEndRef.current?.scrollIntoView();
  }, [messages]);

  return (
    <div>
      <NavBar />
      <div className="max-w-[1340px] mx-auto px-4 min-h-screen bg-center bg-scroll bg-transparent-texture">
        <div className="flex flex-col">
          {messages.map((message, index) => (
            <Message key={index} message={message} />
          ))}
        </div>

        <div ref={messageEndRef} />

        <div className="sticky bottom-0 flex justify-center mt-4 pt-7 pb-10">
          <form onSubmit={handleSubmit}>
            <input
              className="rounded border text-white bg-gray-800 w-[300px] md:w-[500px] px-4 py-2"
              value={question}
              onChange={handleInputChange}
              placeholder="Ask a question..."
            />
            <button
              className="bg-[#00df9a] text-white px-4 py-2 ml-2 rounded-md"
              type="submit"
            >
              ➤
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default ChatPage;
