import { fetchStockData } from './api.js';
import { updateStockData, updateTextColors } from './domUpdates.js';

function updateDisplay() {
    fetchStockData()
        .then(data => {
            updateStockData(data);
            updateTextColors();
        });
}

updateDisplay();
setInterval(updateDisplay, 10000);