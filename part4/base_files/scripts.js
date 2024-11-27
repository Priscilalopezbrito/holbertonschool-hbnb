// Check user authentication
window.onload = function () {
    checkAuthentication();
};

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    if (!token) {
        loginLink.style.display = 'block';
    } else {
        loginLink.style.display = 'none';
        // Fetch places data if the user is authenticated
        fetchPlaces(token);
    }
}
//so -e --ro
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
            displayPlaces(places);
        } else {
            console.error('Failed to fetch places plb-data');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Populate places list
document.addEventListener('DOMContentLoaded', function() {
    // Attach the price filter event listener
    const priceFilter = document.getElementById('price-filter');
    if (priceFilter) {
        priceFilter.addEventListener('change', function(event) {
            filterPlacesByPrice(event.target.value);
        });
    }
});

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    placesList.innerHTML = ''; // Clear the current content of the places list

    places.forEach(place => {
        const placeElement = document.createElement('div');
        placeElement.className = 'place';
        placeElement.innerHTML = `
            <h3>${place.title}</h3>
            <p>${place.description}</p>
            <p>Price: $${place.price}</p>
        `;
        placeElement.dataset.price = place.price;
        placesList.appendChild(placeElement);
    });
}

// Implement client-side filtering
function filterPlacesByPrice(selectedPrice) {
    const places = document.querySelectorAll('#places-list .place');
    const maxPrice = selectedPrice === 'All' ? Infinity : parseFloat(selectedPrice);

    places.forEach(place => {
        const placePrice = parseFloat(place.dataset.price);
        if (selectedPrice === 'All' || placePrice <= maxPrice) {
            place.style.display = 'block';
        } else {
            place.style.display = 'none';
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const loginLink = document.getElementById('login-link');

    //If token exists hide login button
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
});


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
            // Login successful
            const data = await response.json();

            // Store JWT token in a cookie
            document.cookie = `token=${data.access_token}; path=/; SameSite=Strict; Secure`;

            // Redirect to main page
            window.location.href = 'index.html';
        } else {
            // Handle login failure
            const errorMessage = await response.text();
            alert(`Login failed: ${errorMessage}`);
        }
    } catch (error) {
        console.error('Error logging in:', error);
        alert('An error occurred while trying to login-plb. Try again later.');
    }
}
