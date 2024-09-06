export function fetchStockData() {
    return fetch('/read_stock_data_from_file')
        .then(response => response.json())
        .catch(error => {
            console.error('Error fetching stock data:', error);
            throw error; // Re-throw the error for handling in the calling function
        });
}

export function fetchSensorData() {
    return fetch('/read_sensor_data_from_file')
        .then(response => response.json())
        .catch(error => {
            console.error('Error fetching sensor data:', error);
            throw error; // Re-throw the error for handling in the calling function
        });
}