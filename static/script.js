// Function to create and update the banner
function updateBanner() {
    const bannerElement = document.getElementById('update-banner');
    if (!bannerElement) {
        const banner = document.createElement('div');
        banner.id = 'update-banner';
        banner.style.position = 'fixed';
        banner.style.top = '0';
        banner.style.left = '0';
        banner.style.width = '100%';
        // banner.style.backgroundColor = '#f0f0f0';
        banner.style.padding = '10px';
        banner.style.textAlign = 'center';
        banner.style.zIndex = '1000';
        document.body.insertBefore(banner, document.body.firstChild);
    }
    
    let secondsUntilUpdate = 10;
    const updateBannerText = () => {
        document.getElementById('update-banner').textContent = `Updating in ${secondsUntilUpdate} seconds`;
        secondsUntilUpdate--;
        if (secondsUntilUpdate < 0) {
            secondsUntilUpdate = 10;
        }
    };
    updateBannerText();
    setInterval(updateBannerText, 1000);
}

// Function to fetch and update stock data from the server
function fetchStockData() {
    // Fetch stock data from the stock_data.json file
    fetch('/read_stock_data_from_file') // Send a request to the server
    .then(response => {
        console.log(response);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
            return response.json();
        }) // Parse response as JSON
        .then(data => {
            updateStockData(data);
            updateTextColors();
            // Clear any previous error messages
            document.getElementById('error-message').textContent = '';
        })
        .catch(error => {
            console.error('Error fetching stock data:', error);
            document.getElementById('error-message').textContent = 'Failed to fetch stock data. Please try again later.';
        });
}

function updateStockData(data) {
    Object.entries(data).forEach(([symbol, details]) => {
        const stockDiv = document.getElementById(symbol);
        if (stockDiv) {
            stockDiv.innerHTML = `
                <div class="stock-info">
                    <span class="symbol">${symbol}</span>
                    <hr>
                    <span class="data">
                        <span class="price-container">
                            <span class="price">$${details.price}</span>
                            <span class="change">${details.change}</span>
                            <span class="change-percent">${details.change_percent}</span>
                        </span>
                        <span class="timestamp">As of ${details.timestamp}</span>
                    </span>
                    <img src="/static/images/${symbol}_high_prices_with_volume.png" alt="${symbol} High Prices Chart" class="stock-chart">
                </div>
            `;
        }
    });
}

// Function to update text colors based on the content of change and change-percent elements
function updateTextColors() {
    // Select all elements with the class 'change' or 'change-percent'
    const elements = document.querySelectorAll('.change, .change-percent');

    elements.forEach(function(element) {
        // Get the text content of the element
        const text = element.textContent.trim();

        // Check if the text contains a minus sign (-)
        if (text.includes('-')) {
            element.classList.add("red-text");  // Assign red text color
        } else if (text.includes('+')) {
            element.classList.add("green-text");  // Assign green text color
        }
    });
}

// Initial data load when the page first loads
fetchStockData();
updateBanner();

// 10000 milliseconds is equal to 10 seconds
// This means fetchStockData() will be called every 10 seconds
setInterval(fetchStockData, 10000);