// Function to fetch stock data from the server
function fetchStockData() {
    // Send a request to the Flask server to get the stock data
    fetch('/read_stock_data_from_file')
        .then(response => response.json())  // Parse the response as JSON
        .then(data => {
            // Get the HTML element where the stock data will be displayed
            const stockDataDiv = document.getElementById('stock-data');
            let html = '';  // Initialize an empty string to build the HTML content
            
            // Loop through each stock symbol and its details in the received data
            for (const [symbol, details] of Object.entries(data)) {
                // Determine the background color based on the price change
                let cardClass = 'card'; // Default class for card
                if (details.change.includes('-')) {
                    cardClass += ' red-background'; // Class for negative change
                } else if (details.change.includes('+')) {
                    cardClass += ' green-background'; // Class for positive change
                }
                
                // Build the HTML for each stock item and append it to the 'html' string
                html += `
                    <div class="${cardClass}">
                        <h2>${symbol}</h2>
                        <p>Price: ${details.price}</p>
                        <p>Change: ${details.change}</p>
                        <p>Change Percent: ${details.change_percent}</p>
                        <p>Volume: ${details.volume}</p>
                        <p>One year estimate: ${details.one_year_estimate}</p>
                    </div>
                `;
            }

            // Update the stock data div with the newly generated HTML content
            stockDataDiv.innerHTML = html;

            // Optionally, update the 'last-updated' element with the current time
            document.getElementById('last-updated').textContent = 'Last updated: ' + new Date().toLocaleString();
        })
        // Catch and log any errors that occur during the fetch or processing of data
        .catch(error => console.error('Error fetching stock data:', error));
}

// Initial data load when the page first loads
fetchStockData();

// Set an interval to automatically fetch and update the stock data every 10 seconds
setInterval(fetchStockData, 10000); // 10,000 ms = 10 seconds
