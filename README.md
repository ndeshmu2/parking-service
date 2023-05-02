This entire project is build on FIREBASE platform since we wanted to deploy this project completely serverless.

Firebase is a mobile and web application development platform that provides developers with a suite of tools and services to help them build high-quality apps. 
It was originally developed by Firebase Inc. and later acquired by Google in 2014.
Firebase offers a wide range of features such as real-time database, authentication, cloud messaging, hosting, storage, and more.
With Firebase, developers can quickly and easily set up back-end services for their applications without having to worry about server management, infrastructure, or scalability.

We used Firebase Firestore database to make an entry of the data entered.

We used Firebase Storage to store images of the parking spaces entered.

To send email to receipients we have used SendGrid. 


Below is the URL for this project which will take you to our website
https://my-project-2-379220.web.app


In order to run this project we followed below set of steps -:

Set-up a FIREBASE account -:
https://firebase.google.com/.

Create a project -:
https://firebase.google.com/docs/projects/learn-more

Create a web-app in your project -:
https://firebase.google.com/docs/web/setup

To host website and link it to firebase, execute below commands in directory where your front-end and back-end code is present -:

npm install firebase

npm install -g firebase-tools

firebase login

firebase init

firebase deploy

https://firebase.google.com/docs/hosting

Our notifying via email system is working with the help of google functions and SendGrid.

https://firebase.google.com/docs/functions/get-started


