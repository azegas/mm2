import { fetchStockData, fetchSensorData } from './api.js';
import { updateStockData, updateTextColors, updateSensorData } from './domUpdates.js';

function updateDisplay() {
    fetchStockData()
        .then(data => {
            updateStockData(data);
            updateTextColors();
        });
    fetchSensorData()
        .then(data => {
            updateSensorData(data);
        });
}

updateDisplay();
setInterval(updateDisplay, 10000);