import React from "react";
import axios from "axios";

const VerifyEmail = () => {
  const [otp, setOtp] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (otp) {
      const response = await axios.post(
        "http://localhost:8000/api/v1/auth/verify-email",
        { otp: otp }
      );
    }
  };

  return (
    <div className="form-wrapper">
      <div className="signup-form-container">
        <h2>Verify Your Email</h2>
        <form>
          <div className="form-group">
            <label htmlFor="otp">Enter your OTP code:</label>
            <input
              type="text"
              className="email-form"
              name="otp"
              value={otp}
              onChange={(e) => setOtp(e.target.value)}
            />
          </div>
          <input type="submit" value="Send" className="submitButton" />
        </form>
      </div>
    </div>
  );
};

export default VerifyEmail;
