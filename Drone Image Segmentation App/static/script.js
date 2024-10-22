// Trigger file input when 'Load Image' button is clicked
document.getElementById('customLoadImageBtn').addEventListener('click', function() {
    document.getElementById('imageLoader').click(); // Trigger the file input click
});

// Handle image loading and display the loaded image
document.getElementById('imageLoader').addEventListener('change', function() {
    const file = this.files[0];
    const formData = new FormData();
    formData.append('file', file);

    // Upload the image to the server
    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Display the uploaded image
        document.getElementById('originalImage').src = data.original_image;

        // Enable the 'Predict' and 'Clear' buttons
        document.getElementById('predictBtn').disabled = false;
        document.getElementById('clearBtn').disabled = false;

        // Disable 'Save' button until a prediction is made
        document.getElementById('saveBtn').disabled = true;
    });
});

// Handle image prediction
document.getElementById('predictBtn').addEventListener('click', function() {
    const originalImageSrc = document.getElementById('originalImage').src;

    // Send the original image to the server for prediction
    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image_path: originalImageSrc })
    })
    .then(response => response.json())
    .then(data => {
        // Display the predicted image
        document.getElementById('predictedImage').src = data.prediction_image;

        // Enable 'Save' button to allow saving the predicted image
        document.getElementById('saveBtn').disabled = false;
    });
});

// Handle saving the predicted image
document.getElementById('saveBtn').addEventListener('click', function() {
    const predictedImageSrc = document.getElementById('predictedImage').src;

    // Save the predicted image on the server
    fetch('/save', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prediction_image: predictedImageSrc })
    })
    .then(response => response.json())
    .then(data => alert(data.message));
});

// Handle clearing the images
document.getElementById('clearBtn').addEventListener('click', function() {
    fetch('/clear', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        // Clear the displayed images and disable buttons
        document.getElementById('originalImage').src = '';
        document.getElementById('predictedImage').src = '';
        document.getElementById('predictBtn').disabled = true;
        document.getElementById('saveBtn').disabled = true;
        document.getElementById('clearBtn').disabled = true;
    });
});
