const path = require("path")
const express = require("express")
const app = express();

const publicPath = path.resolve(__dirname, "./public");
app.use(express.static(publicPath));

app.set('view engine', 'hbs')
const templatesPath = path.join(__dirname, "./templates/views")
app.set('views', templatesPath)


app.get("", (req, res) => {
    res.render('index', { name: "Parth" })
})

app.get('/myform', function (req, res) {
    var myText = req.query.mytext;

    var spawn = require("child_process").spawn;

    var process = spawn('python', ["./dijkstra.py", myText]);

    process.stdout.on('data', function (data) {
        res.render('index', {
            post: {
                location: myText,
                Data: data
            }
        })
    });

});

app.listen(9000, () => {
    console.log("hello world")
})