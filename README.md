# EmailCheckerAPI
A Simple and Fast [API](https://nobounce.herokuapp.com/) To Check Bounce, Temp and Non Valid eMails 
## USAGE

| Usage  | Request |
|--|--|
Gather All data about The email | `/alldata/email@domain.com` 
Check If The eMail Delivrable | `/isdelivrable/email@domain.com` 
Check If The eMail Is A TempMail |`/istemp/email@domain.com`  

## Responses

> Get All Data About An eMail 

![alldata about email](https://i.ibb.co/1L166Mh/1alldata.png)

> The Script Checks if The email Format is Correct To Avoid Errors 

![Get All data of a valid email](https://i.ibb.co/s2rkRbg/1alldatawrong.png)

> Check If The eMail is not a Bounce

![return error if the email format is incorrect](https://i.ibb.co/kmZtFZG/2isdelivrable.png)

> Check if the eMail is not a Temp mail From our 33K List of TempEmail Providers 

![Check if the email is a tempmail](https://i.ibb.co/Jt0rr38/istemptrue.png)


made by ❤ / [Joe](https://github.com/joevenner) 
