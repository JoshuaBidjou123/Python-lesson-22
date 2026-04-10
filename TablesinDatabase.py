var mysql = require("mysql")
var connection = mysql.createConnection({
    host: "remotemySql.com", // Give your host name
    user:"Rz8hqn1dK4", Give your username
    password:"nd0wKO3xeO", // Give your password
    database:"Rz8hqn1dK4" // Give your DB name
});
connection.connect((err)) => {
    if(err) throw err;
    console.log("connected");
    // Give the name of the table which is existing.
    var sql = "DROP TABLE Student";
    connection.query(sql, function (err, result) {
        if(err) throw err;
        console.log("Table Dropped DB");
    });
};

var mysql = require("mysql")
var connection = mysql.createConnection({
    host:"remotemysql.com", // Give your host name
    user:"Rz8hqn1dK4", // Give your username
    password:"nd0wKO3xeO", // Give your password
    database:"Rz8hqn1dK4", // Give your DB name
});
connection.connect((err)) => {
    if(err) throw err;
    console.log("connection");
    // Give any table which is already existing
    var sql = "ALTER TABLE Students ADD Students_Grade INT";
    connection.query(sql,fuction (err, result){
        if(err) throw err;
        console.log("Table Altered DB");
    });

    var mysql = require("mysql")
    var connection = mysql.createConnection({
        host: "remotemySQL.com", // Give your host name 
        user: "Rz8hqn1dK4", Give your username
        password:"nd0wKO3xeO", // Give your password
        database:"Rz8hqn1dK4", // Give your DB name
});
connection.connect((err)) => {
    if(err) throw err;
    console.log("connected");
    // Insert records into table which is  already created in your database
    var sql = "INSERT TABLE Students(Student_ID, Student_FirstName, Student_LastName, Student_City, Student_Grade)VALUES(1, 'Riya', 'Kumar', 'Bangalore', '5' )";
     connection.query(sql,fuction (err, result){
        if(err) throw err;
        console.log("Data inserted in DB");
        });
        });