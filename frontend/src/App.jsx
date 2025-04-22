import { useState } from "react";
import { ToastContainer, Bounce } from "react-toastify";  // اضافه کردن Bounce
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import {
  Signup,
  Login,
  Profile,
  VerifyEmail,
  ForgetPassword,
} from "./components";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <Router>
        <ToastContainer
          position="top-right"
          autoClose={5000}
          hideProgressBar={false}
          newestOnTop={false}
          closeOnClick={false}
          rtl={false}
          pauseOnFocusLoss
          draggable
          pauseOnHover
          theme="light"
          transition={Bounce}  
        />
        <Routes>
          <Route path="/" element={<Signup />} />
          <Route path="/Login" element={<Login />} />
          <Route path="/dashboard" element={<Profile />} />
          <Route path="/otp/verify" element={<VerifyEmail />} />
          <Route path="/forget_password" element={<ForgetPassword />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
