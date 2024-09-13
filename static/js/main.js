/**
 * Main JavaScript file for handling real-time updates and DOM manipulation
 * 
 * This script sets up WebSocket connections, handles incoming data,
 * and schedules periodic updates for various components of the application.
 */

import { updateStockData, updateTextColors, updateSensorData, updateCvbankasData, updateCurrentTime, updateTestData } from './domUpdates.js';

// Initialize WebSocket connection
const socket = io();

// Update intervals (in milliseconds)
const intervalStock = 10000;    // 10 seconds
const intervalSensor = 1000;    // 1 second
const intervalCvbankas = 10000; // 10 seconds
const intervalTest = 1000;      // 1 second

// Event listener for successful connection
socket.on('connect', () => {
    console.log('Connected to server');
});

// Event listeners for various data updates
socket.on('stock_display_refresh', (data) => {
    updateStockData(data);
    updateTextColors();
});

socket.on('sensor_display_refresh', (data) => {
    updateSensorData(data);
});

socket.on('cvbankas_display_refresh', (data) => {
    updateCvbankasData(data);
});

socket.on('test_display_refresh', (data) => {
    updateTestData(data);
});

// Schedule periodic update requests
setInterval(() => {
    socket.emit('request_cvbankas_update');
}, intervalCvbankas);

setInterval(() => {
    socket.emit('request_sensor_update');
}, intervalSensor);

setInterval(() => {
    socket.emit('request_stock_update');
}, intervalStock);

setInterval(() => {
    socket.emit('request_test_update');
}, intervalTest);

// Update current time every second
setInterval(updateCurrentTime, 1000);
