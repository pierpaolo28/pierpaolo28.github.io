<?php
/*
This first bit sets the email address that you want the form to be submitted to.
You will need to change this value to a valid email address that you can access.
*/
$webmaster_email = "pier.py@hotmail.it";

/*
This bit sets the URLs of the supporting pages.
If you change the names of any of the pages, you will need to change the values here.
*/
$contacts = "contacts.html";
$error_page = "error_message.html";
$thankyou_page = "thank_you.html";

/*
This next bit loads the form field data into variables.
If you add a form field, you will need to add it here.
*/
$first_name = $_REQUEST['firstname'] ;
$last_name = $_REQUEST['lastname'] ;
$email_address = $_REQUEST['email'] ;
$subject = $_REQUEST['subject'] ;
$message = $_REQUEST['message'] ;
$msg =
"First Name: " . $first_name . "\r\n" .
"Last Name: " . $last_name . "\r\n" .
"Email: " . $email_address . "\r\n" .
"Subject: " . $subject . "\r\n" .
"Message: " . $message ;

/*
The following function checks for email injection.
Specifically, it checks for carriage returns - typically used by spammers to inject a CC list.
*/
function isInjected($str) {
	$injections = array('(\n+)',
	'(\r+)',
	'(\t+)',
	'(%0A+)',
	'(%0D+)',
	'(%08+)',
	'(%09+)'
	);
	$inject = join('|', $injections);
	$inject = "/$inject/i";
	if(preg_match($inject,$str)) {
		return true;
	}
	else {
		return false;
	}
}

// If the user tries to access this script directly, redirect them to the feedback form,
if (!isset($_REQUEST['email'])) {
header( "Location: $contacts" );
}

// If the form fields are empty, redirect to the error page.
elseif (empty($first_name) || empty($email_address) || empty($last_name)
 || empty($subject) || empty($message)) {
header( "Location: $error_page" );
}

/*
If email injection is detected, redirect to the error page.
If you add a form field, you should add it here.
*/
elseif ( isInjected($email_address) || isInjected($first_name)  || isInjected($message)
|| isInjected($last_name) || isInjected($subject)) {
header( "Location: $error_page" );
}

// If we passed all previous tests, send the email then redirect to the thank you page.
else {

	mail( "$webmaster_email", "Feedback Form Results", $msg );

	header( "Location: $thankyou_page" );
}
?>
