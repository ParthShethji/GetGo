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

function makePhoneCall() {
    var accountSid = '';
    var authToken = '';
    var client = require('twilio')(accountSid, authToken);
  
    client.calls.create({
      url: 'http://demo.twilio.com/docs/voice.xml',
      to: '+919422755571',
      from: '+16073176923'
    }, function call(err, call) {
      if (err) {
        console.log(err);
      } else {
        console.log(call.sid);
      }
    });
}

app.post('/phone-call', (req, res) => {
makePhoneCall();
console.log('Phone call initiated!');
});

app.listen(9400, () => {
    console.log("hello world")
})
