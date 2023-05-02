const form = document.getElementById('add-data');
console.log(form);

// Initialize Firebase storage
const storage = firebase.storage();

form.addEventListener('submit', (e) => {
  e.preventDefault();

  const locationInput = document.getElementById('location');
  const emptySpacesInput = document.getElementById('empty-spaces');
  const imageInput = document.getElementById('image');
  const file = imageInput.files[0];

  // Upload the image to Firebase Storage
  if (file) {
    const storageRef = storage.ref('images/' + file.name);
    const uploadTask = storageRef.put(file);

    // Handle the snapshot after the image is uploaded
    uploadTask.on('state_changed', null, (error) => {
      console.error('Error uploading image: ', error);
    }, async () => {
      // Get the image URL
      const imageUrl = await storageRef.getDownloadURL();

      // Get the current timestamp
      const timestamp = firebase.firestore.FieldValue.serverTimestamp();

      // Add data to Firestore
      db.collection('parking1').add({
        location: locationInput.value,
        emptySpaces: parseInt(emptySpacesInput.value),
        imageUrl: imageUrl,
        timestamp: timestamp
      })
      .then(() => {
        console.log('Data added to Firestore');
        location.reload(); // Reload the page after successfully adding data
      })
      .catch((error) => {
        console.error('Error adding data to Firestore: ', error);
      });
    });
  } else {
    console.error('No image file selected');
  }
});
