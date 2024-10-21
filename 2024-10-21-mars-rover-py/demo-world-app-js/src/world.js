const mars = document.getElementById("world");
const rover = document.createElement("div");
rover.appendChild(document.createTextNode("🤖"));
mars.appendChild(rover)
fetch(
  "http://127.0.0.1:5000/",
  {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      x:0, y:0, direction: "N",
      commands: ["f", "f", "f", "f","r", "r"]
    }),
  })
    .then(response => response.json())
    .then(json => console.log(json))

