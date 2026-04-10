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