fetch('http://192.168.175.22:8000/festival/festivities/')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log('Data:', data);
    // Process the retrieved data
  })
  .catch(error => {
    console.error('Error:', error);
    // Handle errors
  });
