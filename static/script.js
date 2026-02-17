document.addEventListener("DOMContentLoaded", function () {
  const analyzeButton = document.getElementById("analyze-button");
  const textInput = document.getElementById("text-input");
  const resultDiv = document.getElementById("result");

  document.getElementById("hate-speech-form").addEventListener("submit", function (e) {
      e.preventDefault(); // Prevent default form submission

      const text = textInput.value.trim();

      // Send text to the Flask backend for prediction
      fetch("/predict", {
          method: "POST",
          body: new URLSearchParams({ text }), // Adjusted for form submission
          headers: {
              "Content-Type": "application/x-www-form-urlencoded",
          },
      })
          .then((response) => response.json())
          .then((data) => {
              const prediction = data.prediction;
              const label = prediction === 1 ? "Hate Speech" : "Not Hate Speech";

              // Update UI with the result
              resultDiv.innerHTML = <p>Prediction: ${label}</p>;
          })
          .catch((error) => {
              console.error("Error:", error);
              resultDiv.innerHTML = "<p>Failed to get a prediction.</p>";
          });
  });
});