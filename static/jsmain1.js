var slideIndex = 1;
showDivs(slideIndex);

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("mySlides");
  if (n > x.length) {slideIndex = 1}
  if (n < 1) {slideIndex = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  x[slideIndex-1].style.display = "block";  
}

function check()
{
var a=['$','!','@','#','%'];

	// Check whether the name field is blank
	if(contactusform.fname.value=="")
	{
	  window.alert("Please enter the valid first name! It can not be blank!");
	  window.event.returnValue=false;
	   return false;
	}
	if(contactusform.lname.value=="")
	{
	  window.alert("Please enter the valid last name! It can not be blank!");
	  window.event.returnValue=false;
	   return false;
	}
	
	
var i=0;
	
	// Check whether the first name and last name fields have numbers added
	for(i=0;i<contactusform.fname.value.length;i++)
	{
		if(contactusform.fname.value.charAt(i)>='0' && contactusform.fname.value.charAt(i)<='9')
		{
			 window.alert("Enter the valid first name! You have entered the numbers!");
			 window.event.returnValue=false;
			 return false;
		}
	}
	for(i=0;i<contactusform.lname.value.length;i++)
	{
		if(contactusform.lname.value.charAt(i)>='0' && contactusform.lname.value.charAt(i)<='9')
		{
			 window.alert("Enter the valid last name! You have entered the numbers!");
			 window.event.returnValue=false;
			 return false;
		}
	}
	
	
i=0;
	// Check whether the first name and last name have special characters added
	for(i=0;i<a.length;i++)
	{
		if(contactusform.fname.value.indexOf(a[i])!=-1)
		{
		   window.alert("Enter the valid first name! You have entered the special characters!");
		   window.event.returnValue=false;
			return false;
		}
	}
	for(i=0;i<a.length;i++)
	{
		if(contactusform.lname.value.indexOf(a[i])!=-1)
		{
		   window.alert("Enter the valid last name! You have entered the special characters!");
		   window.event.returnValue=false;
			return false;
		}
	}
	
	// Check whether the email field is blank
	if(contactusform.emailid.value=="")
	{
	  window.alert("Enter the valid Email-ID! It can not be blank!");
	  window.event.returnValue=false;
	   return false;
	}
	
	// Check whether the contact us field is blank
	if(contactusform.contact.value=="")
	{
	  window.alert("Enter the valid contact number! It can not be blank!");
	  window.event.returnValue=false;
	   return false;
	}
	
	// Make sure that contact number is of 10 digits
	if(contactusform.contact.value.length!=10)
	{
	  window.alert("Enter the valid contact number! It must be of 10 digits!");
	  window.event.returnValue=false;
	   return false;
	}

	// Check whether the date of birth field is blank
	if(contactusform.dob.value=="")
	{
	  window.alert("Enter the valid date of birth! It can not be blank!");
	  window.event.returnValue=false;
	   return false;
	}
	
	// Check whether the city field is blank
	if(contactusform.city.value=="")
	{
	  window.alert("Enter the valid city! It can not be blank!");
	  window.event.returnValue=false;
	   return false;
	}
	
	// Check whether the city name has special characters added
	for(i=0;i<a.length;i++)
	{
		if(contactusform.city.value.indexOf(a[i])!=-1)
		{
		   window.alert("Enter the valid city name! You have entered the special characters!");
		   window.event.returnValue=false;
			return false;
		}
	}
	
	// Check whether the state field is blank
	if(contactusform.state.value=="")
	{
	  window.alert("Enter the valid state! It can not be blank!");
	  window.event.returnValue=false;
	   return false;
	}
	
	// Check whether the state name has special characters added
	for(i=0;i<a.length;i++)
	{
		if(contactusform.state.value.indexOf(a[i])!=-1)
		{
		   window.alert("Enter the valid state name! You have entered the special characters!");
		   window.event.returnValue=false;
			return false;
		}
	}
	
	// Check whether the country field is blank
	if(contactusform.country.value=="")
	{
	  window.alert("Enter the valid country! It can not be blank!");
	  window.event.returnValue=false;
	   return false;
	}
	
	// Check whether the query field is blank
	if(contactusform.subject.value=="")
	{
	  window.alert("Enter the valid query! It can not be blank!");
	  window.event.returnValue=false;
	   return false;
	}
}