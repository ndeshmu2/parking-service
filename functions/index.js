const functions = require("firebase-functions");
const admin = require("firebase-admin");
const sgMail = require("@sendgrid/mail");
admin.initializeApp();

sgMail.setApiKey(
    "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"
);

exports.sendEmailNotification = functions.firestore
    .document("parking1/{parkingId}")
    .onCreate(async (snapshot) => { // Removed 'context' from the parameter list
        const data = snapshot.data();

        const msg = {
            to: [
                "mkhan154@binghamton.edu",
                "kkherga1@binghamton.edu",
                "hrautel1@binghamton.edu",
                "ninaddeshmukh998@gmail.com",
            ],
            from: "ndeshmu2@binghamton.edu",
            subject: "New Parking Data",
            html: `
        <h3>New Parking Data</h3>
        <p><strong>Location:</strong> ${data.location}</p>
        <p><strong>Empty Spaces:</strong> ${data.emptySpaces}</p>
        <p><strong>Image URL:</strong> ${data.imageUrl}</p>
      `,
        };

        try {
            await sgMail.send(msg);
            console.log("Email sent");
        } catch (error) {
            console.error("Error sending email:", error);
        }
    });
