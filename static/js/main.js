import { updateStockData, updateTextColors, updateSensorData, updateCvbankasData } from './domUpdates.js';

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

socket.on('cvbankas_display_refresh', (data) => {
    updateCvbankasData(data);
});

setInterval(() => {
    socket.emit('request_cvbankas_update');
}, 60000); // 1 minute

setInterval(() => {
    socket.emit('request_sensor_update');
}, 1000); // 1 second

setInterval(() => {
    socket.emit('request_stock_update');
}, 60000); // 1 minute