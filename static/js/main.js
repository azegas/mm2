import { updateStockData, updateTextColors, updateSensorData, updateCvbankasData, updateUpdateIntervals } from './domUpdates.js';

const socket = io();

let intervalStock = 60000;
let intervalSensor = 1000;
let intervalCvbankas = 60000;

socket.on('connect', () => {
    console.log('Connected to server');
    updateUpdateIntervals(intervalStock, intervalSensor, intervalCvbankas);
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
}, intervalCvbankas); // 1 minute

setInterval(() => {
    socket.emit('request_sensor_update');
}, intervalSensor); // 1 second

setInterval(() => {
    socket.emit('request_stock_update');
}, intervalStock); // 1 minute