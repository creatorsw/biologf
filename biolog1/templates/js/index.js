function sendEmail() {
	Email.send({
	Host: "smtp.gmail.com",
	Username : "chalukya.reddy.9@gmail.com",
	Password : "prasadvckjr",
	To : 'chalukya.reddy.7@gmail.com',
	From : "<sender’s email address>",
	Subject : "<email subject>",
	Body : "<email body>",
	}).then(
		message => alert("mail sent successfully")
	);
}
