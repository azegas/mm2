/**
 * Main JavaScript file for handling real-time updates and DOM manipulation
 * 
 * This script sets up WebSocket connections, handles incoming data,
 * and schedules periodic updates for various components of the application.
 */

import { updateStockData, updateTextColors, updateSensorData, updateCvbankasData, updateCurrentTime, updateSystemInfo, updateRandomQuote } from './domUpdates.js';


// Schedule periodic update requests
// These setInterval functions send requests to the server at regular intervals
// to get updated data for different parts of the application
setInterval(() => {
    socket.emit('server_give_me_cvbankas_data');
}, 10000); // 10sec

setInterval(() => {
    socket.emit('server_give_me_sensor_data');
}, 1000); //1 sec

setInterval(() => {
    socket.emit('server_give_me_stock_data');
}, 10000); //10 sec

setInterval(() => {
    socket.emit('server_give_me_system_info');
}, 10000); //10 sec

setInterval(() => {
    socket.emit('server_give_me_random_quote');
}, 3600000); //1 hour

setInterval(updateCurrentTime, 1000);


// SocketIO Event Handlers (FRONTEND, CLIENT)

// Initialize WebSocket connection
// This creates a connection to the server using Socket.IO, enabling real-time communication
const socket = io();

// Event listener for successful connection
// This logs a message when the client successfully connects to the server
socket.on('connect', () => {
    // load viska vienu kartu, o paskui jau ziurek pagal intervalus kaip daznai updeitinsis
    console.log('Connected to server');
    socket.emit('server_give_me_cvbankas_data');
    socket.emit('server_give_me_sensor_data');
    socket.emit('server_give_me_stock_data');
    socket.emit('server_give_me_system_info');
    socket.emit('server_give_me_random_quote');
    updateCurrentTime();
});

// Event listeners for various data updates
// These functions are called when the server sends new data and the client(browser) receives it
// They update different parts of the webpage with the new information
socket.on('client_here_is_stock_data', (data) => {
    updateStockData(data);
    updateTextColors();
});

socket.on('client_here_is_sensor_data', (data) => {
    updateSensorData(data);
});

socket.on('client_here_is_cvbankas_data', (data) => {
    updateCvbankasData(data);
});

socket.on('client_here_is_system_info', (data) => {
    updateSystemInfo(data);
});

socket.on('client_here_is_random_quote', (data) => {
    updateRandomQuote(data);
});

