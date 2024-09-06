import { updateStockData, updateTextColors, updateSensorData } from './domUpdates.js';

const socket = io();

socket.on('connect', () => {
    console.log('Connected to server');
});

socket.on('stock_display_refresh', (data) => {
    updateStockData(data);
    updateTextColors();
});

socket.on('sensor_display_refresh', (data) => {
    updateSensorData(data);
});

// Request sensor updates every second
setInterval(() => {
    socket.emit('request_sensor_update');
}, 1000);

// Request stock updates every minute
setInterval(() => {
    socket.emit('request_stock_update');
}, 60000);