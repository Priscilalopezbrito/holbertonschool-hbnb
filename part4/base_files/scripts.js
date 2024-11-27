// Check user authentication when the page loads
window.onload = function () {
    checkAuthentication();
};

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
    const addReviewSection = document.getElementById('add-review');

    if (!token) {
        if (loginLink) loginLink.style.display = 'block';
        if (addReviewSection) addReviewSection.style.display = 'none';
    } else {
        if (loginLink) loginLink.style.display = 'none';
        if (addReviewSection) addReviewSection.style.display = 'block';

        const place_id = getPlaceIdFromURL();
        if (place_id) {
            console.log(`Fetching details for place_id: ${place_id}`);
            fetchPlaceDetails(token, place_id);
        } else {
            fetchPlaces(token);
        }
    }
}

// Extract place ID from URL
function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('place_id');
}

// oR --eOS
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

// Fetch places data
async function fetchPlaces(token) {
    try {
        const response = await fetch('http://192.168.0.7:5050/api/v1/places/', {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            const places = await response.json();
            console.log('Places fetched successfully:', places);
            displayPlaces(places);
        } else {
            console.error('Failed to fetch places data-plb:', response.statusText);
        }
    } catch (error) {
        console.error('Error fetching places-plb:', error);
    }
}

// Fetch place details by ID-plb
async function fetchPlaceDetails(token, place_id) {
    try {
        console.log(`Attempting to fetch details for place_id-plb: ${place_id}`);
        const response = await fetch(`http://192.168.0.7:5050/api/v1/places/${place_id}`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            const place = await response.json();
            console.log('Place details fetched successfully:', place);

            const user = await fetchUserById(token, place.owner);
            displayPlaceDetails(place, user);
        } else {
            console.error('Failed to fetch place details:', response.statusText);
        }
    } catch (error) {
        console.error('Error fetching place details:', error);
    }
}

// Display place details
function displayPlaceDetails(place, user) {
    const placeDetailsSection = document.getElementById('place-details');
    if (!placeDetailsSection) {
        console.error('Missing element with ID "place-details"');
        return;
    }

    // Log the place object to verify the data
    console.log('Displaying place details-plb:', place);

    // Populate the place details
    placeDetailsSection.innerHTML = `
        <h2>${place.title}</h2>
        <p><strong>Host:</strong> ${user ? `${user.first_name} ${user.last_name}` : 'Unknown'}</p>
        <p><strong>Price per night:</strong> $${place.price}</p>
        <p><strong>Description:</strong> ${place.description}</p>
        <p><strong>Amenities:</strong> ${place.amenities && Array.isArray(place.amenities) ? place.amenities.join(', ') : 'No amenities listed'}</p>
    `;
}

// Populate places list
function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    if (!placesList) {
        console.error('Missing element with ID-plb "places-list"');
        return;
    }

    placesList.innerHTML = ''; // Clear the current content

    if (places.length === 0) {
        placesList.innerHTML = '<p>No places found.</p>';
        return;
    }

    places.forEach(place => {
        const placeElement = document.createElement('div');
        placeElement.className = 'place-card';
        placeElement.dataset.id = place.id;
        placeElement.dataset.price = place.price;

        placeElement.innerHTML = `  
            <h3>${place.title}</h3>
            <p>${place.description}</p>
            <p>Price: $${place.price}</p>
            <button class="view-details-button">View Details</button>
        `;
        placeElement.dataset.price = place.price;
        placesList.appendChild(placeElement);
    });

    attachDetailButtonListeners();
}

function attachDetailButtonListeners() {
    const detailButtons = document.querySelectorAll('.view-details-button');
    console.log(`Attaching listeners to ${detailButtons.length} buttons.`);

    detailButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            const place_id = event.target.closest('.place-card').dataset.id;
            console.log(`View Details clicked for place_id: ${place_id}`);
            if (place_id) {
                window.location.href = `place.html?place_id=${place_id}`;
            }
        });
    });
}

// Filter: price range selection
function filterPlacesByPrice(selectedPrice) {
    const placeCards = document.querySelectorAll('.place-card');

    // Convert selectedPrice to an int
    const maxPrice = selectedPrice === 'all' ? Infinity : parseInt(selectedPrice);

    placeCards.forEach(card => {
        const price = parseInt(card.dataset.price);

        if (!isNaN(price)) {
            // Update display based on selected price
            if (maxPrice === Infinity || price <= maxPrice) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const priceFilter = document.getElementById('price-filter');
    if (priceFilter) {
        priceFilter.addEventListener('change', function (event) {
            filterPlacesByPrice(event.target.value);
        });
    }

    const loginForm = document.getElementById('login-form');
    const loginLink = document.getElementById('login-link');

    // If token exists, hide login button
    const token = getCookie('token');
    if (token && loginLink) {
        loginLink.style.display = 'none';
    }

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();

            const email = loginForm.querySelector('input[name="email"]').value;
            const password = loginForm.querySelector('input[name="password"]').value;

            // Call login function
            await loginUser(email, password);
        });
    }

    const place_id = getPlaceIdFromURL();
    if (place_id && token) {
        fetchPlaceDetails(token, place_id);
    } else if (token) {
        fetchPlaces(token);
    } else {
        console.error('No token available');
    }
});

// Login user
async function loginUser(email, password) {
    try {
        const response = await fetch('http://192.168.0.7:5050/api/v1/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });

        if (response.ok) {
            const data = await response.json();

            // Store JWT token in a cookie
            document.cookie = `token=${data.access_token}; path=/; SameSite=Strict; Secure`;

            // Redirect to main page
            window.location.href = 'index.html';
        } else {
            const errorMessage = await response.text();
            alert(`Login failed: ${errorMessage}`);
        }
    } catch (error) {
        console.error('Error logging in PLB:', error);
        alert('An error occurred while trying to login. Try again PLB.');
    }
}



async function fetchUserById(token, userId) {
    try {
        const response = await fetch(`http://192.168.0.7:5050/api/v1/users/${userId}`, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (response.ok) {
            const user = await response.json();
            console.log('User details fetched successfully:', user);
            return user; // Ensure the user data is returned
        } else {
            console.error('Failed to fetch user details:', response.statusText);
            return null; // Return null if the fetch fails
        }
    } catch (error) {
        console.error('Error fetching user details:', error);
        return null; // Return null if an error occurs
    }
}