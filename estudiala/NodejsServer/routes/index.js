var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res) {
  res.render('index');
});

router.get('/sala1', function(req, res) {
  res.render('sala1');
});

router.get('/sala2', function(req, res) {
  res.render('sala2');
});

module.exports = router;
