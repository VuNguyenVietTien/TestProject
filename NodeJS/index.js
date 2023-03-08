const express = require("express");

var app = express();
app.use(express.static("./public"));
app.set("view engine", "ejs");
app.set("views", "./views");

var server = require("http").Server(app);
var io = require("socket.io")(server);
server.listen(8080);

io.on("connection", function(socket){
    console.log("co nguoi ket noi")
})


app.get("/", function(req, res){
    res.render("home");
})

app.get("/chat", function(req, res){
    res.render("chat");
})