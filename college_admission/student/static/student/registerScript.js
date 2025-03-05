const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

document.addEventListener('DOMContentLoaded', function() {
  const registerForm = document.getElementById('register-form');
  const loginForm = document.querySelector('#login-form');

  // Handle registration
  registerForm.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission

      
      data = {
          register_username: document.getElementById('register_username').value,
          register_email: document.getElementById('register_email').value,
          register_password: document.getElementById('register_password').value,
          
      }

      

      fetch('http://127.0.0.1:8000/api/register', {
          method: 'POST',
          body: JSON.stringify(data),
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              alert('Registration successful! You can now log in.');
              window.location.replace('/register');
              // Optionally redirect to login page or clear the form
          } else {
              alert('Registration failed: ' + data.message);
          }
      })
      .catch(error => {
          console.error('Error:', error);
      });

      
  });

  // Handle login
  loginForm.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent default form submission

      const formData = new FormData(loginForm);
      data = {
          login_username: document.getElementById('login_username').value,
          
          login_password: document.getElementById('login_password').value,
          
      }

      fetch('http://127.0.0.1:8000/api/login', {
          method: 'POST',
          body: JSON.stringify(data),
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              alert('Login successful!');
              window.location.replace('/dashboard');
              // Optionally redirect to another page
          } else {
              alert('Login failed: ' + data.message);
          }
      })
      .catch(error => {
          console.error('Error:', error);
      });
  });
});