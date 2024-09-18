/**
 * Main JavaScript file for handling real-time updates and DOM manipulation
 * 
 * This script sets up WebSocket connections, handles incoming data,
 * and schedules periodic updates for various components of the application.
 */

import { updateStockData, updateTextColors, updateSensorData, updateCvbankasData, updateCurrentTime, updateSystemInfo, updateRandomQuote, updateRescueTimeData, loadWeatherWidgets, refreshWeatherWidgets } from './domUpdates.js';


// Schedule periodic update requests
// These setInterval functions send requests to the server at regular intervals
// to get updated data for different parts of the application
setInterval(() => {
    socket.emit('request_from_client_to_server_for_cvbankas_data');
}, 10000); // 10sec

setInterval(() => {
    socket.emit('request_from_client_to_server_for_sensor_data');
}, 1000); //1 sec

setInterval(() => {
    socket.emit('request_from_client_to_server_for_stock_data');
}, 10000); //10 sec

setInterval(() => {
    socket.emit('request_from_client_to_server_for_system_info_data');
}, 10000); //10 sec

setInterval(() => {
    socket.emit('request_from_client_to_server_for_random_quote_data');
}, 600000); // 10min

setInterval(() => {
    socket.emit('request_from_client_to_server_for_rescuetime_data');
}, 10000); //10 sec

setInterval(updateCurrentTime, 1000);

setInterval(refreshWeatherWidgets, 600000); // Refresh every 10 minutes (600000 milliseconds)


// SocketIO Event Handlers (FRONTEND, CLIENT)

// Initialize WebSocket connection
// This creates a connection to the server using Socket.IO, enabling real-time communication
const socket = io();

// Event listener for successful connection
// This logs a message when the client successfully connects to the server
socket.on('connect', () => {
    // load viska vienu kartu, o paskui jau ziurek pagal intervalus kaip daznai updeitinsis
    console.log('Connected to server');
    socket.emit('request_from_client_to_server_for_cvbankas_data');
    socket.emit('request_from_client_to_server_for_sensor_data');
    socket.emit('request_from_client_to_server_for_stock_data');
    socket.emit('request_from_client_to_server_for_system_info_data');
    socket.emit('request_from_client_to_server_for_random_quote_data');
    socket.emit('request_from_client_to_server_for_rescuetime_data');
    updateCurrentTime();
    loadWeatherWidgets();
});

// Event listeners for various data updates
// These functions are called when the server sends new data and the client(browser) receives it
// They update different parts of the webpage with the new information
socket.on('response_from_server_to_client_with_stock_data', (data) => {
    updateStockData(data);
    updateTextColors();
});

socket.on('response_from_server_to_client_with_sensor_data', (data) => {
    updateSensorData(data);
});

socket.on('response_from_server_to_client_with_cvbankas_data', (data) => {
    updateCvbankasData(data);
});

socket.on('response_from_server_to_client_with_system_info_data', (data) => {
    updateSystemInfo(data);
});

socket.on('response_from_server_to_client_with_quote_data', (data) => {
    updateRandomQuote(data);
});

socket.on('response_from_server_to_client_with_rescuetime_data', (data) => {
    updateRescueTimeData(data);
});