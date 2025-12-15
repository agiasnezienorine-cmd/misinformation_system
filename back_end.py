<!DOCTYPE html>
<html>
<head>
    <title>Misinformation Risk Scoring System</title>
</head>
<body>
    <h2>Misinformation Risk Scoring System</h2>
    <form method="post">
        <textarea name="user_input" rows="5" cols="60" placeholder="Enter text or URL"></textarea><br>
        <button type="submit">Check</button>
    </form>

    {% if result %}
        {% if result.error %}
            <p style="color:red;">{{ result.error }}</p>
        {% else %}
            <h3>Risk Score: {{ result.score }}%</h3>
            <h4>Risk Level: {{ result.level }}</h4>
            <h4>Relevant Verified Sources:</h4>
            <ul>
            {% for source in result.sources %}
                <li><a href="{{ source.url }}" target="_blank">{{ source.title }} ({{ source.source }})</a></li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endif %}
</body>
</html>
