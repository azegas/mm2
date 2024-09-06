export function fetchStockData() {
    return fetch('/read_stock_data_from_file')
        .then(response => response.json())
        .catch(error => {
            console.error('Error fetching stock data:', error);
            throw error; // Re-throw the error for handling in the calling function
        });
}
