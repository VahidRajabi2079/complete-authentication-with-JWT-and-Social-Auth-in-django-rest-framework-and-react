import React, { useState } from "react";

const Login = () => {
  return (
    <div className="signup-form-container">
      <div className="form-wrapper">
        <h2>Login</h2>
        <form>
          <div className="form-group">
            <label htmlFor="email">Email Address:</label>
            <input type="text" className="email-form" name="email" />
          </div>

          <div className="form-group">
            <label htmlFor="password">Password:</label>
            <input type="password" className="email-form" name="password" />
          </div>
          <input type="submit" value="Login" className="submitButton" />
        </form>
        <h3 className="text-option">OR</h3>
        <div className="githubContainer">
          <button>Sign up with Github</button>
        </div>
        <div className="googleContainer">
          <button>Sign up with Google</button>
        </div>
      </div>
    </div>
  );
};

export default Login;
