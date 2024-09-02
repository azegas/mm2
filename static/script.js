// Function to fetch and update stock data from the server
function fetchStockData() {
    fetch('/read_stock_data_from_file') // Send a request to the server
        .then(response => response.json()) // Parse response as JSON
        .then(data => {
            // Update the HTML elements with the fetched data
            Object.entries(data).forEach(([symbol, details]) => {
                const stockDiv = document.getElementById(symbol);
                if (stockDiv) {
                    stockDiv.innerHTML = `
                        <div class="stock-info">
                            <span class="symbol">${symbol}</span>
                            <span class="price">${details.price}</span>
                            <span class="change">${details.change}</span>
                            <span class="change-percent">${details.change_percent}</span>
                            <img src="/static/images/${symbol}_high_prices.png" alt="${symbol} High Prices Chart" class="stock-chart">
                        </div>
                    `;
                }
            });
        })
        .catch(error => console.error('Error fetching stock data:', error)); // Error handling
}

// Initial data load when the page first loads
fetchStockData();

// Set an interval to automatically fetch and update the stock data every 10 seconds
// setInterval(fetchStockData, 10000); // 10,000 ms = 10 seconds
// setInterval(fetchStockData, 1800000); // 1,800,000 ms = 30 minutes
// setInterval(fetchStockData, 3600000); // 3,600,000 ms = 1 hour
// setInterval(fetchStockData, 18000000); // 18,000,000 ms = 5 hours
setInterval(fetchStockData, 43200000); // 43,200,000 ms = 12 hours
// setInterval(fetchStockData, 86400000); // 86,400,000 ms = 24 hours
