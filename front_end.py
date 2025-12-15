<!DOCTYPE html>
<html>
<head>
  <title>FIND ODD</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont;
      background: linear-gradient(135deg, #000, #222);
      color: white;
      padding: 30px;
    }
    select, textarea, button {
      width: 100%;
      margin-top: 12px;
      padding: 12px;
      border-radius: 10px;
      border: none;
    }
    button {
      background: #00ffcc;
      font-weight: bold;
      cursor: pointer;
    }
    .box {
      margin-top: 20px;
      padding: 15px;
      background: rgba(255,255,255,0.1);
      border-radius: 12px;
      min-height: 100px;
    }
    a { color: #00ffcc; text-decoration: underline; }
    hr { border-color: rgba(255,255,255,0.2); }
    /* Loading spinner */
    .loader {
      border: 4px solid rgba(255,255,255,0.2);
      border-top: 4px solid #00ffcc;
      border-radius: 50%;
      width: 30px;
      height: 30px;
      animation: spin 1s linear infinite;
      margin: 20px auto;
    }
    @keyframes spin {
      0% { transform: rotate(0deg);}
      100% { transform: rotate(360deg);}
    }
  </style>
</head>
<body>

<h1>FIND ODD</h1>

<p><strong>Step 1:</strong> Select the area to verify:</p>
<select id="sector">
  <option value="">-- Select Sector --</option>
  <option value="health">Health</option>
  <option value="politics">Politics</option>
  <option value="finance">Finance</option>
  <option value="education">Education</option>
</select>

<p><strong>Step 2:</strong> Enter your claim:</p>
<textarea id="input" placeholder="Enter any claim..."></textarea>

<button onclick="verify()">Verify</button>

<div id="output" class="box"></div>

<script>
function verify() {
  const sector = document.getElementById("sector").value;
  const claim = document.getElementById("input").value.trim();

  if (!sector) {
    alert("Please select a sector first!");
    return;
  }

  if (!claim) {
    alert("Please enter a claim to verify!");
    return;
  }

  // Show loading indicator
  document.getElementById("output").innerHTML = '<div class="loader"></div>';

  fetch("http://127.0.0.1:5000/verify", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ input: claim, sector: sector })
  })
  .then(res => res.json())
  .then(data => {
    if (data.error) {
      document.getElementById("output").innerHTML = data.error;
      return;
    }

    if (!data.top_articles || data.top_articles.length === 0) {
      document.getElementById("output").innerHTML = "<p>No articles found for this claim.</p>";
      return;
    }

    let html = `<h3>Risk Level: ${data.risk}</h3>`;
    html += `<p>${data.explanation}</p>`;
    html += `<h4>Top Relevant Articles:</h4>`;

    data.top_articles.forEach(article => {
      html += `
        <p><strong>${article.title}</strong> (Source: ${article.source})</p>
        <p>${article.snippet}</p>
        <p><a href="${article.link}" target="_blank">🔗 View Source</a></p>
        <p>Relevance Score: ${article.score}</p><hr>
      `;
    });

    document.getElementById("output").innerHTML = html;
  })
  .catch(err => {
    console.error(err);
    document.getElementById("output").innerHTML = "<p>Error fetching results.</p>";
  });
}
</script>

</body>
</html>
