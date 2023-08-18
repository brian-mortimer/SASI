import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./components/HomePage";
import ChatPage from "./components/ChatPage";

function App() {
  return (
    <div>
      <Router>
        {/* Define your routes here */}
        <Routes>
          <Route exact path="" element={<HomePage />} />
          <Route path="/chat" element={<ChatPage />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
